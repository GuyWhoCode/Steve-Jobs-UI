import pygame
from pygame.locals import K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, KEYDOWN, K_PERCENT, K_PERIOD, K_BACKSLASH, K_MINUS, KMOD_SHIFT, K_EQUALS, K_RETURN
import json
from button import Button
from calculator import Calculator
# https://www.pygame.org/docs/

pygame.init()
config = json.load(open('config.json', 'r'))
buttonWidth = config['button'].get('buttonWidth')
buttonHeight = config['button'].get('buttonHeight')
margin = config['button'].get('margin')
topMargin = config['general'].get('topMargin')
bottomMargin = config['general'].get('bottomMargin')

outputFontSizeOriginal = config['general'].get('outputSize')
# Referenced when resetting the font size to the original size.
outputFontSize = config['general'].get('outputSize')
outputColor = config['general'].get('outputColor')
screenWidth = (buttonWidth * 4) + (margin * 3)
screenHeight = topMargin + (buttonHeight * 5) + (margin * 5) + bottomMargin
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Steve Jobs Calculator UI')

frames = pygame.time.Clock()

calcOutput = ''
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if (event.key == K_0):
                calcOutput += "0"
            elif (event.key == K_1):
                calcOutput += "1"
            elif (event.key == K_2):
                calcOutput += "2"
            elif (event.key == K_3):
                calcOutput += "3"
            elif (event.key == K_4):
                calcOutput += "4"
            elif (event.key == K_5):
                calcOutput += "5"
            elif (event.key == K_6):
                calcOutput += "6"
            elif (event.key == K_7):
                calcOutput += "7"
            elif (event.key == K_8 and KMOD_SHIFT):
                calcOutput += " × "
            elif (event.key == K_EQUALS and KMOD_SHIFT):
                calcOutput += " + "
            elif (event.key == K_MINUS):
                calcOutput += " - "
            elif (event.key == K_BACKSLASH):
                calcOutput += " ÷ "
            elif (event.key == K_PERIOD):
                calcOutput += "."
            elif (event.key == K_8):
                calcOutput += "8"
            elif (event.key == K_9):
                calcOutput += "9"
            elif (event.key == K_PERCENT):
                calcOutput = str(float(calcOutput) / 100)
                pygame.time.delay(100)
                # Delay to prevent multiple inputs within a small period of time
            elif (event.key == K_RETURN):
                calcOutput = Calculator(calcOutput)
    # Mirrors a similar functionality as the onscreen keys except for awaiting a keyboard input
                
                
    screen.fill((config['general'].get('backgroundColor'))) 
    
    for column in range(4):
        leftMargin = (buttonWidth + margin) * column
        for row in range(5):
            if (column == 3):
                color = 'sideBar'
                # Rightmost column color for operations
            elif (row == 0):
                color = 'topBar'
                # 1st row color for misc operations
            else:
                color = 'numBar'
                # Number button colors to input numbers

            if (column == 1 and row == 4):
                break;
            else:
                calcButton = Button(screen, leftMargin, (topMargin + (buttonWidth - margin) * row), color, buttonWidth, buttonHeight, column, row)
                buttonPress = calcButton.checkPressed(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                # Creates instance to check for a button hover and press

                if (buttonPress == "AC"):
                    calcOutput = ""
                    outputFontSize = outputFontSizeOriginal
                    # Reads directly from the pressed button instead of the Calculation function
                elif (buttonPress == "+/-"):
                    calcOutput = str(float(calcOutput) * -1)
                    pygame.time.delay(100)
                elif (buttonPress == "%"):
                    calcOutput = str(float(calcOutput) / 100)
                    pygame.time.delay(100)
                elif (buttonPress == "="):
                    calcOutput = Calculator(calcOutput)
                elif (buttonPress is not None):
                    calcOutput += buttonPress
                    pygame.time.delay(100)      
                    # Delay to prevent multiple inputs within a small period of time


    outputFont = pygame.font.SysFont('arial', outputFontSize)
    calcRender = outputFont.render(calcOutput, True, outputColor)
    if (screenWidth - outputFont.size(calcOutput)[0] < 0):
        outputFontSize -= 1
    else:
        screen.blit(calcRender, (screenWidth - outputFont.size(calcOutput)[0], topMargin - outputFont.size(calcOutput)[1]))
    # Automatic font size resizing -- decreases font size by one until the text width fits the screen width
    # Does not need a while loop since it decreases with each frame -- 1 loop of the outer while loop or game loop

    pygame.display.flip()
    frames.tick(30)
    # Constant 30 frames per second (fps)

pygame.quit()