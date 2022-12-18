from time import *
import threading
from pynput.keyboard import Key, Controller
from Display import *

# This class will take the input from the user and end the input after a period of time selected
class cd1:
    def __init__(self,t):
        self.t = t
    
    def cd(self):
        keyboard = Controller()
        def cd2():
            for i in range(self.t):
                self.t -= 1
                sleep(1)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            print(f"\n{Fore.RED}Out of time{Fore.WHITE}")
            sleep(2)
        cd_thread = threading.Thread(target= cd2)
        cd_thread.start()
        while self.t>0:
            x = input(f"Your Sentence: \n{Fore.GREEN}")
            break
        return x.split()

