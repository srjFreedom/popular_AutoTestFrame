//返回登录事件
$('#register_button_fanhui').click(function () {
    var url = "/proto_regist";
    $.ajax({
        type: 'GET',
        url: url,
        async: true,
        data: {request:"js_goto_login"},
        success: function (result,statusText) {
            if(statusText === "success"){
                if (result.response === 8) {
                    window.location = "/proto_login";
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

//注册时间
$('#register_button_zhuce').click(function () {
    var username = $('#register_input_zhanghao').val();
    var password = $('#register_input_mima').val();
    var nickname = $('#register_input_nicheng').val();
    $('#shuoming_text').text("");
    if(username === ""){
        $('#shuoming_text').text("账号不能为空");
        return;
    }
    if(password === ""){
        $('#shuoming_text').text("密码不能为空");
        return;
    }
    if(nickname === ""){
        $('#shuoming_text').text("昵称不能为空");
        return;
    }
    var url = "/proto_regist";
    $.ajax({
        type: 'POST',
        url: url,
        async: true,
        data: {request:"js_game_register",username:username,password:password,nickname:nickname},
        success: function (result,statusText) {
            if(statusText === "success"){
                if(result.response === 6){
                    $('#shuoming_text').text("注册成功!");
                    $('input.input_register').val("");
                    return;
                }
                else if(result.response === 7) {
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