from ursina import *
from Game_camera import Time_Travel_Camera
import time
from Player import Player
import json

time_S_to_wait = 0

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
        if key == 'z':
            print(player.world_x, player.world_y, player.world_z)
    def update():
        #camera.x += held_keys['w'] * time.dt * 2.5
        #camera.x -= held_keys['s'] * time.dt * 2.5
        #print(player.world_x)
        #with open('data.json', 'r') as f:
        #    data = json.load(f)
        #if 'd' == 'd':
        #if camera.x + .8 >= data['plane1']['x'][0] and camera.x + .8 <= data['plane1']['x'][1]:
        #    if held_keys['w']:
        #        camera.look_at(player, axis='forward')
        #        camera.x += held_keys['w'] * time.dt * 2.5
        #    if held_keys['s']:
        #        camera.look_at(player, axis='forward')     
        #        camera.x -= held_keys['s'] * time.dt * 2.5  
        #    camera.z += held_keys['a'] * time.dt * 2.5
        #    camera.z -= held_keys['d'] * time.dt * 2.5
            #print(camera.position)
        if  player.world_x - camera.world_x != 8:
            camera.x = player.world_x - 8
        if  player.world_z - camera.world_z != 0:
            camera.z = player.world_z 
        """
        time_held = held_keys['s'] * time.dt
        if time_held > 0:
            with open('data.json', 'r') as f:
                data = json.load(f)
            data['Time_S'] += time_held
            if data['Time_S'] > 0.1:
                times = 10
                for _ in range(10):
                    camera.x -= data['Time_S']/10 * 2.5
                data['Time_S'] = 0
            with open('data.json', 'w') as f:
                json.dump(data, f)
        """
    #app.camera = Time_Travel_Camera()
    Sky(color=color.white)
    ground = Entity(model='plane', scale=(10,1,10), color=color.red.tint(-.2), texture='white_cube', texture_scale=(100,100), collider='box')
    ground = Entity(model='plane', scale=(10,1,10), color=color.blue.tint(-.2), texture='white_cube',position = (0,0,-200), texture_scale=(100,100), collider='box')
    ground = Entity(model='plane', scale=(10,1,10), color=color.yellow.tint(-.2), texture='white_cube',position = (0,0,200), texture_scale=(100,100), collider='box')
    #print(dir(ground))
    box = Entity(model='plane', scale=(1,1,1),
        position = (1,1,1), texture_scale=(100,100), collider='box')
    box = Entity(model='plane', scale=(1,1,1),
        position = (1,1.3,2.2), texture_scale=(100,100), collider='box')
    camera.position = Vec3(-8,6,0)

    player = Player(model='hourglass', scale=(0.01,0.01,0.01), position = (0,1,0), collider='box', color=color.gray.tint(-.2))
    camera.look_at(player, axis='forward')
    box2 = Entity(model='cube', position = (2,200,1), texture_scale=(100,100), collider='box')

    app.run()
