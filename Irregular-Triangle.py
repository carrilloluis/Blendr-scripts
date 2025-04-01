bl_info = {
	"name": "Irregular Triangle 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Irregular Triangle 2D (with obtuse angle) with quads onto Front View",
	"warning": "Use under ur own risk!!",
	"category": "Scripting"
}

import bpy
from random import randint
from mathutils import Vector

# Deselect any object
bpy.ops.object.select_all(action='DESELECT')

# Dimensions like constants
SIZE = 1.0
HALF_SIZE = SIZE / 2

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Irregular-Triangle.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_itriangle = bpy.data.meshes.new(name + '.mesh')
object_itriangle = bpy.data.objects.new(name, mesh_itriangle)

vertex_itriangle = [
	(origin.x - (2 * SIZE), origin.y, origin.z + (2 * SIZE)), # P0
	(origin.x, origin.y, origin.z + ((5 ** .5) - 2)), # P1
	(origin.x + (SIZE + HALF_SIZE), origin.y, origin.z - SIZE), # P2
	(origin.x + HALF_SIZE, origin.y, origin.z - SIZE), # P3
	(origin.x - HALF_SIZE, origin.y, origin.z - SIZE), # P4
	(origin.x - SIZE, origin.y, origin.z), # P5
	(origin.x, origin.y, origin.z) # P6
]

edges_itriangle = [
	(0, 1), (1, 2), (2, 3), (3, 4),
	(4, 5), (5, 0), (5, 6), (1, 6), (3, 6)
]

faces_itriangle = [
	(0, 5, 6, 1), (5, 4, 3, 6), (1, 6, 3, 2)
]
mesh_itriangle.from_pydata(vertex_itriangle, edges_itriangle, faces_itriangle)

object_itriangle.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_itriangle.update(calc_edges=True)
mesh_itriangle.update()

bpy.context.scene.collection.objects.link(object_itriangle)
