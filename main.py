from keyboard import read_key
from os import system
from random import randrange
from time import sleep


# Allows to get a menu with an arrow at the specified position
def place_arrow(p_menu, p_pos):
    new_menu = list(p_menu)
    new_menu[p_pos] = "➤" + new_menu[p_pos][1:]
    return new_menu


# Allows to place some text anywhere
def place_text(x, y, texts, decoration_texts=()):
    # Allows to add some blank line to move the text down
    for i in range(y):
        print()

    for deco_txt in decoration_texts:
        print(" " * x + deco_txt)

    for txt in texts:
        print(" " * x + txt)


play_loop = True
while play_loop:
    # Ask the player to 1 player mode or 2 players mode
    print("Hi ! Do you want to play alone or with a friend ?")

    # Menu
    selected_mode = 0
    menu = ("  1 PLAYER", "  2 PLAYERS")
    decoration = ("* SELECT MODE *",)

    # Mode selection
    while True:
        system("clear")
        printed_menu = place_arrow(menu, selected_mode)
        place_text(40, 10, printed_menu, decoration)

        key = read_key()
        if (key == "up" or key == "8") and selected_mode - 1 >= 0:
            selected_mode -= 1

        elif (key == "down" or key == "2") and selected_mode + 1 < len(printed_menu):
            selected_mode += 1

        elif key == "enter":
            break

        sleep(0.001)

    input()  # Bug-Fix ¯\_(ツ)_/¯

    # Generation of number
    number_to_guess = -1
    if selected_mode == 0:
        max = -1
        while max <= 0:
            max = int(input("From 0 to which number do you want to generate the number to guess ? "))
            number_to_guess = randrange(-1, max) + 1

            if max <= 0:
                print("The number given is not greater than 0 !")

    else:
        number_to_guess = int(input("[Player 1] Please enter the number to guess for the player 2 "))

    # Guess starting
    guess = -1
    try_number = 0
    system("clear")
    while guess != number_to_guess:
        guess = int(input("What is the number ? "))
        if guess < number_to_guess:
            print("It is plus !")

        elif guess > number_to_guess:
            print("It is minus !")
        try_number += 1

    print("Congratulation ! You guess the number in", try_number, "try !")
    play_loop = input("Do you want to play again ? (y/n) ") == 'y'
    sleep(0.5)
