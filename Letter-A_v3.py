bl_info = {
	"name": "Letter A v.3",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Letter 2D v.3 onto Front View",
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
TRI_SIZE = 3 * SIZE

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Letter-A.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_letter_a = bpy.data.meshes.new(name + '.mesh')
object_letter_a = bpy.data.objects.new(name, mesh_letter_a)

vertex_letter_a = [
	(origin.x - DBL_SIZE, origin.y, origin.z + SIZE), # P0
	(origin.x, origin.y, origin.z + TRI_SIZE), # P1
	(origin.x, origin.y, origin.z + (DBL_SIZE - .25)), # P2
	(origin.x + DBL_SIZE, origin.y, origin.z + SIZE), # P3

	(origin.x - DBL_SIZE, origin.y, origin.z - DBL_SIZE), # P4
	(origin.x - SIZE, origin.y, origin.z - DBL_SIZE), # P5
	(origin.x + SIZE, origin.y, origin.z - DBL_SIZE), # P6
	(origin.x + DBL_SIZE, origin.y, origin.z - DBL_SIZE), # P7
	
	(origin.x - SIZE, origin.y, origin.z + (SIZE - .25)), # P8
	(origin.x + SIZE, origin.y, origin.z + (SIZE - .25)), # P9
	
	(origin.x - (SIZE - .25), origin.y, origin.z), # P10
	(origin.x + (SIZE - .25), origin.y, origin.z), # P11
	(origin.x + (SIZE - .25), origin.y, origin.z - SIZE), # P12
	(origin.x - (SIZE - .25), origin.y, origin.z - SIZE) # P13
]

edges_letter_a = [
	(0, 1), (1, 3), (3, 9), (9, 2), (2, 8), (0, 8),
	(2, 1), (0, 4), (4, 5), (5, 8), (9, 6), (6, 7), 
	(7, 3), (10, 11), (11, 12), (12, 13), (13, 10)
]

faces_letter_a = [
	(4, 5, 8, 0), 
	(0, 8, 2, 1), 
	(9, 3, 1, 2),
	(6, 7, 3, 9),
	(13, 12, 11, 10)
]
mesh_letter_a.from_pydata(vertex_letter_a, edges_letter_a, faces_letter_a)

object_letter_a.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_letter_a.update(calc_edges=True)
mesh_letter_a.update()

bpy.context.scene.collection.objects.link(object_letter_a)