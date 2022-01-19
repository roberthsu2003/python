var randomNum = Math.floor(Math.random()*1000000) % (49 - 1 + 1) + 1
var el = document.getElementById('info');
el.innerHTML = "<h2>亂數值</h2><p>" + randomNum + "</p>"