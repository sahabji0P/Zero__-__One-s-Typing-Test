import os
from time import *
from Display import *
from Wordbank import *
from Timed_Input import *
from colorama import Fore, Back, Style, init

# Function defined to find the errors user entered/not entered while typing counted from the given statement
def Mistakes_Word(a, b):
    errors = 0
    for i in range(len(a)):
        try:
            if a[i] != b[i]:
                errors += 1
        except:
            errors += 1
    return (errors/len(a))*100

# Finding the errors user entered, counted while typing in the given time
def Mistakes_Time(a, b):
    errors = 0
    for i in range(len(b)):
        try:
            if a[i] != b[i]:
                errors += 1
        except:
            errors += 1
    z1 = 100 - (errors/len(b))*100
    print("Accuracy: " + str(z1) + " %")
    print("Correct words: "+str(len(b)-errors))
    print("Wrong words: "+ str(errors))

# Counting wpm
def wpm(c, d, e):
    tt = d - c
    tr = round(tt, 2)
    sp = (e*60)/tr
    return round(sp)


def Speed_word():
    y2 = words("a",1)
    y2.preinput()
    y1 = input(Fore.WHITE + "\nEnter difficulty level: ")
    y2 = words(y1,1)
    y2.postinput()
    user_input = int(input(Fore.WHITE + "\nEnter No. of words you want to test your skills on: "))
    os.system("cls||clear")
    y2 = words(y1,user_input)
    t = y2.postsel()
    t3 = t.split()
    print(f"\nYour sentence to write is: \n\n{Fore.YELLOW}{t}\n{Fore.WHITE}")
    countdown()
    print("Your Sentence: \n")
    t1 = time()
    y = input(f"\n{Fore.GREEN}").split()
    t2 = time()
    z1 = Mistakes_Word(t3, y)
    z2 = wpm(t1,t2,len(y))
    print(f"\n{Fore.WHITE}Speed: " + str(z2) + " WPM")
    print("Accuracy: " + str(100-z1) + " %")
    f = input("Do you want to continue(Y/N): ")
    f1 = continue_loop(f)
    f1.condition_check()

# This function is to set countdown timer and show the words to enter
def Speed_time():
    a2 = times(1,1)
    a2.preinput()
    a1 = int(input(f"\n{Fore.WHITE}Enter your choice: "))
    a2 = times(a1,1)
    t = a2.postinput()
    a2 = times(a1,t)
    a2.post()
    t1 = sel3()
    t2 = t1.split()
    print(f"\n{Fore.WHITE}Your sentence to write is: \n\n{Fore.YELLOW}{t1}\n{Fore.WHITE}")
    countdown()
    t4 = time()
    y1 = cd1(t)
    y = y1.cd()
    t5 = time()
    z2 = wpm(t4,t5,len(y))
    print(f"\n{Fore.WHITE}Speed: " + str(z2) + " WPM")
    z1 = Mistakes_Time(t2, y)
    f = input("Do you want to continue(Y/N): ")
    f1 = continue_loop(f)
    f1.condition_check()
    

dis()
sleep(0.25)

# This will let the user to choose the mode of setting timer or no. of words
while True:
    print(Fore.CYAN + Style.BRIGHT)
    main_menu()
    f1 = input(Fore.WHITE + "Enter your choice(1-2): ")
    os.system("cls" if os.name == "nt" else "clear")
    if f1 == "2":
        Speed_word()
    elif f1 == "1":
        Speed_time()
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{Fore.RED}Wrong Input")
        sleep(1)
        print(f"{Fore.WHITE}Try Again")
        sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
