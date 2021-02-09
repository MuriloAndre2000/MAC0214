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
        if key == 'space':
            if self.jumping == False and self.falling == False:
                self.jumping = True
        if key == 'q':
            if self.z<150:
                self.z += 200
        if key == 'e':
            if self.z> - 150:
                self.z -= 200

    def update(self):
        with open('data.json', 'r') as f:
            data = json.load(f)
        current_plane = {}
        for d in ['plane1', 'plane2', 'plane3']:
            if self.z <= data[d]['z'][1] and self.z >= data[d]['z'][0]:
                current_plane = data[d]
        for d in data:
            if self.z <= data[d]['z'][1] and self.z >= data[d]['z'][0] and self.x <= data[d]['x'][1] and self.x >= data[d]['x'][0]:
                height = data[d]['y'][0]
        if self.jumping:
            #So + Vo*t -g*t^2/2      
            height = 1      
            for d in data:
                if d != 'plane1' or d != 'plane2' or d != 'plane3':
                    if self.z <= data[d]['z'][1] and self.z >= data[d]['z'][0] and self.x <= data[d]['x'][1] and self.x >= data[d]['x'][0]:
                        height = data[d]['y'][0]
            self.time_jumping += time.dt
            next_time = self.time_jumping + time.dt
            new_y = self.y+ self.speed_jump*next_time - self.gravity*next_time*next_time/2
            #print(new_y)
            if new_y > height:
                self.y += self.speed_jump*self.time_jumping - self.gravity*self.time_jumping*self.time_jumping/2
            else:
                #print(self.time_jumping)
                self.y =height 
                self.jumping = False
                self.time_jumping =0
                self.landing = False
        elif self.y > height and self.falling == False:
            self.falling = True
            self.time_jumping =0
        if self.falling:
            height = 1      
            for d in data:
                if d != 'plane1' or d != 'plane2' or d != 'plane3':
                    if self.z <= data[d]['z'][1] and self.z >= data[d]['z'][0] and self.x <= data[d]['x'][1] and self.x >= data[d]['x'][0]:
                        height = data[d]['y'][0]
            self.time_jumping += time.dt
            next_time = self.time_jumping + time.dt
            new_y = self.y - self.gravity*next_time*next_time/2
            if new_y > height:
                self.y = self.y  - self.gravity*self.time_jumping*self.time_jumping/2
            else:
                #print(self.time_jumping)
                self.y =height 
                self.falling = False
                self.time_jumping =0