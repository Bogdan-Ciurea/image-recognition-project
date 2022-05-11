import cv2
import numpy as np
import pyautogui

def drawElements(image, needle, threshold = 0.8):
    
    #Read the images
    canvas = cv2.imread(f"Assets/{image}", cv2.IMREAD_UNCHANGED)
    #canvas = cv2.imread("Assets/empiremapsmall.png", cv2.IMREAD_UNCHANGED)
    castle = cv2.imread(f"Assets/{needle}", cv2.IMREAD_UNCHANGED)

    #Find the results
    result = cv2.matchTemplate(canvas, castle, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    w = castle.shape[1]
    h = castle.shape[0]

    yloc, xloc = np.where(result >= threshold)

    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

    for (x, y, w, h) in rectangles:
        cv2.rectangle(canvas, (x, y), (x + w, y + h), (0, 255, 255), 2)

    canvas = cv2.resize(canvas, (1000, 600))
    cv2.imshow("Farm", canvas)
    cv2.waitKey()
    cv2.destroyAllWindows()

def findMultipleCoordinates(canvas, needle, threshold = 0.8):
    #Read the images
    #canvas = cv2.imread(f"Assets/{image}", cv2.IMREAD_UNCHANGED)
    needleImg = cv2.imread(f"Assets/{needle}", cv2.IMREAD_UNCHANGED)

    #Find the results
    result = cv2.matchTemplate(canvas, needleImg, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    w = needleImg.shape[1]
    h = needleImg.shape[0]

    yloc, xloc = np.where(result >= threshold)

    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

    if len(rectangles):
        coordinates = []
        for elem in rectangles:
            x = int(elem[0] + (elem[2]/2))
            y = int(elem[1] + (elem[3]/2))
            coordinates.append([x,y])
        return coordinates
    else:
        return False

def findCoordinates(canvas, needle, threshold = 0.8):
    
    #Read the images
    #canvas = cv2.imread(f"Assets/{image}", cv2.IMREAD_UNCHANGED)
    needleImg = cv2.imread(f"Assets/{needle}", cv2.IMREAD_UNCHANGED)

    #Find the results
    result = cv2.matchTemplate(canvas, needleImg, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    w = needleImg.shape[1]
    h = needleImg.shape[0]

    #Select those who are valid
    yloc, xloc = np.where(result >= threshold)

    rectangles = []
    for (x, y) in zip(xloc, yloc):
        #cv2.rectangle(canvas, (x, y), (x + w, y + h), (0, 255, 255), 2)
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

    if len(rectangles) == 1:
        return rectangles[0]
    else:
        return False

def getCenterCoordinates(rectangles):
    return int(rectangles[0] + rectangles[2]/2), int(rectangles[1] + rectangles[3]/2)

def makeScreenshot():
    screenshoot = pyautogui.screenshot()
    screenshoot = np.array(screenshoot)
    return cv2.cvtColor(screenshoot, cv2.COLOR_RGB2BGR)
