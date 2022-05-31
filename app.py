import keyboard
import pyautogui
import time
import os


def menu():

    os.system('cls' if os.name == 'nt' else 'clear')
    print('OPTION 1 to |RECORD|')
    print('OPTION 2 to | START|')
    print('OPTION 3 to | CLEAN|')
    print('OPTION 4 to |  QUIT|')

    option = int(input('OPTION|  : '))
    if option == 1:
        get_coordonates()
    elif option == 2:
        start_action()
    elif option == 3:
        clean_list()

    elif option == 4:
        print('...EXITING...')
        quit()

    else:
        return menu()


def get_coordonates():
    try:

        while True:

            if keyboard.is_pressed('g'):
                with open('coords.txt', 'r+') as f:
                    1
                    content = f.read()
                    x, y = pyautogui.position()
                    f.write(str(x) + ' ' + str(y) + '\n')
                    print(
                        f'x={x},y={y} -Recorded, press g to continue or q to quit')
                    f.close()
                    time.sleep(0.6)
            if keyboard.is_pressed('q'):
                os.system('cls' if os.name == 'nt' else 'clear')
                return menu()
    except:
        return menu()


def start_action():
    try:
        replay = int(input('HOW MANY TIMES TO REPEAT THE ACTION? : '))
        for i in range(replay):

            print('...STARTING PROCESS...')
            print('IF YOU WANT TO QUIT PRESS S')
            with open('coords.txt', 'r+') as f:
                content = f.read()
                coords = content.split('\n')
                for coord in coords:
                    if coord == '':
                        continue
                    x, y = coord.split(' ')
                    pyautogui.click(int(x), int(y))
                    if keyboard.is_pressed('s'):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return menu()
                    time.sleep(0.5)
                f.write('')
                f.close()
                os.system('cls' if os.name == 'nt' else 'clear')
        print('...PROCESS FINISHED...')
        return menu()
    except:
        return menu()


def clean_list():
    with open('coords.txt', 'w') as f:
        f.write('')
        f.close()
        os.system('cls' if os.name == 'nt' else 'clear')
        print('...LIST CLEANED...')
    return menu()


menu()
