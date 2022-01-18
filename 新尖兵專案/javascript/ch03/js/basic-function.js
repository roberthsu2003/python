var msg = "加入會員,得10%折扣";
/*
function updateMessage(){
    var el = document.getElementById('message');
    el.textContent = msg;
}

var funReference = updateMessage;
funReference();
*/

var updateMessage = () => {
    var el = document.getElementById('message');
    el.textContent = msg;
}

updateMessage();