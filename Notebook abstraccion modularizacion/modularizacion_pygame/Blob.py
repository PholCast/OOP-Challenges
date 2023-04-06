
import random
from math import sin, cos, radians
from module_pygame import WIDTH,HEIGHT
class Blob:
 
    def __init__(self, color):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(32,64)
        self.color = color
        self.angle = random.randint(0, 360)
        self.speed = random.randint(1, 3)
 
    def move(self):
        self.angle += self.speed
        self.x = int((cos(radians(self.angle)) * 200) + (WIDTH / 2))
        self.y = int((sin(radians(self.angle)) * 200) + (HEIGHT / 2))