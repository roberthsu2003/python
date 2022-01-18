//建立變數,動態型別
var price;
var quantity;
var total

//給數值
price = 5;
quantity = 14;
total = 5 * 14;

//取得id=cost的DOM參考
var el = document.getElementById('cost');
el.innerHTML = "價格是$" + total;