import pygame
import random
from time import sleep

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 800

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (150,150,150)
RED = (255,0,0)

class Car :
    image_car = ['RacingCar01.png','RacingCar02.png','RacingCar03.png','RacingCar04.png','RacingCar05.png',
                 'RacingCar06.png','RacingCar07.png','RacingCar08.png','RacingCar09.png','RacingCar10.png',
                 'RacingCar11.png','RacingCar12.png','RacingCar13.png','RacingCar14.png','RacingCar15.png',
                 'RacingCar16.png','RacingCar17.png','RacingCar18.png','RacingCar19.png','RacingCar20.png']
    def __init__(self,x=0,y=0,dx=0,dy=0):
        self.image =""
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy

    def load_image(self):
        self.iamge = pygame.image.load(random.choice(self.image_car))
