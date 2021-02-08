from ursina import *
from Game_camera import Time_Travel_Camera
import time
import math
from Player import Player
import json

time_S_to_wait = 0
mouse_sensibility = 1
angle_x = 0
if __name__ == '__main__':
    # window.vsync = False
    angle_x = 0
    app = Ursina()
    def input(key):
        if key == 'q':
            if camera.z<150:
                camera.z += 200
        if key == 'e':
            if camera.z> - 150:
                camera.z -= 200
        if key == 'z':
            print(player.world_x, player.world_y, player.world_z)
            print(camera.getQuat())

    def update():
        #if  player.world_x - camera.world_x != 8:
        #    camera.x = player.world_x - 8
        #if  player.world_z - camera.world_z != 0:
        #    camera.z = player.world_z 
        #print(camera.position, player.position)
        sin = (camera.x-player.world_x)/8
        cos = (camera.z-player.world_z)/8
        angle_horizontal = math.degrees(math.atan2(sin,cos))
        angle_horizontal += held_keys['l']* time.dt *50
        angle_horizontal -= held_keys['j']* time.dt *50
        angle_horizontal = math.radians(angle_horizontal)
        camera.x = player.world_x + 8*math.sin(angle_horizontal)
        camera.z = player.world_z + 8*math.cos(angle_horizontal)
        #sin = (camera.y-player.world_y)/6
        #cos = (camera.x-player.world_x)/6
        #angle_vertical = math.degrees(math.atan2(sin,cos))
        #angle_vertical += held_keys['i']* time.dt *50
        #angle_vertical -= held_keys['k']* time.dt *50
        #angle_vertical = math.radians(angle_vertical)
        #camera.y = player.world_y + 6*math.sin(angle_vertical)
        camera.look_at(player, axis='forward')
    #app.camera = Time_Travel_Camera()
    Sky(color=color.white)
    ground = Entity(model='terrain', scale=(0.1,.1,.1), texture_scale=(100,100), collider='box')
    ground = Entity(model='plane', scale=(10,1,10), color=color.blue.tint(-.2), texture='white_cube',position = (0,0,-200), texture_scale=(100,100), collider='box')
    ground = Entity(model='plane', scale=(10,1,10), color=color.yellow.tint(-.2), texture='white_cube',position = (0,0,200), texture_scale=(100,100), collider='box')
    #print(dir(ground))
    box = Entity(model='plane', scale=(1,1,1),
        position = (1,1,1), texture_scale=(100,100), collider='box')
    box = Entity(model='plane', scale=(1,1,1),
        position = (1,1.3,2.2), texture_scale=(100,100), collider='box')
    platform = Entity(model='plane', scale=(1,1,1),
        position = (1.5,1.4,204), texture_scale=(100,100), collider='box')
    camera.position = Vec3(-8,6,0)

    player = Player(model='hourglass', scale=(0.01,0.01,0.01), position = (0,1,0), collider='box', color=color.gray.tint(-.2))
    camera.look_at(player, axis='forward')
    box2 = Entity(model='cube', position = (2,200,1), texture_scale=(100,100), collider='box')

    app.run()
