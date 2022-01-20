//var list = document.getElementsByTagName('ul')[0]
var list = document.querySelector('ul')

//建立最後的Element
var newItemLast = document.createElement('li')
var newTextLast = document.createTextNode('cream');

newItemLast.appendChild(newTextLast);
list.appendChild(newItemLast)


//建立在最前的Element
var newItemFirst = document.createElement('li')
var newTextFirst = document.createTextNode('kale');
newItemFirst.appendChild(newTextFirst)

list.insertBefore(newItemFirst, list.firstChild)

//增加attribute
var listItems = document.querySelectorAll('li')
list

for(var i=0; i<listItems.length; i++){
    listItems[i].classList.add('cool');
}

var heading = document.querySelector('h2');
var headingText = heading.firstChild.nodeValue;
var totalItems = listItems.length;
var newHeading = headingText + '<span>' + totalItems + '</span>';
heading.innerHTML = newHeading

