'use strict'
// VARIABLES

let lat = 51.505 // here we need to add the longitude and latitude from get_location
let long = -0.09
const map = L.map('map').setView([lat, long], 5);
let mapLocations = {}
const url_py = 'http://127.0.0.1:3000'
const new_game = document.getElementById('newgame-button')
const gamble_button = document.getElementById('gamble-button')

// FUNCTIONS




/*marker1.on('click', () => {
  console.log('marker clicked')
});
}*/

gamble_button.addEventListener('click', () => {

let lat1, lat2, lat3, lat4, lat5, lat6, lat7
let long1, long2, long3, long4, long5, long6, long7

[lat1, lat2, lat3, lat4, lat5, lat6, lat7] = locations_list.map(loc => loc[2]);
[long1, long2, long3, long4, long5, long6, long7] = locations_list.map(loc => loc[3]);


console.log(lat1,long1)
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'}).addTo(map);
    const marker1 = L.marker([lat1, long1]).addTo(map)
    .bindPopup('Pop-up') //adds the pop-up, here we can add the airport info
    .openPopup() // opens the pop-up without the marker being clicked, when the marker is created

  const marker2 = L.marker([lat2, long2]).addTo(map)
  const marker3 = L.marker([lat3, long3]).addTo(map)
  const marker4 = L.marker([lat4, long4]).addTo(map)
  const marker5 = L.marker([lat5, long5]).addTo(map)
  const marker6 = L.marker([lat6, long6]).addTo(map)
  const marker7 = L.marker([lat7, long7]).addTo(map)
})







//const marker = L.marker([lat, long]).addTo(map) //makes a new marker and adds it on the map
    //.bindPopup('Pop-up') //adds the pop-up, here we can add the airport info
    //.openPopup() // opens the pop-up without the marker being clicked, when the marker is created

