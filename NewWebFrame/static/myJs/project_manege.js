
var get_sql=function () {
    var re = "";
    $.ajax({
        type: 'POST',
        url: '/pjm/get_sql',
        async: false,
        data: {},
        success: function (result,statusText) {
            if(statusText === "success"){
                re = JSON.parse(result);
            }
            else {
                console.log("error:"+statusText);
                re = "error";
            }
        },
        dataType: "text"
    });
    for(var i=0;i<re.length;i++){
        var table = document.getElementById("tbody_table_projectList");
        var tr = document.createElement("tr");
        var td = document.createElement("td");
        var bt = document.createElement("button");
        bt.innerHTML=re[i][0]+re[i][1];
        // td.setAttribute("style","color:white");
        tr.setAttribute("id","tr_project_"+re[i][0].toString());
        bt.setAttribute("id","button_project_"+re[i][0].toString());
        bt.setAttribute("class","btn btn-info button_project");
        bt.setAttribute("onclick","project_click('"+re[i][0].toString()+"','"+re[i][1]+"')");
        td.appendChild(bt);
        tr.appendChild(td);
        table.appendChild(tr);
    }
}

var add_sql=function () {
    var pro_id =  document.getElementById("input_add_project_id").value;
    var pro_name =  document.getElementById("input_add_project_name").value;
    if(pro_id === ""){
        console.log("id输入为空");
        var id_kong ={
        title:"添加错误",
        type:"cuowu",
        discrip:"ID输入为空！",
        button_text1:"我知道了",
        button_func1:"tanchuang_close()",
        };
        tanchuang_dis(id_kong);
        return;
    }
    if(pro_name === ""){
        console.log("name输入为空");
        var name_kong ={
        title:"添加错误",
        type:"cuowu",
        discrip:"名称输入为空！",
        button_text1:"我知道了",
        button_func1:"tanchuang_close()",
        };
        tanchuang_dis(name_kong);
        return;
    }
    $.ajax({
        type: 'POST',
        url: '/pjm/add_sql',
        async: false,
        data: {pro_id:pro_id,pro_name:pro_name},
        success: function (result,statusText) {
            if (statusText === "success") {
                if(result === "success"){
                    var table = document.getElementById("tbody_table_projectList");
                    var tr = document.createElement("tr");
                    var td = document.createElement("td");
                    var bt = document.createElement("button");
                    bt.innerHTML=pro_id+pro_name;
                    tr.setAttribute("id","tr_project_"+pro_id);
                    bt.setAttribute("id","button_project_"+pro_id);
                    bt.setAttribute("class","btn btn-info button_project");
                    bt.setAttribute("onclick","project_click('"+pro_id+"','"+pro_name+"')");
                    td.appendChild(bt);
                    tr.appendChild(td);
                    table.appendChild(tr);

                    var add_success ={
                        title:"添加成功！",
                        type:"chenggong",
                        discrip:"",
                        button_text1:"好的",
                        button_func1:"tanchuang_close()",
                        };
                    tanchuang_dis(add_success);
                }
                else if(result === "fail"){
                    var id_chongfu ={
                        title:"添加错误",
                        type:"cuowu",
                        discrip:"ID已存在！",
                        button_text1:"我知道了",
                        button_func1:"tanchuang_close()",
                        };
                    tanchuang_dis(id_chongfu);
                    console.log("id重复");
                }
                else {
                    console.log("re error");
                }
            }
            else {
                console.log("error: "+statusText);
            }
        },
        dataType: "text"
    });
}

var delete_sql=function () {
    var select_code = document.getElementById("text_select_code");
    var select_name = document.getElementById("text_select_name");
    var pro_id = select_code.getAttribute("pro_id");
    if (pro_id === null){
        var no_select ={
            title:"删除错误",
            type:"cuowu",
            discrip:"没有选择项目！",
            button_text1:"我知道了",
            button_func1:"tanchuang_close()",
            };
        tanchuang_dis(no_select);
        console.log("pro_id null");
        return;
    }
    $.ajax({
        type: 'POST',
        url: '/pjm/delete_sql',
        async: false,
        data: {pro_id:pro_id},
        success: function (result,statusText) {
            if (statusText === "success") {
                if(result.split(":")[0] === "success"){
                    var table = document.getElementById("tbody_table_projectList");
                    var tr = document.getElementById("tr_project_"+pro_id);
                    table.removeChild(tr);
                    select_code.setAttribute("pro_id",null);
                    select_code.innerHTML = "未选中";
                    select_name.innerHTML = "未选中";
                    var delete_success ={
                        title:"删除成功！",
                        type:"chenggong",
                        discrip:"",
                        button_text1:"好的",
                        button_func1:"tanchuang_close()",
                        };
                    tanchuang_dis(delete_success);
                }
                else {
                    console.log("re error");
                }
            }
            else {
                console.log("error: "+statusText);
            }
        },
        dataType: "text"
    });
}



window.onload=function(){
    this.get_sql();
}

var project_click=function (id,name) {
    var select_name = document.getElementById("text_select_name");
    var select_code = document.getElementById("text_select_code");

    var id_old = select_code.getAttribute("pro_id");
    if((id_old === null) || (id_old === "null")){
        console.log(id_old);
    }
    else {
        var select_old = document.getElementById("button_project_"+id_old);
        select_old.style.borderLeft = "0";
        select_old.style.borderRight = "0";
        select_old.setAttribute("class","btn btn-info button_project");
        // select_old.style.backgroundColor = "#2c3b41";
    }

    select_code.setAttribute("pro_id",id);
    var select_new = document.getElementById("button_project_"+id);
    select_new.style.borderLeft = "4px solid #b8c7ce";
    select_new.style.borderRight = "4px solid #b8c7ce";
    select_new.setAttribute("class","btn btn-info button_project active");
    // select_new.style.backgroundColor = "#11212c";
    select_code.innerHTML=id;
    select_name.innerHTML=name;
}