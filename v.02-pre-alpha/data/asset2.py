from os import system, name
import time
import sys
#descend_alt.py used to be the file name
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1/64)

def clear():
            if name == 'nt':
                _ = system('cls')
clear()

time.sleep(1)
slowprint("\033[3m\033[1;33mDo forget.\n")
time.sleep(1)
slowprint("Continue to 'Chapter 4: Fracture'?\n\
WARNING: EXITING THE GAME NOW WILL DELETE ALL SAVED DATA")

def cont():
    at_ch4 = False
    while not at_ch4:
        pick = str(input("Input: ")).strip().lower()
        if "y" in pick:
            at_ch4 = True
        elif "n" in pick:
            slowprint("You let him escape. Now you must face the real consequences.\n")
            input("Press ENTER to exit.\n")
            exit()
        else:
            print("Please enter either 'yes/y' or 'no/n'.\n")
cont()

print("-------------------------")

import linecache

particular_line = linecache.getline('hauntedhousedev.py', 479)

print(particular_line)