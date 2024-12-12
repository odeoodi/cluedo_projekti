'use strict'

const overlay = document.querySelector('#overlay')
const popup = document.querySelector('#popup')
const fly_button = document.getElementById('fly-button')
const help_button = document.querySelector('#help-button')
const new_game_button = document.querySelector('#newgame-button')
const save_button = document.querySelector('#save-button')
const load_button = document.querySelector('#load-button')

let loading_stuff = false

let weapons_list = {}
let suspects_list = {}
let locations_list = {}
let player_name = document.querySelector('#player-id')

const flyPopup = document.getElementById('fly-popup')

let weapon = ''
let suspect = ''
let location_game = ''


help_button.addEventListener('click', async () => {
    await help_pop()})

new_game_button.addEventListener('click', async (e) => {
  enter_name()})

save_button.addEventListener('click', async (e) => {await save()})

load_button.addEventListener('click', async (e) => {await load_game()})

fly_button.addEventListener('click', async () => {
    await game_status()
    flyPopup.style.display = 'block'
    overlay.style.display = 'block'
    await createIcaoButtons() // also adds an event listener for icao buttons, where we can use the fly function
})

const odeButton = document.getElementById('ode')
const iidaButton = document.getElementById('iida')
const angelinaButton = document.getElementById('angelina')
const villeButton = document.getElementById('ville')
const makeButton = document.getElementById('make')
const roopeButton = document.getElementById('roope')
const oskariButton = document.getElementById('oskari')
const lucaButton = document.getElementById('luca')
const neaButton = document.getElementById('nea')
const emmetButton = document.getElementById('emmet')
const moriartyButton = document.getElementById('moriarty')
const ghostButton = document.getElementById('the-Ghost-of-the-Late-Queen-of-England')
const poisonButton = document.getElementById('poison')
const ropeButton = document.getElementById('rope')
const pistolButton = document.getElementById('pistol')
const glassAngelButton = document.getElementById('glassAngel')
const glassShardButton = document.getElementById('glassShard')
const drowningButton = document.getElementById('drowning')
const pushedDownButton = document.getElementById('pushedDown')
const fountainPenButton = document.getElementById('fountainPen')
const spoonButton = document.getElementById('spoon')
const brokenGlassBottleButton = document.getElementById('brokenGlassBottle')
const glassTrophyButton = document.getElementById('glassTrophy')
const strawButton = document.getElementById('straw')
const hammerButton = document.getElementById('hammer')
const knifeButton = document.getElementById('knife')
const plasticBagButton = document.getElementById('plasticBag')

document.getElementById('accuse-button').addEventListener('click', () => accuser())
odeButton.addEventListener('click', () => ButtonChooserSuspect(odeButton))
iidaButton.addEventListener('click', () => ButtonChooserSuspect(iidaButton))
angelinaButton.addEventListener('click', () => ButtonChooserSuspect(angelinaButton))
villeButton.addEventListener('click', () => ButtonChooserSuspect(villeButton))
makeButton.addEventListener('click', () => ButtonChooserSuspect(makeButton))
roopeButton.addEventListener('click', () => ButtonChooserSuspect(roopeButton))
emmetButton.addEventListener('click', () => ButtonChooserSuspect(emmetButton))
lucaButton.addEventListener('click', () => ButtonChooserSuspect(lucaButton))
neaButton.addEventListener('click', () => ButtonChooserSuspect(neaButton))
oskariButton.addEventListener('click', () => ButtonChooserSuspect(oskariButton))
moriartyButton.addEventListener('click', () => ButtonChooserSuspect(moriartyButton))
ghostButton.addEventListener('click', () => ButtonChooserSuspect(ghostButton))

fountainPenButton.addEventListener('click', () => ButtonChooserWeapon(fountainPenButton))
knifeButton.addEventListener('click', () => ButtonChooserWeapon(knifeButton))
pistolButton.addEventListener('click', () => ButtonChooserWeapon(pistolButton))
spoonButton.addEventListener('click', () => ButtonChooserWeapon(spoonButton))
poisonButton.addEventListener('click', () => ButtonChooserWeapon(poisonButton))
plasticBagButton.addEventListener('click', () => ButtonChooserWeapon(plasticBagButton))
hammerButton.addEventListener('click', () => ButtonChooserWeapon(hammerButton))
strawButton.addEventListener('click', () => ButtonChooserWeapon(strawButton))
brokenGlassBottleButton.addEventListener('click', () => ButtonChooserWeapon(brokenGlassBottleButton))
glassAngelButton.addEventListener('click', () => ButtonChooserWeapon(glassAngelButton))
glassTrophyButton.addEventListener('click', () => ButtonChooserWeapon(glassTrophyButton))
drowningButton.addEventListener('click', () => ButtonChooserWeapon(drowningButton))
ropeButton.addEventListener('click', () => ButtonChooserWeapon(ropeButton))
pushedDownButton.addEventListener('click', () => ButtonChooserWeapon(pushedDownButton))
glassShardButton.addEventListener('click', () => ButtonChooserWeapon(glassShardButton))
