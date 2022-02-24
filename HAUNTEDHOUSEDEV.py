print("\
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
Select an option below:\n1: Begin Story\n2: Instructions\n")

import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1/64)

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
            slowprint("You look around the room and see a moist, torn up piece of ~paper~ on the floor.\nYou also spot a ~safe~ cowering in the corner of the room.\n")
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
            answer = str(input("Input: ")).strip()
            if answer == "62189537":
                slowprint("You have unlocked the safe.\nInside you find a key.\nThis may be useful for opening a ~door~.\n")
                at_key = True
            else:
                slowprint("The ~safe~ beeps in denial.\nTry again.\n")
        elif "paper" in safe_code:
            slowprint("You take a look at the paper and see symbol decryptions.\nΔ = 3\nΣ = 1\nΠ = 9\nΨ = 6\nΦ = 5\nΘ = 7\nΩ = 2\nΞ = 8\nReturn to the ~safe~ once memorized.\n")
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
                slowprint("You have escaped the room.\n")
                at_exit = True
        else:
            print("Please enter a valid response.\n")
escape()

time.sleep(1)
slowprint("Would you like to continue to 'Chapter 2: Abduction'? (yes/no or y/n)\n\
WARNING, PROGRESS WILL NOT BE SAVED IF YOU EXIT.\n")
def cont():
    at_ch2 = False
    while not at_ch2:
        pick = str(input("Input: ")).strip().lower()
        if "yes" in pick or "y" in pick:
            at_ch2 = True
        elif "no" in pick or "n" in pick:
            print("\nThanks for playing!")
            input("Press ENTER to exit.\n")
            exit()
        else:
            print("Please enter either 'yes/y' or 'no/n'.\n")
cont()

print("-------------------------")

#start ch2 ----------------------------------------------------------------------------------------------------------

print("\
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
Select an option below:\n1: Continue Story\n2: Instructions\n")

import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1/64)

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
Peeping into the suprisingly lit and organized room, you see a ~toolbox~ awkwardly standing at the center.\n")
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

#asset0
time.sleep(5/2)

def jumpscare():
    message = "BEHIND YOU"
    amount = 0
    while amount < 24:
        print(message)
        amount += 1
        time.sleep(1/32)
jumpscare()

from os import system, name
import time
from time import sleep

face = "\
┤├┤├┤├┤├░├░├┤├┤├├├▒████▓√├┤├├├┤├░├┤├┤├┤├\n\
┤├┤├┤├┤├├├├├├├███▓▒├├├┤╫▓███▒├┤├┤├┤├┤├├├\n\
░├├├┤├┤├┤├┤▓██┤├√┤░░░░╫░░░┤├▓██├┤├┤├├├┤├\n\
┤├├├┤├├├√▒█▓├├░░╫░░░╫░░░╫╫╫╫╫├╫██├┤├√├√├\n\
┤├┤├├├√├██┤├░░╫░░░░░░░░░╫╫╫╫╫╫╫├▓█╫├√├√├\n\
┤├┤├├├√█▓├╫╫╫░╫░░░░░░░░░╫░╫╫╫╫▒╫╫░█▓┤├┤├\n\
░├√├√├█▒√╫╫╫╫░░░░┤░┤░░░░╫░╫╫╫╫╫╫▒╫░█▓├┤├\n\
┤├√├┤█▒├╫╫╫░╫░░░░├┤├░░░░░░╫░╫╫╫╫▒▒╫░█▓├├\n\
░├┤├█▓├╫╫╫░├┤├┤├┤├√├┤┤░░░├├╫▒╫├░▒▒▒╫╫█░├\n\
┤├┤▒█├╫╫╫├▒█████├├┤├░┤░├┤██▓╫▓██┤╫▒╫░▓█├\n\
┤├√█▓░╫╫┤██├├├┤├█▒┤├░░├├█▓├├┤├┤▓█┤╫╫▒░█├\n\
┤├▒█░╫╫├▓█┤├▓██├√█┤├░░├▓█├╫▓▓█▒├█▓╫╫▒░▓▓\n\
├├██░╫╫├█▒├▓▓██▓√█▒├░░┤█▓├▓▓███├▓█░╫▒╫▒█\n\
├├█▓╫▒╫├█▒├████▒┤█▒├░░├▓█├▓███▓├█▓░╫▒╫░█\n\
├├█▒╫▒▒░▓█┤├██▓├╫█√░╫╫░├█▒┤├▒├├▒█░╫▒▒╫░█\n\
├├█▒╫▒▒╫├██├├├┤▒█░√╫╫╫╫░┤██├├├██░╫▒▒▒╫░▓\n\
┤├█▒╫╫╫╫█▓┤████▓┤░╫╫╫╫╫╫╫├░▓█▓╫░▒▒▒▒▒╫░█\n\
┤├█▒├├▒█√▓██▓█┤░╫╫╫╫▒╫▒╫▒╫▒╫▒╫▒▒▒▒▒▒▒╫░█\n\
┤├█▒███▒√╫█├├▓█√╫╫▒╫▒╫▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╫░█\n\
├├▒█▓├█▓┤├█░√▓█┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒█\n\
┤▓██▒├▓█┤├█▒┤▓█░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╫╫▒▒▒▒┤█▓\n\
█▓┤█▓├▓█√├█▓┤▓█┤▒▒▒▒▒▒▒▒▒▒▒▒▒╫░▓█░╫▒╫╫█├\n\
█▒┤▓█├▒█┤├█▓┤▒█├░▒▒░╫╫▒▒▒▒▒╫╫├██░╫▒╫░█▓├\n\
█▒┤▓█├╫█├├██┤╫███▒▓█▓┤╫╫╫┤√▒██▒┤╫╫▒░▓█┤├\n\
█▓├▓█├┤├┤├┤├├▒█├┤├┤▒█▓█████▓░░▒▒▒▒░▒█├┤├\n\
▓█├├┤├┤├┤├√├├├┤├├▒██▒√░├┤░╫╫▒▒▒▒▒░▒█┤├┤├\n\
░█┤├┤├├├├├√├┤├├├█▓√░▒╫▒▒▒▒▒▒▒▒▒╫┤▓█├├├├├\n\
┤█▒├┤├√├├├├├├├├█▒░▒▒▒▒▒▒▒▒▒▒▒╫░░██┤├┤├┤├\n\
√▒█├├├┤├┤├├├┤├╫█░╫▒▒▒▒▒▒▒▒▒╫░░██┤├├├├├┤├\n\
├├█▒┤├√├┤├┤├┤├▒█┤├╫╫╫╫╫╫░├░▓██├├┤├┤├┤├┤├\n\
├├░█├├┤├├├┤├├├▓████████████├├├√├┤├√├┤├├├\n\
░├┤├├████████▒├├┤├┤├├├┤├┤├├├├├┤├┤├┤├┤├┤├\n"


def jumpscare():
    for i in range(16):
        def clear():
            if name == 'nt':
                _ = system('cls')
        print(face)
        i += 1
        clear()
        sleep(1/32)
jumpscare()

time.sleep(2)

import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1/64)

#asset1
slowprint("Hm.")
time.sleep(2)
slowprint("You saw something you weren't supposed to see.")
time.sleep(2)
slowprint("Continue to 'Chapter 3: Spitting Image'? (yes/no or y/n)\n\
WARNING, PROGRESS WILL NOT BE SAVED IF YOU EXIT.\n")

def cont():
    at_ch2 = False
    while not at_ch2:
        pick = str(input("Input: ")).strip().lower()
        if "yes" in pick or "y" in pick:
            at_ch2 = True
        elif "no" in pick or "n" in pick:
            slowprint("\nYou will return.")
            input("Press ENTER to exit.\n")
            exit()
        else:
            print("Please enter either 'yes/y' or 'no/n'.\n")
cont()

print("-------------------------")

#start ch3 ----------------------------------------------------------------------------------------------------------
print("\
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
Select an option below:\n1: Continue Story\n2: Instructions\n")

import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1/64)

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
            slowprint("You will not leave.\n")
        else:
            print("Please enter either '1' or '2' to continue.\n")
menu_select()

print("-------------------------")

input()