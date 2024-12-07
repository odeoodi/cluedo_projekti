'use strict';
// FUNCTIONS
async function gamble_win(new_dice1, new_dice2, new_dice3) {
  try {
    const response = await fetch(
        `${url_py}/gamble_winning/${new_dice1}/${new_dice2}/${new_dice3}`);
    if (!response.ok) {
      throw new Error('Dice not working');
    }
    win_stats = await response.json();
    console.log(win_stats);
  } catch (error) {
    console.log(error.message);
  }
  return win_stats
}

async function pay_gambling(cost,select_game) {
  try {
    const response = await fetch(`${url_py}/pay/${cost}/${select_game}`)
    if (!response.ok) {
      throw new Error('Problem with paying gamble')
    }
  } catch (error) {
    console.log(error.message)
  }
}

async function add_money(added,select_game) {
  try {
    const response = await fetch(`${url_py}/add-money-gamble/${added}/${select_game}`)
    if (!response.ok) {
      throw new Error('Could not add win money')
    }
  } catch (error) {
    console.log(error.message)
  }
}


// VARIABLES
const roll = document.getElementById('roll');
let dice1 = document.getElementById('dice1');
let dice2 = document.getElementById('dice2');
let dice3 = document.getElementById('dice3');
let win_stats = {};
let win_message = ''
let win_points = 0
const dicebox = document.getElementById('dicebox');
const end_gamble = document.getElementById('end-gamble')
const url_py = 'http://127.0.0.1:3000'
const gamble = document.getElementById('gamble-button');
const rollDice = document.getElementById('roll')
const gamble_alert = document.getElementById('gamble-text')

roll.addEventListener('click', () => {
  const new_dice1 = Math.floor(Math.random() * 6 + 1);
  const new_dice2 = Math.floor(Math.random() * 6 + 1);
  const new_dice3 = Math.floor(Math.random() * 6 + 1);
  // first dice
  switch (new_dice1) {
    case 1:
      dice1.src = '/html/img/dice-one.png';
      dice1.alt = 'Dice number one';
      break;
    case 2:
      dice1.src = '/html/img/dice-two.png';
      dice1.alt = 'Dice number two';
      break;
    case 3:
      dice1.src = '/html/img/dice-three.png';
      dice1.alt = 'Dice number three';
      break;
    case 4:
      dice1.src = '/html/img/dice-four.png';
      dice1.alt = 'Dice number four';
      break;
    case 5:
      dice1.src = '/html/img/dice-five.png';
      dice1.alt = 'Dice number five';
      break;
    case 6:
      dice1.src = '/html/img/dice-six.png';
      dice1.alt = 'Dice number six';
      break;
    default:
      console.log('what??');
      break;
  }
  // second dice
  switch (new_dice2) {
    case 1:
      dice2.src = '/html/img/dice-one.png';
      dice2.alt = 'Dice number one';
      break;
    case 2:
      dice2.src = '/html/img/dice-two.png';
      dice2.alt = 'Dice number two';
      break;
    case 3:
      dice2.src = '/html/img/dice-three.png';
      dice2.alt = 'Dice number three';
      break;
    case 4:
      dice2.src = '/html/img/dice-four.png';
      dice2.alt = 'Dice number four';
      break;
    case 5:
      dice2.src = '/html/img/dice-five.png';
      dice2.alt = 'Dice number five';
      break;
    case 6:
      dice2.src = '/html/img/dice-six.png';
      dice2.alt = 'Dice number six';
      break;
    default:
      console.log('what??');
      break;
  }
  // third dice
  switch (new_dice3) {
    case 1:
      dice3.src = '/html/img/dice-one.png';
      dice3.alt = 'Dice number one';
      break;
    case 2:
      dice3.src = '/html/img/dice-two.png';
      dice3.alt = 'Dice number two';
      break;
    case 3:
      dice3.src = '/html/img/dice-three.png';
      dice3.alt = 'Dice number three';
      break;
    case 4:
      dice3.src = '/html/img/dice-four.png';
      dice3.alt = 'Dice number four';
      break;
    case 5:
      dice3.src = '/html/img/dice-five.png';
      dice3.alt = 'Dice number five';
      break;
    case 6:
      dice3.src = '/html/img/dice-six.png';
      dice3.alt = 'Dice number six';
      break;
    default:
      console.log('what??');
      break;
  }
  gamble_win(new_dice1, new_dice2, new_dice3).then(async (win_stats) => {
    if (win_stats) {
      // console.log(win_stats.message);
      win_message = win_stats.message
      // console.log(`Points: ${win_stats.points}`);
      win_points = win_stats.points
    } else {
      console.log("Error occurred while fetching win stats.");
    }
    if (win_points === 0) {
      gamble_alert.textContent = 'Sorry, you lost.'
      end_gamble.style.display = 'flex'

    } else if (win_points === 1) {
      gamble_alert.textContent = 'You have two fives, you are winning 100€!'
      await add_money(100, 1)
      let new_budget = check_money()
      let budget = document.getElementById('budget')
      budget.textContent = await new_budget
      end_gamble.style.display = 'flex'

    } else if (win_points === 2) {
      gamble_alert.textContent = 'You have two sixes, you are winning 150€!'
      await add_money(150, 1)
      let new_budget = check_money()
      let budget = document.getElementById('budget')
      budget.textContent = await new_budget
      end_gamble.style.display = 'flex'

    } else if (win_points === 3) {
      gamble_alert.textContent = 'You have three ones, you are winning 250€!'
      await add_money(250, 1)
      let new_budget = check_money()
      let budget = document.getElementById('budget')
      budget.textContent = await new_budget
      end_gamble.style.display = 'flex'
    }
    else {
      console.log('Something went wrong with winning the gamble.')
    }

  });
})

 // opening the gamble dice box
  gamble.addEventListener('click', () => {
    dicebox.style.display = 'flex';
  });

  // paying the gamble
rollDice.addEventListener('click', async () => {
  await pay_gambling(50, 1)
  let new_budget = check_money()
  let budget = document.getElementById('budget')
  budget.textContent = await new_budget
})