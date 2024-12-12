let note_padtext= `
<li>Lorem ipsumLorem ipsumLorem ipsum</li>
<li>Lorem ipsumLorem ipsumLorem ipsum</li>
<li>Lorem ipsumLorem ipsumLorem ipsum</li>
<li>Lorem ipsumLorem ipsumLorem ipsum</li>
<li>Lorem ipsumLorem ipsumLorem ipsum</li>
<li>Lorem ipsumLorem ipsumLorem ipsum</li>
<li>Lorem ipsumLorem ipsumLorem ipsum</li>
<li>Lorem ipsumLorem ipsumLorem ipsum</li>
<li>Lorem ipsumLorem ipsumLorem ipsum</li>
<li>Lorem ipsumLorem ipsumLorem ipsum</li>
<li>Lorem ipsumLorem ipsumLorem ipsum</li>
<li>Lorem ipsumLorem ipsumLorem ipsum</li>
`
let narrtext= `
<p>3Lorem ipsumLorem ipsumLorem ipsum</p>
<p>3Lorem ipsumLorem ipsumLorem ipsum</p>
<p>3Lorem ipsumLorem ipsumLorem ipsum</p>
<p>3Lorem ipsumLorem ipsumLorem ipsum</p>
<p>3Lorem ipsumLorem ipsumLorem ipsum</p>
<p>3Lorem ipsumLorem ipsumLorem ipsum</p>
<p>3Lorem ipsumLorem ipsumLorem ipsum</p>
<p>3Lorem ipsumLorem ipsumLorem ipsum</p>
<p>3Lorem ipsumLorem ipsumLorem ipsum</p>
<p>3Lorem ipsumLorem ipsumLorem ipsum</p>
<p>3Lorem ipsumLorem ipsumLorem ipsum</p>
`



async function add_to_note_padd_load(list_text){
    const hint_box = document.querySelector('#hint-list')
    hint_box.innerHTML=`${list_text}`}

async function add_to_narrator_load(list_text){
    const narator_box = document.querySelector('#narrator_text')
    narator_box.innerHTML=`${list_text}`}

async function player_name_save (){
    const player_name = document.querySelector('#player-id').textContent
    try{
        const response = await fetch(`${url_py}/save_name/${player_name}`)
        if (!response.ok) throw new Error("something went wrong saving name")
        console.log(response)
    }catch(error){console.log(error)}}

async function save() {
    let list_note_text = [note_padtext]
    let list_narrtext = [narrtext]
    let dataToSend = {
        note_text: list_note_text,
        narr_text: list_narrtext }
    try {
        const response = await fetch(`${url_py}/save`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dataToSend)
        })
        if (!response.ok) throw new Error("Something went wrong while saving data.");
        console.log('ok')
        } catch (error) {console.log(error.message)}}

async function load_game() {
    try {
        const response = await fetch(`${url_py}/load`, {})
         if (!response.ok) throw new Error("something went wrong loading")
        const load_data = await response.json()
        console.log(load_data)
        const nottext = load_data.note_text
        const nartext = load_data.narrator_text
        const player_name = load_data.player_name
        await add_to_note_padd_load(nottext[0])
        await add_to_narrator_load(nartext[0])
        console.log(player_name[0])
        const load_name = document.querySelector('#player-id')
        load_name.innerText = player_name[0]
    } catch (error) {console.log(error.message)}}


async function win() {
    showpopup()
    const container = document.querySelector('#popup')
    container.innerHTML = ''
    const fragment = document.createDocumentFragment()
    const header = document.createElement('h2')
    Object.assign(header, {
        id: 'popup_h2',
        textContent: 'You have found the murderer!!!'
    })
    const text = document.createElement('p')
    Object.assign(text, {
        id: 'popup_text',
        textContent: `Congratulations! You've identified the culprit, and the police can now press charges. You've done an amazing job, and I hope you're proud of yourself. Keep up the great work!`
    })
    const close_button = document.createElement('button')
        Object.assign(close_button, {
            id: 'close_button',
            className: "selection",
            textContent: 'Close' })
    close_button.addEventListener('click', async () => {closepopup()})
    fragment.appendChild(header)
    fragment.appendChild(text)
    fragment.appendChild(close_button)
    container.appendChild(fragment)
    document.querySelector('#accuse-button').disabled = true
    document.querySelector('#gamble-button').disabled = true
    document.querySelector('#fly-button').disabled = true
}


async function add_to_hover() {
    const suspects_button_list = [
        villeButton,
        iidaButton,
        odeButton,
        makeButton,
        angelinaButton,
        emmetButton,
        neaButton,
        roopeButton,
        oskariButton,
        lucaButton,
        moriartyButton,
        ghostButton]
    const weapons_listButtons = [fountainPenButton, knifeButton, pistolButton, spoonButton, poisonButton, plasticBagButton, hammerButton, strawButton, brokenGlassBottleButton, glassShardButton, glassAngelButton,  glassTrophyButton, drowningButton, ropeButton, pushedDownButton, ]
    let num1 = 0
    suspects_button_list.forEach(button => {
        let num2 = 0
        const container = document.createElement('div')
        const fragment = document.createDocumentFragment()
        while (num2 < 4) {
            const text = document.createElement('p');
            if ( num2 === 3 ){
                Object.assign(text, {
                    textContent:`Glasses : ${suspects_list[num1][num2]}`});}
            else {
                Object.assign(text, {
                    textContent: suspects_list[num1][num2] });}
        fragment.appendChild(text);
        num2 += 1 }
        container.appendChild(fragment)
        container.classList.add('tooltip')
        container.style.display = 'none'
        container.appendChild(fragment)
        button.appendChild(container)
        num1 += 1 })
    num1 = 0
    weapons_listButtons.forEach(button => {
        console.log(button)
        let num2 = 0
        const container = document.createElement('div')
        const fragment = document.createDocumentFragment()
        while (num2 < 3) {
            const text = document.createElement('p');
                Object.assign(text, {
                    textContent: weapons_list[num1][num2] })
            console.log(weapons_list[num1][num2])
        fragment.appendChild(text);
        num2 += 1 }
        container.appendChild(fragment)
        container.classList.add('tooltip')
        container.style.display = 'none'
        container.appendChild(fragment)
        button.appendChild(container)
        num1 += 1})
            console.log(weapons_listButtons)

}

