from mtgsdk import Card
import random
import pyttsx3

# Sees if the tutorial is complete
tutorial_completed = False

#-------------------Main Menu-----------------------

def mainmenu():
    global tutorial_completed
    while True:
        print("\n--- MTG Commander For Dummies ---")
        print("1. Hands-on Learning (Tutorial / Decks)")
        print("2. Listening Learning")
        print("3. Reading Rainbow")
        print("4. Exit")

        choice = input("Choose your preferd way to learn (1-4): ")

        if choice == "1":
            handsonmenu()
        elif choice == "2":
            listeningmode()
        elif choice == "3":
            readingmode()
        elif choice == "4":
            print("Goodbye My Planeswalker!!")
            break
        else:
            print("In Response Imma tap 2 blue and COUNTERSPELL. Invalid option or locked feature. Finish the tutorial first! ")

def handsonmenu():
    print("\n Hands-On Learning Selected!")
    print("Launching the Commander tutorial")
    runtuturial()

def readingmode():
    print("Reading Rainbow Selected!")
    print("Time to learn Commander!!!!")
    input("Press ENTER to start reading")

    print("\nLesson 1️. What is Commander?")
    print("Commander is a casual multiplayer format of Magic: The Gathering.")
    print("Each player picks 1 legendary creature called your Commander to lead your deck.")
    print("Your deck can only use colors that match your commander's color identity.")
    input("\nPress ENTER to continue")

    print("\nLesson 2. Deck Rules")
    print("• You must have exactly 100 cards total (including your Commander)")
    print("• You can only have ONE copy of any card — except for basic lands.")
    print("• Your Commander starts in a special area called the *Command Zone*.")
    input("\nPress ENTER to continue")

    print("\nLesson 3. How to Start the Game")
    print("• Everyone starts with 40 life instead of 20.")
    print("• Draw 7 cards for your opening hand.")
    print("• You get one FREE mulligan — you can shuffle and redraw 7 cards once per game.")
    print("• After that, each new mulligan makes you draw one less card.")
    print("• Roll a d20 — highest number goes first!")
    input("\nPress ENTER to continue")

    print("\nLesson 4️. Playing the Game")
    print("• You can play one land per turn and cast spells using mana from your lands.")
    print("• You can cast your Commander from the Command Zone any time you can cast a creature.")
    print("• Every time you cast it again from the Command Zone, it costs 2 extra mana (the 'Commander Tax').")
    input("\nPress ENTER to continue")

    print("\nLesson 5️. Winning and Losing")
    print("• If your life hits 0, you lose.")
    print("• If you take 21 or more damage from the SAME Commander, you lose (that’s Commander Damage).")
    print("• Last player standing wins!")
    input("\nPress ENTER to continue")

    print("\nLesson 6. Bonus Tips")
    print("• Focus on synergy: your cards should work well with your Commander’s abilities.")
    print("• Mana ramp (like Sol Ring and Cultivate) helps you cast big spells faster.")
    print("• Have fun! Commander is about creativity and social play, not just winning.")
    input("\nPress ENTER to continue...")

    print("\n That’s it! You now know the basics of Commander.")
    print("Ready to test your skills? Try the Hands-On Tutorial next!")
    input("\nPress ENTER to return to the main menu.")

def listeningmode():
    engine = pyttsx3.init()
    engine.setProperty("rate", 165)
    engine.setProperty("volume", 1.0)

    print("\n Listening Learning - Commander for Dummies")
    print("Time to sit back, Relax and enjoy the lesson.")
    input("Press ENTER to begin")

    lines = [
        "Welcome to Commander for Dummies.",
        "Commander is a fun, multiplayer version of Magic the Gathering.",
        "Each player has a legendary creature as their commander that leads their deck.",
        "You can only use cards that share your commander's colors.",
        "Your deck has exactly 100 cards, including your commander.",
        "You can only have one copy of each card, except basic lands.",
        "Everyone starts with forty life instead of twenty.",
        "You draw seven cards to start your game.",
        "You get one free mulligan, meaning you can reshuffle and draw a new hand of seven cards.",
        "After that, each mulligan makes you draw one fewer card.",
        "Players roll a twenty sided die to see who goes first.",
        "You can cast your commander from the command zone anytime you could cast a creature.",
        "Each time you cast it again, it costs two more mana — that’s the commander tax.",
        "If you take twenty-one damage from one commander, you lose.",
        "Last player standing wins the game!",
        "Commander is about creativity, cool interactions, and having fun with friends.",
        "That’s it! You now know the basics of Commander.",
        "Ready to test your skills? Try the Hands-On Tutorial next!"
    ]

    for line in lines:
        print(line)
        engine.say(line)
        engine.runAndWait()

    engine.say("End of the tutorial. Thanks for listening")
    engine.runAndWait()
    print("\n Listening guide finished. Press ENTER to return to the menu.")
    input()



#--------------Turorial----------------

def runtuturial():
    print("\n--- Welcome to Commander for Dummies ---")
    print("Lesson 1: Basic Rules.")
    print("• Each deck contains exactly 100 cards — no duplicates (except basic lands).")
    print("• You choose one Legendary Creature as your Commander.")
    print("• Your deck can only use cards within your Commander’s color identity.")
    print("• You start the game with 40 life instead of 20.")
    print("• Commander damage: 21 or more from a single Commander = defeat.")
    print("• The first mulligan is free (London Mulligan rule).")
    print("• Each player rolls a d20 — highest roll goes first.")
    print("\nFetching your Commander data from the MTG API...")
    results = Card.where(name="Atraxa, Praetors' Voice").all()

    if results:
        commander = results[0]
        print(f"\nYour Commander: {commander.name}")
        print(f"Type: {commander.type}")
        print(f"Mana Cost: {commander.mana_cost}")
        print(f"Rarity: {commander.rarity}")
        print(f"Text: {commander.text}")
        print(f"Set: {commander.set_name}")
    else:
        print("\n Could not fetch Atraxa data, using default information.")
        print("Atraxa, Praetors' Voice — Legendary Creature — Angel Horror")
        print("Flying, vigilance, deathtouch, lifelink")

    input("\nPress ENTER to continue...")


    print("Lesson 2: Basic Gameplay")
    print(" Every deck starts with your Commander on the battlefield (in the Command Zone).")
    input("Press ENTER to continue")

    print("\n You will now draw 7 cards fo ryour opening hand.")
    tutorial_deck = [
        "Forest", "Island", "Swamp", "Plains", "Sol Ring",
        "Cultivate", "Swords to Plowshares",
        "Arcane Signet", "Command Tower", "Atraxa's Assistant"
    ] * 10
    random.shuffle(tutorial_deck)
    hand = tutorial_deck[:7]
    print("Your Opening hand:")
    for card in hand:
        print("-", card)
    input("\nPress ENTER to continue")

    print("If you dont like your opening hand there is a neet thing call Mulligan where reshuffle your hand and draw and one less card except for the first one.")
    choice = input("Would you like to keep your hand or mulligan? (Y/N): ").lower()

    if choice == "y":
        random.shuffle(tutorial_deck)
        hand = tutorial_deck[:7]
        print("You take your free mulligan. Here's your new hand:")
        for card in hand:
            print("-", card)
    else:
        print("You keep your opening hand.")

    input("\nPress ENTER to continue")
    print("\nYou can take additional mulligans, but each following one reduces your hand by one card.")
    choice = input("Would you like to take another mulligan? (y/n): ").lower()
    if choice == "y":
        random.shuffle(tutorial_deck)
        hand = tutorial_deck[:6]
        print("You take another mulligan and draw 6 cards:")
        for card in hand:
            print("-", card)
    else:
        print("You're ready to start playing the game!")

    input("\nPress ENTER to continue")

    print("To see who goes first we mainly roll a d20 whoever has the highest roll wins!")
    input("Press ENTER to roll you d20")
    player_roll = random.randint(1, 20)
    opponent_roll = random.randint(1, 20)

    if player_roll <= opponent_roll:
        player_roll = opponent_roll + 1
        if player_roll > 20:
            player_roll = 20

    print(f"You rolled a {player_roll}!")
    print(f"Your opponent rolled a {opponent_roll}!")
    print("\n You win the roll! You'll take the first turn.")
    input("\nPress ENTER to continue")

    print("\nStep 5: Play a land and start your turn!")
    print("For example, you could play Command Tower or cast Sol Ring to ramp your mana early.")
    input("\nPress ENTER to finish tutorial")

    print("\n Tutorial completed! You can now build and use decks with your own Commander choices.")

if __name__ == "__main__":
    mainmenu()
