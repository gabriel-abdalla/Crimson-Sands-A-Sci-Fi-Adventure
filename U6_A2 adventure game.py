"""
Adventure Game
ICS3U
Gabriel Abdalla
An adventure game exploring a sci-fi empire in a world of bones.
History:
January 15, 2025 - version 1 
Imported the skeleton of the adventure game.
January 19, 2025 - version 2
Added new items like the bat, and areas like a staff door.
January 20, 2025 - version 3
Fixed conditions relating to items and restrictions based on those items.
January 22, 2025 - version 4
Finished robot fight and function to control health and death.
January 24, 2025 - version 5
Fixed bugs with the robot fight and started to develop the basement.
January 25, 2025 - version 6
More bug fixes
January 28, 2025 - version 7
Added the hacking minigame function
January 30, 2025 - version 8
Game completion with comments, docstrings, and a bit more organization.
"""

# Needed to clear the screen
import os
# Needed for selecting random numbers
import random
# Needed for waiting time between outputs.
import time
# Needed for a timed input from a user.    
import sys
# Needed for a timed input from a user.   
import select

# This function allows for clearing the screen.
def clear():
  """This causes the screen to clear"""
  os.system('clear')
  
def crimson_sands(times_there, description2, item, hpp, description3, item2, count):
  """
  Represents the Crimson Sands location.
  Args:
    times_there (int)
    description2 (bool)
    item (bool)
    hpp (int)
    description3 (bool)
    item2 (bool)
    count (int)
  Returns:
    selection (str)
    times_there (int)
    description2 (bool)
    item (bool)
    hpp (int)
    description3 (bool)
    item2 (bool)
    count (int)
  """
  # Before giving the options of where to go, the options given vary depending on the amount of times traveled there by the user.
  if times_there == 0:
      # User selects next location within or outside of the current location & input is validated
      print("Where would you like to go? \n[m] Train Station (Main Floor) \n[t] Train Station (Top Floor) \n[b] Train Station (Basement) \n[w] Wooden Shack")
      selection = input()
      times_there = times_there + 1
      # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
      while selection not in ['m', 't', 'b', 'M', 't','B', 'w', 'W']:
          print("Invalid selection.")
          selection = input()
          
  # Checks if the times there is more than one and if the user doesn't have the robot eye.
  elif times_there > 0 and item2 == False:
      # User selects next location within or outside of the current location & input is validated.
      # description by Chatgpt 
      print("Red sand stretches endlessly, whipped by the wind over cracked earth and buried ruins. Silence hangs heavy beneath a blood-orange sky.")
      print("Where would you like to go? \n[m] Train Station (Main Floor) \n[t] Train Station (Top Floor) \n[b] Train Station (Basement) \n[w] Wooden Shack \n[a] Attack the robot!")
      selection = input()
      # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
      while selection not in ['m', 't', 'b', 'M', 't','b', 'w', 'W', 'a', 'A']:
        print("Invalid selection.")
        selection = input()
        
  # Checks if the times there is more than one and if the user DOES have the robot eye. The three different options allows for control over what the user can pick from.
  elif times_there > 0 and item2 == True:
      # User selects next location within or outside of the current location & input is validated
      print("Where would you like to go? \n[m] Train Station (Main Floor) \n[t] Train Station (Top Floor) \n[b] Train Station (Basement) \n[w] Wooden Shack \n[s] Scavange Robot Remains")
      selection = input()
      times_there = times_there + 1
      # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
      while selection not in ['m', 't', 'b', 'M', 't','b', 'w', 'W', 's', 'S']:
          print("Invalid selection.")
          selection = input()
          
  # Checks to see if the user selected A to go into the robot fight.   
  if selection == "a" or selection == "A":
      # description by Chatgpt
      print("A squat, one-metre-tall robot trudges through the red sand, its glowing red eyes cutting through the dusty haze. Metal claws twitch hungrily as it closes in, each step crunching against the barren earth.")
      if not description2:
        print("There are robots around, and they will try and to stop you from getting onto the train. Be careful.")
        description2 = True
      # Checks for the wooden bat. If the user doesn't have it, then it kills the user.
      if not item:
          # description by Chatgpt
          print("With a sudden lunge, the robot's metal claw smashes into your head!")
          hp(hpp, 10, "robot_ultrakill")
      else:
          if not description3:
            print("With your weapon, you're able to fight, but you'll need to type a sequence of letters quickly in order to do so.")
            description3 = True
            time.sleep(4)
            victory_determiner, hpp = robot_fights(5,"robot_bat_fight", hpp)
            # Checks to see if the user won the mini game that represented the robot fight.
            if victory_determiner == True:
              print("🥳You've collected a robot eye!🥳")
              item2 = True
              selection = "c"
              
  # Checks to see if the user selected S to look at the piles of robot scrap. This entire thing serves no purpose other than being a troll.
  # It uses the variable count to give a different input until it "kills" the user.
  if selection == "s" or selection == "S":
      if count == 0:
          print("This is some pretty interesting stuff")
          count = count + 1
          selection = "c"
      elif count == 1:
          print("You already looked at this")
          count = count + 1
          selection = "c"
      elif count == 2:
          print("w0w! S0 c00l! S0mE r0B0t paRts!")
          count = count + 1
          selection = "c"
      elif count == 3:
          print("You seem to clearly be invested in this pile of metal junk.")
          count = count + 1
          selection = "c"
      elif count == 4:
          print("Maybe you think there's candy inside like a PINATA!")
          count = count + 1
          selection = "c"
      elif count == 5:
          print("You hear the sounds of lasers charging behind you. You turn ar-")
          hp(hpp, 10, "robot_ultrakill")
      
          
  # returns the selection, status of the descriptions and items, it also returns intergers like count, hpp, and times_there.
  return selection.lower(), times_there, description2, item, hpp, description3, item2, count
  
def main_floor(description, description2, item, item2, description3, item3):
  """
  Represents the Train Station (main floor) location.
  Args:
    description (bool)
    description2 (bool)
    item (bool)
    item2 (bool)
    description3 (bool)
    item3 (bool)
  Returns:
    selection (str)
    description (bool)
    description2 (bool)
    item (bool)
    item2 (bool)
    description3 (bool)
    item3 (bool)
  """
  # Gives a unique description for the main floor, but it only appears the first time the user goes there.  
  if not description:
      # description by Chatgpt
      print("The main floor of the futuristic train station gleams with polished metal and holographic displays, except that these displays were turned off. The power was out. Near the ticket cashier's glowing kiosk, a heavy steel door marked Authorized Personnel Only hums, restricting access to the station's unseen depths.")
      description = True
  
  print("\nYou're in the main floor.")

  # User selects next location within or outside of the current location & input is validated
  print("Where would you like to go? \n[c] Crimson Sands (Outskirts) \n[t] Train Station (Top Floor) \n[b] Train Station (Basement) \n[w] Wooden Shack \n[a] Authorized Personnel only door \n[i] Cashier for train tickets")
  selection = input()
  # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
  while selection not in ['c','a', 'A', 't', 'b', 'C', 't', 'b', 'w', 'W', 'i', 'I']:
    print("Invalid selection.")
    selection = input()
  
  # Checks to see if the user selected A to go into the door.  
  if selection == "a" or selection == "A":
        # description by Chatgpt
        print("The room is pitch dark, filled with dust-covered shelves stacked with forgotten supply boxes. Stale air lingers as silence settles over the cold, lifeless space.")
        if not description2:
          print("Specfic items can unlock new areas with more items, so don't be afraid to look around.")
          description2 = True
        # Checking if the user has the keycard, but doesn't have the computer component.
        if item == True and item2 == False:
            print("🥳You've found a computer component!🥳")
            item2 = True
        # Checking if the user has both items.
        elif item == True and item2 == True:
            print("You've already searched this room.")
        else:
            print("The door is locked and needs a keycard of somesort.")
        selection = "m"
        
  # Checks to see if the user selected I to go to the ticket cashier.
  elif selection == "i" or selection == "I":
        # description by Chatgpt
        print("The ticket counter sits empty, with no one behind it, but the faint hum of a machine suggests it's still operational. Papers and ticket stubs are neatly stacked on the counter, waiting for the next passenger.")
        if not description3:
          print("You're able to search for items by going back and clicking an option over and over again.")
          description3 = True
        # Rng determines if the user gets the item, but it also checks for if the user already has the safe key.
        if random.choice(randomChance) == 2 and not item3:
            item3 = True
            print("🥳You've found a safe key!!🥳")
        elif item3 == True:
            print("There is nothing else here.")
        selection = "m"
      
  
  # returns the selection, status of the descriptions and items.
  return selection.lower(), description, description2, item, item2, description3, item3
  
def top_floor(description, description2, item, item2, activation, tdr, hpp, item3, count, trainpower, description3, boss, switch, gameover):
  """
  Represents the Train Station (top floor) location.
  Args:
    description (bool)
    description2 (bool)
    item (bool)
    item2 (bool)
    activation (bool)
    tdr (bool)
    hpp (int)
    item3 (bool)
    count (int)
    trainpower (bool)
    description3 (bool)
    boss (bool)
    switch (bool)
    gameover (bool)
  Returns:
    selection (str)
    description (bool)
    description2 (bool)
    item (bool)
    item2 (bool)
    activation (bool)
    tdr (bool)
    hpp (int)
    item3 (bool)
    count (int)
    trainpower (bool)
    description3 (bool)
    boss (bool)
    switch (bool)
    gameover (bool)
  """
  # Gives a unique description for the top floor, but it only appears the first time the user goes there.
  if not description:
      # description by Chatgpt
      print("The top floor is quiet, with a train control cabin at the far end, its screens dark and lifeless. Nearby, a deactivated train sits motionless on the tracks, its sleek exterior covered in a thin layer of dust, while cabinets filled with old manuals and tools line the walls, forgotten and untouched.")
      description = True
  
  print("\nYou're in the top floor.")

  # User selects next location within or outside of the current location & input is validated
  print("Where would you like to go? \n[c] Crimson Sands (Outskirts) \n[m] Train Station (Main Floor) \n[b] Train Station (Basement) \n[w] Wooden Shack \n[s] Search cabinets \n[i] Inside the train control centre, \n[r] Board the train")
  selection = input()
  # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
  while selection not in ['s', 'S', 'M', 't', 'b', 'C', 'm', 'c', 'w', 'W', 'i', 'I', 'r', 'R']:
    print("Invalid selection.")
    selection = input()
    
  # Checks to see if the user selected S to go to search the cabinets.
  if selection == "S" or selection == "s":
        print("You search through the large amount of cabinets.")
        if not description2:
          print("Specfic items can unlock new areas with more items, so don't be afraid to look around.")
          description2 = True
        # Rng determines if the user gets the item, but it also checks for if the user already has the keycard.
        if random.choice(randomChance) == 2 and not item:
            item = True
            print("🥳You've found a red keycard!!🥳")
        elif item == True:
            print("There is nothing else here.")
        selection = "t"
        
  # Checks to see if the user selected I to go the train control room.
  elif selection == "i" or selection == "I":
        if not activation:
            print("The door appears to be locked.")
            selection = "t"
        else:
            # Checks to see if the door has already been hacked into. 
            if not tdr:
                print("You must hack into this door.")
                if hacking(4, 4, 1, 4) == True:
                    tdr = True
                print("The door opened revealing the train control room.")
                
            # Two different menus appear after hacking and opening the door. 1 appears from when user hasn't turned on the train, and the other appears when the train is on.
            print("The train control room is small cabin on the rooftop of the building. \n There's a green light to tell that the power is on, \n but there's also a broken switch where the train is powered from. \n Also, a notebook left on a desk inside reveals the train \n has a key to be used in order to be driven.")
            if trainpower == False and item3 == False:
                decision = input("What will you do to start the train and open the locked doors. \n [s] Slap the control panel! \n [b] Use the bat as a lever replacent \n [r] Use the robot eye! \n [q] or do you leave? \n")
                # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
                while not decision in ['r', 'R', 'b', 'B', 'q', 'Q']:
                    if decision == "s" or decision == "S":
                        print("You slapped the controls. That did nothing! All you did was hurt your hand.")
                        if count == 0:
                            hpp = hp(hpp, 1, "slapcontrolpanel")
                            count = count + 1
                    else:
                        print("Invalid input")
                    decision = input("What will you do to start the train and open the locked doors. \n [s] Slap the control panel! \n [b] Use the bat as a lever replacent \n [r] Use the robot eye! \n [q] or do you leave? \n")
                # Checks to see if the user selected R, Q, or B, and gives outputs depending on the input.
                if decision == "r" or decision == "R":
                    print("You fidel around with the robot eye, trying to insert it into every single crevice in the control panel. \n Unfortunately, you get angry because it does nothing. \n You decide to toss it on the ground, and it bangs into a few pieces of metal. \n That's followed by a ticking noise and before you know it, the eye explodes!!")
                    hpp = hp(hpp, 100, "Robotattack")
                elif decision == "q" or decision == "Q":
                    print("You exit the control area.")
                    selection = "t"
                else:
                    print("You decide to place the bat inside the control panel where a lever is supposed to be. \n It doesn't quite fit, and you'll need something metal and bigger.")
                    selection = "t"
                    
            # This is the other decision, and by leaving the room, it starts the boss fight required to get the lever.
            elif trainpower == True and item3 == False:
                decision = input("What will you do to start the train and open the locked doors. \n [s] Slap the control panel! \n [b] Use the bat as a lever replacement \n [r] Use the robot eye! \n [q] or do you leave? \n")
                # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
                while not decision in ['r', 'R', 'b', 'B', 'q', 'Q']:
                    if decision == "s" or decision == "S":
                        print("You slapped the controls. That did nothing! All you did was hurt your hand.")
                        if count == 0:
                            hpp = hp(hpp, 1, "slapcontrolpanel")
                            count = count + 1
                    else:
                        print("Invalid input")
                    decision = input("What will you do to start the train and open the locked doors. \n [s] Slap the control panel! \n [b] Use the bat as a lever replacent \n [r] Use the robot eye! \n [q] or do you leave? \n")
                # Checks to see if the user selected R, Q, or B, and gives outputs depending on the input.
                if decision == "r" or decision == "R":
                    print("You fidel around with the robot eye, trying to insert it into every single crevice in the control panel. \n Unfortunately, you get angry because it does nothing. \n You decide to toss it on the ground, and it bangs into a few pieces of metal. \n That's followed by a ticking noise and before you know it, the eye explodes!!")
                    hpp = hp(hpp, 100, "Robotattack")
                elif decision == "b" or decision == "B":
                    print("You decide to place the bat inside the control panel where a lever is supposed to be. \n It doesn't quite fit, and you'll need something metal and bigger.")
                    selection = "t"
                else:
                    
                    # The beginning of the boss fight, where functions robot_fights is called to force the user into the "fight"
                    print("Your luck has finally run out. As soon as you step outside, you run into a large 10 metre high robot.")
                    print("With only a bat and a robot eye, Your forced to fight.")
                    if not description3:
                        print("Boss fights are much harder than mini fights, and take more skill and reflexes. \n Be prepared to do sequences of letters quickly. \n Stay on your feet!")
                    time.sleep(2)
                    victory_determiner, hpp = robot_fights(7,"Bossfight", hpp)
                    # Checks to see if the user passed the robot mini game.
                    if victory_determiner == True:
                        print("Quickly! He's weakened! Shoot him with the robot eye! Press f!")
                        rlist, wlist, xlist = select.select([sys.stdin], [], [], 2) 
                        if rlist:
                            # Check if they entered "f", and if they didn't or they were too slow, then the game ends.
                            if sys.stdin.readline().strip() == "f":
                                print("Nice! The robot stumbled backward, missing one of it's arms.")
                                print("The robot is getting angrier! It's faster! You need to be more quick to fire next time!")
                                print("You attack again!")
                                time.sleep(2)
                                victory_determiner = False
                                victory_determiner, hpp = robot_fights(7,"Bossfight", hpp)
                                 # Checks to see if the user passed the robot mini game.
                                if victory_determiner == True:
                                    print("Quickly! He's weakened! Shoot him with the robot eye! Press f!")
                                    rlist, wlist, xlist = select.select([sys.stdin], [], [], 1.5) 
                                    if rlist:
                                        # Check if they entered "f", and if they didn't or they were too slow, then the game ends.
                                        if sys.stdin.readline().strip() == "f":
                                            print("Nice! The robot stumbled backward, missing one of it's second arm.")
                                            print("The robot is getting angrier! It's EVEN faster! You need to be SOOOO quick to fire next time!")
                                            print("You attack again!")
                                            time.sleep(2)
                                            victory_determiner = False
                                            victory_determiner, hpp = robot_fights(5,"Bossfight", hpp)
                                            # Checks to see if the user passed the robot mini game.
                                            if victory_determiner == True:
                                                print("FINISH HIM! Press f!")
                                                rlist, wlist, xlist = select.select([sys.stdin], [], [], 1) 
                                                if rlist:
                                                    # Check if they entered "f", and if they didn't or they were too slow, then the game ends.
                                                    if sys.stdin.readline().strip() == "f":
                                                        print("The robot crashes to the ground, after you deliver the final blow!.")
                                                        time.sleep(1)
                                                        print("YOU WON!")
                                                        print("You also obtain a metal rod that can be used to replace the broken switch!")
                                                        boss = True
                                                        item3 = True
                                                        selection = "t"
                                                    else:
                                                        print("The robot crushes you with all of its might!")
                                                        print("💀💀💀💀 You died! 💀💀💀💀") 
                                                else:
                                                    print("Too SLOW! The robot kicks you into the metal of the train, killing you!")
                                                    print("💀💀💀💀 You died! 💀💀💀💀") 
                                        else:
                                            print("The robot crushes you with all of its might!")
                                            print("💀💀💀💀 You died! 💀💀💀💀")
                                    else:
                                        print("The robot crushes you with all of its might!")
                                        print("💀💀💀💀 You died! 💀💀💀💀")
                            else:   
                                print("The robot crushes you with all of its might!")
                                print("💀💀💀💀 You died! 💀💀💀💀")
                        else:   
                            print("The robot crushes you with all of its might!")
                            print("💀💀💀💀 You died! 💀💀💀💀")
            elif switch == True:
                print("The train is active, and it's powered, along with the rest of the building. Go to the train")
                selection = "t"
            else:
                print("You insert the metal rod into the shaft, flicking the lever and making the FULLY operational!")
                switch = True
                selection = "t"
  # Checks to see if the user selected r to go the train itself.
  elif selection == "r" or selection == "R":
      # Checks if all the crucial booleans are True, excluding the key.
      if activation == True and trainpower == True and switch == True:
          print("You enter the train.")
          # description by Chatgpt
          print("Inside the train, the seats are neatly arranged but coated in dust, with faded upholstery that hints at years of neglect. The dim lighting flickers intermittently, casting long shadows over the abandoned control panels, while the smell of stale air lingers in the cabin.")
          print("The drivers cabin reveals that you need a key to drive.")
          # If the user doesn't have the key, it will send them back to the while loop in the main, while having the key ends the while loop and allows the user to win.
          if not item2:
              print("You don't have the key.")
              selection = "t"
          else:
              print("You turn the key, and the train departs from the train station. Your journey is ONLY beginning.....")
              gameover = True
      else:
          print("You are unable to board the train because there is either no power in the building and none in the train itself.")
          selection = "t"
                        
  
  # returns the selection, status of the descriptions and items, as well as the boolean values behind key points of progression in the game, and two integers for health and a counter.
  return selection.lower(), description, description2, item, item2, activation, tdr, hpp, item3, count, trainpower, description3, boss, switch, gameover
  
def wooden_shack(description, item, item2, item3, item4, hpp, count):
  """
  Represents the Wooden Shack location.
  Args:
    description (bool)
    item (bool)
    item2 (bool)
    item3 (bool)
    item4 (bool)
    hpp (int)
    count (int)
  Returns:
    selection (str)
    description (bool)
    item (bool)
    item2 (bool)
    item3 (bool)
    item4 (bool)
    hpp (int)
    count (int)
  """
  # Gives a unique description for the wooden shack, but it only appears the first time the user goes there.
  if not description:
      # description by Chatgpt 
      print("A weathered wooden shack stands alone in the vast desert, its paint peeling and boards creaking in the wind. The cracked windows are covered in layers of dust, and the door hangs loosely on its hinges, swaying with every gust of the dry, relentless breeze.")
      description = True
   
  print("\nYou're at the wooden shack.")

  # User selects next location within or outside of the current location & input is validated
  print("Where would you like to go? \n[c] Crimson Sands (Outskirts) \n[m] Train Station (Main Floor) \n[b] Train Station (Basement) \n[t] Train Station (Top Floor) \n[i] Inside the wooden shack")
  selection = input()
  # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
  while selection not in ['M', 'B', 'b', 'C', 'm', 'c', 't', 'T', 'i', 'I']:
    print("Invalid selection.")
    selection = input()
  
  # Checks to see if the user selected I to go the inside of the wooden shack.
  if selection == "i" or selection == "I":
        # Checks for the wooden key to go inside.
        if not item2:
            print("There's a wooden lock on the shack. Try finding a key for it.")
            selection = "w"
        else:
            # description by Chatgpt
            print("Inside the shack, the air is thick with dust, and the dim light reveals a 30 cm tall robot in the corner, its small frame motionless and covered in grime. A weathered chest sits against the wall, its lid slightly ajar, while a heavy, rusted safe stands nearby, its combination lock worn from years of neglect.")
            # User selects next location within or outside of the current location & input is validated
            decision2 = input("Do you check: \n [c] The chest \n [s] The safe \n [t] The toy robot in the corner \n [q] or do you leave? \n")
            # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
            while not decision2 in ['c', 'C', 's', 'S', 'T', 't', 'q', 'Q']:
                print("Invalid input")
                decision2 = input("Do you check: \n [c] The chest \n [s] The safe \n [t] The toy robot in the corner \n [q] or do you leave? \n")
            # Checks if the user entered "q" as an input and goes back outside the shack.
            if decision2 == "q" or decision2 == "Q":
                print("You exit the shack.")
                selection = "w"
            # Checks if the user entered "c" as an input and gives the user a wooden bat if they don't already have it.
            elif decision2 == "c" or decision2 == "C":
                if not item:
                    print("You open it and discover a wooden bat. \n It may be useful in combat.")
                    print("🥳You've found a wooden bat!!🥳")
                    item = True
                    selection = "w"
                else:
                    print("The chest is empty. You've already searched this.")
                    selection = "w"
            # Checks if the user entered "s" and retrieves the contents of the safe.
            elif decision2 == "s" or decision2 == "S":
                # Checks to see if the user already has the train key.
                if not item4:
                    # Checks to see if the user has the safe key.
                    if not item3:
                        print("The safe is locked and requires a safe key.")
                    else:
                        print("You open it and discover a train key. \n It's useful in powering the train.")
                        print("🥳You've found a train key!!🥳")
                        item4 = True
                        selection = "w"
                else:
                    print("This safe is empty. You already searched it.")
                    selection = "w"
            else:
                # This else part is for the tiny robot option, which takes health and sends the user back to the while loop.
                if count == 0:
                    count = count + 1
                    print("You approach the tiny robot in the corner of the room \n Awww how cute!!!! \n It stands there glancing down on the ground and frozen, so you decide to touch it.")
                    time.sleep(0.5)
                    print("OWWWWWW")
                    hpp = hp(hpp, 10, "Robotattack")
                    print("You swipe the stupid robot off your face.")
                    selection = "w"
                else:
                    print("The robot is no longer in the corner is currently knocked out.")
                    selection = "w"
  
                
  # returns the selection, status of the descriptions and items as well as the integers of hpp and count
  return selection.lower(), description, item, item2, item3, item4, hpp, count
  
def basement(description, item, activation, hpp, description2, dr, item2, trainpower, item3):
  """
  Represents the Train Station (basement) location.
  Args:
    description (bool)
    item (bool)
    activation (bool)
    hpp (int)
    description2 (bool)
    dr (bool)
    item2 (bool)
    trainpower (bool)
    item3 (bool)
  Returns:
    selection (str)
    description (bool)
    item (bool)
    activation (bool)
    hpp (int)
    description2 (bool)
    dr (bool)
    item2 (bool)
    trainpower (bool)
    item3 (bool)
  """
  # Gives a unique description for the basement, but it only appears the first time the user goes there.
  if not description:
      # Description by Chatgpt
       print("The basement of the train station is a maze of dark, narrow corridors, lined with exposed pipes and flickering lights. Old crates and forgotten equipment are scattered around, and the air smells damp and stale, with an unsettling silence hanging in the space.")
       description = True
   
  print("\nYou're in the basement.")

  # The options where to go vary depending on whether the power and/or the train power is activated.
  if activation == False and trainpower == False:
      print("Where would you like to go? \n[c] Crimson Sands (Outskirts) \n[m] Train Station (Main Floor) \n[w] Wooden Shack \n[t] Train Station (Top Floor) \n[s] Straight down the hall \n[r] Take the right. \n[l] Take the left.")
      selection = input()
      # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
      while selection not in ['M', 'W', 'w', 'C', 'm', 'c', 't', 'T', 's', 'S', 'l', 'L', 'r', 'R']:
        print("Invalid selection.")
        selection = input()
        
  # These set of options only appear if the power is on, but the train power isn't.     
  elif activation == True and trainpower == False:
      print("Where would you like to go? \n[c] Crimson Sands (Outskirts) \n[m] Train Station (Main Floor) \n[w] Wooden Shack \n[t] Train Station (Top Floor) \n[r] Take the right. \n[l] Take the left.")
      selection = input()
      # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
      while selection not in ['M', 'W', 'w', 'C', 'm', 'c', 't', 'T', 'l', 'L', 'r', 'R']:
        print("Invalid selection.")
        selection = input()
        
  # These become the options when both powers are working. 
  else:
      print("Where would you like to go? \n[c] Crimson Sands (Outskirts) \n[m] Train Station (Main Floor) \n[w] Wooden Shack \n[t] Train Station (Top Floor) \n[l] Take the left.")
      selection = input()
      # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
      while selection not in ['M', 'W', 'w', 'C', 'm', 'c', 't', 'T', 'l', 'L']:
        print("Invalid selection.")
        selection = input()
        
  # Checks to see if the user selected s to go toward the generator and straight down the hall.
  if selection == "s" or selection == "s":
        # Description by Chatgpt
        print("The tunnel is narrow and dimly lit, with concrete walls smeared in grime and faint electrical hums echoing through the air. At the end, a fusebox is mounted on the wall, surrounded by rusted tools, discarded wires, and old maintenance equipment, all left in disarray.")
        # Checks for the robot eye item, if it's false, then it will set selection to "b".
        if not item:
            print("This generator has been sealed shut by liquid metal. Try and find something to melt it down.")
            selection = "b"
        else:
            print("You melt the metal more, causing it to drip onto the ground. You flick open the fusebox and flick the fuses, turning on everything")
            activation = True
            print("You turn around and see that a laser security system has turned off, seperating you from the way back.")
            decision = input("Do you: \n [g] Go through the lasers \n [u] Use the robot eye \n")
            # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
            while not decision in ['g', 'G', 'u', 'U']:
                print("Invalid input")
                decision = input("Do you: \n [g] Go through the lasers \n [u] Use the robot eye \n")
            # Checks to see if the user selected g to try and jump through lasers, which is just death.
            if decision == "g" or decision == "G":
                print("You jump through the lasers and trip oh no! \n You activate the security system and tons of droids show up!")
                hp(hpp, 10, "robot_ultrakill")
            # Checks to see if the user selected u to try and jump through lasers, which is the correct option.
            elif decision == "u" or decision == "U":
                print("You shoot the laser grid, shutting down the lasers in front of you.")
                selection = "b"
                
  # Checks to see if the user selected "l" to go left.           
  if selection == "L" or selection == "l":
      # Checks if the user has the wooden key already. If they not, they are rewarded with the wooden key.
      if not item3:
        print("You've stumbled upon a storage room with a chest. \n You open it and discover a wooden key. \n It may be useful in opening a place.")
        print("🥳You've found a wooden key!!🥳")
        item3 = True
        selection = "b"
      else:
        print("The storage room is empty. You've already searched this place.")
        selection = "b"
        
  # Checks to see if the user selected "r" to go right.               
  if selection == "r" or selection == "R":
        print("Down the fluorescent white halls, you notice a steel door at the end of the hall.")
        # Checks if the generator has been turned on.
        if activation == False:
            print("The door is shut, and turned off.")
            selection = "b"
        else:
            print("Now it's time to hack the system")
            if description2 == False:
                print("insert description")
                description2 = True
            # Checks to see if the computer lab door has been opened yet. If it hasn't, the user must go through the hacking minigame.
            if not dr:
                if hacking(3, 3, 1, 2) == True:
                    dr = True
                print("The door opened revealing the computer lab")
            print("The computer lab is fairly empty with only three computers. \n One is at the far left of the room. \n One is at the far right. \n And one is near the entrance of the door. \n They look as if they need computer components to make them work, but they may be of use.")
            decision2 = input("Do you check: \n [c] The computer close the door \n [l] The one on the far left \n [r] The one on the far right \n [q] or do you leave? \n")
            # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
            while not decision2 in ['c', 'C', 'l', 'L', 'r', 'R', 'q', 'Q']:
                print("Invalid input")
                decision2 = input("Do you check: \n [c] The computer close to the door \n [l] The one on the far left \n [r] The one on the far right \n [q] or do you leave? \n")
            # Checks to see if the user selected "q" to exit.
            if decision2 == "q" or decision2 == "Q":
                print("You exit the room.")
                selection = "b"
                
            # Checks to see if the user selected "c", refering to the close computer.
            elif decision2 == "c" or decision2 == "C":
                # Checks for the computer component. If the user doesn't have it, then it goes to the main while loop.
                if not item2:
                    print("You don't have a computer component.")
                    selection = "b"
                else:
                    print("You open the computer next to the door and are now forced to hack into it.")
                    decision3 = input("Are you sure you'd like to open it? [y] Yes or [n] No? \n")
                    # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
                    while not decision3 in ['y', 'Y', 'N', 'n']:
                        print("Invalid input")
                        decision3 = input("Are you sure you'd like to open it? [y] Yes or [n] No? \n")
                    # Checks to see if the user selected "y".
                    if decision3 == "y" or decision3 == "Y":
                        if hacking(2, 2, 0.5, 2) == True:
                            print("You opened the computer, but have just discovered that this computer tracks your location. \n You turn around...")
                            hp(hpp, 10, "robot_ultrakill")
                    else:
                        selection = "b"
                        
            # Checks to see if the user selected "r", refering to the right computer.            
            elif decision2 == "r" or decision2 == "R":
                # Checks for the computer component. If the user doesn't have it, then it goes to the main while loop.
                if not item2:
                    print("You don't have a computer component.")
                    selection = "b"
                else:
                    print("You open the computer next to the door and are now forced to hack into it.")
                    decision4 = input("Are you sure you'd like to open it? [y] Yes or [n] No? \n")
                    # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
                    while not decision4 in ['y', 'Y', 'N', 'n']:
                        print("Invalid input")
                        decision4 = input("Are you sure you'd like to open it? [y] Yes or [n] No? \n")
                    # Checks to see if the user selected "y".
                    if decision4 == "y" or decision4 == "Y":
                        if hacking(2, 2, 0.5, 2) == True:
                            print("You opened the computer, but have just discovered that this computer tracks your location. \n You turn around...")
                            hp(hpp, 10, "robot_ultrakill")
                    else:
                        selection = "b"
                        
                # The else option is refering to the computer on the left side.
            else:
                # Checks for the computer component. If the user doesn't have it, then it goes to the main while loop.
                if not item2:
                    print("You don't have a computer component.")
                    selection = "b"
                else:
                    print("You open the computer next to the door and are now forced to hack into it.")
                    decision5 = input("Are you sure you'd like to open it? [y] Yes or [n] No? \n")
                    # Checks that the user has entered a legitimate entry. By using a list with upper & lower case, we can avoid using .lower() and allow both cases.
                    while not decision5 in ['y', 'Y', 'N', 'n']:
                        print("Invalid input")
                        decision5 = input("Are you sure you'd like to open it? [y] Yes or [n] No? \n")
                    # Checks to see if the user selected "y".
                    if decision5 == "y" or decision5 == "Y":
                        if hacking(2, 2, 0.5, 2) == True:
                            print("This computer doesn't track your location and provides a way to turn on power to the train, since it's currently disabled. \n")
                            print("You turn it on.")
                            trainpower = True
                            selection = "b"
                    else:
                        selection = "b"
                
                        
                
  # returns the selection, status of the descriptions and items as well as the hpp (int)
  return selection.lower(), description, item, activation, hpp, description2, dr, item2, trainpower, item3
  
def hp(health, damage_taken, damageType):
  """
  The function manages the players health.
  Args:
    health (int)
    damage_taken (int)
    damageType (str)
  Returns:
    health(int)
  """
  # The program checks which type of damage was passed as an argument string.
  if damageType == "robot_ultrakill":
    while not health <= 0:
        health = health - damage_taken
        print(f"You've just lost {damage_taken} health. You're now at {health} hp!")
        time.sleep(0.5)
        
    print("💀💀💀💀 You died! 💀💀💀💀")
  # This one checks if it's "Robotattack"
  elif damageType == "Robotattack":
      health = health - damage_taken
      print(f"You've just lost {damage_taken} health. You're now at {health} hp!")
      # Makes the user lose if health <= 0.
      if health <= 0:
        print("💀💀💀💀 You died! 💀💀💀💀")
        
  # This one checks for "slapcontrolpanel"     
  elif damageType == "slapcontrolpanel":
      health = health - damage_taken
      print(f"You've just lost {damage_taken} health. You're now at {health} hp!")
      # Makes the user lose if health <= 0.
      if health <= 0:
        print("💀💀💀💀 You died! 💀💀💀💀")
        
  # Health is returned so it's saved across all functions.
  return health
    
def robot_fights(times_to_swing, type, hpp):
  """
  The function manages fights with robots.
  Args:
    times_to_swing (int)
    type (str)
    hpp (int)
  Returns:
    fight_won (bool)
    hpp (int)
  """
  randomLetter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  # The program checks which type of damage was passed as an argument string.
  if type == "robot_bat_fight":
      fight_won = False
      sucessful_attempts = 0
      attempts = 0
      selectedLetter = 0
      # The while loop only stops when the amount of attempts match the times the user guessed letters for.
      while attempts < times_to_swing:
          chosenLetter = random.choice(randomLetter)
          print(chosenLetter)
          rlist, wlist, xlist = select.select([sys.stdin], [], [], 2) 
          if rlist:
              # Checks if the user entered the letter. If it's wrong, or they run out of time, they will fall into the else catorgories.
              if sys.stdin.readline().strip() == chosenLetter:
                  print("You struck him! Nice work!")
                  sucessful_attempts = sucessful_attempts + 1
                  attempts = attempts + 1
              else:
                  print("You missed!")
                  attempts = attempts + 1
          else:
              print("You took too long and now he hit you!")
              attempts = attempts + 1
              hpp = hp(hpp, 10, "Robotattack") 
      # After the while loop, the program checks if at least three of the letters were typed right.
      if sucessful_attempts < 3:
          print("You're too injured. The robot got the best of you, finishing you off!")
          hpp = hp(hpp, 10, "robot_ultrakill")
          # fight_won is returned as a value that carries True or False, while hpp is carried over to be used in the global scope.
          return fight_won, hpp
      else:
          fight_won = True
          # fight_won is returned as a value that carries True or False, while hpp is carried over to be used in the global scope.
          return fight_won, hpp
  # This one checks if it's "Bossfight"
  elif type == "Bossfight":
      fight_won = False
      sucessful_attempts = 0
      attempts = 0
      selectedLetter = 0
      # The while loop only stops when the amount of attempts match the times the user guessed letters for.
      while attempts < times_to_swing:
          chosenLetter = random.choice(randomLetter)
          print(chosenLetter)
          rlist, wlist, xlist = select.select([sys.stdin], [], [], 1.5) 
          if rlist:
              # Checks if the user entered the letter. If it's wrong, or they run out of time, they will fall into the else catorgories.
              if sys.stdin.readline().strip() == chosenLetter:
                  print("You struck him! Nice work!")
                  sucessful_attempts = sucessful_attempts + 1
                  attempts = attempts + 1
              else:
                  print("You missed!")
                  attempts = attempts + 1
          else:
              print("You took too long and now he hit you!")
              attempts = attempts + 1
              hpp = hp(hpp, 10, "Robotattack") 
      # After the while loop, the program checks if at least FIVE  of the letters were typed right.
      if sucessful_attempts < 5:
          print("Unfortunatly, you've taken too much damage. It's ALL over....")
          hpp = hp(hpp, 10, "robot_ultrakill")
          # fight_won is returned as a value that carries True or False, while hpp is carried over to be used in the global scope.
          return fight_won, hpp
      else:
          fight_won = True
          # fight_won is returned as a value that carries True or False, while hpp is carried over to be used in the global scope.
          return fight_won, hpp
      
def hacking(rounds, memory_Numbers, speedBetweenNumbers, speedtoEnter):
  """
  The function manages the hacking parts.
  Args:
    rounds (int)
    memory_Numbers (int)
    speedBetweenNumbers (int)
    speedtoEnter (int)
  Returns:
    successful (bool)
  """
  successful = False
  completed_rounds = 0
  randomNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  code = []
  # This while keeps track of how many rounds were completed by the user.
  while completed_rounds < rounds:
      # The for loop repeats adding random numbers to a list by memory_Numbers before asking the user.
      for i in range(memory_Numbers):
          if len(code) == memory_Numbers:
             password = ''.join(code)
             print("What's the sequence of numbers?")
             rlist, wlist, xlist = select.select([sys.stdin], [], [], speedtoEnter) 
             if rlist:
                # Checks if the user entered the letter. If it's wrong, or they run out of time, they will fall into the else catorgories.
                if sys.stdin.readline().strip() == password:
                   print("Good job!")
                   completed_rounds = completed_rounds + 1
                   code.clear()
                else:
                   print("That's incorrect")
                   code.clear()
                   completed_rounds = 0
                   print("All your hacking work has just been reset.")
                   time.sleep(speedBetweenNumbers)
             else:
                   print("That's incorrect")
                   code.clear()
                   completed_rounds = 0
                   print("All your hacking work has just been reset.")
                   time.sleep(speedBetweenNumbers)
          else:
                (chosenNumber) = random.choice(randomNumber)
                print(chosenNumber)
                time.sleep(speedBetweenNumbers)
                clear()
                code.append(str(chosenNumber))
                
  # Once the user has guessed enough rounds, the function will pass a True value through successful.             
  successful = True
  return successful
         
    
  
# ===Main===
print("The sounds of dust breeze against your hair. You've arrived at a train station in the vast")
print("Crimson Sands. Tumbleweed roll across the red sands of the desert, as the dusty winds shift")
print("the scorching sands across the ground. The train station contrasts the empty desert. It's a")
print("large steel and white concrete constructed building. On the right side of the building,")
print("large steel pillars stood, with a rail leading into the distance. On the left side, a")
print("wooden shack stood, about 50 metres from the building. It's run down, and OLD. While taking")
print("a peek inside the train station, you've discovered it's also been abandoned for a while,")
print("and only some of the lights work. There is a main floor, a basement, and an upward floor.")
print("Your goal? Get the train powered to take a trip to Venture Corp. You hear the sounds of")
print("metal clanging in the distance. Something is coming.")

# initialize user to start in the Crimson Sands.
choice = 'c'
playerHealth = 100
# Initialize list to show no items have been found.
#  [0]=Red Keycard, [1] = Computer component,[2] = bat, [3] = robot eye, [4] wooden key, [5] safe key, [6] train key, [7] train switch,
foundItems = [False, False, False, False, False, False, False, False]
endOfGame = False
# Each location will have a description that will only be outputed once, controled by the list of booleans.
# [0]Main floor, [1]Top Floor, [2]Wooden Shack, [3]Basement (Crimson sands doesn't have a description)
locationDescriptions = [False, False, False, False]
# Mechanic descriptions tell how mechanics in the game work.
# [0] Searching, [1] Opening areas, [2] you can fight stuff, [3] How to fight stuff, [4] Hacking, [5] Bosses
mechanicDescriptions = [False, False, False, False, False, False]
randomChance = [1, 2, 3, 4, 5]
timesVisited = 0
# Three different counters, since counter is being returned, so seperate counter variables need to be used to remove confusion.
counter = 0
counter2 = 0
counter3 = 0
generatorActivation = False
rightDoorOpened = False
trainPowered = False
trainDoorOpened = False
TrainswitchOn = False
Boss1defeated = False

# Calls the appropriate location function based on which selection the user has made.
while endOfGame == False:
  if choice == 'c':
    # The crimson sands location has many important arguments to be passed, ranging from descriptions, items, and integer values like the counter or health.
    choice, timesVisited, mechanicDescriptions[2], foundItems[2], playerHealth, mechanicDescriptions[3], foundItems[3], counter = crimson_sands(timesVisited, mechanicDescriptions[2], foundItems[2], playerHealth, mechanicDescriptions[3], foundItems[3], counter)
  elif choice == 'm':
    # Main floor doesn't have as much, only passing descriptions and items.
    choice, locationDescriptions[0], mechanicDescriptions[1], foundItems[0], foundItems[1], mechanicDescriptions[0], foundItems[5] = main_floor(locationDescriptions[0], mechanicDescriptions[1], foundItems[0], foundItems[1], mechanicDescriptions[0], foundItems[5])
  elif choice == 't':
    # The top part of the train station has many important arguments to be passed, ranging from descriptions, items, and integer values like the counter or health. The top part also contains the boss fight, and how to win, so it also has conditional booleans.
    choice, locationDescriptions[1], mechanicDescriptions[0], foundItems[0], foundItems[6], generatorActivation, trainDoorOpened, playerHealth, foundItems[7], counter3, trainPowered, mechanicDescriptions[5], Boss1defeated, TrainswitchOn, endOfGame = top_floor(locationDescriptions[1], mechanicDescriptions[0], foundItems[0], foundItems[6], generatorActivation, trainDoorOpened, playerHealth, foundItems[7], counter3, trainPowered, mechanicDescriptions[5], Boss1defeated, TrainswitchOn, endOfGame) 
  elif choice == 'w':
    # The wooden shack has many important arguments to be passed, ranging from descriptions, items, and integer values like the counter or health.
    choice, locationDescriptions[2], foundItems[2], foundItems[4], foundItems[5], foundItems[6], playerHealth, counter2 = wooden_shack(locationDescriptions[2], foundItems[2], foundItems[4], foundItems[5], foundItems[6], playerHealth, counter2)
  elif choice == 'b':
    # The basement part of the train station has many important arguments to be passed, ranging from descriptions, items, and integer values like the counter or health. The top part also contains the boss fight, and how to win, so it also has conditional booleans.
    choice, locationDescriptions[3], foundItems[3], generatorActivation, playerHealth, mechanicDescriptions[4], rightDoorOpened, foundItems[1], trainPowered, foundItems[4] = basement(locationDescriptions[3], foundItems[3], generatorActivation, playerHealth, mechanicDescriptions[4], rightDoorOpened, foundItems[1], trainPowered, foundItems[4])

# Will only print when the while loop ends, when the user wins the game.    
print("YOU WIN THE GAME!!!! CONGRATS!!!!")