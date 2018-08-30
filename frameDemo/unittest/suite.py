# -*- coding: utf8 -*-
"""TestSuite"""

import sys
import time
import traceback
from . import case
from . import util

__unittest = True


def _call_if_exists(parent, attr):
    func = getattr(parent, attr, lambda: None)
    func()


class BaseTestSuite(object):
    """A simple test suite that doesn't provide class or module shared fixtures.
    """
    def __init__(self, tests=()):
        self._tests = []
        self.addTests(tests)

    def __repr__(self):
        return "<%s tests=%s>" % (util.strclass(self.__class__), list(self))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return list(self) == list(other)

    def __ne__(self, other):
        return not self == other

    # Can't guarantee hash invariant, so flag as unhashable
    __hash__ = None

    def __iter__(self):
        return iter(self._tests)

    def countTestCases(self):
        cases = 0
        for test in self:
            cases += test.countTestCases()
        return cases

    def addTest(self, test):
        # sanity checks
        if not hasattr(test, '__call__'):
            raise TypeError("{} is not callable".format(repr(test)))
        if isinstance(test, type) and issubclass(test,
                                                 (case.TestCase, TestSuite)):
            raise TypeError("TestCases and TestSuites must be instantiated "
                            "before passing them to addTest()")
        self._tests.append(test)

    def addTests(self, tests):
        if isinstance(tests, basestring):
            raise TypeError("tests must be an iterable of tests, not a string")
        for test in tests:
            self.addTest(test)

    def run(self, result):
        for test in self:
            if result.shouldStop:
                break
            test(result)
        return result

    def __call__(self, *args, **kwds):
        return self.run(*args, **kwds)

    def debug(self):
        """Run the tests without collecting errors in a TestResult"""
        for test in self:
            test.debug()


class TestSuite(BaseTestSuite):
    """A test suite is a composite test consisting of a number of TestCases.

    For use, create an instance of TestSuite, then add test case instances.
    When all tests have been added, the suite can be passed to a test
    runner, such as TextTestRunner. It will run the individual test cases
    in the order in which they were added, aggregating the results. When
    subclassing, do not forget to call the base class constructor.
    """

    def run(self, result, debug=False):
        topLevel = False
        reRunTimes = 1
        if getattr(result, '_testRunEntered', False) is False:
            result._testRunEntered = topLevel = True

        for test in self:
            alRunTimes = 1
            if result.shouldStop:
                break

            if _isnotsuite(test):
                self._tearDownPreviousClass(test, result)
                self._handleModuleFixture(test, result)
                self._handleClassSetUp(test, result)
                result._previousTestClass = test.__class__

                if (getattr(test.__class__, '_classSetupFailed', False) or
                    getattr(result, '_moduleSetUpFailed', False)):
                    continue

            failre = True
            while failre:
                if not debug:
                    test(result)
                else:
                    test.debug()

                if result.result[-1][0] == 1 or result.result[-1][0] == 2:    # fail和error判断失败重跑
                    if reRunTimes < alRunTimes or not _isnotsuite(test):
                        failre = False
                    else:
                        reRunPut = u'用例 %s 第 %d 次重新运行' % (test, alRunTimes)
                        print reRunPut.encode('gb18030')
                        alRunTimes = alRunTimes + 1
                        time.sleep(3)
                else:
                    failre = False


        if topLevel:
            self._tearDownPreviousClass(None, result)
            self._handleModuleTearDown(result)
            result._testRunEntered = False
        return result

    def debug(self):
        """Run the tests without collecting errors in a TestResult"""
        debug = _DebugResult()
        self.run(debug, True)

    ################################

    def _handleClassSetUp(self, test, result):
        previousClass = getattr(result, '_previousTestClass', None)
        currentClass = test.__class__
        if currentClass == previousClass:
            return
        if result._moduleSetUpFailed:
            return
        if getattr(currentClass, "__unittest_skip__", False):
            return

        try:
            currentClass._classSetupFailed = False
        except TypeError:
            # test may actually be a function
            # so its class will be a builtin-type
            pass

        setUpClass = getattr(currentClass, 'setUpClass', None)
        if setUpClass is not None:
            _call_if_exists(result, '_setupStdout')
            try:
                setUpClass()
            except Exception as e:
                if isinstance(result, _DebugResult):
                    raise
                currentClass._classSetupFailed = True
                className = util.strclass(currentClass)
                errorName = 'setUpClass (%s)' % className
                self._addClassOrModuleLevelException(result, e, errorName)
            finally:
                _call_if_exists(result, '_restoreStdout')

    def _get_previous_module(self, result):
        previousModule = None
        previousClass = getattr(result, '_previousTestClass', None)
        if previousClass is not None:
            previousModule = previousClass.__module__
        return previousModule


    def _handleModuleFixture(self, test, result):
        previousModule = self._get_previous_module(result)
        currentModule = test.__class__.__module__
        if currentModule == previousModule:
            return

        self._handleModuleTearDown(result)

        result._moduleSetUpFailed = False
        try:
            module = sys.modules[currentModule]
        except KeyError:
            return
        setUpModule = getattr(module, 'setUpModule', None)
        if setUpModule is not None:
            _call_if_exists(result, '_setupStdout')
            try:
                setUpModule()
            except Exception, e:
                if isinstance(result, _DebugResult):
                    raise
                result._moduleSetUpFailed = True
                errorName = 'setUpModule (%s)' % currentModule
                self._addClassOrModuleLevelException(result, e, errorName)
            finally:
                _call_if_exists(result, '_restoreStdout')

    def _addClassOrModuleLevelException(self, result, exception, errorName):
        error = _ErrorHolder(errorName)
        addSkip = getattr(result, 'addSkip', None)
        if addSkip is not None and isinstance(exception, case.SkipTest):
            addSkip(error, str(exception))
        else:
            result.addError(error, sys.exc_info())

    def _handleModuleTearDown(self, result):
        previousModule = self._get_previous_module(result)
        if previousModule is None:
            return
        if result._moduleSetUpFailed:
            return

        try:
            module = sys.modules[previousModule]
        except KeyError:
            return

        tearDownModule = getattr(module, 'tearDownModule', None)
        if tearDownModule is not None:
            _call_if_exists(result, '_setupStdout')
            try:
                tearDownModule()
            except Exception as e:
                if isinstance(result, _DebugResult):
                    raise
                errorName = 'tearDownModule (%s)' % previousModule
                self._addClassOrModuleLevelException(result, e, errorName)
            finally:
                _call_if_exists(result, '_restoreStdout')

    def _tearDownPreviousClass(self, test, result):
        previousClass = getattr(result, '_previousTestClass', None)
        currentClass = test.__class__
        if currentClass == previousClass:
            return
        if getattr(previousClass, '_classSetupFailed', False):
            return
        if getattr(result, '_moduleSetUpFailed', False):
            return
        if getattr(previousClass, "__unittest_skip__", False):
            return

        tearDownClass = getattr(previousClass, 'tearDownClass', None)
        if tearDownClass is not None:
            _call_if_exists(result, '_setupStdout')
            try:
                tearDownClass()
            except Exception, e:
                if isinstance(result, _DebugResult):
                    raise
                className = util.strclass(previousClass)
                errorName = 'tearDownClass (%s)' % className
                self._addClassOrModuleLevelException(result, e, errorName)
            finally:
                _call_if_exists(result, '_restoreStdout')


class _ErrorHolder(object):
    """
    Placeholder for a TestCase inside a result. As far as a TestResult
    is concerned, this looks exactly like a unit test. Used to insert
    arbitrary errors into a test suite run.
    """
    # Inspired by the ErrorHolder from Twisted:
    # http://twistedmatrix.com/trac/browser/trunk/twisted/trial/runner.py

    # attribute used by TestResult._exc_info_to_string
    failureException = None

    def __init__(self, description):
        self.description = description

    def id(self):
        return self.description

    def shortDescription(self):
        return None

    def __repr__(self):
        return "<ErrorHolder description=%r>" % (self.description,)

    def __str__(self):
        return self.id()

    def run(self, result):
        # could call result.addError(...) - but this test-like object
        # shouldn't be run anyway
        pass

    def __call__(self, result):
        return self.run(result)

    def countTestCases(self):
        return 0

def _isnotsuite(test):
    "A crude way to tell apart testcases and suites with duck-typing"
    try:
        iter(test)
    except TypeError:
        return True
    return False


class _DebugResult(object):
    "Used by the TestSuite to hold previous class when running in debug."
    _previousTestClass = None
    _moduleSetUpFailed = False
    shouldStop = False



'''New TestSuite To Run Again After Failure --By Srj'''
# class SrjSuite(TestSuite):
#     def run(self, result, debug=False):
#         failcount = 0  # 失败总运行次数
#         class_num = 1
#         topLevel = False
#         if getattr(result, '_testRunEntered', False) is False:
#             result._testRunEntered = topLevel = True
#
#         for test in self:
#             case_num = 1
#             if result.shouldStop:
#                 break
#
#             success_flag = True
#             while success_flag:
#                 if _isnotsuite(test):
#                     self._tearDownPreviousClass(test, result)
#                     self._handleModuleFixture(test, result)
#                     self._handleClassSetUp(test, result)
#                     result._previousTestClass = test.__class__
#                     if (getattr(test.__class__, '_classSetupFailed', False) or
#                             getattr(result, '_moduleSetUpFailed', False)):
#                         if class_num > failcount:
#                             success_flag = False
#                         else:
#                             result._previousTestClass = None
#                             cshzx = '类%s第 %s 次重新初始化执行\n' % (test.__class__, class_num)
#                             print cshzx.encode('gb18030')
#                             time.sleep(3)
#                             class_num += 1
#                         continue
#
#                 if not debug:
#                     # startTime = datetime.datetime.now()
#                     test(result)
#                     # stopTime = datetime.datetime.now()
#                     # caseRunTime = stopTime - startTime
#                     # try:
#                     #     if _isnotsuite(self._tests[suitei]):
#                     #         pass
#                     #     else:
#                     #         if len(self._tests[suitei]._tests) > 0:
#                     #             for modi, modTest in enumerate(self._tests[suitei]):
#                     #                 if self._tests[suitei]._tests[modi]._testMethodDoc == None:
#                     #                     self._tests[suitei]._tests[modi]._testMethodDoc = '<br />用例第%s次执行耗时：' % (case_num) + str(caseRunTime)
#                     #                 else:
#                     #                     self._tests[suitei]._tests[modi]._testMethodDoc = self._tests[suitei]._tests[modi]._testMethodDoc + '<br />用例第%s次执行耗时：' % (case_num) + str(caseRunTime)
#                     # except Exception:
#                     #     traceback.print_exc()
#                 else:
#                     test.debug()
#
#                 if result.result[-1][0] == 1 or result.result[-1][0] == 2:  # 结果为fail和err用例判断
#                     if case_num > failcount:
#                         success_flag = False
#                     else:
#                         cxzx = '用例%s第 %s 次重新执行\n' % (test, case_num)
#                         print cxzx.encode('gb18030')
#                         time.sleep(3)
#                         case_num += 1
#                 else:
#                     success_flag = False
#
#         if topLevel:
#             self._tearDownPreviousClass(None, result)
#             self._handleModuleTearDown(result)
#             result._testRunEntered = False
#         return result