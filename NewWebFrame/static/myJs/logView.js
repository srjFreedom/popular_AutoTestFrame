function load_autoTestLogRun(logName) {
    //  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            document.getElementById("logView").innerHTML = xmlhttp.responseText.replace(/\n/g, "<br>");
            window.location = "#bottom";
        }
    }
    xmlhttp.open("post","/index/autoTestLogRun",true);
    xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xmlhttp.send("logName="+logName);
}