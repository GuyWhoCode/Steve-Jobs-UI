import pygame
from pygame.locals import K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, KEYDOWN
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

outputFontSize = config['general'].get('outputSize')
outputColor = config['general'].get('outputColor')
screenWidth = (buttonWidth * 4) + (margin * 3)
screenHeight = topMargin + (buttonHeight * 5) + (margin * 5) + bottomMargin
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Steve Jobs Calculator UI')

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
            elif (event.key == K_8):
                calcOutput += "8"
            elif (event.key == K_9):
                calcOutput += "9"


                
    screen.fill((config['general'].get('backgroundColor'))) 
    
    for column in range(4):
        leftMargin = (buttonWidth + margin) * column
        for row in range(5):
            if (column == 3):
                color = 'sideBar'
                # Rightmost column color
            elif (row == 0):
                color = 'topBar'
                # 1st row color
            else:
                color = 'numBar'
                # Number button colors

            if (column == 1 and row == 4):
                break;
            else:
                calcButton = Button(screen, leftMargin, (topMargin + (buttonWidth - margin) * row), color, buttonWidth, buttonHeight, column, row)
                buttonPress = calcButton.checkPressed(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                
                if (buttonPress == "AC"):
                    calcOutput = ""
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
    # Button generator

    
    outputFont = pygame.font.SysFont('arial', outputFontSize)
    calcRender = outputFont.render(calcOutput, True, outputColor)
    if (screenWidth - outputFont.size(calcOutput)[0] < 0):
        outputFontSize -= 1
    else:
        screen.blit(calcRender, (screenWidth - outputFont.size(calcOutput)[0], topMargin - outputFont.size(calcOutput)[1]))
    
    pygame.display.flip()

pygame.quit()