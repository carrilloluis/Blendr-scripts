bl_info = {
	"name": "Semi capsule 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Semi capsule 2D (Top Half Shape) in front view of Blender",
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
DBL_SIZE = 2 * SIZE

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Semi-Capsule.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_semi_capsule = bpy.data.meshes.new(name + '.mesh')
object_semi_capsule = bpy.data.objects.new(name, mesh_semi_capsule)

vertex_leaf = [
	(origin.x - SIZE, origin.y, origin.z + DBL_SIZE), # P0
	(origin.x + SIZE, origin.y, origin.z + DBL_SIZE), # P1
	(origin.x + DBL_SIZE, origin.y, origin.z + SIZE), # P2
	(origin.x + DBL_SIZE, origin.y, origin.z - DBL_SIZE), # P3
	(origin.x + SIZE, origin.y, origin.z - DBL_SIZE), # P4
	(origin.x - SIZE, origin.y, origin.z - DBL_SIZE), # P5
	(origin.x - DBL_SIZE, origin.y, origin.z - DBL_SIZE), # P6
	(origin.x - DBL_SIZE, origin.y, origin.z + SIZE), # P7
	(origin.x - SIZE, origin.y, origin.z), # P8
	(origin.x + SIZE, origin.y, origin.z)  # P9
]

edges_leaf = [
	(0, 1), (1, 2), (2, 3), (3, 4), 
	(4, 5), (5, 6), (6, 7), (7, 0),
	(7, 8), (8, 9), (5, 8), (4, 9)
]

faces_leaf = [
	(0, 7, 2, 1), (2, 9, 4, 3), (9, 8, 5, 4),
	(8, 7, 6, 5), (2, 7, 8, 9)
]
mesh_semi_capsule.from_pydata(vertex_leaf, edges_leaf, faces_leaf)

object_semi_capsule.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_semi_capsule.update(calc_edges=True)
mesh_semi_capsule.update()

bpy.context.scene.collection.objects.link(object_semi_capsule)