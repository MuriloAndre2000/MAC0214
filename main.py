from ursina import *
from Game_camera import Time_Travel_Camera
import time

class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.speed = 2.5
        self.jumping = False
        self.gravity = 2
        self.speed_jump = 0.5
        self.time_jumping = 0

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
            #print(new_y)
            if new_y > 0:
                self.y += self.speed_jump*self.time_jumping - self.gravity*self.time_jumping*self.time_jumping/2
            else:
                self.y =0.25
                self.jumping = False
                self.time_jumping =0




if __name__ == '__main__':
    # window.vsync = False
    app = Ursina()
    def input(key):
        if key == 'q':
            if camera.z<150:
                camera.z += 200
        if key == 'e':
            if camera.z> - 150:
                camera.z -= 200
    #app.camera = Time_Travel_Camera()
    Sky(color=color.gray)
    ground = Entity(model='plane', scale=(10,1,10), color=color.red.tint(-.2), texture='white_cube', texture_scale=(100,100), collider='box')
    ground = Entity(model='plane', scale=(10,1,10), color=color.blue.tint(-.2), texture='white_cube',position = (0,0,-200), texture_scale=(100,100), collider='box')
    ground = Entity(model='plane', scale=(10,1,10), color=color.yellow.tint(-.2), texture='white_cube',position = (0,0,200), texture_scale=(100,100), collider='box')

    camera.position = Vec3(-8,6,-8)
    camera.rotation = (30,45,0)

    player = Player(model='cube', color=color.dark_gray, scale=(0.25,0.25,0.25), position = (0,0.25,0), collider='box')
    app.run()
