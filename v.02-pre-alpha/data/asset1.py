from os import system, name
import time
import sys
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1/64)

slowprint("\033[3m\
\033[1;33m\
Hm.")
time.sleep(2)
slowprint("You saw something you weren't supposed to see.\n")
time.sleep(2)
slowprint("Continue to 'Chapter 3: Spitting Image'? [y/n]\n\
WARNING: EXITING THE GAME NOW WILL DELETE ALL SAVED DATA\n")

def cont():
    at_ch2 = False
    while not at_ch2:
        pick = str(input("Input: ")).strip().lower()
        if "y" in pick:
            at_ch2 = True
        elif "n" in pick:
            slowprint("\nYou will return.")
            input("Press ENTER to exit.\n")
            exit()
        else:
            print("Please enter either 'yes/y' or 'no/n'.\n")
cont()

print("-------------------------")

import linecache
  

particular_line = linecache.getline('hauntedhousedev.py', 296)

print(particular_line)