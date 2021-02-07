# Imports
from tkinter import *
import fontTools.ttLib
import random

# Helper Methods
# ====================================================
def convertToWord(amount):
    return number_to_words[amount];

def generateDice(amount, type):
    print("hi")

# Model Declarations
# ====================================================
class Dice:
    def __init__(self, value, sides):
        self.value = value
        self.sides = sides

# Frames and Classes
# ====================================================
class MainFrameLeft():
    def __init__(self):
        print("Hi")

class MainFrameRight():
    def __init__(self):
        print("Hi")

class MainWindow():
    def __init__(self, master):
        self.master = master
        master.title = "D&D Diceroller!"

# Main
# ====================================================
class AppWindow:
    def __init__(self, parent):
        self.parent = parent
        self.mainFrames()

    def mainFrames(self):
        diceWindow = MainWindow()

if __name__ == '__main__':
    window = Tk()
    app = AppWindow(window)
    window.mainloop()
