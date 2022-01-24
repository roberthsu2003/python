


el = document.getElementById("list");
el.addEventListener('click',(event) => {
    alert(event.currentTarget.innerHTML);
},false);

el1 = document.getElementById('item');
el1.addEventListener('click',(event) => {
    alert(event.currentTarget.innerHTML);
},false);

el2 = document.getElementById('link');
el2.addEventListener('click',(event) => {
    event.stopPropagation();
    event.preventDefault();
    alert(event.currentTarget.innerHTML);
},false);
