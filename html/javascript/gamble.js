'use strict';

// FUNCTIONS

async function closeGamble() {
  dicebox.style.display = 'none';
}

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
  return win_stats;
}

async function pay_gambling(cost) {
  try {
    const response = await fetch(`${url_py}/pay/${cost}/`);
    if (!response.ok) {
      throw new Error('Problem with paying gamble');
    }
  } catch (error) {
    console.log(error.message);
  }
}

async function add_money(added) {
  try {
    const response = await fetch(`${url_py}/add-money-gamble/${added}`);
    if (!response.ok) {
      throw new Error('Could not add win money');
    }
  } catch (error) {
    console.log(error.message);
  }
}

// VARIABLES
const roll = document.getElementById('roll');
let dice1 = document.getElementById('dice1');
let dice2 = document.getElementById('dice2');
let dice3 = document.getElementById('dice3');
let win_stats = {};
let win_message = '';
let win_points = 0;
const dicebox = document.getElementById('dicebox');
const end_gamble = document.getElementById('end-gamble');
//const url_py = 'http://127.0.0.1:3000'
const gamble = document.getElementById('gamble-button');
const gamble_alert = document.getElementById('gamble-text');

roll.addEventListener('click', () => {
  const new_dice1 = Math.floor(Math.random() * 12 + 1);
  const new_dice2 = Math.floor(Math.random() * 12 + 1);
  const new_dice3 = Math.floor(Math.random() * 12 + 1);
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
    case 7:
      dice1.src = '/html/img/dice-one.png';
      dice1.alt = 'Dice number one';
      break;
    case 8:
      dice1.src = '/html/img/dice-two.png';
      dice1.alt = 'Dice number two';
      break;
    case 9:
      dice1.src = '/html/img/dice-two.png';
      dice1.alt = 'Dice number two';
      break;
    case 10:
      dice1.src = '/html/img/dice-three.png';
      dice1.alt = 'Dice number three';
      break;
    case 11:
      dice1.src = '/html/img/dice-four.png';
      dice1.alt = 'Dice number four';
      break;
    case 12:
      dice1.src = '/html/img/dice-four.png';
      dice1.alt = 'Dice number four';
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
    case 7:
      dice2.src = '/html/img/dice-one.png';
      dice2.alt = 'Dice number one';
      break;
    case 8:
      dice2.src = '/html/img/dice-two.png';
      dice2.alt = 'Dice number two';
      break;
    case 9:
      dice2.src = '/html/img/dice-two.png';
      dice2.alt = 'Dice number two';
      break;
    case 10:
      dice2.src = '/html/img/dice-three.png';
      dice2.alt = 'Dice number three';
      break;
    case 11:
      dice2.src = '/html/img/dice-four.png';
      dice2.alt = 'Dice number four';
      break;
    case 12:
      dice2.src = '/html/img/dice-four.png';
      dice2.alt = 'Dice number four';
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
    case 7:
      dice3.src = '/html/img/dice-one.png';
      dice3.alt = 'Dice number one';
      break;
    case 8:
      dice3.src = '/html/img/dice-two.png';
      dice3.alt = 'Dice number two';
      break;
    case 9:
      dice3.src = '/html/img/dice-two.png';
      dice3.alt = 'Dice number two';
      break;
    case 10:
      dice3.src = '/html/img/dice-three.png';
      dice3.alt = 'Dice number three';
      break;
    case 11:
      dice3.src = '/html/img/dice-four.png';
      dice3.alt = 'Dice number four';
      break;
    case 12:
      dice3.src = '/html/img/dice-four.png';
      dice3.alt = 'Dice number four';
      break;
    default:
      console.log('what??');
      break;
  }
  gamble_win(new_dice1, new_dice2, new_dice3).then(async (win_stats) => {
    if (win_stats) {
      // console.log(win_stats.message);
      win_message = win_stats.message;
      // console.log(`Points: ${win_stats.points}`);
      win_points = win_stats.points;
    } else {
      console.log('Error occurred while fetching win stats.');
    }

    if (win_points === 0) {
      await game_status()
      await pay_gambling(50);
      let new_budget = check_money();
      let budget = document.getElementById('budget');
      budget.textContent = await new_budget;
      gamble_alert.textContent = 'Sorry, you lost.';
      roll.style.display = 'none';
      end_gamble.style.display = 'flex';
    }

    else if (win_points === 1) {
      await game_status()
      await pay_gambling(50);
      gamble_alert.textContent = 'You got a six, you are winning 100€!';
      roll.style.display = 'none';
      end_gamble.style.display = 'flex';
      await add_money(100);
      let new_budget = check_money();
      let budget = document.getElementById('budget');
      budget.textContent = await new_budget;

    } else if (win_points === 2) {
      await game_status()
      await pay_gambling(50);
      gamble_alert.textContent = 'You have two fives, you win 150€!';
      roll.style.display = 'none';
      end_gamble.style.display = 'flex';
      await add_money(150);
      let new_budget = check_money();
      let budget = document.getElementById('budget');
      budget.textContent = await new_budget;

    } else if (win_points === 3) {
      await game_status()
      await pay_gambling(50);
      gamble_alert.textContent = 'You have two sixes, you are winning 250€!';
      roll.style.display = 'none';
      end_gamble.style.display = 'flex';
      await add_money(250);
      let new_budget = check_money();
      let budget = document.getElementById('budget');
      budget.textContent = await new_budget;


    } else {
      console.log('Something went wrong with winning the gamble.');
    }

  });
});

// opening the gamble dice box and re-setting it for next gamble
gamble.addEventListener('click', async () => {
  await game_status()
  dicebox.style.display = 'flex';
  end_gamble.style.display = 'none';
  roll.style.display = 'flex';
  dice1.src = 'img/dice-six.png';
  dice2.src = 'img/dice-six.png';
  dice3.src = 'img/dice-six.png';
  dice1.alt = 'Dice number six';
  dice2.alt = 'Dice number six';
  dice3.alt = 'Dice number six';
  gamble_alert.textContent = 'Roll the dice for a chance to get more money!';
});



// ending gamble
end_gamble.addEventListener('click', () => {
  dicebox.style.display = 'none';
});