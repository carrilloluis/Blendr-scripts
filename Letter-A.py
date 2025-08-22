bl_info = {
	"name": "Letter A",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Letter 2D onto Front View",
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
DBL_SIZE = 2 * SIZE
REDUCE = 0.45

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Letter-A.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_letter_a = bpy.data.meshes.new(name + '.mesh')
object_letter_a = bpy.data.objects.new(name, mesh_letter_a)

vertex_letter_a = [
	(origin.x - DBL_SIZE, origin.y, origin.z + DBL_SIZE), # P0
	(origin.x - .05, origin.y, origin.z + DBL_SIZE), # P1
	(origin.x + REDUCE, origin.y, origin.z + SIZE), # P2
	(origin.x + DBL_SIZE, origin.y, origin.z - DBL_SIZE), # P3
	(origin.x + (SIZE - REDUCE), origin.y, origin.z - DBL_SIZE), # P4
	(origin.x - SIZE, origin.y, origin.z + SIZE), # P5
	(origin.x - SIZE, origin.y, origin.z - DBL_SIZE), # P6
	(origin.x - DBL_SIZE, origin.y, origin.z - DBL_SIZE) # P7
] # (origin.x, origin.y, origin.z) # P8

edges_letter_a = [
	(0, 1), (1, 2), (2, 3), (3, 4),
	(4, 5), (5, 2), (5, 6), (6, 7), (7, 0)
]

faces_letter_a = [
	(5, 2, 1, 0), (4, 3, 2, 5), (7, 6, 5, 0)
]
mesh_letter_a.from_pydata(vertex_letter_a, edges_letter_a, faces_letter_a)

object_letter_a.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_letter_a.update(calc_edges=True)
mesh_letter_a.update()

bpy.context.scene.collection.objects.link(object_letter_a)
