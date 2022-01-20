var elUsername = document.getElementById('username');

elUsername.addEventListener('blur',(event)=>{
    var targetElement = event.target
    console.log(targetElement);
    targetElement.value = "";
    var elMsg = document.getElementById('feedback');
    var elUsername = document.getElementById('username');
    if(elUsername.value.length < 5){
        elMsg.textContent = "必需要5個字以上"
    }else{
        elMsg.textContent = ""
    }
});