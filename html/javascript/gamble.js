'use strict';

const roll = document.getElementById('roll');
let dice1 = document.getElementById('dice1');
let dice2 = document.getElementById('dice2');
let dice3 = document.getElementById('dice3');

roll.addEventListener('click', () => {
      const new_dice1 = Math.floor(Math.random() * 6 + 1);
      const new_dice2 = Math.floor(Math.random() * 6 + 1);
      const new_dice3 = Math.floor(Math.random() * 6 + 1);

      switch (new_dice1) {
            case 1:
                  dice1.src = '/html/img/dice-one.png'
                dice1.alt = 'Dice number one'
          break
            case 2:
                  dice1.src = '/html/img/dice-two.png'
                dice1.alt = 'Dice number two'
          break
            case 3:
                  dice1.src = '/html/img/dice-three.png'
                dice1.alt = 'Dice number three'
          break
            case 4:
                  dice1.src = '/html/img/dice-four.png'
                dice1.alt = 'Dice number four'
          break
            case 5:
                  dice1.src = '/html/img/dice-five.png'
                dice1.alt = 'Dice number five'
          break
            case 6:
                  dice1.src = '/html/img/dice-six.png'
                dice1.alt = 'Dice number six'
          break
            default:
                  console.log('what??')
                break}
                // second dice
    switch (new_dice2) {
      case 1:
            dice2.src = '/html/img/dice-one.png'
          dice2.alt = 'Dice number one'
    break
      case 2:
            dice2.src = '/html/img/dice-two.png'
          dice2.alt = 'Dice number two'
    break
      case 3:
            dice2.src = '/html/img/dice-three.png'
          dice2.alt = 'Dice number three'
    break
      case 4:
            dice2.src = '/html/img/dice-four.png'
          dice2.alt = 'Dice number four'
    break
      case 5:
            dice2.src = '/html/img/dice-five.png'
          dice2.alt = 'Dice number five'
    break
      case 6:
            dice2.src = '/html/img/dice-six.png'
          dice2.alt = 'Dice number six'
    break
      default:
            console.log('what??')
        break
      }
      // third dice
      switch (new_dice3) {
      case 1:
            dice3.src = '/html/img/dice-one.png'
          dice3.alt = 'Dice number one'
    break
      case 2:
            dice3.src = '/html/img/dice-two.png'
          dice3.alt = 'Dice number two'
    break
      case 3:
            dice3.src = '/html/img/dice-three.png'
          dice3.alt = 'Dice number three'
    break
      case 4:
            dice3.src = '/html/img/dice-four.png'
          dice3.alt = 'Dice number four'
    break
      case 5:
            dice3.src = '/html/img/dice-five.png'
          dice3.alt = 'Dice number five'
    break
      case 6:
            dice3.src = '/html/img/dice-six.png'
          dice3.alt = 'Dice number six'
    break
      default:
            console.log('what??')
        break
      }
    }
);

const gamble = document.getElementById('gamble-button')
const dicebox = document.getElementById('dicebox')
gamble.addEventListener('click', () => {
  dicebox.style.display = 'flex'
})