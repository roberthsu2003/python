//使用物件樣版function,建立物件

function Hotel(name, rooms, booked){
    this.name = name;
    this.rooms = rooms;
    this.booked = booked;
    this.checkAvailability = function(){
        return this.rooms - this.booked
    }
};

var quayHotel = new Hotel('Quay', 40, 25);
var parkHotel  = new Hotel('Park', 120, 77);

var details1 = quayHotel.name + ' rooms:';
    details1 += quayHotel.checkAvailability();
var elHotel1 = document.getElementById('hotel1');
elHotel1.textContent = details1;

var details2 = parkHotel.name + ' rooms:';
    details2 += parkHotel.checkAvailability();
var elHotel2 = document.getElementById('hotel2');
elHotel2.textContent = details2;
