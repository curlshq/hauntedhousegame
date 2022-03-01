from os import system, name
import time
import sys
#followit_EE.py used to be the file name

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
slowprint("\033[3m\
\033[1;33m\
You follow it.")

time.sleep(2)
def creep():
    message = "\033[1;31m\
YOU NEED TO GET OUT"
    amount = 0
    while amount < 50:
        print(message)
        time.sleep(1/64)
        amount += 1
creep()

def clear():
            if name == 'nt':
                _ = system('cls')
clear()

time.sleep(2)
print("\033[1;34m\
                   (@@@@@@\n\
                  &@@@@@@@@/\n\
                 ,&@@@@@@@@#\n\
                 ,@@@@@@@@@@\n\
                   #@@@@@@\n\
                   #@@@@@@\n\
                .@@@@@@@@@@(\n\
         @@@@@@@@@@@@@@@@@@@@@@@@%\n\
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@(\n\
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\
     /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\
     /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\
     (@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@\n\
     @@@@@%@@@@@@@@@@@@@@@@@@@@*@@@@@\n\
    #@@@@@,@@@@@@@@@@@@@@@@@@@@/@@@@@\n\
    @@@@@@(@@@@@@@@@@@@@@@@@@@@#@@@@@\n\
    @@@@@ @@@@@@@@@@@@@@@@@@@@@#@@@@@.\n\
    @@@@ .@@@@@@@@@@@@@@@@@@@@@@@@@@@.\n\
   (@#%. &@@@@@@@@@@@@@@@@@@@@@&(@@@,\n\
    .@@   ,@@@@@@@@@@@@@@@@@@@@(  &@@\n\
          (@@@@@@@@@@@@@@@@@@@@ %@@@\n\
          ,@@@@@@@@@@@@@@@@@@@@\n\
           @@@@@@@@@#/@@@@@@@@@\n\
           @@@@@@@@@  &@@@@@@@#\n\
          #@@@@@@@@,  .@@@@@@@/\n\
          @@@@@@@@@    @@@@@@@,\n\
         *@@@@@@@@/    ,@@@@@@.\n\
         @@@@@@@@@      @@@@@@.\n\
        .@@@@@@@@*      %@@@@@\n\
        #@@@@@@@@       (@@@@@\n\
        @@@@@@@@.       /@@@@@.\n\
       *@@@@@@@/        #@@@@@,\n\
       @@@@@@@&         /@@@@@/\n\
       @@@@@@@          @@@@@@\n\
       @@@@@@          .@@@@@@*\n\
      @@@@@#             *@@@@@(\n\
     @@@@@@               &@@@@@(\n\
     @@@@                   %@@@@\n")

time.sleep(1)
slowprint("Hello player.")
time.sleep(2)
slowprint("My name is")

def clear():
            if name == 'nt':
                _ = system('cls')
clear()

time.sleep(2)
slowprint("\033[1;33m\
Stay away from him.")
time.sleep(1)
slowprint("followit")
time.sleep(2)
slowprint("I SAID FOLLOW IT!\n")

def follow():
    following = False
    while not following:
        follow_not = str(input("Input: ")).strip().lower()
        if "no" in follow_not:
            slowprint("What have you done.")
            time.sleep(2)
            import asset2
            following = True
        elif "follow" in follow_not:
            slowprint("Good.")
            time.sleep(1)
            slowprint("Don't pay him attention.")
            time.sleep(1)
            import asset2
            following = True
        else:
            print("GODDAMNIT SENTIENT, I SAID FOLLOW!\n")
follow()