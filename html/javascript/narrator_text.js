const li = document.createElement('li');

function addtext(content) {
    const li = document.createElement('li'); // Create a new list item
    li.textContent = content;                // Set the text content of the list item
    printing_text.appendChild(li);           // Append the new list item to the text box
}
const story_text  = "You are a private detective on vacation with your closest friends. You’ve rented a private plane that’s been flying all around Europe. At the end of your trip, in the final country on your itinerary, you discover a body hidden in the cargo hold of the plane. Without hesitation, you put your detective hat back on, determined to catch your friend's killer. Interpol informs you that you have a limited budget of 500 €, and each trip costs 125 €. You must seek justice for your friend by bringing the culprit behind bars. To do so, you’ll need to gather clues about the crime and use them to make accusations about the murderer, the murder weapon, and the country where the crime took place.\n"
const story_ask_text = "Do you wish to read the introduction story? \"yes\" or \"no\": "
const begin_text = "Let the game begin!"
const spelling_text = "check spelling."
const weapon_acc = "Make your weapon accusation."
const suspect_acc = "Who do you suspect?"
const weapon_incorrect = "This was not the murder weapon."
const suspect_incorrect = "They are innocent."
const weapon_correct = "You have the correct weapon!"
const suspect_correct = "You have the correct suspect!"
const location_correct = "You have the correct airport!"
const location_incorrect = "The murder did not happen here."
const location_welcome =`You are currently at the ${airport_name}.`
const check_acc = "You have accused:"
addtext(story_text)
addtext(begin_text)
addtext(spelling_text)
