import pygame as PG

import retropong


class bar():
    def __init__(self, position, screenW, screenH, width=400, height=400):
        self.width = width
        self.height = height
        self.position = position
        self.screenW = screenW
        self.screenH = screenH

    def moveDown(self):
        # If Player VS Computer, adapt the speed
        if self.position[1] + self.height + 20 <= self.screenH and self.position[1] + 20 >= 0:
            if not (retropong.PVP_CONTROL == False and retropong.COMPUTERONLYCONTROL == False):
                self.position[1] += 5
            else:
                self.position[1] += 2.5

    def moveUp(self):
        # If Player VS Computer, adapt the speed
        if self.position[1] + self.height - 20 <= self.screenH and self.position[1] - 20 >= 0:
            if not (retropong.PVP_CONTROL == False and retropong.COMPUTERONLYCONTROL == False):
                self.position[1] -= 5
            else:
                self.position[1] -= 2.5

    def getSize(self):
        return [self.width, self.height]

    def setSize(self, list):
        self.width = list[0]
        self.height = list[1]

    def getPosition(self):
        return self.position

    def setPosition(self, list):
        self.position = list
