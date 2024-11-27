def rules():
    #Asks the user if they want to know the rules of the game then prints them.
    rule = input('Do you want to read the rules? Type "yes" or "no": ').lower()
    while rule != "yes" and rule != "no":
        print("Check your spelling.")
        rule = input('Do you want to read the rules? Type "yes" or "no": ').lower()
    if rule == "yes":
        print("1. You will start at a random airport which is one of the options for the murder scene. "
              "At the start you will get three clues, that are not a part of the murder.\n You can see them later at the top of the"
              "accusations you have made. "
              "You can start your round by making an accusation there or flying somewhere else straight away.\n"
              "2. After making an accusation you must change the airport your at, the game will prompt you to fly to a new destination."
              " Flying costs 125 €.\n"
              "3. You lose the game if your money runs out before solving the mystery.\n"
              "4. You win the game by making an accusation with a correct weapon, suspect and airport.\n")
    return