var tanchuang_dis=function(neirong){
    // path_tishi = path+"/icon_tishi.png";
    // path_cuowu = path+"/icon_cuowu.png";
    // path_queren = path+"/icon_queren.png";
    // path_zhezhao = path+"/zhezhao.png";
    // path_background = path+"/tanchuang_background.png";
    var info = {
        title:neirong.title,
        discrip:neirong.discrip,
        img_src:"",
        button_type:"",
        button_text1:neirong.button_text1,
        button_func1:neirong.button_func1,
        button_text2:neirong.button_text2,
        button_func2:neirong.button_func2,
        // path_zhezhao:path_zhezhao,
        // path_background:path_background
    };
    switch(neirong.type){
        case "tishi":
            // info.img_src = this.tanchuang_get_img_path()+'static/img/proto/icon_tishi.png';
            info.img_src ='/static/img/proto/icon_tishi.png';
            info.button_type = "single";
            break;
        case "cuowu":
            // info.img_src = this.tanchuang_get_img_path()+'static/img/proto/icon_cuowu.png';
            info.img_src ='/static/img/proto/icon_cuowu.png';
            info.button_type = "single";
            break;
        case "queren":
            // info.img_src = this.tanchuang_get_img_path()+'static/img/proto/icon_queren.png';
            info.img_src ='/static/img/proto/icon_queren.png';
            info.button_type = "double";
            break;
        case "chenggong":
            // info.img_src = this.tanchuang_get_img_path()+'static/img/proto/icon_cuowu.png';
            info.img_src ='/static/img/proto/icon_chenggong.png';
            info.button_type = "single";
            break;
        default:console.log("neirong.type error");break;
    }
    this.tanchuang_creat(info);
}

var tanchuang_creat=function (info) {
    var html_button = "";
    switch (info.button_type){
        case "single": html_button='<button id="button_messegeBox_queren" name="button_messegeBox_queren" class="btn btn-primary button_tishi" onclick="'+info.button_func1+'">'+info.button_text1+'</button>';break;
        case "double": html_button='<button id="button_messegeBox_queren" name="button_messegeBox_queren" class="btn btn-primary button_queren" onclick="'+info.button_func1+'">'+info.button_text1+'</button>'+
                                   '<button id="button_messegeBox_quxiao" name="button_messegeBox_quxiao" class="btn btn-primary button_quxiao" onclick="'+info.button_func2+'">'+info.button_text2+'</button>';
        break;
        default:console.log("info.button_type error");break;
    }
    var body = document.body;
    // var url_zhezhao = this.tanchuang_get_img_path()+"static/img/proto/zhezhao.png";
    var url_zhezhao = '/static/img/proto/zhezhao.png';
    // var url_back = this.tanchuang_get_img_path()+"static/img/proto/tanchuang_background.png";
    var url_back = '/static/img/proto/tanchuang_background.png';
    var html_txt = '<div id="div_messegeBox_zhezhao" style="background:url('+url_zhezhao+')">'+
                    '<div id="div_messegeBox_tanchuang" class="div_messegeBox_tanchuang alert alert-info" style="background:url('+url_back+')">'+
                        '<img src="'+info.img_src+'" id="img_messegeBox_tanchuang_icon" class="img_messegeBox">'+
                        '<div id="div_messegeBox_tanchuang_head" class="div_messegeBox_tanchuang_head">'+
                            '<span id="div_messegeBox_tanchuang_title" class="text_messegeBox_title">'+info.title+'</span>'+
                        '</div>'+
                        '<span class="text_messegeBox_disc" id="text_messegeBox_tishi_tanchuang_disc">'+info.discrip+'</span><br>'+
                        html_button+
                    '</div>'+
                '</div>';
    body.innerHTML += html_txt;
}
var tanchuang_close=function () {
    var t_div = document.getElementById("div_messegeBox_zhezhao");
    var body = document.body;
    body.removeChild(t_div);
    return;
}


//暂时没用了
var tanchuang_get_img_path=function () {
    var re = "";
    $.ajax({
        type: 'POST',
        url: '../code_pic',
        async: false,
        data: {},
        success: function (result,statusText) {
            if(statusText === "success"){
                re = result;
            }
            else {
                console.log("error:"+statusText);
                re = "error";
            }
        },
        dataType: "text"
    });
    return re;
}

// 示例
// var click_ccc=function (path) {
//     var neirong ={
//         title:"我是标题",
//         type:"queren",
//         discrip:"我是描述描述描述描述",
//         button_text1:"确定",
//         button_func1:"tanchuang_close()",
//         button_text2:"取消",
//         button_func2:"tanchuang_close()"
//     };
//     this.tanchuang_dis(neirong);
// }