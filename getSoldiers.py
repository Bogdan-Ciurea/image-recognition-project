import pandas as pd

levels=[1, 1, 1, 1, 2, 2, 3, 3, 3, 3,
        4, 4, 4, 5, 5, 5, 5, 6, 6, 6,
        6, 7, 7, 7, 7, 8, 8, 8, 8, 9,
        9, 9, 9, 9, 10, 10, 10, 10, 10, 11,
        11, 11, 12, 11, 12, 12, 12, 13, 13, 13, 
        13, 13, 14, 14, 14, 14, 14, 15, 15, 15, 
        15, 15, 16, 16, 16, 16, 16, 17, 17, 17,
        17, 17, 18, 18, 18, 18, 18, 19, 18, 19,
        0 
    ]

# Will get the index at the specific level and attacks to the next level 
def getIndex(level, attacksToNextLevel):
    global levels
    s = 0
    for i in range(0, level):
        s += levels[i]
    return s - attacksToNextLevel

# Get the line at the specific level and attacks to the next level
def getLine(level, attacksToNextLevel):
    # Read the excel
    sheet = pd.read_excel('Assets/CastleTroops.xlsx', sheet_name = 'CastleTroops')
    
    # Find the index depending on the level and attack to the next level
    index = getIndex(level, attacksToNextLevel)

    # Gets the data in the desired format
    toolsLeft = sheet['Tools Left'].values[index]
    toolsMiddle = sheet['Tools Middle'].values[index]
    toolsRight = sheet['Tools Right'].values[index]
    menLeft = sheet['Men Left'].values[index]
    menMiddle = sheet['Men Middle'].values[index]
    menRight = sheet['Men Right'].values[index]

    # Sets a desired format to the data
    if type(toolsLeft) != str:
        toolsLeft = ""
    if type(toolsMiddle) != str:
        toolsMiddle = ""
    if type(toolsRight) != str:
        toolsRight = ""
    if type(menLeft) != str:
        menLeft = ""
    if type(menMiddle) != str:
        menMiddle = ""
    if type(menRight) != str:
        menRight = ""
    
    return toolsLeft, toolsMiddle, toolsRight, menLeft, menMiddle, menRight


# This class will store the number of tools or troops
class Soldiers():
    number = 0
    unit = ''
    img = 'Assets/Maceman.jpg'

    def __init__(self, code):
        code = code.split(' ')
        self.number = int(code[0])
        self.unit = code[1]
        #self.img = 'Assets/Maceman.jpg'

# This class will save the position of each unit/tool 
class Wave():
    troopsLeft = 0
    troopsMid = 0
    troopsRight = 0
    toolsLeft = 0
    toolsMid = 0
    toolsRight = 0

    def __init__(self):
        self.troopsLeft = 0
        self.troopsMid = 0
        self.troopsRight = 0
        self.toolsLeft = 0
        self.toolsMid = 0
        self.toolsRight = 0

    def buildTroops(self):
        if self.troopsLeft:
            x = self.troopsLeft.split(' , ')
            self.troopsLeft = []
            for i in range(len(x)):
                self.troopsLeft.append(Soldiers(x[i]))

        if self.troopsMid:
            x = self.troopsMid.split(' , ')
            self.troopsMid = []
            for i in range(len(x)):
                self.troopsMid.append(Soldiers(x[i]))

        if self.troopsRight:
            x = self.troopsRight.split(' , ')
            self.troopsRight = []
            for i in range(len(x)):
                self.troopsRight.append(Soldiers(x[i]))

        if self.toolsLeft:
            x = self.toolsLeft.split(' , ')
            self.toolsLeft = []
            for i in range(len(x)):
                self.toolsLeft.append(Soldiers(x[i]))

        if self.toolsMid:
            x = self.toolsMid.split(' , ')
            self.toolsMid = []
            for i in range(len(x)):
                self.toolsMid.append(Soldiers(x[i]))

        if self.toolsRight:
            x = self.toolsRight.split(' , ')
            self.toolsRight = []
            for i in range(len(x)):
                self.toolsRight.append(Soldiers(x[i]))

    def getToolsLeft(self):
        if self.toolsLeft:
            return self.toolsLeft
        else:
            return 0
    
    def getToolsMid(self):
        if self.toolsMid:
            return self.toolsMid
        else:
            return 0

    def getToolsRight(self):
        if self.toolsRight:
            return self.toolsRight
        else:
            return 0

    def getTroopsLeft(self):
        if self.troopsLeft:
            return self.troopsLeft
        else:
            return 0
    
    def getTroopsMid(self):
        if self.troopsMid:
            return self.troopsMid
        else:
            return 0

    def getTroopsRight(self):
        if self.troopsRight:
            return self.troopsRight
        else:
            return 0

# This class will store all the inforamtion about an attack
class Attack():
    waves = []

    def __init__(self, toolLeft, toolMid, toolRight, menLeft, menMid, menRight):
        self.troopsLeft = menLeft
        self.troopsMid = menMid
        self.troopsRight = menRight
        self.toolsLeft = toolLeft
        self.toolsMid = toolMid
        self.toolsRight = toolRight

        self.buildWaves()
        self.putTroopsInWaves()

    def buildWaves(self):
        n = max(self.toolsLeft.count('|'), self.toolsMid.count('|'), self.toolsRight.count('|'),
                    self.troopsLeft.count('|'), self.troopsMid.count('|'), self.troopsRight.count('|'))

        
        for i in range(n + 1):
            self.waves.append(Wave())

        self.toolsLeft = formatWave(self.toolsLeft)
        self.toolsMid = formatWave(self.toolsMid)
        self.toolsRight = formatWave(self.toolsRight)
        self.troopsLeft = formatWave(self.troopsLeft)
        self.troopsMid = formatWave(self.troopsMid)
        self.troopsRight = formatWave(self.troopsRight)

    def putTroopsInWaves(self):
        n = self.numberOfWaves()
        try:
            for i in range(n):
                if self.toolsLeft[i] != '':
                    self.waves[i].toolsLeft = self.toolsLeft[i]
        except:
            pass

        try:
            for i in range(n):
                if self.toolsMid[i] != '':
                    self.waves[i].toolsMid = self.toolsMid[i]
        except:
            pass

        try:
            for i in range(n):
                if self.toolsRight[i] != '':
                    self.waves[i].toolsRight = self.toolsRight[i]
        except:
            pass

        try:
            for i in range(n):
                if self.troopsLeft[i] != '':
                    self.waves[i].troopsLeft = self.troopsLeft[i]
        except:
            pass

        try:
            for i in range(n):
                if self.troopsMid[i] != '':
                    self.waves[i].troopsMid = self.troopsMid[i]
        except:
            pass

        try:
            for i in range(n):
                if self.troopsRight[i] != '':
                    self.waves[i].troopsRight = self.troopsRight[i]
        except:
            pass

        for i in range(n):
            self.waves[i].buildTroops()
        
    def numberOfWaves(self):
        return len(self.waves)


def formatWave(rawWave):
    if rawWave != '':
        return rawWave.split(' | ')
    else:
        return ''


def getCurrentAttack(level, attacksToNextLevel):
    toolsLeft, toolsMiddle, toolsRight, menLeft, menMiddle, menRight = getLine(level, attacksToNextLevel)
    currentAttack = Attack(toolsLeft, toolsMiddle, toolsRight, menLeft, menMiddle, menRight)
    return currentAttack

