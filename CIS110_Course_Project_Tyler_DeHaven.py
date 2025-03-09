#Greet the user and provide instructions. 
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

#5 Questions before the story begins
characterName =input("\nWhat is your name?    ")
location =input("\nWhere are you from?   ")
favoriteNumber =input("\nWhat is your favorite number?    ")
fearEnforcer =input("\nWhat are you afraid of?   ")
colorBanner =input("\nWhat is your favorite color?    ")


#The Story Starts
print(f"{characterName} wakes up to the sound of the factory alarm, signaling the start of another grueling day") 
print(f"You are exausted having to continue to make pizzas for the Pizza Bot 9000 overlord.")
print(f"As you don your {colorBanner} uniform and stumble to your station with pained movements")
print(f"While you move over to your pizza station you notice the {colorBanner} banners and propaganda along the wall")
print(f"As you peer out the grimy broken windows at the ruins of {location}, You can't help but wonder if there's more to life than this....")
print(f"You look around terrified... if the {fearEnforcer} catch you slacking off and read your thoughts you would be excuted for heresy..")

# Decision 1
getBackToWork =input(f"\nShould {characterName} get back to work?   Type Yes or No:    ")
if getBackToWork == "Yes" :
    print(f"\n{characterName} snaps out of his daydream and continues working diligently in fear.")
    print(f"\nYou hope for a better future, but you are too afraid of the {fearEnforcer}")
    print(f"\nIf the{fearEnforcer} catch you slacking off they might punish you for your insolence..")
    print(f"\nOr even worse... bring you to the depths of the factory where the pizza sauce is made...")
else:
    print(f"\n{characterName} decides to risk it and continue to stare out the window at the ruins of {location}..")
    print(f"\n You start to gain courage for yourself and think of a better future.")
    print(f"\n {characterName} starts dreaming of escape and overthrowing the {fearEnforcer} or a way to escape from Pizza Bot 9000 grasp.")
 
import time

# Decision 2
print(f"\nAfter several days while working you are provided with a rare opportunity to deliver a pizza outside of the factory." )time.sleep(3)
print(f"\nWhile walking on the grounds to the front gate you notice a commotion outside of the gates and some workers are causing a scene."  )
print(f"\nLooks like the {fearEnforcer} Enforcers are about to punish a group of people for trying to speak out against the Pizza Bot 9000." )
print(f"\nWhile walking near the the growing crowd you hear some wispers and rumors that there might be a safe zone out side of the factory" )
print(f"\nYou hear some people murmer about a safe zone in the ruins of {location} outside of the factory... Where there is no pizza.... ")

theOpportunity =input(f"\nDo you continue to deliver the pizza without delay? Or do you linger and continue to watch the commotion and see what happens?   Type Yes or No:   ")