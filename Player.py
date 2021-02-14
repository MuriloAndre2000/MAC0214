from ursina import *
import json
class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.speed = 2.5
        self.jumping = False
        self.gravity = 3
        self.speed_jump = 0.5
        self.time_jumping = 0
        self.landing = False
        self.falling = False

        for key, value in kwargs.items():
            setattr(self, key, value)
    def input(self, key):
        if key == 'q':
            if self.z<150:
                self.z += 200
        if key == 'e':
            if self.z> - 150:
                self.z -= 200

        