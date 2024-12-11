'use strict'
// VARIABLES
let airport_ICAO = ''
let airport_name = ''
const map = L.map('map').setView([48.499998, 23.3833318 ], 3.4);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'}).addTo(map);

const url_py = 'http://127.0.0.1:3000'

const markerGroup = L.layerGroup().addTo(map);

const bluePin = L.icon({
    iconUrl: 'pindrop_blue.png',
    iconSize:     [25, 41], // size of the icon
    iconAnchor:   [25/2, 41] , // point of the icon which will correspond to marker's location
    popupAnchor:  [0, -44] // point from which the popup should open relative to the iconAnchor
});

const redPin = L.icon({
    iconUrl: 'pindrop_red.png',
    iconSize:     [25, 41], // size of the icon
    iconAnchor:   [25 / 2, 41] , // point of the icon which will correspond to marker's location
    popupAnchor:  [0, -44] // point from which the popup should open relative to the iconAnchor
});

const greyPin = L.icon({
    iconUrl: 'pindrop_grey.png',
    iconSize:     [25, 41], // size of the icon
    iconAnchor:   [25 / 2, 41] , // point of the icon which will correspond to marker's location
    popupAnchor:  [0, -44] // point from which the popup should open relative to the iconAnchor
});

const flyList = document.getElementById('fly-list')

// FUNCTIONS

async function fly(airport_name) {
  try {
    const response = await fetch(`${url_py}/fly/${airport_name}`)
    if (!response.ok) {
      throw new Error('Problem flying in js')
    }
  } catch(error) {
    console.log(error.message)
  }
}

async function playerLocation() {
  try {
    const response = await fetch(`${url_py}/player-location-now`)
    if (!response.ok) {
      throw new Error('Location now having issues...')
    }
        return await response.text();
  } catch (error) {
    console.log(error.message)
  }
}

async function CreateMap() {
  let lat1, lat2, lat3, lat4, lat5, lat6, lat7
  let long1, long2, long3, long4, long5, long6, long7

  [lat1, lat2, lat3, lat4, lat5, lat6, lat7] = locations_list.map(
      loc => loc[2]);
  [long1, long2, long3, long4, long5, long6, long7] = locations_list.map(
      loc => loc[3]);

  const marker1 = L.marker([lat1, long1], { icon: redPin}).addTo(map).bindPopup(`
            <div class= "flex-wrap" id="map-popup">
                <p><strong>Airport:</strong> ${locations_list[0][0]}</p>
                <p><strong>Country:</strong> ${locations_list[7][0][2]}</p>
                <p><strong>Capital:</strong> ${locations_list[7][0][0]}</p>
                <p><strong>Flag:</strong></p>
                <img src="${locations_list[7][0][1]}" alt="Country Flag"
                       style="width:30px;height:auto;">
</div>
    `).addTo(markerGroup)
  const marker2 = L.marker([lat2, long2], { icon: redPin}).addTo(map).bindPopup(`
            <div class= "flex-wrap" id="map-popup">
                <p><strong>Airport:</strong> ${locations_list[1][0]}</p>
                <p><strong>Country:</strong> ${locations_list[7][1][2]}</p>
                <p><strong>Capital:</strong> ${locations_list[7][1][0]}</p>
                <p><strong>Flag:</strong></p>
                <img src="${locations_list[7][1][1]}" alt="Country Flag" style="width:30px;height:auto;">
            </div>
        `).addTo(markerGroup)
  const marker3 = L.marker([lat3, long3], { icon: redPin}).addTo(map).bindPopup(`
            <div class= "flex-wrap" id="map-popup">
                <p><strong>Airport:</strong> ${locations_list[2][0]}</p>
                <p><strong>Country:</strong> ${locations_list[7][2][2]}</p>
                <p><strong>Capital:</strong> ${locations_list[7][2][0]}</p>
                <p><strong>Flag:</strong></p>
                <img src="${locations_list[7][2][1]}" alt="Country Flag" style="width:30px;height:auto;">
            </div>
        `).addTo(markerGroup)
  const marker4 = L.marker([lat4, long4], { icon: redPin}).addTo(map).bindPopup(`
              <div class= "flex-wrap" id="map-popup">
                  <p><strong>Airport:</strong> ${locations_list[3][0]}</p>
                  <p><strong>Country:</strong> ${locations_list[7][3][2]}</p>
                  <p><strong>Capital:</strong> ${locations_list[7][3][0]}</p>
                  <p><strong>Flag:</strong></p>
                  <img src="${locations_list[7][3][1]}" alt="Country Flag" style="width:30px;height:auto;">
              </div>
          `).addTo(markerGroup)
  const marker5 = L.marker([lat5, long5], { icon: redPin}).addTo(map).bindPopup(`
              <div class= "flex-wrap" id="map-popup">
                  <p><strong>Airport:</strong> ${locations_list[4][0]}</p>
                  <p><strong>Country:</strong> ${locations_list[7][4][2]}</p>
                  <p><strong>Capital:</strong> ${locations_list[7][4][0]}</p>
                  <p><strong>Flag:</strong></p>
                  <img src="${locations_list[7][4][1]}" alt="Country Flag" style="width:30px;height:auto;">
              </div>
          `).addTo(markerGroup)
  const marker6 = L.marker([lat6, long6], { icon: redPin}).addTo(map).bindPopup(`
              <div class= "flex-wrap" id="map-popup">
                  <p><strong>Airport:</strong> ${locations_list[5][0]}</p>
                  <p><strong>Country:</strong> ${locations_list[7][5][2]}</p>
                  <p><strong>Capital:</strong> ${locations_list[7][5][0]}</p>
                  <p><strong>Flag:</strong></p>
                  <img src="${locations_list[7][5][1]}" alt="Country Flag" style="width:30px;height:auto;">
              </div>
          `).addTo(markerGroup)
  const marker7 = L.marker([lat7, long7], { icon: redPin}).addTo(map).bindPopup(`
              <div class= "flex-wrap" id="map-popup">
                  <p><strong>Airport:</strong> ${locations_list[6][0]}</p>
                  <p><strong>Country:</strong> ${locations_list[7][6][2]}</p>
                  <p><strong>Capital:</strong> ${locations_list[7][6][0]}</p>
                  <p><strong>Flag:</strong></p>
                  <img src="${locations_list[7][6][1]}" alt="Country Flag" style="width:30px;height:auto;">
              </div>
          `).addTo(markerGroup)
}

async function createIcaoButtons() {
  for (let i = 0; i < 7; i++) {
    if (flyList.querySelector('button')) {
      flyList.removeChild(flyList.querySelector('button'))
    }
  }

  for (let i = 0; i < 7; i++) {
    if (await playerLocation() !== locations_list[i][0]) {
      flyList.appendChild(document.createElement('button')).textContent = locations_list[i][0]
    }
  }
  const icao_buttons = flyList.querySelectorAll('button')

  icao_buttons.forEach(button => {
  button.addEventListener('click', async () => {
    await fly(button.textContent);
    let new_budget = check_money();
    let budget = document.getElementById('budget');
    budget.textContent = await new_budget
    flyPopup.style.display = 'none'
    await changePins()
    showpopup()
    popup.textContent = `Welcome to: ${button.textContent}`
    setTimeout( () => {
      popup.style.display = 'none'
      overlay.style.display = 'none'
    }, 2000)
  });
});
}

async function DeleteMap() {
markerGroup.clearLayers();
}


async function checkPinColor(marker_num,airport_name) {
  if (await playerLocation() === airport_name) {
    marker_num.setIcon(redPin);
  }
  // else if (airport_ICAO === accused_ICAO) {
//    marker_num.setIcon(greyPin);
// }
  else {
    marker_num.setIcon(bluePin);
  }

}
async function changePins(){
  const layers = markerGroup.getLayers();
  for (let i = 0; i < layers.length; i++) {
    if (locations_list[i]) {
      await checkPinColor(layers[i], locations_list[i][0]);
    } else {
      console.error(`No data for marker at index ${i}`);
    }
  }
}




