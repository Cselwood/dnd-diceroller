# Imports
# ====================================================
from tkinter import Tk, Frame
import fontTools.ttLib
import random

# Helper Methods
# ====================================================
def convertToWord(amount):
    return number_to_words[amount];

def generateDice(amount, type):
    print("Generate Dice Test")

# Model Declarations
# ====================================================
class Dice:
    def __init__(self, value, sides):
        self.value = value
        self.sides = sides

# Main Frames and Classes
# ====================================================
class MainFrameLeft():
    def __init__(self):
        print("Main Frame Left Test")

class MainFrameRight():
    def __init__(self):
        print("Main Frame Right Test")

class MainWindow():
    def __init__(self):
        self.mainWidgets()

    def mainWidgets(self):
        print("Building Widgets Test")

# Left Widgets and Frames
# ====================================================

# Right Widgets and Frames
# ====================================================

# Main
# ====================================================
class AppWindow(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.mainFrames()

    def mainFrames(self):
        self.winfo_toplevel().title("D&D Diceroller!")
        self.winfo_toplevel().geometry("900x600")

if __name__ == '__main__':
    window = Tk()
    app = AppWindow(window)
    window.mainloop()
