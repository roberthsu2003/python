/*
function checkUsername(){
    var elMsg = document.getElementById('feedback');
    var elUsername = document.getElementById('username');
    if(elUsername.value.length < 5){
        elMsg.textContent = "必需要5個字以上"
    }else{
        elMsg.textContent = ""
    }
}
*/

var elUsername = document.getElementById('username');
elUsername.addEventListener('blur',()=>{
    //console.log(event);
    var elMsg = document.getElementById('feedback');
    var elUsername = document.getElementById('username');
    if(elUsername.value.length < 5){
        elMsg.textContent = "必需要5個字以上"
    }else{
        elMsg.textContent = ""
    }
});