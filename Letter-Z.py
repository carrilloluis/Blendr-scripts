bl_info = {
	"name": "Shape simulating the Letter Z with quads",
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
SIZE = 2.0
HALF_SIZE = SIZE / 2

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Letter-Z.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_letter_z = bpy.data.meshes.new(name + '.mesh')
object_letter_z = bpy.data.objects.new(name, mesh_letter_z)

vertex_letter_z = [
	(origin.x - SIZE, origin.y, origin.z + SIZE),  # P0
	(origin.x + HALF_SIZE, origin.y, origin.z + SIZE),   # P1
	(origin.x + SIZE, origin.y, origin.z + SIZE),  # P2
	
	(origin.x + SIZE, origin.y, origin.z + HALF_SIZE), # P3
	(origin.x, origin.y, origin.z - HALF_SIZE),  # P4
	(origin.x + SIZE, origin.y, origin.z - HALF_SIZE),  # P5
	
	(origin.x + SIZE, origin.y, origin.z - SIZE),  # P6
	(origin.x - HALF_SIZE, origin.y, origin.z - SIZE),  # P7
	(origin.x - SIZE, origin.y, origin.z - SIZE),  # P8
	
	(origin.x - SIZE, origin.y, origin.z - HALF_SIZE),  # P9
	(origin.x, origin.y, origin.z + HALF_SIZE),  # P10
	(origin.x - SIZE, origin.y, origin.z + HALF_SIZE),  # P11
	
	(origin.x, origin.y, origin.z) # 12
]

edges_letter_z = [
	(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
	(6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 0),
	(10, 12), (4, 12), (1, 10), (4, 7)
]

faces_letter_z = [
	(0, 11, 10, 1), (1, 10, 12, 2),
	(2, 12, 4, 3), (10, 9, 8, 12),
	(12, 8, 7, 4), (4, 7, 6, 5)
]

mesh_letter_z.from_pydata(vertex_letter_z, edges_letter_z, faces_letter_z)

object_letter_z.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_letter_z.update(calc_edges=True)
mesh_letter_z.update()

bpy.context.scene.collection.objects.link(object_letter_z)