// window.onload = function () {
//     connectSocket();
// }
// function connectSocket() {
//     var host = "ws://127.0.0.1:7777";
//     socket = new WebSocket(host);
//
//     socket.onopen = function () {
//         console.log('socket已连接');
//     }
//     socket.onmessage = function (msg) {
//         var message = msg.data.split(",");
//         if (message[1] == "finish") {
//             document.getElementById(message[0]).className = 'progress';
//             document.getElementById(message[0]).getElementsByTagName('div')[0].className = 'progress-bar progress-bar-success';
//             document.getElementById(message[0]).getElementsByTagName('div')[0].style.width = '100%';
//             document.getElementById(message[0] + "_button").innerHTML = "查看";
//             document.getElementById(message[0] + "_button").disabled = false;
//             socket.send('1');
//         }
//         else {
//             document.getElementById(message[0]).getElementsByTagName('div')[0].style.width = message[1];
//             socket.send('1');
//         }
//     }
//     socket.onclose = function () {
//         console.log('客户端连接断开');
//     }
//     socket.onerror = function () {
//         // socket.close();
//         socket = null;
//         console.log('socket异常');
//     }
// }
// window.onbeforeunload = function() {
//         socket.send('0');
//         socket.close();
//         socket = null;
//         console.log('服务端连接断开');
// }

function reportFenYe(pageCount, reportName, testRunner, projectCode) {
    if (reportName == "" && testRunner == "" && projectCode == "") {
        parent.window.document.getElementById("viewFrame").src="/index/autoTestReport?pageCount="+pageCount;
    }
    else
    {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                document.open();
                document.write(xmlhttp.responseText);
                document.close();
            }
        }
        xmlhttp.open("POST","/index/autoTestReport",true);
        xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
        xmlhttp.send("pageCount="+pageCount+"&reportName="+reportName+"&testRunner="+testRunner+"&projectCode="+projectCode);
    }
}

function projectWait(projectCode) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 1) {
            document.getElementById("overlay").style.display="block";
        }
        if (xmlhttp.readyState == 3) {
            document.getElementById("overlay").style.display="none";
        }
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            document.open();
            document.write(xmlhttp.responseText);
            document.close();
        }
    }
    xmlhttp.open("GET","/index/autoTestScript?projectCode="+projectCode,true);
    xmlhttp.send();
}