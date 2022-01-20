var el = document.getElementById('message');
el.addEventListener('keyup',(event) => {
    var textEntered  = document.getElementById('message').value;
    var charDisplay = document.getElementById('charactersLeft');
    counter = (180 - (textEntered.length));
    charDisplay.textContent = counter;
    lastkey = document.getElementById('lastKey');
    lastkey.textContent = "最後打的字是:" + event.key;
})