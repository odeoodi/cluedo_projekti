'use strict'

// this is url to python and after this add the flask address
const url_py = 'http://127.0.0.1:3000'


async function start_newgame() {
    try {
    const response = await fetch( `${url_py}/new_game`)
    if (!response.ok) throw new Error("something went wrong")
    console.log(response)
  } catch (error){
      console.log(error.message)}}


document.querySelector('#newgame').addEventListener('click', (e) => {
  start_newgame()})

// things we need for the map
let lat = 51.505 // here we need to add the longitude and latitude from the fly function
let long = -0.09

const map = L.map('map').setView([lat, long], 5);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

const marker = L.marker([lat, long]).addTo(map);

L.marker([lat, long]).addTo(map)
    .bindPopup('Here we can add the airport and flag.')
    .openPopup();

// map stuff ends