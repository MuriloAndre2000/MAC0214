from ursina import *
from Game_camera import Time_Travel_Camera
import time
import math
from Player import Player
import numpy as np
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
        #define variables
        player_speed = 2.5
        #angle of camera to player
        sin = (camera.x-player.world_x)/8
        cos = (camera.z-player.world_z)/8
        angle_horizontal = math.degrees(math.atan2(sin,cos))
        #player rotate the camera by the player in horizontal way
        angle_horizontal += held_keys['l']* time.dt *50
        angle_horizontal -= held_keys['j']* time.dt *50
        angle_horizontal = math.radians(angle_horizontal)
        #define camera position by angle
        camera.x = player.world_x + 8*math.sin(angle_horizontal)
        camera.z = player.world_z + 8*math.cos(angle_horizontal)
        #define vector of player-camera and get x and z
        vector_x = (player.world_position - camera.world_position).x
        vector_z = (player.world_position - camera.world_position).z
        #the moviment is a mix of x and z, in this way the player when press w
        #will move as 3 person
        if held_keys['w']:
            time_held = held_keys['w'] * time.dt
            player.world_x += time_held * player_speed * vector_x/8
            player.world_z += time_held * player_speed * vector_z/8
            camera.x += time_held * player_speed * vector_x/8
            camera.z += time_held * player_speed * vector_z/8
        if held_keys['s']:
            time_held = held_keys['s'] * time.dt
            player.world_x -= time_held * player_speed * vector_x/8
            player.world_z -= time_held * player_speed * vector_z/8
            camera.x -= time_held * player_speed * vector_x/8
            camera.z -= time_held * player_speed * vector_z/8
        if held_keys['d']:
            time_held = held_keys['d'] * time.dt
            player.world_x += time_held * player_speed * vector_z/8
            player.world_z -= time_held * player_speed * vector_x/8
            camera.x += time_held * player_speed * vector_z/8
            camera.z -= time_held * player_speed * vector_x/8
        if held_keys['a']:
            time_held = held_keys['a'] * time.dt
            player.world_x -= time_held * player_speed * vector_z/8
            player.world_z += time_held * player_speed * vector_x/8
            camera.x -= time_held * player_speed * vector_z/8
            camera.z += time_held * player_speed * vector_x/8
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
