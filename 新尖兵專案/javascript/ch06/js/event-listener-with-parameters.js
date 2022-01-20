var elUsername = document.getElementById('username');
function abc(val){
    console.log(val);
    var elMsg = document.getElementById('feedback');
    var elUsername = document.getElementById('username');
    if(elUsername.value.length < 5){
        elMsg.textContent = "必需要5個字以上"
    }else{
        elMsg.textContent = ""
    }
}

elUsername.addEventListener('blur',(event)=>{
    console.log(event);
    abc(10);
});