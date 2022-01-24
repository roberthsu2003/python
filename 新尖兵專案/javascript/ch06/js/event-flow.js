function showElement(){
    alert(this.innerHTML);
}


el = document.getElementById("list");
el.addEventListener('click',showElement,false);

el1 = document.getElementById('item');
el1.addEventListener('click',showElement,false);

el2 = document.getElementsById('link');
el2.addEventListener('click',showElement,false);
