import pygame
import json
config = json.load(open('config.json', 'r'))
margin = config['button'].get('margin')
fontColor = config['button'].get('fontColor')

class basicButton():
    def __init__(self, marginLeft, marginTop, buttonWidth, buttonHeight, section, buttonText):
        self.marginLeft = marginLeft
        self.marginTop = marginTop
        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight
        self.section = section
        self.buttonText = buttonText
    
    def checkPressed(self, mouseX, mouseY):
        if ((mouseX > self.marginLeft and mouseX < self.marginLeft + self.buttonWidth) and (mouseY > self.marginTop and mouseY < self.marginTop + self.buttonHeight)):
            if (config[self.section].get("highlight") is None):
                return "hi"
            else:
                self.color = config[self.section].get("highlight")
                if (pygame.mouse.get_pressed()[0]):
                    return self.buttonText
                # Draw highlight hover
        else:
            if (config[self.section].get("highlight") is None):
                return "hi"
            else:
                self.color = config[self.section].get("color")
            # Draw normal button color
        
        self.drawButton()


class Button(basicButton):
    def __init__(self, screen, marginLeft, marginTop, color, buttonWidth, buttonHeight, col, row):
        text = self.calculatorText(col, row)
        super().__init__(marginLeft, marginTop, buttonWidth, buttonHeight, color, text)
        # Inherit the basic button functionality

        if (col == 0 and row == 4): self.buttonWidth = (buttonWidth * 2) + margin
        else: self.buttonWidth = buttonWidth
        # Zero number button takes up the space of two number buttons. 
        
        self.screen = screen
        self.buttonText = text
        self.color = config[color].get('color')
        self.section = color
        self.marginTop = marginTop
        self.marginLeft = marginLeft
        self.buttonHeight = buttonHeight
        self.drawButton()

    def drawButton(self):
        pygame.draw.rect(self.screen, self.color, (self.marginLeft, self.marginTop, self.buttonWidth, self.buttonHeight))
        buttonFont = pygame.font.SysFont("arial", 30)
        myText = buttonFont.render(self.buttonText.strip(), True, fontColor)
        self.screen.blit(myText, (self.marginLeft + ((self.buttonWidth - buttonFont.size(self.buttonText.strip())[0]) / 2), self.marginTop + ((self.buttonHeight / 3) - margin)))
                
    def calculatorText(self, col, row):
        if (col == 0):
            if (row == 0):
                return "AC"
            elif (row == 1):
                return "7"
            elif (row == 2):
                return "4"
            elif (row == 3):
                return "1"
            return "0"

        elif (col == 1):
            if (row == 0):
                return "+/-"
            elif (row == 1):
                return "8"
            elif (row == 2):
                return "5"
            elif (row == 3):
                return "2"

        elif (col == 2):
            if (row == 0):
                return "%"
            elif (row == 1):
                return "9"
            elif (row == 2):
                return "6"
            elif (row == 3):
                return "3"
            return "."

        elif (col == 3):
            if (row == 0):
                return " ÷ "
            elif (row == 1):
                return " × "
            elif (row == 2):
                return " - "
            elif (row == 3):
                return " + "
            return "="