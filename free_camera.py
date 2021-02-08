from ursina import *

if __name__ == '__main__':
    # window.vsync = False
    app = Ursina()
    Sky(color=color.white)
    ground = Entity(model='terrain', scale=(0.1,.1,.1), texture_scale=(100,100), collider='box')
    #print(dir(ground))
    EditorCamera()
    app.run()
