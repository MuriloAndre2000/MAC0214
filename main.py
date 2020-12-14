from ursina import *
from Game_camera import Time_Travel_Camera
import time
from Player import Player


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

    box = Entity(model='cube', scale=(0.5,0.5,0.5), color=color.yellow.tint(-.2), texture='white_cube',position = (0,0.25,0), texture_scale=(100,100), collider='box')
    camera.position = Vec3(-8,6,-8)
    camera.rotation = (30,45,0)

    player = Player(model='cube', color=color.dark_gray, scale=(0.25,0.25,0.25), position = (0,0.25,0), collider='box')
    app.run()
