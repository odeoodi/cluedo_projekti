'use strict'
// VARIABLES
let lat = 51.505 // here we need to add the longitude and latitude from get_location
let long = -0.09
const map = L.map('map').setView([lat, long], 5);
let mapLocations = {}
const url_py = 'http://127.0.0.1:3000'
const new_game = document.getElementById('newgame-button')

// FUNCTIONS
new_game.addEventListener('click', () => {

})


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

const marker = L.marker([lat, long]).addTo(map) //makes a new marker and adds it on the map
    .bindPopup('Pop-up') //adds the pop-up, here we can add the airport info
    .openPopup() // opens the pop-up without the marker being clicked, when the marker is created


marker.on('click', () => {
  console.log('marker clicked')
});
