var el = document.getElementById('username');
var elMsg = document.getElementById('feedback');

el.addEventListener('focus',(event)=>{
    var inner = 5;
    elMsg.className = 'tip';
    elMsg.innerHTML = "username最少要5個字元";
    inner  = 10;
})

el.addEventListener('blur',(event)=>{
    
    if(event.target.value.length < 5){

        elMsg.className ='warning';
        elMsg.textContent = "字元不足";
    }else{
        elMsg.textContent = "";
    }
    
    
})