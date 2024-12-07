'use strict'

// this is url to python and after this add the flask address
// const url_py = 'http://127.0.0.1:3000'
const overlay = document.querySelector('#overlay')
const popup = document.querySelector('#popup')

let loading_stuff = false

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

function loading() {
    showpopup()
    const container = document.querySelector('#popup')
    container.innerHTML = ''
    const fragment = document.createDocumentFragment()
    const text_thing = document.createElement('h2')
    Object.assign(text_thing, {
        id: 'popup_h2',
        textContent: 'Loading data'
    })
    fragment.appendChild(text_thing)
    container.appendChild(fragment)

    function dotst() {
        if (!loading_stuff) return
        let i = 0;
        const interval = setInterval(() => {
            if (i < 3) {
                text_thing.textContent = 'Loading data' + '.'.repeat(i + 1)
                i++
            } else {
                clearInterval(interval)
                setTimeout(() => {
                    text_thing.textContent = 'Loading data'
                    dotst()
                }, 800)
            }
        }, 600)
    }
    dotst()
}

async function get_locations(){
    loading_stuff = true

    try {
        const response3 = await fetch(`${url_py}/getlocations`)
        if (!response3.ok) throw new Error("something went wrong locations")
        locations_list = await response3.json()
        console.log(locations_list)

        return locations_list

    }catch(error){console.log(error)}}

async function get_lists() {
    try {
    const response = await fetch( `${url_py}/getweapons`)
    if (!response.ok) throw new Error("something went wrong weapons")
    const response2 = await fetch( `${url_py}/getsuspects`)
    if (!response2.ok) throw new Error("something went wrong suspects")
    weapons_list = await response.json()
    suspects_list = await response2.json()
    console.log(weapons_list, suspects_list)
    return{
        weapons_list,
        suspects_list,
        }} catch (error) {console.log(error.message)}}

async function check_money () {
    try {
    const response = await fetch( `${url_py}/checkmoney`)
    if (!response.ok) throw new Error("money not found")
    const money_at_bank = await response.json()
    console.log(money_at_bank)
    return money_at_bank
      } catch (error){
      console.log(error.message)}}

async function start_newgame() {
    try {
    const response = await fetch( `${url_py}/new_game`)
    if (!response.ok) throw new Error("something went wrong new game")
    console.log(response)
  } catch (error){
      console.log(error.message)}}

async function enter_name(){
    const container = document.querySelector('#popup')
    container.innerHTML = ''
    const fragment = document.createDocumentFragment()
    const text_thing = document.createElement('h2')
        Object.assign(text_thing,{
            id: 'popup_h2',
            textContent: 'Start a new game by writing your name:' })
    const start_button = document.createElement('button')
        Object.assign(start_button, {
            id: 'start_newgame',
            className: "selection",
            textContent: 'Start' })
    const cancel_button = document.createElement('button')
        Object.assign(cancel_button, {
            id: 'cance_newgame',
            className: "selection",
            textContent: 'Cancel' })
    const input = document.createElement('input')
        Object.assign(input, {
            type: 'text',
            id: 'player_nameInput',
            placeholder: 'Your name' })
    const button_cont = document.createElement('div')
        Object.assign(button_cont, {
            id: 'button_cont' })
    button_cont.appendChild(start_button)
    button_cont.appendChild(cancel_button)
    fragment.appendChild(text_thing)
    fragment.appendChild(input)
    fragment.appendChild(button_cont)
    container.appendChild(fragment)
    showpopup()
    async function start_click() {
        const new_name = document.querySelector('#player_nameInput').value
        player_name.innerText = new_name
        const stat_money = await check_money()
        let budget = document.getElementById('budget')
        budget.textContent = stat_money
        document.querySelector('#accuse-button').disabled = false
        document.querySelector('#gamble-button').disabled = false
        const narrator_text = document.querySelector('#printing_text')
        narrator_text.textContent = ''
        closepopup()
        loading_stuff = true
        loading()
        await start_newgame()
        await get_locations()
        await get_lists()
        loading_stuff = false
        closepopup()}
    input.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {start_click()}})
    start_button.addEventListener('click', async () => {start_click()})
    cancel_button.addEventListener('click', async () => {closepopup()})}

function fail(){
    const texts = document.querySelector('#popup')
    const fragment = document.createDocumentFragment()
    texts.innerHTML = ''
    const loost_text = document.createElement('h2')
        Object.assign(loost_text, {
        id: 'loost_newgame',
        textContent: 'Oh no! You have run out of the money!\nGame Over!'})
        loost_text.style.fontSize = '20px'
    const ok_button = document.createElement('button')
        Object.assign(ok_button, {
        id: 'ok',
        className: "selection",
        innerText: 'Ok',})
        ok_button.style.paddingLeft = '10px'
        ok_button.style.paddingRight = '10px'
        ok_button.style.transform = 'scale(1.5)'
    ok_button.addEventListener('click', () => {closepopup()})
    fragment.appendChild(loost_text)
    fragment.appendChild(ok_button)
    texts.appendChild(fragment)
    document.querySelector('#dicebox').style.display = 'none'
    document.querySelector('#accuse-button').disabled = true
    document.querySelector('#gamble-button').disabled = true
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

document.querySelector('#newgame-button').addEventListener('click', async (e) => {
  enter_name()})


function selectImage(img) {
        // Remove 'pressed' class from all images
        const allImages = document.querySelectorAll('.img_wrapper img');
        allImages.forEach(image => image.classList.remove('pressed'));

        // Add 'pressed' class to the clicked image
        img.classList.add('pressed')
  }