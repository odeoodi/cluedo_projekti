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
        document.querySelector('#accuse-button').disabled = false
        document.querySelector('#gamble-button').disabled = false
        document.querySelector('#fly-button').disabled = false
        printing_text.innerHTML = ''
        closepopup()
        loading_stuff = true
        loading()
        await start_newgame()
        await player_name_save()
        await get_locations()
        await get_lists()
        await DeleteMap()
        await CreateMap()
        await changePins()
        await closeGamble()
        await add_to_hover()
        const stat_money = await check_money()
        let budget = document.getElementById('budget')
        budget.textContent = stat_money
        await addtext(story_text)
        await addtext(begin_text)
        loading_stuff = false
        closepopup()}
    input.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {start_click()}})
    start_button.addEventListener('click', async () => {start_click()})
    cancel_button.addEventListener('click', async () => {closepopup()})}

async function help_pop(){
    showpopup()
    const container = document.querySelector('#popup')
    container.innerHTML = ''
    const fragment = document.createDocumentFragment()
    const header = document.createElement('h2')
    Object.assign(header, {
        id: 'popup_h2',
        textContent: 'Need help?'
    })
    const close_button = document.createElement('button')
        Object.assign(close_button, {
            id: 'close_button',
            className: "selection",
            textContent: 'Close' })
    close_button.addEventListener('click', async () => {closepopup()})
    const help_text_container = document.createElement('div')
    help_text_container.innerHTML = help_text_html
    fragment.appendChild(help_text_container)
    fragment.appendChild(close_button)
    container.appendChild(fragment)

}

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
    document.querySelector('#fly-button').disabled = true
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

async function hintThis(weapon, suspect, location) {
    try {
        const response = await fetch(`${url_py}/hints/${weapon}/${suspect}/${location}`)
        if (!response.ok) throw new Error("something went wrong hints")
        let result = await response.json()
        console.log(result)
    } catch (error){
      console.log(error.message)}
}

async function accuse(weapon,suspect) {
    try {
        const response = await fetch( `${url_py}/accuse/${weapon}/${suspect}/${location_game}`)
        if (!response.ok) throw new Error("something went wrong")
        let result = await response.json()
        console.log(result)
        } catch (error){
      console.log(error.message)}}

function selectImage(imgElement) {
    // Find the parent category (suspect or weapon) of the clicked image
    const category = imgElement.closest('.image-container').parentElement;

    // Remove 'pressed' class from all image containers in the same category
    const allImageContainersInCategory = category.querySelectorAll('.image-container');
    allImageContainersInCategory.forEach(container => container.classList.remove('pressed'));

    // Add 'pressed' class to the clicked image container
    imgElement.closest('.image-container').classList.add('pressed');
}

function moveTooltip(event, element) {
    const tooltip = element.querySelector('.tooltip');
    tooltip.style.position = 'absolute'
    tooltip.style.backgroundColor = '#57432E'
    tooltip.style.color = '#EEE9DA'
    tooltip.style.padding = '8px'
    tooltip.style.borderRadius = '5px'
    tooltip.style.whiteSpace = 'nowrap'
    tooltip.style.zIndex = '10'
    tooltip.style.fontSize = '12px'
    tooltip.style.pointerEvents = 'none'
    tooltip.style.display = 'block'
    const mouseX = event.pageX;
    const mouseY = event.pageY;
    tooltip.style.top = mouseY + 10 + 'px';
    tooltip.style.left = mouseX + 10 + 'px';
    }

function hideTooltip(element) {
    const tooltip = element.querySelector('.tooltip');
    tooltip.style.display = 'none';

}

const idList = ["suspect","weapon"]

async function ButtonChooserSuspect(button) {
    idList[0]=button.id
    console.log("Suspect selected:", idList[0]);
}

async function ButtonChooserWeapon(button) {
    idList[1]=button.id
    console.log("weapon selected:", idList[1]);
}

async function accuser() {
    const idListsend = idList
    let dataToSend = {
        suspect: idListsend[0],  // Suspect selected
        weapon: idListsend[1]    // Weapon selected
    };

    try {
        const response = await fetch(`${url_py}/accuse/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dataToSend) })
        if (!response.ok) throw new Error("Something went wrong while fetching hints.")
        const result = await response.json()
        if (!result[0]) {
            const listItem = document.createElement('li')
            hintList.appendChild(listItem).textContent = result[1]
            const li = document.createElement('li');
            printing_text.appendChild(li).textContent = result[1]}
        else
            await win()
        console.log(result);// For debugging
        document.querySelector('#accuse-button').disabled = true
    } catch (error) {
        console.log(error.message);
    }
}

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
