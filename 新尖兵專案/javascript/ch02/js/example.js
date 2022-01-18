var greeting = 'Howdy';
var name1 = "徐國堂";
var message = ',請檢查您的帳單:';
var welcome = greeting + name1 + message;

var sign = "特力屋"
var tiles = sign.length;
var subTotal = tiles * 5;
var shipping = 7;
var grandToTal = subTotal + shipping;

var el = document.getElementById('greeting');
el.textContent = welcome;

var elSign = document.getElementById('userSign');
elSign.textContent = sign;

var elTiles = document.getElementById('tiles');
elTiles.textContent = tiles;

var elSubTotal = document.getElementById('subTotal');
elSubTotal.textContent = '$' + subTotal;

var elShipping = document.getElementById('shipping')
elShipping.textContent = '$' + shipping;

var elGrandtotal = document.getElementById('grandTotal');
elGrandtotal.textContent = '$' + grandToTal;