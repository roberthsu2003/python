var msg = '<h2>window可見視窗</h2><p>width:' + window.innerWidth + '</p>';
msg += '<p>heigh:' + window.innerHeight + '</p>';
msg += '<h2>歷史記錄:</h2><p>items'+ window.history.length +'</p>';
msg += '<h2>螢幕資訊:</h2><p>window:'+ window.screen.width +'<p>';
msg += '<p>height:'+ window.screen.height +'<p>';

var el = document.getElementById('info');
el.innerHTML = msg
alert('目前網址:'+ window.location)

