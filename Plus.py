bl_info = {
	"name": "Simulating Plus/Cross Shape Plane 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Plus Plane 2D onto Front View",
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
TRI_SIZE = 3 * 1.0

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'PlusShape.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_plus = bpy.data.meshes.new(name + '.mesh')
object_plus = bpy.data.objects.new(name, mesh_plus)

vertex_plus = [
	(origin.x, origin.y, origin.z), # P0
	(origin.x - SIZE, origin.y, origin.z + SIZE), # P1
	(origin.x - SIZE, origin.y, origin.z + TRI_SIZE), # P2
	(origin.x, origin.y, origin.z + TRI_SIZE), # P3
	(origin.x + SIZE, origin.y, origin.z + TRI_SIZE), # P4
	(origin.x + SIZE, origin.y, origin.z + SIZE), # P5
	
	(origin.x + TRI_SIZE, origin.y, origin.z + SIZE), # P6
	(origin.x + TRI_SIZE, origin.y, origin.z), # P7
	(origin.x + TRI_SIZE, origin.y, origin.z - SIZE), # P8
	(origin.x + SIZE, origin.y, origin.z - SIZE), # P9
	
	(origin.x + SIZE, origin.y, origin.z - TRI_SIZE), # P10
	(origin.x, origin.y, origin.z - TRI_SIZE), # P11
	(origin.x - SIZE, origin.y, origin.z - TRI_SIZE), # P12
	
	(origin.x - SIZE, origin.y, origin.z - SIZE), # P13
	(origin.x - TRI_SIZE, origin.y, origin.z - SIZE), # P14
	(origin.x - TRI_SIZE, origin.y, origin.z), # P15
	(origin.x - TRI_SIZE, origin.y, origin.z + SIZE)  # P16
]

edges_plus = [
	(0, 1), (1, 2), (2, 3), (3, 0), 
	(0, 5), (4, 5), (3, 4), (5, 6), 
	(6, 7), (7, 8), (7, 0), (8, 9), 
	(9, 0), (9, 10), (10, 11), (11, 0),
	(11, 12), (12, 13), (13, 0), (15, 0),
	(13, 14), (14, 15), (15, 16), (16, 1)
]

faces_plus = [
	(1, 0, 3, 2), (0, 5, 4, 3), 
	(5, 0, 7, 6), (0, 9, 8, 7),
	(9, 0, 11, 10), (0, 13, 12, 11),
	(13, 0, 15, 14), (0, 1, 16, 15)
]
mesh_plus.from_pydata(vertex_plus, edges_plus, faces_plus)

object_plus.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_plus.update(calc_edges=True)
mesh_plus.update()

bpy.context.scene.collection.objects.link(object_plus)