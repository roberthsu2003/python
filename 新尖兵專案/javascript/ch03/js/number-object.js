var originalNumber = 10.23456;
var msg = '<h2>original number</h2><p>' + originalNumber + '</p>';
msg += '<h2>顯示小數點後3位數</2><p>' + originalNumber.toFixed(3) + '</p>';
msg += '<h2>顯示3個字元</h2><p>' + originalNumber.toPrecision(3) + '</p>';

var el = document.getElementById('info');
el.innerHTML = msg;