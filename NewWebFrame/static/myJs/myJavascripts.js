function load_TestPro(func) {
    document.getElementById("viewFrame").src="/index/TestPro?func="+func;
    document.getElementById("viewDiv").style.display = "block";
}

function load_TestReport() {
    document.getElementById("viewFrame").src="/index/autoTestReport";
    document.getElementById("viewDiv").style.display = "block";
}

function load_project_manager() {
    document.getElementById("viewFrame").src="/pjm/project_manege";
    document.getElementById("viewDiv").style.display = "block";
}

// function load_autoTestDir() {
//     //  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
//     var xmlhttp = new XMLHttpRequest();
//     xmlhttp.onreadystatechange = function() {
//         if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
//             $("#viewDiv").load("/index/autoTestDir");
//             document.getElementById("viewDiv").style.display = "block";
//             document.getElementById("viewFrame").style.display = "block";
//         }
//     }
//     xmlhttp.open("GET","/index/autoTestDir",true);
//     xmlhttp.send();
// }