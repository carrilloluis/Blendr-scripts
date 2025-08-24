bl_info = {
	"name": "Letter H",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Letter H 2D onto Front View",
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

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Letter-H.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_letter_h = bpy.data.meshes.new(name + '.mesh')
object_letter_h = bpy.data.objects.new(name, mesh_letter_h)

vertex_letter_h = [
	(origin.x - SIZE, origin.y, origin.z + .5), # P0
	(origin.x + SIZE, origin.y, origin.z + .5), # P1
	(origin.x - DBL_SIZE, origin.y, origin.z), # P2
	(origin.x + DBL_SIZE, origin.y, origin.z), # P3
	(origin.x - SIZE, origin.y, origin.z - .5), # P4
	(origin.x + SIZE, origin.y, origin.z - .5), # P5
	(origin.x - DBL_SIZE, origin.y, origin.z + DBL_SIZE), # P6
	(origin.x - SIZE, origin.y, origin.z + DBL_SIZE), # P7
	(origin.x + SIZE, origin.y, origin.z + DBL_SIZE), # P8
	(origin.x + DBL_SIZE, origin.y, origin.z + DBL_SIZE), # P9
	(origin.x - DBL_SIZE, origin.y, origin.z - DBL_SIZE), # P10
	(origin.x - SIZE, origin.y, origin.z - DBL_SIZE), # P11
	(origin.x + SIZE, origin.y, origin.z - DBL_SIZE), # P12
	(origin.x + DBL_SIZE, origin.y, origin.z - DBL_SIZE) # P13
]

edges_letter_h = [
	(0, 1), (1, 3), (3, 5), (5, 4),
	(4, 2), (2, 0), (2, 3), (2, 10), 
	(10, 11), (11, 4), (5, 12), (12, 13),
	(13, 3), (2, 6), (6, 7), (7, 0),
	(1, 8), (8, 9), (9, 3)
]

faces_letter_h = [
	(2, 0, 7, 6), 
	(1, 3, 9, 8),
	(2, 3, 1, 0),
	(10, 11, 4, 2),
	(4, 5, 3, 2),
	(12, 13, 3, 5)
]
mesh_letter_h.from_pydata(vertex_letter_h, edges_letter_h, faces_letter_h)

object_letter_h.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_letter_h.update(calc_edges=True)
mesh_letter_h.update()

bpy.context.scene.collection.objects.link(object_letter_h)
