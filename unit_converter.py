#/usr/bin/python

# author: cryptoB3nD3R

import os
import colored
from colored import fg

color = fg('blue')

def ask_and_display_conver(unitl: str, unit2: str, factor: float):
    value_str = input(color + f'''Conversion {unitl} -> {unit2}.
Give value by {unitl} (Press '00' to exit or 'b' to return to conversion choice): ''')

    if value_str == "00":
        return quit()
    elif value_str == "b":
        os.system('cls')
        return menu()

    try:
        value_float = float(value_str)
    except ValueError:
        print("ERROR: You must enter a numeric value")
        print("use the point and not the comma for the decimals")
        return ask_and_display_conver(unitl, unit2, factor)

    convert_value = round(value_float * factor, 2)
    print(f"Conversion result: {value_float} {unitl} = {convert_value} {unit2}")
    return False

def menu():
    while True:
        #Menu choice of convertion
        print(color + '''
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
          █                          __    __   __  _   _   _______                                 █
          █                         |  |  |  | |  \/ | |_| |__   __|                                █
          █                         |  |  |  | |     |  _     | |                                   █
          █                         |  |__|  | | |\  | | |    | |                                   █
          █                         |________| |_| \_| |_|    |_|                                   █
          █   _______   ______   __  _  __         __  _____   ______    _______   _____   ______   █
          █  | ______| |  __  | |  \/ | \ \       / / |  ___| |   _  \  |       | |  ___| |   _  \  █
          █  | |       | |  | | |     |  \ \     / /  | |__   |  |_|  | |__   __| | |___  |  |_|  | █
          █  | |       | |  | | |     |   \ \   / /   |  __|  |     _/     | |    |  ___| |     _/  █
          █  | |_____  | |__| | | |\  |    \ \_/ /    | |___  |  |\  \     | |    | |___  |  |\  \  █
          █  |_______| |______| |_| \_|     \___/     |_____| |__| \__\    |_|    |_____| |__| \__| █
          █                                                                                         █
          █ By cryptoBender                                                                         █
          █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
            ''')
        print(color + "This program allows you to perform unit conversions")
        print(color + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print(color + "█ 1 - Inch to cm    █")
        print(color + "█ 2 - cm to Inch    █ ")
        print(color + "█ 3 - Feet to Meter █ ")
        print(color + "█ 4 - Meter to Feet █")
        print(color + "█ 5 - Inch to Feet  █")
        print(color + "█ 6 - Feet to Inch  █")
        print(color + "█ 00 - Quit         █")
        print(color + "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")
        choice = input("Your choice between (1 and 6) or (00) to Exit: ")
        if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "00":
            break
        print("ERROR: you must choose between 1 and 6")

    while True:
        # ask value to convert
        if choice == "1":
            if ask_and_display_conver("inch", "cm", 2.54):
                break
        if choice == "2":
            if ask_and_display_conver("cm", "inch", 0.394):
                break
        if choice == "3":
            if ask_and_display_conver("feet", "m", 0.3048):
                break
        if choice == "4":
            if ask_and_display_conver("m", "feet", 3.280):
                break
        if choice == "5":
            if ask_and_display_conver("inch", "feet", 0.0833333):
                break
        if choice == "6":
            if ask_and_display_conver("feet", "inch", 12):
                break
        if choice == "00":
            return quit()

menu()
os.system('color 4')
