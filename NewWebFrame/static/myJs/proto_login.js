//登录事件
$('#login_button_login').click(function () {
    var username = $('#login_input_zhanghao').val();
    var password = $('#login_input_mima').val();
    $('#shuoming_text').text("");
    if(username === "" | password === ""){
        $('#shuoming_text').text("账号或密码不能为空");
        return;
    }
    var url = "/proto_login";
    $.ajax({
        type: 'POST',
        url: url,
        async: true,
        data: {request:"js_game_login",username:username,password:password},
        success: function (result,statusText) {
            if(statusText === "success"){
                if(result.response === 3){
                    window.location = '/proto_test';
                    return;
                }
                else if(result.response === 4) {
                    $('#shuoming_text').text(result.info);
                    return;
                }
                else if (result.response === -1) {
                    alert("您的用户信息已过期，请重新登录！");
                    window.parent.location = "/login";
                }
                else if(result.response === -2){
                    alert("选取的项目验证失败，请重新选择！");
                    window.location = "/TestPro";
                }
            }
            else {
                $('#shuoming_text').text(statusText);
            }
        },
        dataType: "json"
    });
});

//跳转注册事件
$('#login_button_zhuce').click(function () {
    var url = "/proto_login";
    $.ajax({
        type: 'GET',
        url: url,
        async: true,
        data: {request:"js_goto_register"},
        success: function (result,statusText) {
            if(statusText === "success"){
                if(result.response === 5){
                    window.location = "/proto_regist";
                    return;
                }
                else if (result.response === -1) {
                    alert("您的用户信息已过期，请重新登录！");
                    window.parent.location = "/login";
                }
                else if(result.response === -2){
                    alert("选取的项目验证失败，请重新选择！");
                    window.location = "/TestPro";
                }
            }
            else {
                $('#shuoming_text').text(statusText);
            }
        },
        dataType: "json"
    });
});

