'use strict'

// this is url to python and after this add the flask address
const url_py = 'http://127.0.0.1:3000'

let weapons_list = {}
let suspects_list = {}
let locations_list = {}

let weapon = ''
let suspect = ''
let location = ''


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
get_lists()

async function start_newgame() {
    try {
    const response = await fetch( `${url_py}/new_game`)
    if (!response.ok) throw new Error("something went wrong")
    console.log(response)
        get_lists()
  } catch (error){
      console.log(error.message)}}

async function accuse() {
    try {
        const response = await fetch( `${url_py}/accuse/${weapon}/${suspect}/${location}`)
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