# Imports
# ====================================================
from tkinter import Tk, Frame, Label
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
class MainFrameLeft(Frame):
    def __init__(self):
        print("Main Frame Left Test")
        self.label = Label(text="Hello There", bg="#fff")

class MainFrameRight(Frame):
    def __init__(self):
        print("Main Frame Right Test")

class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.grid_columnconfigure(2, weight = 1)
        framesLeft = MainFrameLeft()
        framesRight = MainFrameRight()

class AppWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("D&D Diceroller!")
        self.master.geometry("900x600")
        self.master.configure(bg="#000")
        mainWindow = MainWindow(self.master);

# Main
# ====================================================
def main():
    window = Tk()
    app = AppWindow(window)
    window.mainloop()

if __name__ == '__main__':
    main()
