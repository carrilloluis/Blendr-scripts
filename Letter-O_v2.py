bl_info = {
	"name": "Letter O (Ring) on 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 2),
	"blender": (4, 2, 7),
	"description": "Letter O (Ring) onto Front View",
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
DBL_SIZE = 2 * SIZE

# Set the reference POINT to build mesh
center = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Letter-O.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_letter_o = bpy.data.meshes.new(name + '.mesh')
object_letter_o = bpy.data.objects.new(name, mesh_letter_o)

vertex_letter_o = [
	(center.x - SIZE, center.y, center.z + DBL_SIZE), # P0
	(center.x + SIZE, center.y, center.z + DBL_SIZE), # P1
	(center.x + DBL_SIZE, center.y, center.z + SIZE), # P2
	(center.x + DBL_SIZE, center.y, center.z - SIZE), # P3
	(center.x + SIZE, center.y, center.z - DBL_SIZE), # P4
	(center.x - SIZE, center.y, center.z - DBL_SIZE), # P5
	(center.x - DBL_SIZE, center.y, center.z - SIZE), # P6
	(center.x - DBL_SIZE, center.y, center.z + SIZE), # P7
	
	(center.x - HALF_SIZE, center.y, center.z + SIZE), # P8
	(center.x + HALF_SIZE, center.y, center.z + SIZE), # P9 
	(center.x + SIZE, center.y, center.z + HALF_SIZE), # P10 
	(center.x + SIZE, center.y, center.z - HALF_SIZE), # P11 
	(center.x + HALF_SIZE, center.y, center.z - SIZE), # P12 
	(center.x - HALF_SIZE, center.y, center.z - SIZE), # P13
	(center.x - SIZE, center.y, center.z - HALF_SIZE), # P14
	(center.x - SIZE, center.y, center.z + HALF_SIZE) # P15
]

edges_letter_o = [
	(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 0),
	(8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 8),
	(0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15)
]

faces_letter_o = [
	(0, 7, 15, 8), (1, 0, 8, 9), (1, 9, 10, 2), (2, 10, 11, 3),
	(15, 7, 6, 14), (14, 6, 5, 13), (12, 13, 5, 4), (3, 11, 12, 4)
]
mesh_letter_o.from_pydata(vertex_letter_o, [], faces_letter_o)

object_letter_o.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_letter_o.update(calc_edges=True)
# mesh_letter_o.update()

bpy.context.scene.collection.objects.link(object_letter_o)
