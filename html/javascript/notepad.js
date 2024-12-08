'use strict'

const hintPlaceholder = document.getElementById('hint-holder')
const hintList = document.getElementById('hint-list')
const newgameButton = document.getElementById('newgame-button')
const accuseButton = document.getElementById('accuse-button')


// emptying the notepad for a new game
newgameButton.addEventListener('click', () => {
  hintList.innerHTML = ''
})



