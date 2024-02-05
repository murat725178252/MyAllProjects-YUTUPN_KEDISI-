from ursina import *
from ursina.shaders import *

app = Ursina()
EditorCamera()
Entity(model='plane', scale=10, color=color.gray, 
shader=basic_lighting_shader)
Entity(model='cube', y=1, shader=basic_lighting_shader)
pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45))

app.run()