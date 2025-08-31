bl_info = {
	"name": "Shape simulating the Letter V with quads",
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
SIZE = 1.0

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Letter-V.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_letter_v = bpy.data.meshes.new(name + '.mesh')
object_letter_v = bpy.data.objects.new(name, mesh_letter_v)

vertex_letter_v = [
	(origin.x - SIZE, origin.y, origin.z), # P0
	(origin.x - SIZE, origin.y, origin.z + (4 * SIZE)), # P1
	(origin.x, origin.y, origin.z + (4 * SIZE)), # P2
	(origin.x, origin.y, origin.z + SIZE), # P3
	(origin.x + SIZE, origin.y, origin.z  + SIZE), # P4
	(origin.x + (3 * SIZE), origin.y, origin.z + (4 * SIZE)), # P5
	(origin.x + (4 * SIZE), origin.y, origin.z + (4 * SIZE)), # P6
	(origin.x + (3 * (SIZE / 2)), origin.y, origin.z) # P7
]

edges_letter_v = [
	(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
	(6, 7), (7, 0), (0, 3), (4, 7)
]

faces_letter_v = [
	(0, 3, 2, 1), (0, 7, 4, 3), (7, 6, 5, 4)
]

mesh_letter_v.from_pydata(vertex_letter_v, edges_letter_v, faces_letter_v)

object_letter_v.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_letter_v.update(calc_edges=True)
mesh_letter_v.update()

bpy.context.scene.collection.objects.link(object_letter_v)