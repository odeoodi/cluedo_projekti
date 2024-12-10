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

async function load() {
    try {
        const response = await fetch(`${url_py}/load`, {})
         if (!response.ok) throw new Error("something went wrong loading")
        const load_data = await response.json()
        console.log(load_data)
        const nottext = load_data.note_text
        const nartext = load_data.narrator_text
        await add_to_note_padd_load(nottext[0])
        await add_to_narrator_load(nartext[0])
    } catch (error) {console.log(error.message)}}