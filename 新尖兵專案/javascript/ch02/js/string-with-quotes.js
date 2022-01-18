var title;
var message;

title = "高富帥有特別價格";
message = '<a href=\"sale.html\">特價75折</a>'

var elTitle = document.getElementById('title');
var elNote = document.getElementById('note');

elTitle.innerHTML = title;
elNote.innerHTML = message;