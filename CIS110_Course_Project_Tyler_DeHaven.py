#Greet the user and provide instructions. 
def printSeparator():
        print('-' * 495)
        
def start_game():
    print(f"Your head aches as you slowly regain consciouness.") 
    print(f"You smell industrial grease and melted cheese. Around you, the clang of machinery hums in a unsettling rhythm.") 
    print(f"You cant remember where you are, your thoughts are muddled, fragmented memories surface.")
    print(f"But they slip through your fingers like pizza sauce. ")
    print(f"Was it...laughter? Waking up to the warm sun on your face? A world with out the tyrant Pizza Bot 9000?")
    print(f"Your memory begins to fade...you are jarred and startled as a screen is shoved in your face!") 
    print(f"It's forcing you to snap back to the present.") 
    print(f"Words begin to scroll across its pixelated surface.....")
    print(f"Welcome, new recruit. Pizza Bot 9000 demands to know more about you before you are assigned your directive.")
    print(f"Answer the following questions truthfully...or face the wath of the Etarnal Oven! All hail Pizza Bot 9000!") 
    print(f"You hear a beep and deep robotic voice in your mind cuts through the hum and clangs of the pizza factory.")

    import time
    time.sleep(2)
    
    printSeparator()

    characterName = input(f"\nWhat is your name?")
    while len(characterName) == 0:
        characterName = input(f"\nI said tell me your name?   ")
    
    location =input(f"\nWhere are you from?   ")
    while len(location) == 0:
        location = input(f"I asked you Where are you from?   ")
    
    favoriteNumber = input(f"\nWhat is your favorite number?    ")
    while len(favoriteNumber) == 0:
        favoriteNumber = input(f"\nI told you to tell me a number..   ")

    fearEnforcer =input(f"\nWhat are you afraid of?   ")
    while len(fearEnforcer) == 0:
        fearEnforcer =input(f"\nDon't be scared what are you afraid of?   ")

    colorBanner =input(f"\nWhat is your favorite color?    ")
    while len(colorBanner) == 0:
        colorBanner =input(f"\nJust pick a color already...  ")

    
    time.sleep(2)
    printSeparator()

    #The Story Starts
    print(f"{characterName} wakes up to the sound of the factory alarm, signaling the start of another grueling day") 
    print(f"You are exausted having to continue to make pizzas for the Pizza Bot 9000 overlord.")
    print(f"As you don your {colorBanner} uniform and stumble to your station with pained movements")
    print(f"While you move over to your pizza station you notice the {colorBanner} banners and propaganda along the wall")
    print(f"As you peer out the grimy broken windows at the ruins of {location}, You can't help but wonder if there's more to life than this....")
    print(f"You look around terrified... if the {fearEnforcer} catch you slacking off and read your thoughts you would be excuted for heresy..")

    
    time.sleep(3)
    printSeparator()

    # Decision 1
    getBackToWork =input(f"\nShould {characterName} get back to work?   Type yes or no:    ")
    while getBackToWork.lower() != "yes" and getBackToWork.lower() != "no": 
        getBackToWork = input("Please type yes or no:   ")
    if getBackToWork == "yes" :
        print(f"\n{characterName} snaps out of his daydream and continues working diligently in fear.")
        print(f"\nYou hope for a better future, but you are too afraid of the {fearEnforcer}")
        print(f"\nIf the{fearEnforcer} catch you slacking off they might punish you for your insolence..")
        print(f"\nOr even worse... bring you to the depths of the factory where the pizza sauce is made...")
    else:
        print(f"\n{characterName} decides to risk it and continue to stare out the window at the ruins of {location}..")
        print(f"\n You start to gain courage for yourself and think of a better future.")
        print(f"\n {characterName} starts dreaming of escape and overthrowing the {fearEnforcer} or a way to escape from Pizza Bot 9000 grasp.")
 
    

    # Decision 2
    time.sleep(3)
    printSeparator()
    time.sleep(3)

    print(f"\nAfter several days while working you are provided with a rare opportunity to deliver a pizza outside of the factory." ) 
    print(f"\nWhile walking on the grounds to the front gate you notice a commotion outside of the gates and some workers are causing a scene."  )
    print(f"\nLooks like the {fearEnforcer} Enforcers are about to punish a group of people for trying to speak out against the Pizza Bot 9000." )
    print(f"\nWhile walking near the the growing crowd you hear some wispers and rumors that there might be a safe zone out side of the factory" )
    print(f"\nYou hear some people murmer about a safe zone in the ruins of {location} outside of the factory... Where there is no pizza.... ")

    
    time.sleep(3)
    printSeparator()


    theOpportunity =input(f"\nDo you continue to deliver the pizza without delay?  Type yes or no:   ")
    while theOpportunity.lower() != "yes" and theOpportunity.lower() != "no":
        theOpportunity = input("Please type yes or no:    ")
    if theOpportunity == "yes" :
        print(f"\nYou don't hesitate with your duties regardless of the commontion at the factory gates." )
        print(f"\nFrightned by the {fearEnforcer} Enforcers you try to hurry past as {favoriteNumber} factory workers gather" )
        print(f"\nThe workers gather and rip down the {colorBanner} banners and face off with the {fearEnforcer} Enforcers." )
        print(f"\nTerrified that you will get cought up in the mixup you keep your head down and deliver the pizza like you are told" )
        print(f"\nThe Pizza Bot 9000 is pleased with your dedication and for not faltering when faced with temptation"  )
    else:
        print(f"\nYou see {favoriteNumber} factory workers gather and rip down the {colorBanner} banners and face off with the {fearEnforcer} Enforcers.")
        print(f"\n{characterName} notices the {fearEnforcer} Enforcers get ready to punish the factory workers. The mob starts to chant.." )
        print(f"\nDown with the pizza bot! Down with the pizza bot! in a rhythmic chant." )
        print(f"\nAll this commotion and you notice the front gate was left open by the {fearEnforcer} Enforcers when they left the gate to deal with the riot..." )
        print(f"\nThen you see the riot of factory workers rush the {fearEnforcer} Enforcers and start to fight!")
 
    
    time.sleep(3)
    printSeparator()

    #Alternate Endings
    if getBackToWork.lower() == "yes" and theOpportunity.lower() == "yes":
        print(f"\nYou chose to accept your fate and continue working for Pizza Bot 9000.")
        print(f"Despite your hopes for a better life you don your {colorBanner} uniform and get back to work")
        print(f"After the recent riot the {fearEnforcer} Enforcers grip tightens, and you find yourself making pizzas for the rest of your life.")
        print(f"{characterName} dreams about what could have been if you had enough courage that day... but gets back to work before something bad happens.")
    elif getBackToWork.lower() == "no" and theOpportunity.lower() == "no":
        print(f"\nWith the factory in chaos and Pizza Bot 9000's systems compromised you join your fellow workers in the riot")
        print(f"you and the {favoriteNumber} other factory workers rip down all the {colorBanner} banners and take down the {fearEnforcer} Enforcers.")
        print(f"{characterName} and the other factory workers cheer with victory over the tyrannical robot overloard.")
        print(f"The world begins to rebuild starting with the ruins of {location}.. Free from the Pizza Bot 9000 tyranny and from pizza!")
    else: 
        print(f"\nWith the confusion and the gate left unguarded you rush out while the {fearEnforcer} Enforcers are dealing with the riot")
        print(f"{characterName} hears the other {favoriteNumber} workers clash with the {fearEnforcer} Enforcers but you continue to run!")
        print(f"Though the journey is perilous, you find freedom in the safe zone in {location} the rumors were true!")
        print(f"You join the other resistance warriors away from the horrors of the factory and start a new life away from the overlord's control")

    
    time.sleep(3)
    printSeparator()
    print(f"\nThe End")
    

keepPlaying = "yes"
while keepPlaying.lower() == "yes":
    start_game()
    keepPlaying = input(f"\nDo you want to play again? Enter yes or no:   ")
if keepPlaying.lower() == "no":
    print("\nThanks for playing! All hail Pizza Bot 9000!")
    