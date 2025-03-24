bl_info = {
	"name": "Basic Leaf",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "",
	"warning": "Use under ur own risk!!",
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
origin_location = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Basic-Leaf.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_leaf = bpy.data.meshes.new(name + '.mesh')
object_leaf = bpy.data.objects.new(name, mesh_leaf)

vertex_leaf = [
	(origin_location.x, origin_location.y, origin_location.z  + (SIZE + HALF_SIZE)), # P0
	(origin_location.x + HALF_SIZE, origin_location.y, origin_location.z + SIZE),   # P1
	(origin_location.x + SIZE, origin_location.y, origin_location.z),  # P2
	(origin_location.x + HALF_SIZE, origin_location.y, origin_location.z - SIZE),   # P3
	(origin_location.x, origin_location.y, origin_location.z - (SIZE + HALF_SIZE)), # P4
	(origin_location.x - HALF_SIZE, origin_location.y, origin_location.z - SIZE),   # P5
	(origin_location.x - SIZE, origin_location.y, origin_location.z),  # P6
	(origin_location.x - HALF_SIZE, origin_location.y, origin_location.z + SIZE),   # P7
	(origin_location.x, origin_location.y, origin_location.z  + HALF_SIZE),  # P8
	(origin_location.x, origin_location.y, origin_location.z), # P9
	(origin_location.x, origin_location.y, origin_location.z - HALF_SIZE)  # P10
]

edges_leaf = [
	(0, 1), (1, 2), (2, 3), (3, 4), 
	(4, 5), (5, 6), (6, 7), (7, 0),
	(7, 0), (7, 8), (1, 8), (6, 9),
	(9, 2), (5, 10), (10, 3)
]

faces_leaf = [
	(0, 7, 8, 1), (7, 6, 9, 8), (8, 9, 2, 1),
	(6, 5, 10, 9), (9, 10, 3, 2), (10, 5, 4, 3)
]
mesh_leaf.from_pydata(vertex_leaf, edges_leaf, faces_leaf)

object_leaf.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_leaf.update(calc_edges=True)
mesh_leaf.update()

bpy.context.scene.collection.objects.link(object_leaf)