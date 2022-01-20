var msg = '<div class=\"header\"><a id=\"close\" href="#">close X</a></div>';
msg += '<div><h2>System Maintenance</h2>';
msg += 'Our servers are being updated between 3 and 4 a.m. ';
msg += 'During this time, there may be minor disruptions to service.</div>';

var elNote = document.createElement('div');
elNote.setAttribute('id', 'note');
elNote.innerHTML  = msg;
document.body.appendChild(elNote)

var elClose = document.getElementById('close');
elClose.addEventListener('click',(event)=>{
    document.body.removeChild(elNote);
})