bl_info = {
	"name": "BaseBone 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "BaseBone 2D on Front View",
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
name = 'BaseBone.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_bbone = bpy.data.meshes.new(name + '.mesh')
object_bbone = bpy.data.objects.new(name, mesh_bbone)

vertex_bbone = [
	(origin.x - DBL_SIZE, origin.y, origin.z), # P0
	(origin.x - SIZE, origin.y, origin.z), # P1
	(origin.x, origin.y, origin.z + SIZE), # P2
	(origin.x, origin.y, origin.z + DBL_SIZE), # P3
	(origin.x - DBL_SIZE, origin.y, origin.z - DBL_SIZE), # P4
	(origin.x - SIZE, origin.y, origin.z - SIZE), # P5
	(origin.x + SIZE, origin.y, origin.z + SIZE), # P6
	(origin.x + DBL_SIZE, origin.y, origin.z + DBL_SIZE), # P7
	(origin.x, origin.y, origin.z - DBL_SIZE), # P8
	(origin.x, origin.y, origin.z - SIZE), # P9
	(origin.x + SIZE, origin.y, origin.z), # P10
	(origin.x + DBL_SIZE, origin.y, origin.z) # P11
]

edges_bbone = [
	(4, 0), (0, 1), (1, 2), (2, 3), (3, 7),
	(5, 1), (5, 9), (2, 6), (10, 6), (4, 8),
	(8, 9), (9, 10), (10, 11), (11, 7)
]

faces_bbone = [
	(4, 5, 1, 0), (5, 6, 2, 1),
	(6, 7, 3, 2), (4, 8, 9, 5),
	(9, 10, 6, 5), (10, 11, 7, 6)
]
mesh_bbone.from_pydata(vertex_bbone, edges_bbone, faces_bbone)

object_bbone.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_bbone.update(calc_edges=True)
mesh_bbone.update()

bpy.context.scene.collection.objects.link(object_bbone)
