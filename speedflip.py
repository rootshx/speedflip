import time
import keyboard
import mouse
 
multiplier = 0.85  # increasing or decreasing this value will adjust the timing
RMB = "right"  # jump key
right = "d"
left = "a"
airRollRight = "e"
airRollLeft = "q"
 
randomizerChange = 0.06  # how much the "randomizer" will change the delays
randomizer = True  # starts on
randomizerPlus = 0
 
def PrintBanner(endTime=0.0):
    print(
        f"""\n\n\n\n\n
 ██████╗ █████╗  █████╗ ██████╗ ███████╗  ██╗██╗ █████╗  █████╗ 
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔╝██║██╔══██╗██╔══██╗
╚█████╗ ███████║███████║██║  ██║██████╗ ██╔╝ ██║╚██████║╚██████║
 ╚═══██╗██╔══██║██╔══██║██║  ██║╚════██╗███████║ ╚═══██║ ╚═══██║
██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝╚════██║ █████╔╝ █████╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝      ╚═╝ ╚════╝  ╚════╝
feat. rootshx
----------------------------------------------------------------
(">": Increase, "<": Decrease)  Delays multiplier:     {multiplier}
(Speed flip time)               Speed flip time:       {str(endTime)[0:5]}
(Less sus toggle: "/")          "Randomizer":          {randomizer}
    """)
 
def UpdateDelays(print=True):
    global delay1, delay2, delay3, delay4, delay5, delay6
    delay1 = round(0.007 * multiplier, 4)
    delay2 = round(0.06 * multiplier, 4)
    delay3 = round(0.012 * multiplier, 4)
    delay4 = round(0.6 * multiplier, 4)
    delay5 = round(0.15 * multiplier, 4)
    delay6 = round(0.1 * multiplier, 4)
    if print:
        PrintBanner()
 
UpdateDelays()
 
def Increase(x):
    global multiplier
    if x == 'False':
        multiplier = round(multiplier + randomizerChange, 4)
        UpdateDelays(print=False)
    else:
        if randomizer: ToggleRandomizer('x')
        multiplier = round(multiplier + 0.025, 4)
        UpdateDelays()
 
def Decrease(x):
    global multiplier
    if x == 'False':
        multiplier = round(multiplier - randomizerChange, 4)
        if (multiplier < 0): multiplier = 0
        UpdateDelays(print=False)
    else:
        if randomizer: ToggleRandomizer('x')
        multiplier = round(multiplier - 0.025, 4)
        if (multiplier < 0): multiplier = 0
        UpdateDelays()
 
i = 1
 
def UpdateI():
    global i, randomizerPlus
    if randomizer:
        if i == 1:
            Increase('False')
            i = 2
            randomizerPlus = randomizerChange
        elif i == 2:
            Decrease('False')
            i = 3
            randomizerPlus = 0
        elif i == 3:
            Decrease('False')
            i = 4
            randomizerPlus = -randomizerChange
        elif i == 4:
            Increase('False')
            i = 1
            randomizerPlus = 0
 
def DoSpeedFlip(mainKey, airRollKey):
    UpdateI()
    start = time.time()
 
    lastW = keyboard.is_pressed('w')
 
    mouse.press(RMB)
    time.sleep(delay2)
    mouse.release(RMB)
    time.sleep(delay3)
    keyboard.press(mainKey)
    keyboard.press('w')
    time.sleep(delay1)
    mouse.press(RMB)
    time.sleep(delay3)
    mouse.release(RMB)
    time.sleep(delay3)
    keyboard.release('w')
    keyboard.release(mainKey)
    time.sleep(delay3)
    keyboard.press('s')
    keyboard.press(airRollKey)
    time.sleep(delay4)
    keyboard.press(mainKey)
    time.sleep(delay5)
    keyboard.release(mainKey)
    keyboard.release('s')
    time.sleep(delay6)
    keyboard.release(airRollKey)
 
    if lastW:
        keyboard.press('w')
 
    end = time.time() - start
    PrintBanner(endTime=end)
 
def ManageSpeedFlip(x):
    if keyboard.is_pressed('d'):
        DoSpeedFlip(right, airRollRight)
        time.sleep(0.3)
    elif keyboard.is_pressed('a'):
        DoSpeedFlip(left, airRollLeft)
        time.sleep(0.3)
 
def ToggleRandomizer(x):
    global randomizer
    if randomizer == True:
        while i != 1:
            UpdateI()
        randomizer = False
    elif randomizer == False:
        randomizer = True
    PrintBanner()
 
keyboard.on_press_key(">", Increase)
keyboard.on_press_key("<", Decrease)
keyboard.on_press_key("/", ToggleRandomizer)
 
while True:
    time.sleep(0.005)
    if mouse.is_pressed("x2"):  # Detect ThumbMouse2
        ManageSpeedFlip('x')
