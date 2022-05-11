


# Introduction

**Farming Bot for Goodgame Empire**

**This software was made by Bogdan Alexandru Ciurea**

**Email: ciureabogdanalexandru@yahoo.com**

This is a **personal project** that has the purpose of showing my skills in writing Python code that has the scope of automating tasks but also Python code that uses image recognition.
The idea of this project came when playing [Goodgame Empire](https://empire.goodgamestudios.com), a game played in the browser that need a lot of repetitive moves and procedures in order to get a higher level.

The basic ideas is that there are multiple NPC castles that, in order to attack, you will need to do a lot of steps in order to attack as many of these "Robber Baron" castles. 
The problem appears after attacking one of these Castles, because the level of them will increase and the troops that will defend the castle will change.
But there is a catch. Because of the way the game is coded, you will always know how what troops there will be in these NPS Castles at a certain level. You can check [this](https://goodgameempire.fandom.com/wiki/Robber_Baron_Castle_Level_1-10) website for more details.

**By the way, it is not my fault if you get banned or if you lost X amount of troops.**
And another thing: **the software is not finished** as it still needs polishing and to work regardless of the resolution.

----

# The software

## Used software
The presented software has been made using:
 - Python 🐍
 - PyQt5 (for the UI)
 - OpenCV
 - stackedit.io (for formatting the `.md` files)
 - lots of image recognition videos on YouTube 😀

## About the files
The project has the following structure:
```
├── assets/
├── castle.py
├── excel.py
├── getSoldiers.py
├── imgRecog.py
├── main.py
├── README.md
```

The folder named `assets` will contains the database of what castles have been attacked, the UI that is used by PyQt5 but also the images that will be found by the image recognition functions.


## How to run this project

This is the hardest part of this project so be ready to install some software.

### Installation part

What you have to install:

 - [Python3](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)
 - [Qt Designer](https://build-system.fman.io/qt-designer-download)

After installing be sure install the next packages. Run this in the PowerShell (press the Win Button, search for the PowerShell) and run the next command:
`pip install pyautogui, opencv-python, numpy, PyQt5`

### Personalization part

After this you should take a screenshot of your map. You can see that in the `assets` folder I three files named `main.jpg`, `av1.jpg` and `av2.jpg`. All of these have one main thing in common: they have at least 20 Barron Castles for each castle.

**Keep in mind that you will only be able to attack 20 Barron Castles for each of your Castles.**

Now you should save a screenshot for each of you castles and override mine but keep in mind the next step.

After you have overwritten my screenshots with yours, you should open Qt Designer and start reposition the checkboxes so that they will show be on top of the castles you have selected.
A personal recommendation: **try to chose the closest castles**.

Now the most annoying part so **be careful!**
**Each checkbox has an id** (for the main castle, the ids will be from 1 to 20; 21 to 40 for the second castle etc...) and **each** of these **checkboxes will kind of represent one castle** (because you've just put one over each castle in the last step). Now will have to go to the map of the game and identify the coordinates of every castle and introduce them in the `Assets/Database.xlsm` file. 

**A short example**
![Image](https://i.postimg.cc/8cjzb01b/Castles.png)

### Database part
Now that you have the database kind of done, don't forget to have each level of the Baron Castles correct but also the number of how many attacks you will need in order to level up the Baron Castle.

**And this is the end of the setup** so congrats!

Now you can run the program by running the `main.py` file.

## Drawbacks

**The program is not complete.** There are still multiple variables and things that should be added. It does some things the right way but it is still not good for operations. And it still has to be supervised.
Using image recognition is the best idea but it gets the thinks done as you cannot use html tags/xpath to automate this.

After I finish the basic functionality there are still multiple things to be added:
 - Add an auto attacker that will attack the Baron castles when they become available.
 - Also take into consideration the leaders and their powers.
