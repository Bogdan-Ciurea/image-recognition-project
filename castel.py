import time
import pyautogui
import imgRecog, getSoldiers
pyautogui.PAUSE = 1

def click(pozx, pozy):
    pyautogui.click(x = pozx, y = pozy)

def doubleClick(pozx, pozy):
    pyautogui.doubleClick(x = pozx, y = pozy)

# Click the map button
def initializeMap():
    # Go to the tab
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')

    # Go to the map if the we are in the castle
    try:
        x, y = imgRecog.getCenterCoordinates(imgRecog.findCoordinates(imgRecog.makeScreenshot(), 'mapImage.jpg'))
        click(x, y)
        time.sleep(1)
    # Center on the castle if we are outside
    except:
        x, y = imgRecog.getCenterCoordinates(imgRecog.findCoordinates(imgRecog.makeScreenshot(), 'toCastle.jpg'))
        click(x, y)

# Inputs the coordinates of a castle and launches the 'attack' interface
def initializeAttack(x, y):
    xSearch, ySearch, width, height = imgRecog.findCoordinates(imgRecog.makeScreenshot(), 'coordinates.jpg')
    # Type the x coordinates
    doubleClick(xSearch + width / 4, ySearch + height / 2)
    pyautogui.write(str(x))

    # Type the y coordinates
    doubleClick(xSearch + width / 4 * 3, ySearch + height / 2)
    pyautogui.write(str(y))

    # Go to the castle
    pyautogui.press('enter')
    x, y = imgRecog.getCenterCoordinates(imgRecog.findCoordinates(imgRecog.makeScreenshot(), 'searchIcon.jpg'))
    click(x, y)

    # Click the attack icon
    x, y = imgRecog.getCenterCoordinates(imgRecog.findCoordinates(imgRecog.makeScreenshot(), 'attackArrow.jpg'))
    click(x, y)

    # Accepts the attack
    x, y = imgRecog.getCenterCoordinates(imgRecog.findCoordinates(imgRecog.makeScreenshot(), 'acceptIcon.jpg'))
    click(x, y)

# We get the data for the current attack 
# And put the soldiers in the coresponding zones
def attack(level, attackToNextLevel, resursa = 1):
    # This variable will store all the data of the attack
    currentAttack = getSoldiers.getCurrentAttack(level, attackToNextLevel)    
    numberOfWaves = currentAttack.numberOfWaves()

    for i in range(numberOfWaves):
        # We need to go to the next wave
        if i > 0:
            nextWave()

        # Select the troops
        if currentAttack.waves[i].getTroopsLeft():
            inputTroopsLeft(currentAttack.waves[i].getTroopsLeft())

        if currentAttack.waves[i].getTroopsMid():
            inputTroopsMid(currentAttack.waves[i].getTroopsMid())

        if currentAttack.waves[i].getTroopsRight():
            inputTroopsRight(currentAttack.waves[i].getTroopsRight())

        # Change to the tools section
        x, y = imgRecog.getCenterCoordinates(imgRecog.findCoordinates(imgRecog.makeScreenshot(), 'toolsIcon.jpg'))
        click(x, y)

        # Select the tools
        if currentAttack.waves[i].getToolsLeft():
            inputToolsLeft(currentAttack.waves[i].getToolsLeft())

        if currentAttack.waves[i].getToolsMid():
            inputToolsMid(currentAttack.waves[i].getToolsMid())

        if currentAttack.waves[i].getToolsRight():
            inputToolsRight(currentAttack.waves[i].getToolsRight())

    #accept attack
    x, y = imgRecog.getCenterCoordinates(imgRecog.findCoordinates(imgRecog.makeScreenshot(), 'attackButton.jpg'))
    click(x, y)
	#boost speed
    #click(780, 500)

    if resursa != '1':
        click(1039, 646)
        if resursa == '2':
            click(1045, 690)
        elif resursa == '3':
            click(1038, 715)
        elif resursa == '4':
            click(1040, 740) 

    #Launch the attack
    x, y = imgRecog.getCenterCoordinates(imgRecog.findCoordinates(imgRecog.makeScreenshot(), 'acceptIcon.jpg'))
    click(x, y)

# Next Wave
def nextWave():
    x, y = imgRecog.getCenterCoordinates(imgRecog.findCoordinates(imgRecog.makeScreenshot(),'nextWaveIcon.jpg'))
    click(x, y)

# Select the desired tool
def selectTool(a):
    # TODO The function will get a Soldiers class
    # TODO The function will search for the icon depending in the type of tool

    if a == 'ladd':
        click(950, 900)
    elif a == 'ram':
        click(1161, 900)

# Select the desired unit
def selectUnit(a):
    # TODO The function will get a Soldiers class
    # TODO The function will search for the icon depending in the type of unit


    if a == 'mm':
        click(1085, 900)
    elif a == 'cb':
        click(1160, 900)
    elif a == 'sp':
        click(950, 900)
    elif a == 'ar':
        click(1015, 900)
    elif a == 'sm':
        click(1230, 900)
    elif a == 'ths':
        click(1300, 900)
    elif a == 'hc':
        click(1375, 900)

def inputToolsLeft(tools):
    pass

def inputToolsMid(tools):
    pass

def inputToolsRight(tools):
    pass

def inputTroopsLeft(tools):
    pass

def inputTroopsMid(tools):
    pass

def inputTroopsRight(tools):
    pass


def atacCastel(x, y, level, lvlToLvl):
    initializeMap()
    print("Attacking the castle at", x, y)
    initializeAttack(x, y)
    #attack(level, lvlToLvl)
    return True

atacCastel(625, 790, 1,1)