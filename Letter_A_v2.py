bl_info = {
	"name": "Letter A v.2",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Letter 2D v.2 onto Front View",
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
REDUCE = 0.5

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
	(origin.x + DBL_SIZE, origin.y, origin.z + DBL_SIZE), # P1
	(origin.x + SIZE, origin.y, origin.z + SIZE), # P2
	(origin.x - SIZE, origin.y, origin.z + SIZE), # P3

	(origin.x - SIZE, origin.y, origin.z + REDUCE), # P4
	(origin.x + SIZE, origin.y, origin.z + REDUCE), # P5
	(origin.x + DBL_SIZE, origin.y, origin.z), # P6
	(origin.x - DBL_SIZE, origin.y, origin.z), # P7

	(origin.x - DBL_SIZE, origin.y, origin.z - DBL_SIZE), # P8
	(origin.x - SIZE, origin.y, origin.z - DBL_SIZE), # P9
	(origin.x - SIZE, origin.y, origin.z - REDUCE), # P10
	(origin.x + SIZE, origin.y, origin.z - REDUCE), # P11

	(origin.x + SIZE, origin.y, origin.z - DBL_SIZE), # P12
	(origin.x + DBL_SIZE, origin.y, origin.z - DBL_SIZE) # P13
]

edges_letter_a = [
	(0, 1), (1, 2), (2, 3), (3, 4),
	(4, 5), (5, 6), (6, 7), (7, 8),
	(8, 9), (9, 10), (7, 10), (10, 11),
	(11, 6), (11, 12), (12, 13), (13, 6)
]

faces_letter_a = [
	(3, 2, 1, 0), (2, 5, 6, 1), (7, 4, 3, 0), (7, 6, 5, 4),
	(8, 9, 10, 7), (10, 11, 6, 7), (12, 13, 6, 11)
]
mesh_letter_a.from_pydata(vertex_letter_a, edges_letter_a, faces_letter_a)

object_letter_a.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_letter_a.update(calc_edges=True)
mesh_letter_a.update()

bpy.context.scene.collection.objects.link(object_letter_a)
