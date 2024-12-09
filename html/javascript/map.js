'use strict'
// VARIABLES

const map = L.map('map').setView([48.499998, 23.3833318 ], 3.4);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'}).addTo(map);

const url_py = 'http://127.0.0.1:3000'

const markerGroup = L.layerGroup().addTo(map);

// FUNCTIONS

async function CreateMap() {
let lat1, lat2, lat3, lat4, lat5, lat6, lat7
let long1, long2, long3, long4, long5, long6, long7

[lat1, lat2, lat3, lat4, lat5, lat6, lat7] = locations_list.map(loc => loc[2]);
[long1, long2, long3, long4, long5, long6, long7] = locations_list.map(loc => loc[3]);


const marker1 = L.marker([lat1, long1]).addTo(map)
    .bindPopup(`
            <div class= "flex-wrap" id="map-popup">
                <p><strong>Airport:</strong> ${locations_list[0][0]}</p>
                <p><strong>Country:</strong> ${locations_list[7][0][2]}</p>
                <p><strong>City:</strong> ${locations_list[7][0][0]}</p>
                <p><strong>Flag:</strong></p>
                <img src="${locations_list[7][0][1]}" alt="Country Flag"
                       style="width:30px;height:auto;">
</div>
    `)
    .addTo(markerGroup)
    .openPopup() // opens the pop-up without the marker being clicked, when the marker is created

  const marker2 = L.marker([lat2, long2]).addTo(map).bindPopup()
    .bindPopup(`
            <div class= "flex-wrap" id="map-popup">
                <p><strong>Airport:</strong> ${locations_list[1][0]}</p>
                <p><strong>Country:</strong> ${locations_list[7][1][2]}</p>
                <p><strong>City:</strong> ${locations_list[7][1][0]}</p>
                <p><strong>Flag:</strong></p>
                <img src="${locations_list[7][1][1]}" alt="Country Flag" style="width:30px;height:auto;">
            </div>
        `)
        .addTo(markerGroup)
  const marker3 = L.marker([lat3, long3]).addTo(map).bindPopup()
    .bindPopup(`
            <div class= "flex-wrap" id="map-popup">
                <p><strong>Airport:</strong> ${locations_list[2][0]}</p>
                <p><strong>Country:</strong> ${locations_list[7][2][2]}</p>
                <p><strong>City:</strong> ${locations_list[7][2][0]}</p>
                <p><strong>Flag:</strong></p>
                <img src="${locations_list[7][2][1]}" alt="Country Flag" style="width:30px;height:auto;">
            </div>
        `)
          .addTo(markerGroup)
  const marker4 = L.marker([lat4, long4]).addTo(map).bindPopup()
    .bindPopup(`
              <div class= "flex-wrap" id="map-popup">
                  <p><strong>Airport:</strong> ${locations_list[3][0]}</p>
                  <p><strong>Country:</strong> ${locations_list[7][3][2]}</p>
                  <p><strong>City:</strong> ${locations_list[7][3][0]}</p>
                  <p><strong>Flag:</strong></p>
                  <img src="${locations_list[7][3][1]}" alt="Country Flag" style="width:30px;height:auto;">
              </div>
          `)
          .addTo(markerGroup)
  const marker5 = L.marker([lat5, long5]).addTo(map).bindPopup()
      .bindPopup(`
              <div class= "flex-wrap" id="map-popup">
                  <p><strong>Airport:</strong> ${locations_list[4][0]}</p>
                  <p><strong>Country:</strong> ${locations_list[7][4][2]}</p>
                  <p><strong>City:</strong> ${locations_list[7][4][0]}</p>
                  <p><strong>Flag:</strong></p>
                  <img src="${locations_list[7][4][1]}" alt="Country Flag" style="width:30px;height:auto;">
              </div>
          `)
          .addTo(markerGroup)
  const marker6 = L.marker([lat6, long6]).addTo(map).bindPopup()
      .bindPopup(`
              <div class= "flex-wrap" id="map-popup">
                  <p><strong>Airport:</strong> ${locations_list[5][0]}</p>
                  <p><strong>Country:</strong> ${locations_list[7][5][2]}</p>
                  <p><strong>City:</strong> ${locations_list[7][5][0]}</p>
                  <p><strong>Flag:</strong></p>
                  <img src="${locations_list[7][5][1]}" alt="Country Flag" style="width:30px;height:auto;">
              </div>
          `)
          .addTo(markerGroup)
  const marker7 = L.marker([lat7, long7]).addTo(map).bindPopup()
      .bindPopup(`
              <div class= "flex-wrap" id="map-popup">
                  <p><strong>Airport:</strong> ${locations_list[6][0]}</p>
                  <p><strong>Country:</strong> ${locations_list[7][6][2]}</p>
                  <p><strong>City:</strong> ${locations_list[7][6][0]}</p>
                  <p><strong>Flag:</strong></p>
                  <img src="${locations_list[7][6][1]}" alt="Country Flag" style="width:30px;height:auto;">
              </div>
          `)
          .addTo(markerGroup)

  marker1.on('click', () => {
  console.log(`marker 1 in ${locations_list[7][0][0]} clicked`)});
  marker2.on('click', () => {
  console.log(`marker 2 in ${locations_list[7][1][0]} clicked`)});
  marker3.on('click', () => {
  console.log(`marker 3 in ${locations_list[7][2][0]} clicked`)});
  marker4.on('click', () => {
  console.log(`marker 4 in ${locations_list[7][3][0]} clicked`)});
  marker5.on('click', () => {
  console.log(`marker 5 in ${locations_list[7][4][0]} clicked`)});
  marker6.on('click', () => {
  console.log(`marker 6 in ${locations_list[7][5][0]} clicked`)});
  marker7.on('click', () => {
  console.log(`marker 7 in ${locations_list[7][6][0]} clicked`)});


  let clicked = ''
  function onMapClick(e) {
          clicked = "You clicked the map at " + e.latlng.toString()
          console.log(clicked)
}
map.on('click', onMapClick);
}

async function DeleteMap() {
markerGroup.clearLayers();
}




//const marker = L.marker([lat, long]).addTo(map) //makes a new marker and adds it on the map
    //.bindPopup('Pop-up') //adds the pop-up, here we can add the airport info
    //.openPopup() // opens the pop-up without the marker being clicked, when the marker is created

