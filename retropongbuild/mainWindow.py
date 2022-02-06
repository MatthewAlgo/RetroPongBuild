import pygame as PG
import time
import threading
import bar
import ball
import random
import os
import pygame
import retropong
import randomball

timethen = time.time()
timenow = time.time()


class mainWindow():
    screenwidth = 620
    screenheight = 480

    ScorePlayer1 = 0
    ScorePlayer2 = 0

    def __init__(self, bar1, bar2, ball, width=620, height=480):
        self.tuplesize = (width, height)
        self.width = width
        self.height = height
        self.screen = PG.display.set_mode((self.width, self.height))
        self.background_colour = (0, 0, 0)
        self.bar1 = bar1
        self.bar2 = bar2
        self.ball = ball

        self.font = PG.font.Font('PressStartFont/PressStart2P-vaV7.ttf', 32)
        self.fontscore = PG.font.Font(
            'PressStartFont/PressStart2P-vaV7.ttf', 20)

        self.text = self.font.render(
            'PongArena', True, (0, 255, 0), (0, 0, 255))
        self.textRect = self.text.get_rect()

        self.textRect.center = (mainWindow.screenwidth //
                                2, mainWindow.screenheight // 2)

    def createOne(self):
        PG.display.set_caption('RetroPong - Made By MatthewAlgo')
        self.screen.fill(self.background_colour)

    def mainWindowLoop(self, PVP_CONTROL):
        running = True
        clock = PG.time.Clock()
        timethen = time.time()
        self.Intermediary_Selection_Screen()
        TIME_SINCE_SELECTION_UNMODIFIED = time.time()
        TIME_SINCE_SELECTION = time.time()
        # Load initial file
        if retropong.MUSIC_ON:
            random_file = random.choice(os.listdir("WAVSelectorDirectory"))
            soundObj = pygame.mixer.Sound(
                f"WAVSelectorDirectory/{random_file}")
            print(f"Loaded WAVSelectorDirectory/{random_file}")
            soundObj.play()

        while running:
            # Check for background music
            timenow = time.time()
            if timenow - TIME_SINCE_SELECTION > 10:  # Change ball speed first of all
                TIME_SINCE_SELECTION += 10
                retropong.BALLSPEED += 0.1
                if retropong.SOUND_ON:
                    sob = pygame.mixer.Sound('ResourcesInUse/LevelUp.wav')
                    sob.play()
            if retropong.MUSIC_ON:
                if timenow - TIME_SINCE_SELECTION_UNMODIFIED > soundObj.get_length():  # The current music is finished
                    random_file = random.choice(
                        os.listdir("WAVSelectorDirectory"))
                    soundObj = pygame.mixer.Sound(
                        f"WAVSelectorDirectory/{random_file}")
                    print(f"Loaded WAVSelectorDirectory/{random_file}")
                    TIME_SINCE_SELECTION_UNMODIFIED = time.time()
                    soundObj.play()

            keys = PG.key.get_pressed()  # checking pressed keys

            if retropong.PVP_CONTROL:
                if keys[PG.K_UP]:
                    self.bar2.moveUp()
                if keys[PG.K_DOWN]:
                    self.bar2.moveDown()
                if keys[PG.K_w]:
                    self.bar1.moveUp()
                if keys[PG.K_s]:
                    self.bar1.moveDown()
            elif not retropong.COMPUTERONLYCONTROL:
                if keys[PG.K_w]:
                    self.bar1.moveUp()
                if keys[PG.K_s]:
                    self.bar1.moveDown()
                if self.ball.getPosition()[1] < self.bar2.getPosition()[1] + self.bar2.getSize()[1] / 2:
                    self.bar2.moveUp()
                if self.ball.getPosition()[1] > self.bar2.getPosition()[1] + self.bar2.getSize()[1] / 2:
                    self.bar2.moveDown()
            else:
                if self.ball.getPosition()[1] < self.bar1.getPosition()[1] + self.bar1.getSize()[1] / 2:
                    self.bar1.moveUp()
                if self.ball.getPosition()[1] > self.bar1.getPosition()[1] + self.bar1.getSize()[1] / 2:
                    self.bar1.moveDown()
                if self.ball.getPosition()[1] < self.bar2.getPosition()[1] + self.bar2.getSize()[1] / 2:
                    self.bar2.moveUp()
                if self.ball.getPosition()[1] > self.bar2.getPosition()[1] + self.bar2.getSize()[1] / 2:
                    self.bar2.moveDown()

            for event in PG.event.get():
                if event.type == PG.QUIT:
                    running = False
                    print(
                        "Game End\nHope you enjoy the game. Please check my github page: github.com/MatthewAlgo")
                    exit()
                if event.type == PG.KEYDOWN:
                    if event.key == PG.K_ESCAPE:
                        # RETURN TO MAIN MENU
                        try:
                            soundObj.stop()
                        except:
                            pass
                        mainWindow.ScorePlayer1 = 0
                        mainWindow.ScorePlayer2 = 0
                        retropong.BALLSPEED = 1
                        # START RECURSION
                        mainWindow.mainWindowLoop(self, retropong.PVP_CONTROL)


                if event.type == PG.WINDOWRESIZED:
                    pass
            # Redraw frame window
            self.screen.fill((0, 0, 0))

            # Draw the text inside the rectangle
            self.screen.blit(self.text, self.textRect)

            self.textscore = self.fontscore.render(
                f'Player1: {mainWindow.ScorePlayer1} # Player2: {mainWindow.ScorePlayer2}', True, (
                    0, 255, 0),
                (0, 0, 255))
            self.textRectscore = self.textscore.get_rect()
            self.textRectscore.center = (
                mainWindow.screenwidth // 2, mainWindow.screenheight // 5)

            if mainWindow.ScorePlayer1 == 20 or mainWindow.ScorePlayer2 == 20:
                try:
                    soundObj.stop()
                except:
                    pass
                self.DisplayWinnerPart()
                running = False
                break

            self.screen.blit(self.textscore, self.textRectscore)

            PG.draw.rect(self.screen, (255, 0, 0), (
                self.bar1.getPosition()[0], self.bar1.getPosition()[1], self.bar1.getSize()[0], self.bar1.getSize()[1]),
                2)
            PG.draw.rect(self.screen, (255, 0, 0), (
                self.bar2.getPosition()[0], self.bar2.getPosition()[1], self.bar2.getSize()[0], self.bar2.getSize()[1]),
                2)

            self.ball.moveaccordingtoEngine()
            self.ball.updatepositionAccordingtohits(self.bar1, self.bar2)

            PG.draw.circle(self.screen, (255, 0, 0), (self.ball.getPosition()[0], self.ball.getPosition()[1]),
                           self.ball.getSize()[0], 0)

            PG.display.flip()
            clock.tick(100)

    def Intermediary_Selection_Screen(self):
        running = True
        SELECTION = 1
        localtimethen = time.time()
        localtimenow = time.time()
        random_file = random.choice(os.listdir("WAVSelectorDirectory"))
        localsoundObj = pygame.mixer.Sound(
            f"WAVSelectorDirectory/{random_file}")

        if retropong.MUSIC_ON:
            random_file = random.choice(os.listdir("WAVSelectorDirectory"))
            localsoundObj = pygame.mixer.Sound(
                f"WAVSelectorDirectory/{random_file}")
            print(f"Loaded WAVSelectorDirectory/{random_file}")
            localsoundObj.play()

        while running:
            for event in PG.event.get():
                if event.type == PG.QUIT:
                    running = False
                    print(
                        "Game End\nHope you enjoy the game. Please check my github page: github.com/MatthewAlgo")
                    exit()
                if event.type == PG.WINDOWRESIZED:
                    pass
                if event.type == pygame.KEYDOWN:
                    if retropong.SOUND_ON:
                        sob = pygame.mixer.Sound(
                            'ResourcesInUse/ItemChanged.wav')
                        sob.play()
                    if event.key == pygame.K_UP:
                        if SELECTION > 1:
                            SELECTION -= 1
                    if event.key == pygame.K_DOWN:
                        if SELECTION < 5:
                            SELECTION += 1
                    if event.key == pygame.K_RETURN:
                        if SELECTION == 1:
                            retropong.PVP_CONTROL = True
                            retropong.COMPUTERONLYCONTROL = False
                            try:
                                localsoundObj.stop()
                            except:
                                pass

                        if SELECTION == 2:
                            retropong.PVP_CONTROL = False
                            retropong.COMPUTERONLYCONTROL = False
                            try:
                                localsoundObj.stop()
                            except:
                                pass
                        if SELECTION == 3:
                            retropong.PVP_CONTROL = False
                            retropong.COMPUTERONLYCONTROL = True
                            try:
                                localsoundObj.stop()
                            except:
                                pass
                        if SELECTION == 4:
                            if retropong.MUSIC_ON == True:
                                retropong.MUSIC_ON = False
                                try:
                                    localsoundObj.stop()
                                except:
                                    pass
                            else:
                                localtimethen = time.time()
                                localtimenow = time.time()

                                retropong.MUSIC_ON = True
                                random_file = random.choice(
                                    os.listdir("WAVSelectorDirectory"))
                                localsoundObj = pygame.mixer.Sound(
                                    f"WAVSelectorDirectory/{random_file}")
                                print(
                                    f"Loaded WAVSelectorDirectory/{random_file}")
                                localsoundObj.play()
                        if SELECTION == 5:
                            if retropong.SOUND_ON == True:
                                retropong.SOUND_ON = False
                            else:
                                retropong.SOUND_ON = True
                        if SELECTION != 4 and SELECTION != 5:
                            localsoundObj.stop()
                            running = False
                            break

            # Redraw frame window
            self.screen.fill((0, 0, 0))

            # Init Fonts
            self.font = PG.font.Font(
                'PressStartFont/PressStart2P-vaV7.ttf', 25)
            self.fontscore = PG.font.Font(
                'PressStartFont/PressStart2P-vaV7.ttf', 20)

            # Draw Entities -> Textboxes
            text = self.font.render(
                'RetroPong - The Game', True, (0, 255, 0), (0, 0, 255))
            textRect = self.text.get_rect()
            textRect.center = (mainWindow.screenwidth // 3,
                               mainWindow.screenheight // 8)
            self.screen.blit(text, textRect)

            # First Menu Item
            if SELECTION != 1:
                text = self.fontscore.render(
                    'Player VS Player', True, (0, 255, 0), (0, 0, 255))
            else:
                text = self.fontscore.render(
                    'Player VS Player', True, (0, 0, 255), (0, 255, 0))
            textRect = self.text.get_rect()
            textRect.center = (mainWindow.screenwidth // 3,
                               mainWindow.screenheight // 3.5)
            self.screen.blit(text, textRect)

            # Second Menu Item
            if SELECTION != 2:
                text = self.fontscore.render(
                    'Player VS Computer', True, (0, 255, 0), (0, 0, 255))
            else:
                text = self.fontscore.render(
                    'Player VS Computer', True, (0, 0, 255), (0, 255, 0))

            textRect = self.text.get_rect()
            textRect.center = (mainWindow.screenwidth // 3,
                               mainWindow.screenheight // 2.5)
            self.screen.blit(text, textRect)

            # Third Menu Item
            if SELECTION != 3:
                text = self.fontscore.render(
                    'Computer VS Computer', True, (0, 255, 0), (0, 0, 255))
            else:
                text = self.fontscore.render(
                    'Computer VS Computer', True, (0, 0, 255), (0, 255, 0))

            textRect = self.text.get_rect()
            textRect.center = (mainWindow.screenwidth // 3,
                               mainWindow.screenheight // 2)
            self.screen.blit(text, textRect)

            # Music Toggle
            if SELECTION != 4:
                if retropong.MUSIC_ON:
                    text = self.fontscore.render(
                        'o Music Toggle', True, (0, 255, 0), (0, 0, 255))
                else:
                    text = self.fontscore.render(
                        'Music Toggle', True, (0, 255, 0), (0, 0, 255))
            else:
                if retropong.MUSIC_ON:
                    text = self.fontscore.render(
                        'o Music Toggle', True, (0, 0, 255), (0, 255, 0))
                else:
                    text = self.fontscore.render(
                        'Music Toggle', True, (0, 0, 255), (0, 255, 0))

            textRect = self.text.get_rect()
            textRect.center = (mainWindow.screenwidth // 3,
                               mainWindow.screenheight // 1.45)
            self.screen.blit(text, textRect)

            # Sound effects Toggle
            if SELECTION != 5:
                if retropong.SOUND_ON:
                    text = self.fontscore.render(
                        'o Sound Toggle', True, (0, 255, 0), (0, 0, 255))
                else:
                    text = self.fontscore.render(
                        'Sound Toggle', True, (0, 255, 0), (0, 0, 255))
            else:
                if retropong.SOUND_ON:
                    text = self.fontscore.render(
                        'o Sound Toggle', True, (0, 0, 255), (0, 255, 0))
                else:
                    text = self.fontscore.render(
                        'Sound Toggle', True, (0, 0, 255), (0, 255, 0))

            textRect = self.text.get_rect()
            textRect.center = (mainWindow.screenwidth // 3,
                               mainWindow.screenheight // 1.25)
            self.screen.blit(text, textRect)

            PG.display.flip()
            PG.display.update()

    def DisplayWinnerPart(self):
        running = True
        while running:
            for event in PG.event.get():
                if event.type == PG.QUIT:
                    running = False
                    if mainWindow.ScorePlayer1 == 20:
                        print(f"Player 1 has won the game")
                    elif mainWindow.ScorePlayer2 == 20:
                        print(f"Player 2 has won the game")
                    print(
                        "Game End\nHope you enjoy the game. Please check my github page: github.com/MatthewAlgo")

                    exit()
                if event.type == PG.KEYDOWN:
                    running = False
                    if mainWindow.ScorePlayer1 == 20:
                        print(f"Player 1 has won the game")
                    elif mainWindow.ScorePlayer2 == 20:
                        print(f"Player 2 has won the game")
                    mainWindow.ScorePlayer1 = 0
                    mainWindow.ScorePlayer2 = 0
                    retropong.BALLSPEED = 1
                    # START RECURSION
                    mainWindow.mainWindowLoop(self, retropong.PVP_CONTROL)
                    exit()
                    break
            self.screen.fill((0, 0, 0))
            if mainWindow.ScorePlayer1 == 20:
                text = self.fontscore.render(
                    'Player1 has won the game!', True, (0, 255, 0), (0, 0, 255))
                textRect = self.text.get_rect()
                textRect.center = (mainWindow.screenwidth //
                                   3, mainWindow.screenheight // 1.5)
                self.screen.blit(text, textRect)
            if mainWindow.ScorePlayer2 == 20:
                text = self.fontscore.render(
                    'Player2 has won the game!', True, (0, 255, 0), (0, 0, 255))
                textRect = self.text.get_rect()
                textRect.center = (mainWindow.screenwidth //
                                   3, mainWindow.screenheight // 1.5)
                self.screen.blit(text, textRect)
            text = self.fontscore.render(
                'Press any key to continue', True, (0, 255, 0), (0, 0, 255))
            textRect = self.text.get_rect()
            textRect.center = (mainWindow.screenwidth // 3,
                               mainWindow.screenheight // 2)
            self.screen.blit(text, textRect)
            PG.display.flip()
        if mainWindow.ScorePlayer1 == 20:
            print(f"Player 1 has won the game")
        elif mainWindow.ScorePlayer2 == 20:
            print(f"Player 2 has won the game")
