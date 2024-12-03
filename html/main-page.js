'use strict'

// this is url to python and after this add the flask address
const url_py = 'http://127.0.0.1:3000'


async function start_newgame() {
    try {
    const response = await fetch( `${url_py}/new_game`)
    if (!response.ok) throw new Error("something went wrong")
    console.log(response)
  } catch (error){
      console.log(error.message)
    }
}





document.querySelector('#newgame').addEventListener('click', (e) => {
  start_newgame()
})