//var today = new Date(2022,1,19,10,0,0);
today = new Date();
var year = today.getFullYear();
var est = new Date(2022,1,19,9,0,0);
var todayTime = today.getTime();
var estTime = est.getTime();
console.log(todayTime);
console.log(estTime);
var difference = todayTime - estTime;
difference = difference / (60 * 60 * 1000)
var elMsg = document.getElementById('message');
elMsg.textContent = Math.floor(difference) + '小時'