var noteName = document.getElementById('noteName');
var noteInput = document.getElementById('noteInput');
var button = document.getElementById('buttons');
//handler
button.onclick = (event) => {
    event.preventDefault();
    var noteString = noteInput.value;
    if(noteString.length > 3){
        console.log('表單送出');
        document.myForm.submit()
    }
}