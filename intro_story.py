import textwrap

story = '''
You are a private detective on vacation with your closest friends. You’ve rented a private plane that’s been flying all around Europe. At the end of your trip, in the final country on your itinerary, you discover a body hidden in the cargo hold of the plane. Without hesitation, you put your detective hat back on, determined to catch your friend's killer. Interpol informs you that you have a limited budget of 500 €, and each trip costs 125 €. You must seek justice for your friend by bringing the culprit behind bars. To do so, you’ll need to gather clues about the crime and use them to make accusations about the murderer, the murder weapon, and the country where the crime took place.
'''

wrapper = textwrap.TextWrapper(width=80, break_long_words=False, replace_whitespace=False)
intro_list = wrapper.wrap(text=story)


def getStory():
    return intro_list

def print_story():
    while True:
        question = input('Do you wish to read the introduction story? "yes" or "no": ')
        question = question.lower()
        if question == 'yes':
            for line in getStory():
                print(line)
            break
        elif question == 'no':
            print("\nLet the game begin!")
            break
        else:
            print("check spelling.")
        return