# Imports
import tkinter as tk
import random

class mainWindow:
    window = tk.Tk()
    program_name="D&D Diceroller!"

    main_label_ending = " Die!"
    number_of_dice = "One"
    dice_sides = 20
    width = 1000
    height = 600
    default_roll = 20

    background_color = "#026670"
    text_color = "#edeae5"
    highlighted_color = "#9fedd7"

    number_to_words = { 0: "Zero",
                        1: "One",
                        2: "Two",
                        3: "Three",
                        4: "Four",
                        5: "Five",
                        6: "Six",
                        8: "Eight",
                        10: "Ten",
                        12: "Twelve",
                        20: "Twenty",
                        100: "One Hundred"}

    window.resizable(width=False, height=False)
    window.minsize(width=width, height=height)
    window.configure(background=background_color)
    window.iconbitmap('favicon.ico')
    window.title(program_name)

    main_label = tk.Label(window)
    main_label.configure(background=background_color, font=("Garamond Bold", 30), height=2, fg=text_color)

    dice_label = tk.Label(window, text=default_roll)
    dice_label.configure()

    # Create Layout
    main_label.grid(column=0, row=0)
    window.columnconfigure(0, weight=1)

    def updateMainLabel(self):

        if self.number_of_dice == 1:
            self.main_label_ending = " Dice!"
        else:
            self.main_label_ending = " Die!"

        self.main_label_full = "Rolling " + self.number_of_dice + " " + str(self.dice_sides) + " Sided" + str(self.main_label_ending)
        self.main_label.configure(text=self.main_label_full)

# Class Declarations
class Dice:
    def __init__(self, value, sides):
        self.value = value
        self.sides = sides

# Method Declarations
def convertToWord(amount):
    return number_to_words[amount];

def generateDice(amount, type):
    print("hi")

# Beginning Program
def main():
    diceWindow = mainWindow()
    diceWindow.updateMainLabel()
    diceWindow.window.mainloop()

if __name__ == '__main__':
    main()
