from time import *
from Wordbank import *
import os
from art import *

class words():
    def __init__(self,y1,user_input):
        self.y1 = y1
        self.ui = user_input
    
    def preinput(self):
        print(f"""Choose your Mode:

{Fore.GREEN}1. Easy - Simple words but input is Case-Sensitive
{Fore.YELLOW}2. Medium - Words with symbols and numbers, to test your speed on whole keyboard
{Fore.LIGHTRED_EX}3. Hell - Try it if you want, although i don't think you will finish it""")

    def postinput(self):
        if self.y1.upper() == "E" or self.y1 == "1":
            print(Fore.GREEN + "Easy, I see, All The Best!")
            sleep(1)
            os.system("cls||clear")
            menu()
        elif self.y1.upper() == "M" or self.y1 == "2":
            print(Fore.YELLOW + "Pushing Limits i see, All the Best!")
            sleep(1)
            os.system("cls||clear")
            menu2()
        elif self.y1.upper() == "H" or self.y1 == "3":
            print(Fore.RED + "Well, Bravo for choosing this even after my warning.")
            sleep(1)
            print(Fore.LIGHTRED_EX + "Welcome to Hell!!")
            sleep(2)
            os.system("cls||clear")
            menu3()
        else:
            os.system("cls||clear")
            init()
            print(Fore.LIGHTRED_EX)
            tprint("Wrong Input")
            sleep(1)
            init()
            print(Fore.YELLOW)
            tprint("                See Yaa!")
            sleep(1)
            quit()

    
    def postsel(self):
        if self.y1.upper() == "E" or self.y1 == "1":
            return sel(self.ui)
        elif self.y1.upper() == "M" or self.y1 == "2":
            return sel1(self.ui)
        elif self.y1.upper() == "H" or self.y1 == "3":
            return sel2(self.ui)


class times():
    def __init__(self,a1,t):
        self.a1 = a1
        self.t = t

    def preinput(self):
        print(f"""Choose your Mode

{Fore.GREEN}1. 30 seconds
{Fore.YELLOW}2. 60 seconds
{Fore.LIGHTRED_EX}3. 120 seconds""")

    def postinput(self):
        if self.a1 == 1 or self.a1 == 30:
            return 30
        elif self.a1 == 2 or self.a1 == 60:
            return 60
        elif self.a1 == 3 or self.a1 == 120:
            return 120
        else:
            return self.a1

    def post(self):
        print(f"{Fore.YELLOW}{self.t} seconds it is, All The Best!")
        sleep(1)
        os.system("cls||clear")


class continue_loop():
    def __init__(self,f):
        self.f = f
    
    def condition_check(self):
        if self.f.upper() == "N":
            os.system("cls" if os.name == "nt" else "clear")
            tprint("\nSee Ya!\n")
            sleep(3)
            quit()
        elif self.f.upper() == "Y":
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("I take that as a YES")
            sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
    


def dis():
    print(Fore.CYAN+Style.BRIGHT)
    l = "Zero_&_One's Typing Test"
    l1 = ""
    for i in range(len(l)):
        os.system("cls" if os.name == "nt" else "clear")
        l1 += l[i]
        tprint(l1)
        sleep(0.025)
    for i in range(5):
        os.system("cls" if os.name == "nt" else "clear")
        tprint(l1)
        sleep(0.025)
    os.system("cls" if os.name == "nt" else "clear")


def main_menu():
    tprint("Zero_&_One's Typing Test")
    print(Fore.WHITE + Style.NORMAL)
    print(f"""\nHow do you want to Test:
{Fore.LIGHTGREEN_EX}1. By Time
{Fore.LIGHTYELLOW_EX}2. By Words""")


def countdown():
    l = ["5", "4", "3", "2", "Start Typing!"]
    l1 = ""
    print("Test will start in 5 seconds.\n")
    sleep(1)
    for i in range(len(l)):
        l1 = l[i]
        print(l1)
        sleep(1)
        print("\033[A                              \033[A")
    print("\033[A                              \033[A")
    print("\033[A                              \033[A")
