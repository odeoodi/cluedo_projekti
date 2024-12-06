'use strict'

// this is url to python and after this add the flask address
const url_py = 'http://127.0.0.1:3000'
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
    const weapons_list = await response.json()
    const response2 = await fetch( `${url_py}/getsuspects`)
    if (!response2.ok) throw new Error("something went wrong suspects")
    const suspects_list = await response2.json()
    const response3 = await fetch( `${url_py}/getlocations`)
    if (!response3.ok) throw new Error("something went wrong locations")
    const locations_list = await response3.json()
    console.log(weapons_list)
    console.log(suspects_list)
    console.log(locations_list)
  } catch (error){
      console.log(error.message)
      }}

async function start_newgame() {
    try {
    const response = await fetch( `${url_py}/new_game`)
    if (!response.ok) throw new Error("something went wrong new game")
    console.log(response)
    enter_name()
  } catch (error){
      console.log(error.message)}}

async function check_money () {
    try {
    const response = await fetch( `${url_py}/checkmoney`)
    if (!response.ok) throw new Error("money not found")
    const money_at_bank = await response.json()
        console.log(money_at_bank)
      } catch (error){
      console.log(error.message)
      }}

function first_start() {
    if (player_name.textContent === 'ID'){
        enter_name()
    }}
// lets use it when we need it: first_start()


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


// gamble pop-up

// gamble pop-up ends

// things we need for the map

// map stuff ends