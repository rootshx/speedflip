import time
import keyboard
import mouse
import os
import socket

if os.name == 'nt':
    os.system('')

RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'

def print_colored_text(text, color='', background='', style=''):
    formatted_text = f"{style}{color}{background}{text}{RESET}"
    print(formatted_text, end='', flush=True)
    
def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    logo = """
                    \033[38;5;196m (       )     )       (       )    )  \033[0m
                    \033[38;5;202m )\ ) ( /(  ( /(  *   ))\ ) ( /( ( /(  \033[0m
                    \033[38;5;202m(()/( )\()) )\()` )  /(()/( )\()))\()) \033[0m
                    \033[38;5;208m /(_)((_)\ ((_)\ ( )(_)/(_)((_)\((_)\  \033[0m
                    \033[38;5;208m(_))   ((_)  ((_(_(_()(_))  _((___((_) \033[0m
                    \033[38;5;214m| _ \ / _ \ / _ |_   _/ __|| || \ \/ / \033[0m
                    \033[38;5;214m|   /| (_) | (_) || | \__ \| __ |>  <  \033[0m
                    \033[38;5;220m|_|_\ \___/ \___/ |_| |___/|_||_/_/\_\ \033[0m

                                   \033[38;5;220mSPEEDFLIP\033[0m
                          \033[38;5;220mgithub.com/rootshx/speedflip\033[0m

"""
    Clear()
    print(logo)

if __name__ == "__main__":
    main()

RMB = "right" #jump key
right = "d"
left = "a"
airRollRight = "e"
airRollLeft = "q"

delay1 = 0.007
delay2 = 0.06
delay3 = 0.012
delay4 = 0.6
delay5 = 0.15
delay6 = 0.1


def DoSpeedFlip(mainKey, airRollKey):
    # Check if 'w' is already pressed
    lastW = keyboard.is_pressed('w')

    # Perform the jump
    mouse.press(RMB)
    time.sleep(delay2)
    mouse.release(RMB)
    time.sleep(delay3)

    # Only press 'w' if it wasn't already held down
    if not lastW:
        keyboard.press('w')
    
    # Press the direction key (main key)
    keyboard.press(mainKey)
    time.sleep(delay1)
    
    # Release and re-press the mouse button to perform the flip
    mouse.press(RMB)
    time.sleep(delay3)
    mouse.release(RMB)
    time.sleep(delay3)

    # Release the keys
    keyboard.release('w')
    keyboard.release(mainKey)
    time.sleep(delay3)
    
    # Perform the air roll and backward movement
    keyboard.press('s')
    keyboard.press(airRollKey)
    time.sleep(delay4)
    
    # Perform the final action of pressing the main key again
    keyboard.press(mainKey)
    time.sleep(delay5)
    
    # Release all keys
    keyboard.release(mainKey)
    keyboard.release('s')
    time.sleep(delay6)
    keyboard.release(airRollKey)

    # If 'w' was originally pressed, re-press it to maintain its state
    if lastW:
        keyboard.press('w')

def ManageSpeedFlip(x):
    if keyboard.is_pressed('d'):
        DoSpeedFlip(right, airRollRight)
        time.sleep(0.3)  # Short cooldown
    elif keyboard.is_pressed('a'):
        DoSpeedFlip(left, airRollLeft)
        time.sleep(0.3)  # Short cooldown

# Main loop to detect the mouse button press
while True:
    if mouse.is_pressed("x2"):  # Detect ThumbMouse2
        ManageSpeedFlip('x')
    time.sleep(0.005)  # Minimal loop sleep