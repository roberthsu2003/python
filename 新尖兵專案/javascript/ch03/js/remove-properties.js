var hotel = {
    name:'Park',
    rooms:120,
    booked:77
};

//增加屬性
hotel.gym = true;
hotel.pool = false;
//刪除屬性
delete hotel.booked;

var elName = document.getElementById('hotelName');
elName.textContent = hotel.name;

var elPool = document.getElementById('pool');
elPool.classList.add(hotel.pool)

var elGym = document.getElementById('gym')
elGym.classList.add(hotel.gym)
