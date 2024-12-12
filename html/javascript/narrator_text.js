
const printing_text = document.getElementById('printing_text');
const new_game_text = ``
const story_text  = `You are a private detective on vacation with your closest friends. You’ve rented a private plane that’s been flying all around Europe. At the end of your trip, in the final country on your itinerary, you discover a body hidden in the cargo hold of the plane. Without hesitation, you put your detective hat back on, determined to catch your friend's killer. Interpol informs you that you have a limited budget of 500 €, and each trip costs 125 €. You must seek justice for your friend by bringing the culprit behind bars. To do so, you’ll need to gather clues about the crime and use them to make accusations about the murderer, the murder weapon, and the country where the crime took place.`
const begin_text = `Let the game begin!`
const gamble_lose_text = `Tough luck chump, but you know what they say; "99% of gamblers guit before hitting big"`
const gamble_win_text1 = `Scoffs* Beginner's luck.`
const gamble_win_text2 = `Well ain't you a lucky feller.`
const gamble_win_text3 = `Lady Luck must really like ya.`
const location_welcome =`You have landed.`
const out_of_monney = `You have run out of money to fly. Try gambling to win some more.`
const saved_game = `Game saved!`
const load_game_text = `Game loaded!`

async function addtext(content) {
    const li = document.createElement('li');
    printing_text.appendChild(li).textContent = content;
}
