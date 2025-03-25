bl_info = {
	"name": "Shape simulating the Letter T with quads",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 1),
	"blender": (4, 2, 7),
	"description": "",
	"warning": "Use under ur own risk!",
	"category": "Scripting"
}

import bpy
from random import randint
from mathutils import Vector

# Deselect any object 
bpy.ops.object.select_all(action='DESELECT')

# Dimensions like constants 
ONE_THIRD_SIZE = .5 
SIZE = (3 * ONE_THIRD_SIZE)

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Letter-T.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_letter_t = bpy.data.meshes.new(name + '.mesh')
object_letter_t = bpy.data.objects.new(name, mesh_letter_t)

vertex_letter_t = [
	(origin.x, origin.y, origin.z + SIZE),  # P0
	(origin.x + SIZE, origin.y, origin.z + SIZE),   # P1
	(origin.x + SIZE, origin.y, origin.z + ONE_THIRD_SIZE),  # P2
	(origin.x + ONE_THIRD_SIZE, origin.y, origin.z + ONE_THIRD_SIZE), # P3
	(origin.x + ONE_THIRD_SIZE, origin.y, origin.z - SIZE),  # P4
	(origin.x, origin.y, origin.z - SIZE),  # P5
	(origin.x - ONE_THIRD_SIZE, origin.y, origin.z - SIZE),  # P6
	(origin.x - ONE_THIRD_SIZE, origin.y, origin.z + ONE_THIRD_SIZE),  # P7
	(origin.x - SIZE, origin.y, origin.z + ONE_THIRD_SIZE),  # P8
	(origin.x - SIZE, origin.y, origin.z + SIZE),  # P9
]

edges_letter_t = [
	(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), 
	(7, 8), (8, 9), (9, 0), (5, 0), (0, 7), (0, 3)
]

faces_letter_t = [
	(0, 3, 2, 1), (0, 9, 8, 7),
	(0, 7, 6, 5), (0, 5, 4, 3)
]

mesh_letter_t.from_pydata(vertex_letter_t, edges_letter_t, faces_letter_t)

object_letter_t.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_letter_t.update(calc_edges=True)
mesh_letter_t.update()

bpy.context.scene.collection.objects.link(object_letter_t)