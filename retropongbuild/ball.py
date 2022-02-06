import random
import pygame as PG

import bar
import retropong
import randomball
import mainWindow
import pygame
from mainWindow import mainWindow
from randomball import randomBallEngine


class ball(bar.bar):

    def __init__(self, position, screenW, screenH, width=400, height=400):
        bar.bar.__init__(self, position, screenW, screenH, width, height)

    def moveaccordingtoEngine(self):
        self.position = [self.getPosition()[0] + randomball.randomBallEngine.speedx,
                         self.getPosition()[1] + randomball.randomBallEngine.speedy]
        self.updatepositionAccordingToWalls()

    def updatepositionAccordingToWalls(self):
        height = mainWindow.screenheight
        width = mainWindow.screenwidth
        if self.getPosition()[1] >= height or self.getPosition()[1] <= 0:
            randomBallEngine.speedy = -randomBallEngine.speedy
            # Wall hit sound
            if retropong.SOUND_ON:
                soundObj = pygame.mixer.Sound('ResourcesInUse/WallHit.wav')
                soundObj.play()

        if self.getPosition()[0] >= width or self.getPosition()[0] <= 0:
            randomBallEngine.speedx = -randomBallEngine.speedx
            # One of the borders were hit
            # We need to reset and add a point to the player that won the game
            if self.getPosition()[0] >= width:
                # Player 1 has won the game
                mainWindow.ScorePlayer1 += 1

                # Play Sound
                if retropong.SOUND_ON:
                    soundObj = pygame.mixer.Sound('ResourcesInUse/Powerup.wav')
                    soundObj.play()

                self.setPosition([mainWindow.screenwidth / 2,
                                 mainWindow.screenheight / 2])
                randomball.randomBallEngine(self)

            if self.getPosition()[0] <= 0:
                # Player 2 has won the game
                mainWindow.ScorePlayer2 += 1

                # Play Sound
                if retropong.SOUND_ON:
                    soundObj = pygame.mixer.Sound('ResourcesInUse/Powerup.wav')
                    soundObj.play()

                self.setPosition([mainWindow.screenwidth / 2,
                                 mainWindow.screenheight / 2])
                randomball.randomBallEngine(self)

        # Update the position
        self.position = [self.getPosition()[0] + randomball.randomBallEngine.speedx,
                         self.getPosition()[1] + randomball.randomBallEngine.speedy]

    def updatepositionAccordingtohits(self, bar1, bar2):
        if bar1.getPosition()[1] <= self.getPosition()[1] <= bar1.getPosition()[1] + bar1.getSize()[1] and \
                30 + bar1.getSize()[0]-20 <= self.getPosition()[0] <= 30 + bar1.getSize()[0]:
            # Play sound
            if retropong.SOUND_ON:
                soundObj = pygame.mixer.Sound('ResourcesInUse/BoardHit.wav')
                soundObj.play()

            randomBallEngine.speedx = retropong.BALLSPEED
            randomBallEngine.speedy = random.randrange(
                int(-100*retropong.BALLSPEED), int(+100*retropong.BALLSPEED), 1) / 100
            # Then update the position
            self.position = [self.getPosition()[0] + randomball.randomBallEngine.speedx,
                             self.getPosition()[1] + randomball.randomBallEngine.speedy]

        if bar2.getPosition()[1] <= self.getPosition()[1] <= bar2.getPosition()[1] + bar2.getSize()[1] and \
                mainWindow.screenwidth - (30 + bar2.getSize()[0]) <= self.getPosition()[0] <= mainWindow.screenwidth - (30 + bar2.getSize()[0]) + 20:
            # Play sound
            if retropong.SOUND_ON:
                soundObj = pygame.mixer.Sound('ResourcesInUse/BoardHit.wav')
                soundObj.play()

            randomBallEngine.speedx = -randomBallEngine.speedx
            randomBallEngine.speedy = random.randrange(
                int(-100*retropong.BALLSPEED), int(+100*retropong.BALLSPEED), 1) / 100
            # Then update the position
            self.position = [self.getPosition()[0] + randomball.randomBallEngine.speedx,
                             self.getPosition()[1] + randomball.randomBallEngine.speedy]
