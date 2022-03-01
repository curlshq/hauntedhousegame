from os import system, name
import time
import sys
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1/64)

slowprint("DISCLAIMER: It is recommended that you do not resize the terminal at any point within gameplay.\n\
If you wish to adjust the window size, do so now. Thank you.\n")
time.sleep(2)
slowprint("WARNING: This game contains triggering content to some players, such as flashing lights or violent content.\n\
Continue with caution.\n")
time.sleep(2.5)

input("Press ENTER to begin.")
def clear():
    if name == 'nt':
        _ = system('cls')
clear()

print("\033[0;31m\
░█████╗░██╗░░██╗░█████╗░██████╗░████████╗███████╗██████╗░  ░░███╗░░██╗\n\
██╔══██╗██║░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  ░████║░░╚═╝\n\
██║░░╚═╝███████║███████║██████╔╝░░░██║░░░█████╗░░██████╔╝  ██╔██║░░░░░\n\
██║░░██╗██╔══██║██╔══██║██╔═══╝░░░░██║░░░██╔══╝░░██╔══██╗  ╚═╝██║░░░░░\n\
╚█████╔╝██║░░██║██║░░██║██║░░░░░░░░██║░░░███████╗██║░░██║  ███████╗██╗\n\
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚══════╝╚═╝\n\
\n\
███████╗░██████╗░█████╗░░█████╗░██████╗░███████╗  ██████╗░░█████╗░░█████╗░███╗░░░███╗\n\
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██╔══██╗████╗░████║\n\
█████╗░░╚█████╗░██║░░╚═╝███████║██████╔╝█████╗░░  ██████╔╝██║░░██║██║░░██║██╔████╔██║\n\
██╔══╝░░░╚═══██╗██║░░██╗██╔══██║██╔═══╝░██╔══╝░░  ██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║\n\
███████╗██████╔╝╚█████╔╝██║░░██║██║░░░░░███████╗  ██║░░██║╚█████╔╝╚█████╔╝██║░╚═╝░██║\n\
╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝  ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝\n\
\n\
\033[1;30m\
\033[3m\
Written By\n\
Derrick Martinez\n\
\n")
print("\033[1;33m\
Select an option below:\n1: Begin Story\n2: Instructions\n")

def menu_select():
    valid = False
    while not valid:
        selection = str(input("Input: "))
        if selection == "1":
            valid = True
        elif selection == "2":
            print("You must respond to prompts with valid responses in order to escape the room.\n")
        else:
            print("Please enter either '1' or '2' to continue.\n")
menu_select()

print("-------------------------")
slowprint("You wake up in a ~room~, crowded with desolation.\nThe first thing you notice is a chipped, wooden ~door~ looking down on you.\n")

def first_move():
    at_paper = False
    while not at_paper:
        door_room = str(input("Input: ")).strip().lower()
        if "door" in door_room:
            slowprint("You inspect the door and notice it's locked. It requires a key.\nMaybe take a look around the ~room~?\n")
        elif "room" in door_room:
            slowprint("You look around the room and see a soggy, torn up piece of ~paper~ on the floor.\nYou also spot a ~safe~ cowering in the corner of the room.\n")
            at_paper = True
        else:
            print("Please enter a valid response.\n")
first_move()

def decryption():
    at_trans = False
    while not at_trans:
        safe_paper = str(input("Input: ")).strip().lower()
        if "safe" in safe_paper:
            slowprint("You inspect the safe and see a keypad with an etching above it, marking 'Ψ Ω Σ Ξ Π Φ Δ Θ'.\nYou may need to find something that has writing on it. Perhaps a piece of ~paper~.\n")
        elif "paper" in safe_paper:
            slowprint("You take a look at the paper and see symbol decryptions.\nΔ = 3\nΣ = 1\nΠ = 9\nΨ = 6\nΦ = 5\nΘ = 7\nΩ = 2\nΞ = 8\nThis may be useful to unlocking something. Perhaps a ~safe~.\n")
            at_trans = True
        else:
            print("Please enter a valid response.\n")
decryption()

def unlock():
    at_key = False
    while not at_key:
        safe_code = str(input("Input: ")).strip().lower()
        if "safe" in safe_code:
            slowprint("You inspect the safe and see a keypad with an etching above it, marking 'Ψ Ω Σ Ξ Π Φ Δ Θ'.\nEnter the code.\n")
            while True:
                answer = str(input("Input: ")).strip()
                if answer == "62189537":
                    slowprint("You have unlocked the safe.\nInside you find a key.\nThis may be useful for opening a ~door~.\n")
                    break
                else:
                    slowprint("The safe beeps in denial.\nTry again.\n")
            at_key = True
        else:
            print("Please enter a valid response.\n")
unlock()

def escape():
    at_exit = False
    while not at_exit:
        door = str(input("Input: ")).strip().lower()
        if "door" in door:
            slowprint("You walk up to the door as it stands over you.\nIt looks like you need a ~key~ to unlock it.\n")
            use_key = str(input("Input: ")).strip().lower()
            if "key" in use_key:
                slowprint("You have escaped the room!\n")
                at_exit = True
        else:
            print("Please enter a valid response.\n")
escape()

time.sleep(1)
slowprint("Would you like to continue to 'Chapter 2: Abduction'? [y/n]\n\
WARNING: EXITING THE GAME NOW WILL DELETE ALL SAVED DATA\n")

def cont():
    at_ch2 = False
    while not at_ch2:
        pick = str(input("Input: ")).strip().lower()
        if "y" in pick:
            at_ch2 = True
        elif "n" in pick:
            print("\nThanks for playing!")
            input("Press ENTER to exit.\n")
            exit()
        else:
            print("Please enter either 'yes/y' or 'no/n'.\n")
cont()

print("-------------------------")

#start ch2

print("\033[0;31m\
░█████╗░██╗░░██╗░█████╗░██████╗░████████╗███████╗██████╗░  ██████╗░██╗\n\
██╔══██╗██║░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  ╚════██╗╚═╝\n\
██║░░╚═╝███████║███████║██████╔╝░░░██║░░░█████╗░░██████╔╝  ░░███╔═╝░░░\n\
██║░░██╗██╔══██║██╔══██║██╔═══╝░░░░██║░░░██╔══╝░░██╔══██╗  ██╔══╝░░░░░\n\
╚█████╔╝██║░░██║██║░░██║██║░░░░░░░░██║░░░███████╗██║░░██║  ███████╗██╗\n\
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚══════╝╚═╝\n\
\n\
░█████╗░██████╗░██████╗░██╗░░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗\n\
██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║\n\
███████║██████╦╝██║░░██║██║░░░██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║\n\
██╔══██║██╔══██╗██║░░██║██║░░░██║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║\n\
██║░░██║██████╦╝██████╔╝╚██████╔╝╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║\n\
╚═╝░░╚═╝╚═════╝░╚═════╝░░╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝\n\
\n\
\033[1;30m\
\033[3m\
Written By\n\
Derrick Martinez\n\
\n")
print("\033[1;33m\
Select an option below:\n1: Continue Story\n2: Instructions\n")

def menu_select():
    valid = False
    while not valid:
        selection = str(input("Input: "))
        if selection == "1":
            valid = True
        elif selection == "2":
            print("You must respond to prompts with valid responses in order to reach the end of the hall.\n")
        else:
            print("Please enter either '1' or '2' to continue.\n")
menu_select()

print("-------------------------")
slowprint("\
Upon exiting the room, a long hallway stretches long before you.\n\
Within the fading darkness, you make out two doors.\n\
Each to your ~left~ and to your ~right~.\n")

def first_move():
    at_room2 = False
    while not at_room2:
        left_right = str(input("Input: ")).strip().lower()
        if "left" in left_right:
            slowprint("You notice that the the door is fastened by large, rusty chains held together by a padlock.\n\
Maybe try the door to the ~right~?\n")
        elif "right" in left_right:
            slowprint("The hinges barely hold on to the door, but you managed to carefully open it.\n\
The room's pungent must causes your breathing to become sluggish and burdensome.\n\
You scan the room and find a ~hairpin~ on top of a ~drawer~.\n")
            at_room2 = True
        else:
            print("Please enter a valid response.\n")
first_move()

def get_code():
    at_password = False
    while not at_password:
        drawer_pin = str(input("Input: ")).strip().lower()
        if "drawer" in drawer_pin:
            slowprint("You search the drawer thoroughly and find a note.\n\
Written on it is a message that instructs:\n\
'Starting from 0, go to 8, then 3, then 12, then 7, then back to 12.'\n\
This may be a sequence for unlocking a ~padlock~.\n")
            at_password = True
        elif "hairpin" in drawer_pin:
            slowprint("You pick up the hairpin and decide to try picking the padlock on the door to the left.\n\
Unfortunately, you don't know how to pick locks.\n\
Perhaps the ~drawer~ has something more useful for you.\n")
        else:
            print("Please enter a valid response.\n")
get_code()

def lock():
    at_lock = False
    while not at_lock:
        code_padlock = str(input("Input: ")).strip().lower()
        if "padlock" in code_padlock:
            slowprint("You kneel in front of the padlock that gatekeeps the door to the left.\n\
You must enter the combination chronologically using '<' and '>' in order to go from number to number.\n")
            at_lock = True
        else:
            print("Please enter a valid response.\n")
lock()

def unlock():
    at_unlock = False
    while not at_unlock:
        answer = str(input("Input: ")).strip()
        if ">>>>>>>><<<<<>>>>>>>>><<<<<>>>>>" in answer:
            slowprint("The padlock clicks open and drops dead to the ground as if hanging on the chain link was debilitating.\n\
You unwind the chains as the door creaks open.\n\
Peeping into the suprisingly lit and organized room, you see a ~toolbox~ awkwardly standing in the center.\n")
            at_unlock = True
        else:
            slowprint("The padlock resets.\n\
Take a look at the pattern once more.\n\
Then, make another attempt.\n")
unlock()

def flashlight():
    at_tool = False
    while not at_tool:
        open_toolbox = str(input("Input: ")).strip().lower()
        if "toolbox" in open_toolbox:
            slowprint("You lift the hood of the toolbox and find only a ~flashlight~.\n\
With some light, you could feasibly discover what remains of the barren ~hall~.\n")
            at_tool = True
        else:
            print("Please enter a valid response.\n")
flashlight()

def discovery():
    at_hall = False
    while not at_hall:
        walk_to = str(input("Input: ")).strip().lower()
        if "flashlight" in walk_to:
            slowprint("You take a look at the flashlight in your possession.\n\
It looks like it's built to be resilient.\n\
It is exactly what you need for the long, dark ~hall~ right outside.\n")
        elif "hall" in walk_to:
            slowprint("You step out of the cleanly room, back into the heavy, humid environment that resides within the rest of the facility.\n\
You turn on your newly obtained flashlight and see that there's a highly reflective ~thing~ hanging from the ceiling.\n")
            at_hall = True
        else:
            print("Please enter a valid response.\n")
discovery()

def end():
    at_end = False
    while not at_end:
        inspect_thing = str(input("Input: ")).strip().lower()
        if "thing" in inspect_thing:
            slowprint("You go to inspect the thing, it's a.aaa.a.a.aa...a")
            at_end = True
        else:
            print("Please enter a valid response.")
end()

time.sleep(5/2)

def jumpscare():
    message = "\033[0;31m\033[3mBEHIND YOU"
    amount = 0
    while amount < 24:
        print(message)
        amount += 1
        time.sleep(1/32)
jumpscare()

import asset0

#start ch3

print("\033[0;31m\
░█████╗░██╗░░██╗░█████╗░██████╗░████████╗███████╗██████╗░  ██████╗░██╗\n\
██╔══██╗██║░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  ╚════██╗╚═╝\n\
██║░░╚═╝███████║███████║██████╔╝░░░██║░░░█████╗░░██████╔╝  ░█████╔╝░░░\n\
██║░░██╗██╔══██║██╔══██║██╔═══╝░░░░██║░░░██╔══╝░░██╔══██╗  ░╚═══██╗░░░\n\
╚█████╔╝██║░░██║██║░░██║██║░░░░░░░░██║░░░███████╗██║░░██║  ██████╔╝██╗\n\
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░╚═╝\n\
\n\
░██████╗██████╗░██╗████████╗████████╗██╗███╗░░██╗░██████╗░  ██╗███╗░░░███╗░█████╗░░██████╗░███████╗\n\
██╔════╝██╔══██╗██║╚══██╔══╝╚══██╔══╝██║████╗░██║██╔════╝░  ██║████╗░████║██╔══██╗██╔════╝░██╔════╝\n\
╚█████╗░██████╔╝██║░░░██║░░░░░░██║░░░██║██╔██╗██║██║░░██╗░  ██║██╔████╔██║███████║██║░░██╗░█████╗░░\n\
░╚═══██╗██╔═══╝░██║░░░██║░░░░░░██║░░░██║██║╚████║██║░░╚██╗  ██║██║╚██╔╝██║██╔══██║██║░░╚██╗██╔══╝░░\n\
██████╔╝██║░░░░░██║░░░██║░░░░░░██║░░░██║██║░╚███║╚██████╔╝  ██║██║░╚═╝░██║██║░░██║╚██████╔╝███████╗\n\
╚═════╝░╚═╝░░░░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝\n\
\n\
\033[1;30m\
\033[3m\
Written By\n\
Derrick Martinez\n\
\n")
print("\033[1;33m\
Select an option below:\n1: Continue Story\n2: Instructions\n")

def menu_select():
    valid = False
    while not valid:
        selection = str(input("Input: "))
        if selection == "1":
            valid = True
        elif selection == "2":
            print("You must respond to prompts with valid responses in order to...")
            time.sleep(2)
            slowprint("Hm... ")
            time.sleep(3/2)
            slowprint("You will follow it.\n")
        else:
            print("Please enter either '1' or '2' to continue.\n")
menu_select()

print("-------------------------")

time.sleep(1)
slowprint("I don't know anymore.\n")
time.sleep(1)
slowprint("You may proceed down the ~hall~.")
time.sleep(1)
slowprint("Or you can just ~stand~ there.\n")


def first_move():
    at_outhall = False
    while not at_outhall:
        hall_stand = str(input("Input: ")).strip().lower()
        if "stand" in hall_stand:
            slowprint("You stand there.\n\
Processing what just happened.\n")
            time.sleep(1)
            slowprint("Yield ~onward~, whenever you are ready.\n")
        elif "hall" in hall_stand or "onward" in hall_stand:
            slowprint("The hall seems to never end.\n\
Even with your flashlight, you cannot see past the void of darkness.\n\
Regardless, you take precarious steps into the hall, still in immense shock.\n")
            time.sleep(1)
            slowprint("Enter however many steps you'd like to take forward.\n")
            at_outhall = True
        else:
            print("Please enter a valid response.\n")
first_move()

def person():
    at_person = False
    amount = 0
    while not at_person:
        while True:
            try:
                amount += int(input("Input: "))
            except ValueError:
                print("Please enter a number.")
            else:
                break
        if amount < 32:
            slowprint("Your flashlight reveals nothing.\n\
Walk further.\n")
        elif amount >= 32:
            slowprint("Stop.\n")
            time.sleep(2)
            slowprint("A person stands upended at the end of the hall with its back turned towards you.\n\
You can't make out its features but can notice its unusually long limbs and very inhuman sillouette.\n")
            time.sleep(1)
            slowprint("Do you want to try to get its attention by flickering your ~flashlight~?\n\
Or you can try approaching it for a closer ~look~.\n")
            at_person = True
person()

def inspect():
    gone = False
    while not gone:
        light_look = str(input("Input: ")).strip().lower()
        if "light" in light_look:
            slowprint("You flicker your flashlight at it.")
            time.sleep(1)
            slowprint("It doesn't react.")
            time.sleep(1)
            slowprint("~Approach~ it.")
        elif "look" in light_look or "approach" in light_look:
            slowprint("You slowly creep up to it but get distracted by quick, light footsteps rapidly approaching you from behind.")
            time.sleep(2)
            slowprint("You look back and the footsteps stop.")
            time.sleep(2)
            slowprint("You intently search for the source with your light, but can't find anything.")
            time.sleep(2)
            slowprint("You decide to shrug it off and look back at the creature.")
            time.sleep(3)
            slowprint("It's bleeding.")
            time.sleep(1)
            gone = True
        else:
            print("Please enter a valid response.\n")
inspect()

def creep():
    message = "I'm bleeding."
    amount = 0
    while amount < 4:
        slowprint(message)
        time.sleep(1)
        amount += 1
creep()

slowprint("I'm")

def clear():
            if name == 'nt':
                _ = system('cls')
clear()

slowprint("You don't know the truth.")
time.sleep(1)
slowprint("Follow. It.")

time.sleep(2)

def clear():
            if name == 'nt':
                _ = system('cls')
clear()

time.sleep(2)
slowprint("My apologies.\n")
time.sleep(1)
slowprint("You spot a third ~door~ to the right of where the person once stood.")
time.sleep(1)
slowprint("But you also have an opportunity to go ~downstairs~ through the lobby at the end of the hall.\n")

def manda():
    at_stairs = False
    while not at_stairs:
        third_stairs = str(input("Input: ")).strip().lower()
        if "door" in third_stairs:
            slowprint("The door doesn't budge.Isaidfollowit\nGo ~downstairs~?")
        elif "downstairs" in third_stairs:
            slowprint("You .followit. go downstairs and hear rustling as you descend.")
            time.sleep(1)
            slowprint("The lower you go, a deep rumbling grows.\n\
Circling and enveloping you.\n")
            time.sleep(2)
            slowprint("You can keep ~descending~.\n..\n")
            at_stairs = True
manda()

def follow():
    at_thing = False
    while not at_thing:
        follow_down = str(input("Input: ")).strip().lower()
        if "follow" in follow_down:
            import asset3
            at_thing = True
        elif "desending" in follow_down or "descend" in follow_down:
            slowprint("You descend.\nDescend into madness.\nDescend.\nDescend.\nDescend.\nDescend.\nDesc")
            import asset2
            at_thing = True
follow()

print("\033[0;31m\
░█████╗░██╗░░██╗░█████╗░██████╗░████████╗███████╗██████╗░  ░░██╗██╗██╗\n\
██╔══██╗██║░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  ░██╔╝██║╚═╝\n\
██║░░╚═╝███████║███████║██████╔╝░░░██║░░░█████╗░░██████╔╝  ██╔╝░██║░░░\n\
██║░░██╗██╔══██║██╔══██║██╔═══╝░░░░██║░░░██╔══╝░░██╔══██╗  ███████║░░░\n\
╚█████╔╝██║░░██║██║░░██║██║░░░░░░░░██║░░░███████╗██║░░██║  ╚════██║██╗\n\
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░░░░░╚═╝╚═╝\n\
\n\
███████╗██████╗░░█████╗░░█████╗░████████╗██╗░░░██╗██████╗░███████╗\n\
██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║░░░██║██╔══██╗██╔════╝\n\
█████╗░░██████╔╝███████║██║░░╚═╝░░░██║░░░██║░░░██║██████╔╝█████╗░░\n\
██╔══╝░░██╔══██╗██╔══██║██║░░██╗░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░\n\
██║░░░░░██║░░██║██║░░██║╚█████╔╝░░░██║░░░╚██████╔╝██║░░██║███████╗\n\
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝\n\
\n\
\033[1;30m\
\033[3m\
Written By\n\
Derrick Martinez\n\
\n")
print("\033[1;33m\
Select an option below:\n1: Continue Story\n2: Instructions\n")

def menu_select():
    valid = False
    while not valid:
        selection = str(input("Input: "))
        if selection == "1":
            valid = True
        elif selection == "2":
            print("You can't fix this.")
            time.sleep(1)
            slowprint("\033[1;34mSo let me help you.\033[1;33m\n")
        else:
            print("Please enter either '1' or '2' to continue.\n")
menu_select()

print("-------------------------")

input()

