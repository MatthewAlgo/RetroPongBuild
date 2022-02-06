import random
import mainWindow
import retropong


class randomBallEngine():
    speedx = 0
    speedy = 0

    def __init__(self, ballintern):
        self.vectorx = random.randint(-10, 10)
        self.vectory = random.randint(-10, 10)
        self.ballintern = ballintern
        self.Logic()

    def Logic(self):
        if self.vectorx <= 0 and self.vectory <= 0:
            # 3rd quadrant
            randomBallEngine.speedx = -retropong.BALLSPEED
            randomBallEngine.speedy = random.randrange(
                int(-100*retropong.BALLSPEED), 0, 1) / 100
        if self.vectorx > 0 and self.vectory <= 0:
            # 4th quadrant
            randomBallEngine.speedx = +retropong.BALLSPEED
            randomBallEngine.speedy = random.randrange(
                int(-100*retropong.BALLSPEED), 0, 1) / 100
        if self.vectorx <= 0 and self.vectory > 0:
            # 2nd quadrant
            randomBallEngine.speedx = -retropong.BALLSPEED
            randomBallEngine.speedy = random.randrange(
                0, int(+100*retropong.BALLSPEED), 1) / 100
        if self.vectorx > 0 and self.vectory > 0:
            # 3rd quadrant
            randomBallEngine.speedx = +retropong.BALLSPEED
            randomBallEngine.speedy = random.randrange(
                0, int(+100*retropong.BALLSPEED), 1) / 100
