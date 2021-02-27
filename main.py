from ursina import *
from Game_camera import Time_Travel_Camera
import time
import math
from Player import Player
import numpy as np
import json

time_S_to_wait = 0

if __name__ == '__main__':
    # window.vsync = False
    angle_x = 0
    app = Ursina()
    def input(key):
        if key == 'q':
            if camera.z<150:
                camera.z += 200
                player.world_z += 200
                camera.y += 0.1
                player.world_y += .1
        if key == 'e':
            if camera.z> - 150:
                camera.z -= 200
                player.world_z -= 200
                camera.y += .1
                player.world_y += .1
        if key == 'space':
            direction = Vec3(0,-1,0).normalized()
            origin = (player.world_x,player.world_y - 0.2,player.world_z)
            middle_ray = raycast(origin , direction, distance=0.02, debug=True)
            if middle_ray.hit:
                player.jumping = True
                player.speed_jump =10
                player.time_jumping = 0
        #if key == 'z':
        #    if text.visible:
        #        text.visible = False
        #    else:
        #        text.appear(speed=.025)
        #        text.visible = True

    def update():
        #define variables
        player_speed = 2.5
        radius_horizontal = 8
        mouse_sensibility = 200
        radius_horizontal = math.sqrt(15**2 - (camera.y*camera.y))
        position_Y = 0.054013315588235855
        gravity = 25
        #angle of camera to player
        sin_horizontal = (camera.x-player.world_x)/radius_horizontal
        cos_horizontal = (camera.z-player.world_z)/radius_horizontal
        angle_horizontal = math.degrees(math.atan2(sin_horizontal,cos_horizontal))
        angle_vertical = math.degrees(math.atan2(camera.y,radius_horizontal))

        #player rotate the camera by the player in horizontal way
        angle_horizontal += mouse.velocity.x * mouse_sensibility
        angle_vertical += mouse.velocity.y * mouse_sensibility/2

        #angle_vertical_x_y += mouse.velocity.y *200
        angle_horizontal = math.radians(angle_horizontal)
        angle_vertical = math.radians(angle_vertical)

        #define camera position by angle
        camera.x = player.world_x + radius_horizontal*math.sin(angle_horizontal)
        camera.z = player.world_z + radius_horizontal*math.cos(angle_horizontal)
        if radius_horizontal*math.tan(angle_vertical) < 15:
            if radius_horizontal*math.tan(angle_vertical) > -1:
                camera.y = radius_horizontal*math.tan(angle_vertical)
        #the moviment is a mix of x and z, in this way the player when press w
        #will move as 3 person
        if held_keys['w']:
            time_held = held_keys['w'] * time.dt
            #define vector of player-camera and get x and z
            vector_x = (player.world_position - camera.world_position).x
            vector_z = (player.world_position - camera.world_position).z
            player.world_x += time_held * player_speed * vector_x/radius_horizontal
            player.world_z += time_held * player_speed * vector_z/radius_horizontal
            camera.x += time_held * player_speed * vector_x/radius_horizontal
            camera.z += time_held * player_speed * vector_z/radius_horizontal
        if held_keys['s']:
            time_held = held_keys['s'] * time.dt
            #define vector of player-camera and get x and z
            vector_x = (player.world_position - camera.world_position).x
            vector_z = (player.world_position - camera.world_position).z
            player.world_x -= time_held * player_speed * vector_x/radius_horizontal
            player.world_z -= time_held * player_speed * vector_z/radius_horizontal
            camera.x -= time_held * player_speed * vector_x/radius_horizontal
            camera.z -= time_held * player_speed * vector_z/radius_horizontal
        if held_keys['d']:
            time_held = held_keys['d'] * time.dt
            #define vector of player-camera and get x and z
            vector_x = (player.world_position - camera.world_position).x
            vector_z = (player.world_position - camera.world_position).z
            player.world_x += time_held * player_speed * vector_z/radius_horizontal
            player.world_z -= time_held * player_speed * vector_x/radius_horizontal
            camera.x += time_held * player_speed * vector_z/radius_horizontal
            camera.z -= time_held * player_speed * vector_x/radius_horizontal
        if held_keys['a']:
            time_held = held_keys['a'] * time.dt
            #define vector of player-camera and get x and z
            vector_x = (player.world_position - camera.world_position).x
            vector_z = (player.world_position - camera.world_position).z
            player.world_x -= time_held * player_speed * vector_z/radius_horizontal
            player.world_z += time_held * player_speed * vector_x/radius_horizontal
            camera.x -= time_held * player_speed * vector_z/radius_horizontal
            camera.z += time_held * player_speed * vector_x/radius_horizontal

        next_time = player.time_jumping + time.dt
        next_pos = 0.054013315588235855 + player.speed_jump*next_time - (gravity*next_time**2)/2
        direction = Vec3(0,-1,0).normalized()
        origin = (player.world_x,player.world_y-0.2,player.world_z)
        middle_ray = raycast(origin , direction, distance=0.02, debug=True)
        if next_pos <= 0.056:
            if middle_ray.hit:
                player.world_y = 0
                player.jumping = False
                player.speed_jump = 0
                player.time_jumping = 0
            else:
                player.world_y += -player.speed_jump*time.dt - (10*gravity*time.dt**2)/2
        else:
            player.world_y = 0.054013315588235855 + player.speed_jump*player.time_jumping - (gravity*player.time_jumping**2)/2
        player.time_jumping =next_time

        if player.world_y < -2:
            player.jumping = False
            player.world_x= 0
            player.world_y= 0.054013315588235855
            player.world_z= 0
            camera.x = -8
            camera.y = 6
            camera.z = 0
        camera.look_at(player, axis='forward')

    #app.camera = Time_Travel_Camera()
    Sky(color=color.white)
    mouse.locked = True
    window.fullscreen = True 
    with open('data.json','r') as f:
        data = json.load(f) 
    distance = .35642
    for texture in data:
        objs = data[texture]
        for obj in objs:
            row = objs[obj]
            ground = Entity(model='models/block', scale=(.2,.2,.2), position = (row['x']*distance,row['y']-distance,row['z']*distance),
                texture = 'models/texture/'+texture, collider = 'box')
            ground.collider.visible = True

    camera.position = Vec3(-8,6,0)
    bridge = Entity(model='models/bridge_dest', scale=(2.5,1,1), position = (4,-.1,7),collider = 'box')
    bridge = Entity(model='models/bridge', scale=(2.5,1,1), position = (4,-.1,-193),collider = 'box')
    #migué
    for i in range(0,15):
        ground = Entity(model='models/block', scale=(.2,.2,.2), position = (1.44+i*.35641,-0.35641,-192.9),
                    texture = 'models/texture/'+texture, collider = 'box')
        ground.visible = False
        ground = Entity(model='models/block', scale=(.2,.2,.2), position = (1.44+i*.35641,-0.35641,-192.7),
                    texture = 'models/texture/'+texture, collider = 'box')
        ground.visible = False
    player = Player(model='hourglass', scale=(0.01,0.01,0.01), position = (0,0.054013315588235855,0), collider='box', color=color.gray.tint(-.2))
    player.collider.visible = False


    descr = dedent('''
      Movimentação
      w a s d para movimentação
      aperte q para voltar ao passado
      aperte e para avançar ao futuro''').strip()

    Text.default_resolution = 720 * Text.size
    #test = Text(origin=(.5,.5), text=descr)
    text = Text(text=descr, wordwrap=8, origin=(-.5,.5), y=.25, background=True)

    camera.look_at(player, axis='forward')

    app.run()
