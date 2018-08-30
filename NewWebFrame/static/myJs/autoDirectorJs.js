window.onload = function() {
    var obj = document.getElementById('demo').getElementsByTagName('input');
    for (var i = 0; i < obj.length; i ++) {
        obj[i].onclick = function() {
            var childrenObj = this.parentNode.getElementsByTagName('ul');
            if (childrenObj.length > 0) {
                for (var j = 0; j < childrenObj.length; j ++) {
                    var o = childrenObj[j].getElementsByTagName('input');
                    for (var k = 0; k < o.length; k ++) {
                        o[k].checked = this.checked;
                    }
                }
            }
        checkParent(this);
        }
    }
}

function checkParent(obj) {
    var parentObj = obj.parentNode.parentNode;
    if (parentObj.id != 'demo') {
        parentObj = parentObj.parentNode;
        var FLAG;
        var count = 0
        var o = parentObj.getElementsByTagName('input');
        for (var i = 1; i < o.length; i ++) {
            if (!o[i].checked) {
                count += 1
            }
        }
        if (count == 0) {
            FLAG = true;
            o[0].indeterminate = false;
        }
        else if (count == o.length-1) {
            FLAG = false;
            o[0].indeterminate = false;
        }
        else if (count > 0 && count < o.length-1) {
            FLAG = false;
            o[0].indeterminate = true;
        }
        if (FLAG) o[0].checked = true;
        else o[0].checked = false;
        if (parentObj.parentNode.parentNode.id != 'demo') checkParent(o[0]);
    }
}

function showhide(id) {
    var o = document.getElementById(id);
    o.style.display = o.style.display == 'block' ? 'none' : 'block';
}

function allCheck() {
    var all = document.getElementsByTagName("input");
    for (i = 0; i < all.length; i++) {
        if (all[i].checked == false) {
            for (j = i; j < all.length; j++) {
                all[j].indeterminate = false;
                all[j].checked = true;
            }
            return;
        }
    }
    for (j = 0; j < all.length; j++) {
        all[j].indeterminate = false;
        all[j].checked = false;
    }
    return;
}

// function runAutoTest() {
//     var phoneip = document.getElementById('server_ready');
//     phoneip.submit();
//     var scripts = document.getElementById('scripts_ready');
//     scripts.submit();
// }

function runAutoTest() {
    //  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
    document.getElementById('scripts_ready').submit();
}