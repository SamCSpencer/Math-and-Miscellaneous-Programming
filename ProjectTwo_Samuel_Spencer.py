#creating the player's inventory which starts out empty
inventory = []
#Creating a dictionary of the rooms in the castle along with their items,
# how they connect to other rooms, and #descriptions to be referenced and
# interacted with throughout the game
rooms = {
    "Servants' quarters": {
        "South": "Dining Hall",
        "West": "Workshop",
        "Item": "None"
    },
    "Workshop": {
        "South": "Distillery",
        "West": "Tannery",
        "East": "Servants' quarters",
        "Item": "VIALS",
        "Prompt": "a messy workshop in the process of constructing various torture devices with all sorts of bits and\n"
                  "bobs strewn about. Oddly nothing appears to be useful. As you go to leave you trip on a\n"
                  "judus cradle which bumps into an iron maiden which causes some loose VIALS to roll off the top of\n"
                  "it and go clanging to the floor.\n"
    },
    "Tannery": {
        "East": "Workshop",
        "Item": "ETHER",
        "Prompt": "a tannery filled with the skins of your cousin’s enemies. Normally you’d think it’s pretty messed up\n"
                  "but for some reason you can’t concentrate since your head feels like it’s filled with a swarm of bees. \n"
                  "After following a terrible smell you deduce it is coming from an open bottle of ETHER and a rag that\n"
                  "was left sitting about.\n"
    },
    "Dining Hall": {
        "North": "Servants' quarters",
        "South": "Garden",
        "Item": "IODINE POWDER",
        "Prompt": "the remnants of a raucous party. Furniture is damaged. The floor sticks to each one of your footsteps.\n"
                  "There are all sorts of substances strewn about better left undescribed. You notice laying on one\n"
                  "of the stools is some white substance that appears to be IODINE POWDER. You question the judgment of\n"
                  "whoever thought iodine powder would be something you’d want to have at a party.\n"
    },
    "Garden": {
        "North": "Dining Hall",
        "South": "Dungeon",
        "West": "Distillery",
        "Item": "SNAKEROOT",
        "Prompt": "a garden in surprisingly immaculate condition. The place used to be covered with weeds that you\n"
                  "could never seem to get rid of no matter how much you tried. Now every inch of it is full of the most\n"
                  "incredibly immaculate hydrangeas chrysanthemums lilies and baby’s breath. Who knew the vile treacherous\n"
                  "Ratislav was such an avid fan of flowers. You notice in the corner a tiny bit of SNAKEROOT poking\n"
                  "through the soil. Just what you were looking for! Thank goodness weeds always find a way!\n"
    },
    "Distillery": {
        "North": "Workshop",
        "South": "Child’s bedroom",
        "East": "Garden",
        "West": "Library of Cruelty",
        "Item": "ALCHEMY STATION",
        "Prompt": "an old distillery just making copious amounts of vodka to be handed out to the locals to keep them drunk\n"
                  "and incapable of organizing. You notice an ALCHEMY STATION in the corner. Would you like to Use it?\n"
    },
    "Dungeon": {
        "North": "Garden",
        "West": "Child’s bedroom",
        "Item": "SLIPPERS",
        "Prompt": "a big pit and well ok this is just grim. You really get an up-close look of exactly how much disdain\n"
                  "Ratislav has for the Khazars he’s supposed to be ruling over. You also notice a separate corner for torturing\n"
                  "and where the Byzantine emissaries that were cursed with receiving the task of your cousin delivering a message have been left for dead.\n"
                  "You suspect the Byzantines might happily take the credit for your cousin’s untimely end. You notice one\n"
                  "of the emissaries has a really nice pair of SLIPPERS which seem a lot quieter than the wooden clogs your\n"
                  "dad gave you for your birthday which you never liked but felt too guilty to take off.\n"
    },
    "Child’s bedroom": {
        "North": "Distillery",
        "East": "Dungeon",
        "West": "Treasure hall",
        "Item": "NEEDLE",
        "Prompt": "a wondrous nursery containing a beautiful baby. Awe! What an adorable little guy! Suddenly you turn white\n"
                  "as you remember your cousin was castrated. 'Whose child is this??' you think to yourself. You become overwhelmed\n"
                  "with concern as thousands of horrible possibilities go through your head. Anyway, someone left a sewing\n"
                  "NEEDLE on the counter.\n"
    },
    "Treasure hall": {
        "North": "Library of Cruelty",
        "East": "Child’s bedroom",
        "Item": "PERFUME",
        "Prompt": "a ridiculous hall filled with extravagant treasures from far and wide. While some seemed like they were\n"
                  "given as gifts or won through conquest on closer inspection most of the treasures just seem to be random\n"
                  "crap stolen from local peasants like a plain necklace or an old fork. You do notice a collection of\n"
                  "Byzantine PERFUME in the corner though.\n"
    },
    "Library of Cruelty": {
        "East": "Distillery",
        "South": "Treasure hall",
        "Item": "Ratislav",
        "Prompt": "your cousin sitting with his back toward you in a large chair made of 'leather.' There are also a lot\n"
                  "of 'leather'-bound books. There are a few open on the table next to you. There are no words in them.\n"
                  "You grab one to examine. They seem to all be picture books of torture potentially drawn by Ratislav.\n"
    },
    "Exit": {
        "Exit": "Exit",
        "North": "Servants' quarters",
        "South": "Servants' quarters",
        "East": "Servants' quarters",
        "West": "Servants' quarters",
        "Item": "Exit sign",
        "Prompt": "You've gone to the exit of the castle. An odd choice. Why did you come here?\n"
    }
}

# Creating a list ‘valid_directions’ to tell which directions the player can go in
valid_directions = ["North", "South", "East", "West", "Exit"]

# Set string ‘currentroom’ equal to ‘Servants quarters’ to make 'Servants quarters' the starting room
currentroom = "Servants' quarters"

# Both the hero and villian are alive when value is 0 signifying the game can continue
both_alive = 0

#a variable to check if the player wants the game to end to break the main game loop
end_game = 0

#a variable to check if the player used a shortcut command
just_walked = False

#A variable to see if the player has already
one_escape: bool = False

# a variable to make sure you only get one secret exit sign
only_one = False


# Function that takes 'direction' and returns the room in that direction from the current room
def get_room(direct):
    if direct == "Exit":
        return rooms[direct][direct]
    elif direct in rooms[currentroom]:
        return rooms[currentroom][direct]
    return 'invalid'


def print_inventory():
    print("Inventory: ")
    if not inventory:
        print("Your inventory is empty.\n")
        return

    # Determine the width of the box (longest item + padding)
    max_length = max(len(item) for item in inventory)
    box_width = max_length + 4  # Adding padding

    # Print top border
    print("+" + "-" * box_width + "+")

    # Print each item center-aligned
    for item in inventory:
        print("|" + item.center(box_width) + "|")

    # Print bottom border
    print("+" + "-" * box_width + "+")

# Placeholder function for ‘uhoh_ratislav’
def uhoh_ratislav():
    global one_escape
    global currentroom
    global just_walked
    #Give option to leave if you have slippers
    while True:
        if "SLIPPERS" in inventory:
            attack = input("You feel sneaky. Do you feel prepared...(Y or N)? ")
            print("\n")
            # Check to see if the player has already escaped before
            if one_escape:
                print("Your cousin stirs in his chair. You won't be able to make it out of the room without him noticing.\n"
                      "Now is your only shot!\n")
                input("Enter anything to continue to your fate...")
                print("\n")
                break
            # User decides not to leave and proceeds with end game
            elif attack == "Y" or attack == "y":
                break
            # User decides to leave and is sent to the distillery
            elif attack == "N" or attack == "n":
                print("You stealthily slide out the door to the Distillery like a stealthy person.\n")
                currentroom = "Distillery"
                just_walked = True
                one_escape = True
                return
            # Check if the input was invalid
            else:
                print("Shh... stop speaking gibberish or he'll hear you!\n")
        else:
            input("Enter anything to continue to your fate...")
            print("\n")
            break

    # Secret ending when everything is collected
    if "SLIPPERS" in inventory and "NEEDLE" in inventory and "BYZ. POISON" in inventory and "EXIT SIGN" in inventory and "PERFUME" in inventory and "ETHER" in inventory:
        print("You sneak as silent as Чоловік-Моль across the room towards your cousin. As you approach you swiftly open your\n"
              "satchel from under your cloak and dip your NEEDLE into the writhing, demonic POISON, and pull out your ETHER rag.\n"
              "Just as you close the final distance, Ratislav's ears perk up and he turns to confront you but its too late.\n"
              "'Solodki sniv, oozurpator z netrymannyam sechi' you mutter as you stick the rag over his face, causing his\n"
              "mind to fade from the conscious world. You go to strike him with the NEEDLE when suddenly an idea comes over you.\n"
              "You hang the EXIT SIGN over the window so that anyone walking by will think it's a normal exit instead of a\n"
              "deadly fall. You lean him against the window and remove your disguise. When one of Ratislav's advisors enters\n"
              "You loudly announce 'What's that cousin??! You're giving me back Tmutarakan!? Wow that's so generous of you!\n"
              "Anway, enjoy your retirement!' \n")
        input("Enter anything to open the window: ")
        print("\n You fling open the window causing your trecherous cousin to plummit to his watery, crocodile-infested,\n"
              "moaty grave! You shrug and exclaim 'What a lovely gentleman!'\n\n"
              "With all Ratislav's henchmen thinking that your return was their former master's desire, your entire principality\n"
              "stands united and more powerful than you could possibly imagine. With your new found power you march up\n"
              "the Kerch Straight, ford the Dnipro, and overthrow your father, rebuilding the old empire of Volodymyr.\n"
              "You marry the Princess of Sweden and after many years you are ready to launch your grand campaign.\n")
        input("Enter anything to conquer the Franks: ")
        print("You, Korel Gleb, with an army of Varangians and Slavs at your back march east and topple Paris.\n"
              "The bounds of your empire exceed what the Romans ever dreamed of. A generation later, a united Europe easily\n"
              "repels the Mongol invasion, leaving the Mongol Empire to shrivel and collapse. With no Mongols, the Bubonic Plauge\n"
              "and subsiquent Renaissance never sweep through Europe. Europe stays illiterate, and eventually the Inca conquer\n"
              "the world.\n\n"
              "What a gleb!\n")
        quit()

    # Normal victrious ending
    elif "SLIPPERS" in inventory and "NEEDLE" in inventory and "BYZ. POISON" in inventory and "PERFUME" in inventory and "ETHER" in inventory:
        print(
            "You sneak as silent as Чоловік-Моль across the room towards your cousin. As you approach you swiftly open your\n"
            "satchel from under your cloak and dip your NEEDLE into the writhing, demonic BYZ. POISON, and pull out your ETHER rag.\n"
            "Just as you close the final distance, Ratislav's ears perk up and he turns to confront you but its too late\n."
            "'Solodki sniv, oozurpator' you mutter as you stick the rag over his face, causing his "
            "mind to fade from the conscious world.\n")
        input("Enter anything to end Ratislav")

        print(
            "\nYou strike with the NEEDLE into your cousin's neck, and watch as the poison takes hold of him, tearing through one vein\n"
            "after the next. You watch as the bane of your life who humiliated you so thoroughly twice, silently suffers a\n"
            "most deserved fate. But there is no time to enjoy your masterpiece. You spray your cousin's corpse with the perfume and\n"
            "dart out of the window to clamber down the side of the castle, and disappear into the night. When Ratislav's servants\n"
            "find him consumed from the inside on the floor of the Library of Suffering, they smell the perfume and know it must\n"
            "have been that pesky Governor of Crimea. The Byzantines, once blamed, are happy to take the credit for removing\n"
            "such a scourge from their borders. Your father order's you reinstated to your rightful seat.\n")
        input("Enter anything to reclaim your thrown: ")
        print("\nYOU WIN: You climb atop the seat that is your birthright, to rule once again from the seat of the Principality of Tmutarakan.\n"
              "From there you prepare for your long rule and the lineage you will spawn. Many grand plans unfold in your head for about\n"
              "six months before the peasants rebel and you die trying to run away.\n\n"
              "Poor Gleb\n\n"
              "Even in victory he was a loser...\n")
        quit()

    # Ending for if you have everything but the perfume leading to you getting blamed
    elif "SLIPPERS" in inventory and "NEEDLE" in inventory and "BYZ. POISON" in inventory and "PERFUME" not in inventory and "ETHER" in inventory:
        print(
            "You sneak as silent as Чоловік-Моль across the room towards your cousin. As you approach you swiftly open your\n"
            "satchel from under your cloak and dip your NEEDLE into the writhing, demonic BYZ. POISON, and pull out your ETHER rag.\n"
            "Just as you close the final distance, Ratislav's ears perk up and he turns to confront you but its too late\n."
            "'Solodki sniv, oozurpator' you mutter as you stick the rag over his face, causing his "
            "mind to fade from the conscious world.\n")
        input("Enter anything to end Ratislav")

        print(
            "\nYou strike with the NEEDLE into your cousin's neck, and watch as the poison takes hold of him, tearing through one vein\n"
            "after the next. You watch as the bane of your life who humiliated you so thoroughly twice, silently suffers a\n"
            "most deserved fate. But there is no time to enjoy your masterpiece."
            " You dart out of the window and clamber down the side of the castle,\nand disappear into the night. Ratislav's servants"
            "find him consumed from the inside out on the floor of the Library of Suffering.\n"
            "They recognize the poison as Byzantine but they know many outside said Empire know how to make it, and they suspect foul play.\n"
            "Your motive makes you a prime suspect. After some investigation your alibi falls apart and you are arrested by SLAVPOL.\n"
            "Your dad tries to intervene on your behalf, but there are limits to his power and the judge just has it out for you.\n"
            "You are sentenced to execution by Zmiy\n")
        input("Enter anything to be fed to a mythical, wife-stealing dragon")
        print("\nGULP\n")
        print("You lose...\n")
        quit()

    #Ending for if you have everything but Ether and disregard Perfume
    elif "SLIPPERS" in inventory and "NEEDLE" in inventory and "BYZ. POISON" in inventory  and "ETHER" not in inventory:
        print(
            "You sneak as silent as Чоловік-Моль across the room towards your cousin. As you approach you swiftly open your\n"
            "satchel from under your cloak and dip your NEEDLE into the writhing, demonic BYZ. POISON.\n"
            "Just as you close the final distance, Ratislav's ears perk up and he turns to confront you but its too late\n."
            "'Zabaraysya het z moho domu!' you demand.\n")
        input("Enter anything to end Ratislav")

        print(
            "\nYou strike with the NEEDLE into your cousin's neck, and watch as the poison takes hold of him, tearing through one vein\n"
            "after the next. While rolling in pain, he lets out a desperate screem, and you quickly hear the sounds of footsteps from\n"
            "down the hall. You turn to see 10 ironclad guards enter the room. All entrances are blocked. You try to charge through them\n"
            "but they throw you back to the ground. Before you can get up you a sword is thrust through your throat. You remember nothing else.\n")
        print("You lose...\n")
        quit()

    #Ending for if you have slippers and NEEDLE but not ether and the poison
    elif "SLIPPERS" in inventory and "NEEDLE" in inventory and "BYZ. POISON" not in inventory and "ETHER" not in inventory:
        print(
            "You sneak as silent as Чоловік-Моль across the room towards your cousin. As you approach you swiftly open your\n"
            "satchel from under your cloak and wield your NEEDLE in your right hand.\n\n"
            "Just as you close the final distance, Ratislav's ears perk up and he turns to confront you but its too late\n."
            "'Ataka Holok!' you cry.\n")
        input("Enter anything to attack Ratislav")
        print("You jab at Ratislav with your NEEDLE rapidly and ferociously! You draw blood and Ratislav is clearly in pain but\n"
             "not much else. Ratislav grabs for his belt, but before he can find what he is looking for you get two jabs into each\n"
              "eye. He recoils in desperation and terror and you step forward to finish the job, when you feel the steel of his\n"
              "dagger enter your stomach. You keel over onto the floor and watch as every thing slowly goes black. The last thing\n"
              "you hear is Ratislav screams of Ratislav. 'I CAN'T SEE! I CAN'T SEE...'\n\n"
              "You lose...\n")
        quit()

    #Ending if you have all main items but poison.
    elif "SLIPPERS" in inventory and "NEEDLE" in inventory and "BYZ. POISON" not in inventory and "ETHER" in inventory and "PERFUME" in inventory:
        print(
            "You sneak as silent as Чоловік-Моль across the room towards your cousin. As you approach you swiftly open your\n"
            "satchel from under your cloak and wield your NEEDLE in your right hand, and pull out your ETHER rag.\n"
            "Just as you close the final distance, Ratislav's ears perk up and he turns to confront you but its too late\n."
            "'Solodki sniv, duren' you mutter as you stick the rag over his face, causing his"
            " mind to fade from the conscious world.\n")
        input("Enter anything to end Ratislav")

        print("You stab at your cousin ferciously and endlessly. You don't stop until every visible inch of him has been as been\n"
              "punctured. No way anyone could survive that all that! But there is no time to enjoy your masterpiece. You spray your\n"
              "cousin's corpse with the perfume and "
              "dart out of the window and clamber down the side of the castle, and disappear into the night.\n"
              "It is a long journey back towards the Norse Sea. A storm is churns overhead and the crossing of the Volga river is out.\n"
              "You must wait until morning and find a ferryman. As you pass the night quietly in a tavern, trying not to make eye contact\n"
              "with anyone. Suddenly a man in a black cloak approaches.\n")
        input("Enter anything to escape")
        print("\nYou turn to walk away from the man and bump into another.\n"
              "He says to you, 'You should have finished the job.' You turn to leave when the first man says, 'Ratislav sends his regards,'\n"
              "and sticks you with the knife he was concealing. You feel another knife in your back but by then you are too in shock to feel\n"
              "the pain. Onlookers try to quietly avoid the conflict as you accept you mutter a prayer and accept your fait.\n\n"
              "You died...\n")
        quit()

    # Ending if you have all the items except the poison and perfume
    elif "SLIPPERS" in inventory and "NEEDLE" in inventory and "BYZ. POISON" not in inventory and "ETHER" in inventory and "PERFUME" not in inventory:
        print(
            "You sneak as silent as Чоловік-Моль across the room towards your cousin. As you approach you swiftly open your\n"
            "satchel from under your cloak and wield your NEEDLE in your right hand.\n"
            "Just as you close the final distance, Ratislav's ears perk up and he turns to confront you but its too late\n."
            "'Solodki sniv, duren' you mutter as you stick the rag over his face, causing his "
            "mind to fade from the conscious world.\n")
        input("Enter anything to end Ratislav")

        print("You stab at your cousin ferciously and endlessly. You don't stop until every visible inch of him has been as been\n"
              "punctured. No way anyone could survive that all that! But there is no time to enjoy your masterpiece. You spray your\n"
              "cousin's corpse with the perfume and "
              "dart out of the window to clamber down the side of the castle, and disappear into the night.\n"
              "It is a long journey back towards the Norse Sea. A storm is churns overhead and the crossing of the Volga river is out.\n"
              "You must wait until morning and find a ferryman. As you pass the night quietly in a tavern, trying not to make eye contact\n"
              "with anyone. Suddenly a man in a black cloak approaches.\n")
        input("Enter anything to escape...")
        print(
              "\nYou turn to walk away from the man and bump into another.\n"
              "He says to you, 'You should have finished the job.' You turn to leave when the first man says, 'Ratislav sends his regards,'\n"
              "and sticks you with the knife he was concealing. You feel another knife in your back but by then you are too in shock to feel\n"
              "the pain. Onlookers try to quietly avoid the conflict as you accept you mutter a prayer and accept your fait.\n\n"
              "You lose...\n")
        quit()

    # Ending if you have slippers and poison but not the NEEDLE
    elif "SLIPPERS" in inventory and "NEEDLE" not in inventory and "BYZ. POISON" in inventory:
        print(
            "You sneak as silent as Чоловік-Моль across the room towards your cousin. As you approach you swiftly you realize you\n"
            "have no idea what you're doing. You notice Ratislav is starting to stir, so you desperately try to think of something.\n")
        input("Enter anything to do something...")
        print("\nIn a panic you drink the poison. 'Syupryz na den narrodjennya!' you hear yourself say as you kiss Cousin Ratislav on\n"
              "the lips. You both die, potentially from embarrassment.\n\n"
              "You lose...\n")
        quit()

    # Ending if you just have slippers.
    elif "SLIPPERS" in inventory and "NEEDLE" not in inventory and "BYZ. POISON" in inventory:
        print(
            "You sneak as silent as Чоловік-Моль across the room towards your cousin. You approach swiftly.\n"
            "What exactly is the plan here? You notice Ratislav is starting to stir in his seat.\n")
        input("Enter anything to do something...")
        print("\n You start begin tickling Ratislav the terrible. Koochie Koochie Koo! Your subjects lose all respect for you.\n"
              "You live the rest of your life in shame and exile.\n\n"
              "You lose...\n")
        quit()

    #Ending if you don't have slippers but have the main other three (Not including exit sign or perfume)
    elif "SLIPPERS" not in inventory and "NEEDLE" in inventory and "BYZ. POISON" in inventory and "ETHER" in inventory:
        print(
            "You sneak across the room towards your cousin. As you approach you swiftly open your\n"
            "satchel from under your cloak and dip your NEEDLE into the writhing, demonic BYZ. POISON, and pull out your ETHER rag.\n")
        input("Enter anything to end Ratislav...")
        print(
            "\n'Z Chernhova z priyemnistu' you say as you lerch to smother him with the rag. Ratislav pulls back and in one motion he\n"
            "pulls away from the rag and stabs you with his dagger. You collapse on the floor. All you dreams fade with you.\n\n"
            "You lose...\n"
        )
        quit()

    # Ending if you don't have the slippers or Ether but have the NEEDLE and poison
    elif "SLIPPERS" not in inventory and "NEEDLE" in inventory and "BYZ. POISON" in inventory and "ETHER" not in inventory:
        print(
            "You sneak across the room towards your cousin. As you approach you swiftly open your\n"
            "satchel from under your cloak and dip your NEEDLE into the writhing, demonic BYZ. POISON.\n")
        input("Enter anything to end Ratislav...")
        print(
            "\n'Z Chernhova z priyemnistu' you say as you lerch to poison him. Ratislav pulls back and in one motion dodges\n"
            "your attack and stabs you with his dagger. You collapse on the floor. All you dreams fade with you.\n\n"
            "You lose...\n"
        )
        quit()

    #Ending if you don't have slippers nor poison but have the main other two (Not including exit sign or perfume)
    elif "SLIPPERS" not in inventory and "NEEDLE" in inventory and "BYZ. POISON" not in inventory and "ETHER" in inventory:
        print(
            "You sneak across the room towards your cousin. As you approach you swiftly open your\n"
            "satchel from under your cloak and wield your NEEDLE in your right hand, and pull out your ETHER rag with the other.\n")
        input("Enter anything to end Ratislav...")
        print(
            "\n'Z Chernhova z priyemnistu' you say as you lerch to smother him with the rag. Ratislav pulls back and in one motion he\n"
            "pulls away from the rag and stabs you with his dagger. You collapse on the floor. All you dreams fade with you.\n\n"
            "You lose...\n"
        )
        quit()

    # Ending if of the main four items you only have a NEEDLE
    elif "SLIPPERS" not in inventory and "NEEDLE" in inventory and "BYZ. POISON" not in inventory and "ETHER" not in inventory:
        print(
            "You sneak across the room towards your cousin. As you approach you swiftly open your\n"
            "satchel from under your cloak and wield your NEEDLE in your right hand.\n")
        input("Enter anything to end Ratislav...")
        print(
            "\n'Z Chernhova z priyemnistu' you say as you lerch to stab him. Ratislav pulls back and in one motion dodges\n"
            "your attack and stabs you with his dagger. You collapse on the floor. All you dreams fade with you.\n\n"
            "You lose...\n"
        )
        quit()

    #Ending if you don't have slippers nor NEEDLE but have the main other two (Not including exit sign or perfume)
    elif "SLIPPERS" not in inventory and "NEEDLE" not in inventory and "BYZ. POISON" in inventory and "ETHER" in inventory:
        print(
            "You sneak across the room towards your cousin. As you approach you swiftly open your\n"
            "satchel from under your cloak and wield the vial of writing BYZ POISON in your right hand, and pull out your\n"
            "ETHER rag with the other.\n")
        input("Enter anything to end Ratislav...")
        print(
            "\n'Z Chernhova z priyemnistu' you say as you lerch to smother him with the rag. Ratislav pulls back and in one motion he\n"
            "pulls away from the rag and stabs you with his dagger. You collapse on the floor. All you dreams fade with you.\n\n"
            "You lose...\n"
        )
        quit()

    # Ending if of the main four items, you only have poison
    elif "SLIPPERS" not in inventory and "NEEDLE" not in inventory and "BYZ. POISON" in inventory and "ETHER" not in inventory:
        print(
            "You sneak across the room towards your cousin. As you approach you swiftly open your\n"
            "satchel from under your cloak and wield your NEEDLE in your right hand.\n")
        input("Enter anything to end Ratislav...")
        print(
            "\n'Z Chernhova z priyemnistu' you say as you lerch to kiss him with poison lips. Ratislav pulls back and in one motion dodges\n"
            "your smooch and stabs you with his dagger. You collapse on the floor. All you dreams fade with you.\n\n"
            "You lose...\n"
        )
        quit()

    # Secret ending where the only endgame item you have is the exit sign
    elif "SLIPPERS" not in inventory and "NEEDLE" not in inventory and "BYZ. POISON" not in inventory and "EXIT SIGN" in inventory and "PERFUME" not in inventory and "ETHER" not in inventory:
        print(
            "You step forward and yell your cousins name. ‘RATISLAV!’ He gets up and turns around to identify and confront his \n"
            "challenger. Upon recognizing you, his blood boils and face turns as red as the moonrise. He screams and charges you.\n"
            "You suddenly pull out the weapon he fears most, an EXIT SIGN! \n"
            "He tries to stop but it’s too late. You smash him over the head with it leaving him dead on the floor. \n"
            "His guards come in and arrest you. They sentence you to summary execution. Before you die you get a letter from your dad,\n"
            "saying he’s proud of you.\n"
        )
        input("Press anything to feel complete...")
        print(
            "\n *Sighs*...\n"
        )
        quit()

    else:
        print(
            "You startle yourself as you realize how wholly unprepared you are for this moment. As you go to put the book down\n"
            "you knock over a lamp and your cousin turns around in shock, confusion, and anger. You try to leave through the door\n"
            "you came in on but you can’t figure out if it’s a push or a pull. Suddenly your limbs stop listening to you\n"
            "and your world goes dark. Looks like you quite muffed that one up.\n"
        )
        print("You lose...\n")
        quit()
    #print("Placeholder: This is the uhoh_ratislav function. It will handle the encounter with Ratislav.")
#Create function to determine what happens with the alchemy table if you use it.
def do_alchemy():
    #Kills player if they try to make poison with just iodine powder
    if "IODINE POWDER" in inventory and "SNAKEROOT" not in inventory:
        print("The iodine powder sizzles alone in the cauldron, you slowly churn it first counter clockwise\n"
              "then clockwise. The temperature raises and the sizzling turns to a whistle. You take a deep breath in\n"
              "and... KABOOM!!!\n")
        print("Here lies Prince Gleb: 1052-1067\n")
        quit()
    #Check if player has ingredients but doesn't have vials to contain it
    elif "VIALS" not in inventory and ("IODINE POWDER" in inventory and "SNAKEROOT" in inventory):
        print("You lean over the alchemy set with all the ingredients you need to make the Byzantine poison.\n"
              "As you look through your bag you realize you have nothing to contain it! Instead you take a pinch\n"
              "of your ingredients and put it the cauldron. They hiss and whistle and dance around each other before\n"
              "turning black. It seems as if ghostly cries of agony emanate from the new substance and echoes through\n"
              "the halls. Yes. This recipe will do nicely.\n")
    #Check if the player doesn't have either ingredients and so nothing happens
    elif "IODINE POWDER" not in inventory and "SNAKEROOT" not in inventory:
        print("You look at some shiny metal. That was boring.\n")
    #Check if the player doesn't have iodine powder and nothing happens
    elif "IODINE POWDER" not in inventory:
        print("You put some leaves in a big metal bowl. Nothing happens. You take them out. You question\n"
              "the quality of your eduction.\n")
   #Checks if the player has all ingredients and makes the poison, replacing the ingredients
    #in the inventory with poison and then displays inventory
    elif "IODINE POWDER" in inventory and "SNAKEROOT" in inventory and "VIALS" in inventory:
        print("You lean over the ALCHEMY SET with all the ingredients you need to make the Byzantine poison.\n"
              "You empty the entirty of the IODINE POWDER and SNAKEROOT into the boiling cauldron shaped from twisted metal\n"
              "The ingredients hiss and whistle and dance around each other before"
              "turning black and joining together into a shimmering ferrofluid.\n"
              "A tall flame, black as midnight shoots from the cauldron, It seems as if ghostly cries of agony emanate\n"
              "from the new substance and echoes through the halls\n"
              "Yes. This recipe will do nicely.\n")
        # Breaking up text and making experience more interactive
        input("Enter anything to collect poison...")
        print("\nYou use tongs to carefully dip the VIALS into the concoction and scoop out your completed poison\n")
        #Print and remove ingredients from inventory
        print("SNAKEROOT, IODINE POWDER, and VIALS removed from inventory\n")
        inventory.remove("SNAKEROOT")
        inventory.remove("IODINE POWDER")
        inventory.remove("VIALS")
        #Print and add poison to inventory
        print("BYZ. POISON added to inventory\n")
        new_item = "BYZ. POISON"
        inventory.append(new_item)
        #Show updated inventory
        print_inventory()
# Handles all the inputs outside the actual movement
def get_input(c_room):
    global currentroom
    global just_walked
    # Resetting just_walked check so that it doesn't always stay on if used once
    just_walked = False
    while True:
        user_input = input("What would you like to do? (Status, Move, Get ITEM, Use): ")
        print("\n")
        #Checking if user_input contains a space in order split it so both can be checked
        if ' ' in user_input:
            command = user_input.split(' ', 1)
        #If user_input is not two words, it creates a command so the check won't create an error but will
        #be failed
        else:
            command = []
            not_get = "Not Get"
            command.append(not_get)
        #Print player current room and inventory and other goodies
        if user_input == "Status" or user_input == "status" or user_input == "STATUS":
            print("Current room:", currentroom, "\n")
            print_inventory()
            print("Aliveness: Alive\n")
            print("Desire for Vengeance: Unquenched\n")

        # Sends the user out of the function so they can enter what direction they want to go
        elif user_input == "Move" or user_input == "move" or user_input == "MOVE":
            break

        #Checks if the player can use the alchemy station
        elif user_input == "Use" or user_input == "use" or user_input == "USE":
            # Starts the process of using the alchemy station
            if currentroom == "Distillery" or "ALCHEMY STATION" in inventory:
                do_alchemy()
            # Detects the player can't use the alchemy station
            else:
                print("There is nothing to Use.\n")

        # Check if the two word input command is valid
        elif (command[0] != 'Get' and command[0] != "get" and command[0] != "GET" and command[0] != "MOVE") and command[0] != 'Move' and command[0] != 'move':
            print('Invalid command. Try another command.\n')

        # Check if the item isn't in the current room
        elif (command[0] == 'Get' or command[0] == "get" or command[0] == "GET") and command[1] != rooms[c_room]["Item"]:
            print(
                f'{command[1]} is not in the room. Remember to write the object’s name in ALL CAPS. Try another command.\n')

        # Checking if the user is using a move shortcut command but not entering a valid direction
        elif (command[0] == 'Move' or command[0] == 'move' or command[0] == "MOVE") and command[1] not in valid_directions:
                print("Invalid direction. Please try again.\n")

        # Checking if the user is using a shortcut command correctly
        elif (command[0] == 'Move' or command[0] == 'move' or command[0] == "MOVE") and command[1] in valid_directions:
            command_room = get_room(command[1])
           # Checking if there is a room in the direction of the given command
            if command_room == "invalid" and command[1] in valid_directions:
                print("There is no room in that direction. Maybe try a different direction.\n")
            # Moves the user into the room
            else:
                print("You walk into the:", command_room, "\n")

                currentroom = command_room
                just_walked = True
                #Avoiding an unbreakable cycle if shortcut move is used to exit
                break

        # If the 'Get' command is valid, add the item to the inventory
        else:
            # Putting item into the inventory
            print(f"You got {command[1]} and put it in your inventory.\n")
            new_item = command[1]
            inventory.append(new_item)
            print('Your inventory now contains: \n')
            print_inventory()

            # Remove the item from the current room
            rooms[c_room]["Item"] = "None"

#Game Start message and first commands
print("\nWelcome young Prince Gleb of Chernihiv and of the Kievan Rus\n\n"
      "The year is 1067:\n"
      "You have entered Castle Tmutarakan, your birthright twice stolen from you by your ruthless cousin, Ratislav,\n"
      "whom you once gave refuge to and repaid you in treachery. You've waited three years, and now, at the age of 15, \n"
      "you've snuck off in the night from your current holding "
      "of Novgorod to reclaim the stolen Principality once granted to you by\n"
      "your father, King Svyatislav\n")
start_input = input("Enter anything to accept the mission. Else, enter 'Quit': ")

#Give player the option to quit
if start_input == 'Quit':
    print("\nOk, whatever, Gleb. Go be a Gleb somewhere and let your kingdom fall apart.\n")
    quit()

#Give instructions
print("\nGreat! Beremos Do Spravy! Your plan is to brew a Byzantine poison, and poison your treacherous cousin, while framing\n"
    "The Governor of Byzantine Crimea.\n\n"
    "You have entered through the window of the Servants' quarters, and dawned a servants' "
    "uniform.\n\n"
    "You can move through the castle by using the 'Move Direction' command.\n\n"
    "In the rooms you will find items that will help you in your final confrontation with your cousin.\n\n"
    "You can collect the items using the 'Get ITEM' command.\n\n")
input("Enter anything to continue...")
print("\nThere may be features or items you can interact with.\n\n"
      "To interact with them, use the 'Use' command\n\n"
      "You can also check your status using the 'Status' command.\n\n"
      "Beware! Your disguise will allow you to move through the castle unnoticed by the servants, but if run into Ratislav,\n"
      "who is in one of these rooms, he will recognize you, so try to make sure you are fully prepared before you do.\n")

input("Enter anything to start...")
#get first input
get_input(currentroom)

# Main game loop for moving between rooms
while True:
    #Loop for getting input from the player of which direction they would like to go
    #and checking if it is a valid input
    while True:
        #Seeing if a shortcut move command was just issued
        if just_walked:
            break

        direction = input("Enter the direction you would like to go (North, East, South, West, or Exit): ")
        room = get_room(direction)
        print("\n")

        #Check for if the direction is valid but there just happens not to be a room
        #in that direction from the current room
        if room == "invalid" and direction in valid_directions:
            print("There is no room in that direction. Maybe try a different direction.\n")
        #Checking if the input was completely invalid and re-prompting
        elif room == 'invalid':
            print("Invalid entry. Please try again.\n")
        #elif room == 'Exit':
        #    currentroom = room
        #Checking if input was valid
        else:
            print("You walk into the:", room, "\n")
            currentroom = room
            break
    #Checking if the room contains Ratislav and calls function to start end game sequences
    if rooms[currentroom].get("Item") == "Ratislav":
        print('You see', rooms[currentroom]["Prompt"])
        uhoh_ratislav()
    #Checks if the player wanted to exit
    elif currentroom == "Exit":
        #Avoiding unending loop if shortcut move command was used to get to the exit
        just_walked = False
        print(rooms[currentroom]["Prompt"])
        #Loop to check for proper input
        while True:
            #Double-checking if they want to quit
            end_input = input("Do you want to end the game or sometin'...(Y or N)? ")
            print("\n")
            #Starting quit sequence
            if end_input == 'Y' or end_input == 'y':
                print("Fine. King Svyatoslov never liked you anyways. We're officially team Ratislav from now on. :'(")
                end_game = 1
                #break
                exit()
            #Continuing game
            elif end_input == 'N' or end_input == 'n':
                print("Phew. We knew we could count on good ol' Gleb\n")
                break
            # Allows you to secretly take the exit sign
            elif end_input == 'Get' and only_one == False:
                # Putting item into the inventory
                print(f"You got EXIT SIGN and put it in your inventory.\n")
                secret_item = "EXIT SIGN"
                inventory.append(secret_item)
                print('Your inventory now contains: \n')
                print_inventory()

                # Remove the item from the current room
                rooms[currentroom]["Item"] = "None"
                only_one = True
            # Checking if input is invalid
            else:
                print("Invalid entry. Please try again.")
    #Checking if this is the first time a player entered a room
    elif rooms[currentroom].get("Item") != 'None':
        print('You see', rooms[currentroom]["Prompt"])
        get_input(currentroom)
    #The player has been in the room before so the prompt is skipped
    else:
        print("You have already been here before.\n")
        get_input(currentroom)
    #The player wanted to end the game so the while loop is ended and program exits
    #if end_game == 1:
    #   break
