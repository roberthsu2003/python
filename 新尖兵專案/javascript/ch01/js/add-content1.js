var today = new Date();
var hourNow = today.getHours();
var greeting;

if(hourNow > 18){
    greeting = '晚安';
}else if(hourNow > 12){
    greeting = '午安';
}else if(hourNow >0){
    greeting = "早安"
}else{
    greeting = "welcome"
}

document.write('<h3>' + greeting + '</h3>')