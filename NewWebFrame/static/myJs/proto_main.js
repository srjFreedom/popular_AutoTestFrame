//获取昵称请求方法，在onload中加载
var rqstnknm = function () {
    var url = "/proto_test";
    $.ajax({
        type: 'POST',
        url: url,
        async: true,
        data: {request: "js_request_nickname"},
        success: function (result, statusText) {
            if (statusText === "success") {
                if (result.response === 22) {
                    $('#main_head_name').text(result.info);
                }
                else if (result.response === -1) {
                    alert("您的用户信息已过期，请重新登录！");
                    window.parent.location = "/login";
                }
                else if(result.response === -2){
                    alert("选取的项目验证失败，请重新选择！");
                    window.location = "/TestPro";
                }
                else if(result.response === -3){
                    alert("与服务器连接发生中断，请重新登录游戏！");
                    window.location = "/proto_login";
                }
            }
            else {
                alert(statusText);
            }
        },
        dataType: "json"
    });
};

//清空协议队列显示
$('#button_jieshou_qingkong').click(function () {
    $('#jiehsou_xianshi').text("");
});

//
$('#button_main_head_zhuxiao').click(function () {
    var url = "/proto_test";
    $.ajax({
        type: 'GET',
        url: url,
        async: true,
        data: {request:"js_game_logout"},
        success: function (result,statusText) {
            if(statusText === "success") {
                if (result.response === 21) {
                    window.location = '/choose_server';
                    return;
                }
                else if (result.response === 22) {
                    alert('发生未知异常，注销账号失败！');
                    return;
                }
                else if (result.response === -1) {
                    alert("您的用户信息已过期，请重新登录！");
                    window.parent.location = "/login";
                }
                else if (result.response === -2) {
                    alert("选取的项目验证失败，请重新选择！");
                    window.location = "/TestPro";
                }
                else if (result.response === -3) {
                    alert("与服务器连接发生中断，请重新登录游戏！");
                    window.location = "/proto_login";
                }
            }
            else {
                    alert(statusText);
            }
        },
        complete : function(XMLHttpRequest,status){ //请求完成后最终执行参数
　　　　    if(status=='parsererror'){//超时,status还有success,error等值的情况
    　　　　　  alert("服务器返回异常，注销失败！");
　　　　    }
　　    },
        dataType: "json"
    });
});

//系统选择操作
$('#form_control_select_xitong').change(function () {
    var id = parseInt(($(this).children('option:selected')).val());
    var system = $.trim(($(this).children('option:selected')).text());
    //选中0号标签不做处理，0号标签用于占位与显示
    if(id === 0){
        $("#form_control_select_xieyi").html("");
        $("#control_xieyishuom_text").text("");
        return;
    }
    var url = "/proto_test";
    $.ajax({
        type: 'POST',
        url: url,
        async: true,
        data: {request:"js_system_choose",system:system},
        success: function (result,statusText) {
            if(statusText === "success"){
                if(result.response === 9){
                    var protolist = result.list;
                    var html =  "<option id='form_control_select_xieyi_0' name='form_control_select_xieyi_0' value= '0'>请选择协议</option>";
                    for(var i = 0; i < protolist.length; i++) {
                        html += "<option id='form_control_select_xieyi_" + String(i + 1) + "' name='form_control_select_xieyi_" + String(i + 1) +
                            "' value='" + String(i + 1) + "'>" + protolist[i] + "</option>";
                    }
                    $('#form_control_select_xieyi').html(html);
                    return;
                }
                else if(result.response === 10) {
                    alert(result.info);
                    return;
                }
                else if(result.response === -1){
                    alert("您的用户信息已过期，请重新登录！");
                    window.parent.location = "/login";
                }
                else if(result.response === -2){
                    alert("选取的项目验证失败，请重新选择！");
                    window.location = "/TestPro";
                }
                else if(result.response === -3){
                    alert("与服务器连接发生中断，请重新登录游戏！");
                    window.location = "/proto_login";
                }
            }
            else {
                alert(statusText);
            }
        },
        dataType: "json"
    });
});

//协议选择操作
$('#form_control_select_xieyi').change(function () {
    var id = parseInt(($(this).children('option:selected')).val());
    var proto = $.trim(($(this).children('option:selected')).text());
    $('#control_xieyishuom_text').css("color","black");
    //选中0号标签不做处理，0号标签用于占位与显示
    if(id === 0){
        $("#control_xieyishuom_text").text("");
        return;
    }
    var url = "/proto_test";
    $.ajax({
        type: 'POST',
        url: url,
        async: true,
        data: {request:"js_proto_choose",proto:proto},
        success: function (result,statusText) {
            if(statusText === "success"){
                if(result.response === 11){
                    var output = symbol(result.info);
                    $('#control_xieyishuom_text').html(output);
                    return;
                }
                else if(result.response === 12) {
                    $('#control_xieyishuom_text').text(result.info);
                    $('#control_xieyishuom_text').css("color","red");
                    return;
                }
                else if(result.response === -1){
                    alert("您的用户信息已过期，请重新登录！");
                    window.parent.location = "/login";
                }
                else if(result.response === -2){
                    alert("选取的项目验证失败，请重新选择！");
                    window.location = "/TestPro";
                }
                else if(result.response === -3){
                    alert("与服务器连接发生中断，请重新登录游戏！");
                    window.location = "/proto_login";
                }
            }
            else {
                $('#control_xieyishuom_text').text(statusText);
                $('#control_xieyishuom_text').css("color","red");
            }
        },
        dataType: "json"
    });
});


//发送协议
$('#button_control_xieyifasong').click(function () {
    var id = ($('#form_control_select_xieyi').children('option:selected')).val();
    var proto = $.trim(($('#form_control_select_xieyi').children('option:selected')).text());
    var vaule = $('#input_control_xieyicanshu').val();
    var count = parseInt($('#input_control_xieyicishu').val());
    $('#control_xieyishuom_text').css("color","black");
    //选中0号协议或是没有选择协议时做报错返回
    if(id === "0" | proto === ""){
        alert("请先选择协议！");
        return;
    }
    //并发提示输入
    if(isNaN(count)){
        alert("请输入正确的并发数！");
        return;
    }
    var url = "/proto_test";
    $.ajax({
        type: 'POST',
        url: url,
        async: true,
        data: {request:"js_send_proto",c2s:proto,values:vaule,counts:count},
        success: function (result,statusText) {
            if(statusText === "success"){
                if(result.response === 13){
                    alert('协议发送成功!');
                    return;
                }
                else if(result.response === 14) {
                    alert('协议发送失败！');
                    return;
                }
                else if(result.response === -1){
                    alert("您的用户信息已过期，请重新登录！");
                    window.parent.location = "/login";
                }
                else if(result.response === -2){
                    alert("选取的项目验证失败，请重新选择！");
                    window.location = "/TestPro";
                }
                else if(result.response === -3){
                    alert("与服务器连接发生中断，请重新登录游戏！");
                    window.location = "/proto_login";
                }
            }
            else {
                    alert(statusText);
            }
        },
        dataType: "json"
    });
});

//结果码查询操作
$("#button_jiehsou_chaxun_fasong").click(function () {
    var inputCode = $("#input_jieshou_chaxun").val();
    $('#control_xieyishuom_text').css("color","black");
    if(inputCode === ""){
        $('#jiehsou_chaxun_jieguo').text("输入的结果码不能为空！");
        $('#jiehsou_chaxun_jieguo').css("color","red");
        return;
    }
    var url = "/proto_test";
    $.ajax({
        type: 'POST',
        url: url,
        async: true,
        data: {request:"js_check_code",code:inputCode},
        success: function (result,statusText) {
            if(statusText === "success"){
                if(result.response === 15){
                    $('#jiehsou_chaxun_jieguo').text(result.info);
                    return;
                }
                else if(result.response === 16) {
                    $('#jiehsou_chaxun_jieguo').text(result.info);
                    $('#jiehsou_chaxun_jieguo').css("color","red");
                    return;
                }
                else if(result.response === -1){
                    alert("您的用户信息已过期，请重新登录！");
                    window.parent.location = "/login";
                }
                else if(result.response === -2){
                    alert("选取的项目验证失败，请重新选择！");
                    window.location = "/TestPro";
                }
                else if(result.response === -3){
                    alert("与服务器连接发生中断，请重新登录游戏！");
                    window.location = "/proto_login";
                }
            }
            else {
                $('#jiehsou_chaxun_jieguo').text(statusText);
                $('#jiehsou_chaxun_jieguo').css("color","red");
            }
        },
        dataType: "json"
    });
});

// 发送GM命令
$("#button_gm_fasong").click(function () {
    var gmvalue = $("#input_gm").val();
    var url = "/proto_test";
    var flag = 0;
    $.ajax({
        type: 'POST',
        url: url,
        async: false,
        data: {request:"js_send_gm",gm:gmvalue},
        success: function (result,statusText) {
            if(statusText === "success"){
                if(result.response === 17){
                    alert("GM发送成功！");
                }
                else if(result.response === 18) {
                    alert("GM发送失败！");
                }
                else if(result.response === -1){
                    alert("您的用户信息已过期，请重新登录！");
                    window.parent.location = "/login";
                }
                else if(result.response === -2){
                    alert("选取的项目验证失败，请重新选择！");
                    window.location = "/TestPro";
                }
                else if(result.response === -3){
                    alert("与服务器连接发生中断，请重新登录游戏！");
                    window.location = "/proto_login";
                }
            }
            else {
                alert(statusText);
            }
        },
        dataType: "json"
    });
});

//查询功能
$("button.btn-sm").click(function () {
    var fuc = parseInt($(this).attr("id").split("_")[2]);
    $('#chaxun_jieguo').css("color","black");
    var url = "/proto_test";
    $.ajax({
        type: 'POST',
        url: url,
        async: true,
        data: {request:"js_check_details",fuc:fuc},
        success: function (result,statusText) {
            if(statusText === "success"){
                if(result.response === 19){
                   var output = symbol(result.info);
                    $('#chaxun_jieguo').html(output);
                    return;
                }
                else if(result.response === 20) {
                    $('#chaxun_jieguo').html(result.info);
                    $('#chaxun_jieguo').css("color","red");
                    return;
                }
                else if(result.response === -1){
                    alert("您的用户信息已过期，请重新登录！");
                    window.parent.location = "/login";
                }
                else if(result.response === -2){
                    alert("选取的项目验证失败，请重新选择！");
                    window.location = "/TestPro";
                }
                else if(result.response === -3){
                    alert("与服务器连接发生中断，请重新登录游戏！");
                    window.location = "/proto_login";
                }
            }
            else {
                $('#chaxun_jieguo').html(statusText);
                $('#chaxun_jieguo').css("color","red");
            }
        },
        dataType: "json"
    });
});

//字符串处理方法，主要是用于保留字符串中的空格以及回车
var symbol = function (str) {
    var i;
    var result = "";
    var c;
    for (i = 0; i < str.length; i++) {
        c = str.substr(i, 1);
        if ( c === "\n")
            result = result + "</br>";
        else if(c === " ")
            result = result + "&nbsp;"
        else if (c != "\r")
            result = result + c;
    }
    return result;
};

//将unicode解码成中文字符
var decodeUnicode = function(str) {
    str = str.replace(/\\/g, "%");
    return unescape(str);
};

//将中文字符编码成unicode字符
var encodeUnicode = function (str) {
    var res = [];
    for (var i = 0; i < str.length; i++) {
        res[i] = ( "00" + str.charCodeAt(i).toString(16) ).slice(-4);
    }
    return "\\u" + res.join("\\u");
};
