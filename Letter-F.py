bl_info = {
	"name": "Shape simulating the Letter F with quads",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 1),
	"blender": (4, 2, 7),
	"description": "Letter F on Front View",
	"warning": "Use under ur own risk!",
	"category": "Scripting"
}

import bpy
from random import randint
from mathutils import Vector

# Deselect any object 
bpy.ops.object.select_all(action='DESELECT')

# Dimensions like constants 
SIZE = 1.0

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Letter-F.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_letter_f = bpy.data.meshes.new(name + '.mesh')
object_letter_f = bpy.data.objects.new(name, mesh_letter_f)

vertex_letter_f = [
	(origin.x - SIZE, origin.y, origin.z + (2 * SIZE)), # P0
	(origin.x, origin.y, origin.z + (2 * SIZE)), # P1
	(origin.x, origin.y, origin.z + SIZE), # P2
	(origin.x + SIZE, origin.y, origin.z + SIZE), # P3
	(origin.x - SIZE, origin.y, origin.z - SIZE), # P4
	(origin.x, origin.y, origin.z), # P5
	(origin.x, origin.y, origin.z - SIZE), # P6
	(origin.x + SIZE, origin.y, origin.z), # P7
	(origin.x - SIZE, origin.y, origin.z - (3 * SIZE)), # P8
	(origin.x, origin.y, origin.z - (2 * SIZE)) # P9
]

edges_letter_f = [
	(0, 1), (1, 3), (3, 2),
	(2, 0), (0, 4), (4, 5),
	(5, 7), (7, 6), (6, 4),
	(4, 8), (8, 9), (9, 6)
]

faces_letter_f = [
	(2, 3, 1, 0), (4, 5, 2, 0),
	(6, 7, 5, 4), (8, 9, 6, 4)
]

mesh_letter_f.from_pydata(vertex_letter_f, edges_letter_f, faces_letter_f)

object_letter_f.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_letter_f.update(calc_edges=True)
mesh_letter_f.update()

bpy.context.scene.collection.objects.link(object_letter_f)