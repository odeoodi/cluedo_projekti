'use strict'

// this is url to python and after this add the flask address
// const url_py = 'http://127.0.0.1:3000'
const overlay = document.querySelector('#overlay')
const popup = document.querySelector('#popup')

let weapons_list = {}
let suspects_list = {}
let locations_list = {}
let player_name = document.querySelector('#player-id')

let weapon = ''
let suspect = ''
let location_game = ''

function showpopup() {
    overlay.style.display = 'block'
    popup.style.display = 'block' }
function closepopup() {
    overlay.style.display = 'none'
    popup.style.display = 'none' }

async function enter_name(){
    showpopup()
    document.querySelector('#start_newgame').addEventListener('click', () => {
        const new_name = document.querySelector('#player_nameInput').value
        player_name.innerText = new_name
        closepopup()})
    document.querySelector('#cance_newgame').addEventListener('click', () => {closepopup()})
    get_lists()
}

async function get_lists() {
    try {
    const response = await fetch( `${url_py}/getweapons`)
    if (!response.ok) throw new Error("something went wrong weapons")
    weapons_list = await response.json()
    const response2 = await fetch( `${url_py}/getsuspects`)
    if (!response2.ok) throw new Error("something went wrong suspects")
    suspects_list = await response2.json()
    const response3 = await fetch( `${url_py}/getlocations`)
    if (!response3.ok) throw new Error("something went wrong locations")
    locations_list = await response3.json()
    console.log(weapons_list, suspects_list, locations_list)
    return{
        weapons_list,
        suspects_list,
        locations_list,
        }

  } catch (error){
      console.log(error.message)
      }}

async function start_newgame() {
    try {
    // MUITSTA DOMITAA TEKSTIT POIS NARRATORISTA
    const response = await fetch( `${url_py}/new_game`)
    if (!response.ok) throw new Error("something went wrong new game")
    console.log(response)
    enter_name()
        // dom komento joka otaa lore.js muutujan intro ja laitaa sen narratoreen.

  } catch (error){
      console.log(error.message)}}

async function check_money () {
    try {
    const response = await fetch( `${url_py}/checkmoney`)
    if (!response.ok) throw new Error("money not found")
    const money_at_bank = await response.json()
    console.log(money_at_bank)
    return money_at_bank
      } catch (error){
      console.log(error.message)}}

function fail(){
    const texts = document.querySelector('#popup')
    const no_needed = document.querySelectorAll('h2, #player_nameInput,#cance_newgame')
    no_needed.forEach(element => {element.remove()})
    const loost_text = document.createElement('h2')
    loost_text.textContent = 'Oh no! You have run out of the money!\nGame Over!'
    loost_text.style.fontSize = '1.4rem'
    texts.appendChild(loost_text)
    const new_game_button = document.querySelector('#start_newgame')
    new_game_button.innerText = 'Ok'
    new_game_button.addEventListener('click', () => {closepopup()})
    new_game_button.style.transform = 'scale(1.5)'
    texts.appendChild(new_game_button)
    showpopup()
}

async function game_status () {
    try {
        const response = await fetch( `${url_py}/game_status`)
        if (!response.ok) throw new Error("game_status is wierd")
        let game_status_is = await response.json()
        console.log(game_status_is.status )
        switch (game_status_is.status) {
            case 'loose' :
                return fail()
            case 'win' :
                return game_status_is
            default:
                return console.log('lul nothing')
        }
        } catch (error){
      console.log(error.message)}}


function first_start() {
    if (player_name.textContent === 'ID'){
        enter_name()
    }}
// let's use it when we need it: first_start()

async function accuse() {
    try {
        const response = await fetch( `${url_py}/accuse/${weapon}/${suspect}/${location_game}`)
        if (!response.ok) throw new Error("something went wrong")
        let result = await response.json()
        console.log(result)
        } catch (error){
      console.log(error.message)}}

document.querySelector('#newgame-button').addEventListener('click', (e) => {
  start_newgame()})



function selectImage(img) {
        // Remove 'pressed' class from all images
        const allImages = document.querySelectorAll('.img_wrapper img');
        allImages.forEach(image => image.classList.remove('pressed'));

        // Add 'pressed' class to the clicked image
        img.classList.add('pressed')
  }