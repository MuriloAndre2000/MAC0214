from ursina import *
class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.speed = 2.5
        self.jumping = False
        self.gravity = 3
        self.speed_jump = 0.5
        self.time_jumping = 0
        self.landing = False

        for key, value in kwargs.items():
            setattr(self, key, value)
    def input(self, key):
        if key == 'space':
            if self.jumping == False:
                self.jumping = True
        if key == 'q':
            if self.z<150:
                self.z += 200
        if key == 'e':
            if self.z> - 150:
                self.z -= 200

    def update(self):
        self.x += held_keys['d'] * time.dt * self.speed
        self.x -= held_keys['a'] * time.dt * self.speed
        self.z += held_keys['w'] * time.dt * self.speed
        self.z -= held_keys['s'] * time.dt * self.speed
        if self.jumping:
            #So + Vo*t -g*t^2/2
            self.time_jumping += time.dt
            next_time = self.time_jumping + time.dt
            new_y = self.y+ self.speed_jump*next_time - self.gravity*next_time*next_time/2
            if new_y < self.y and self.landing == False:
                print(self.time_jumping)
                self.landing = True
            #print(new_y)
            if new_y > 0.2:
                self.y += self.speed_jump*self.time_jumping - self.gravity*self.time_jumping*self.time_jumping/2
            else:
                print(self.time_jumping)
                self.y =0.25
                self.jumping = False
                self.time_jumping =0
                self.landing = False

