function checkUsername(){
    var elMsg = document.getElementById('feedback');
    var elUsername = document.getElementById('username');
    if(elUsername.nodeValue.length < 5){
        elMsg.textContent = "必需要5個字以上"
    }else{
        elMsg.textContent = ""
    }
}