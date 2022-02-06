import multiprocessing
import os
import random
import threading
import time
from multiprocessing import Process
import concurrent.futures

import pygame

import retropong


class WavPlayerRandom():
    def __init__(self):
        # th = threading.Thread(target=self.fileChooser(), args=(), daemon=True)
        process = multiprocessing.Process(self.fileChooser(), args=())
        main.threads.append(process)

    def fileChooser(self):
        print("Wav Player engine started")
        while True:
            if len(os.listdir("WAVSelectorDirectory")) != 0:
                random_file = random.choice(os.listdir("WAVSelectorDirectory"))
                soundObj = pygame.mixer.Sound(
                    f"WAVSelectorDirectory/{random_file}")
                print(f"Loaded WAVSelectorDirectory/{random_file}")
                soundObj.play()
                timenow = time.time()
                while True:
                    timethen = time.time()
                    if timethen - timenow > soundObj.get_length():
                        break
