# Imports
import tkinter as tk

# Variable Declarations and Initialisations
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

# Settings
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

# Method Declarations
def convertToWord(amount):
    return number_to_words[amount];

def updateMainLabel():
    global main_label_ending
    global main_label_full
    global main_label

    if number_of_dice == number_to_words[1]:
        main_label_ending = " Dice!"
    elif number_of_dice != number_to_words[1]:
        main_label_ending = " Die!"

    main_label_full = "Rolling " + number_of_dice + " " + str(dice_sides) + " Sided" + str(main_label_ending)
    main_label.configure(text=main_label_full)

# Beginning Program
def main():
    global window
    updateMainLabel()
    window.mainloop()

if __name__ == '__main__':
    main()
