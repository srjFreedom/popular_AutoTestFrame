//选择服务器
$('button').click(function () {
    var id = $(this).attr("id");
    var url = "/choose_server";
    $.ajax({
        type: 'POST',
        url: url,
        async: true,
        data: {request:"js_choose_server",id:id},
        success: function (result,statusText) {
            if(statusText === "success"){
                if(result.response === 1){
                    window.location = "/proto_login";
                }
                else if(result.response === 2) {
                    alert('选择服务器失败，请重新选服！');
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
                alert(statusText);
            }
        },
        dataType: "json"
    });
});