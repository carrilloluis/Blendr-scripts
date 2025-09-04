bl_info = {
	"name": "Arrow 2D v3",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Arrow 2D v3 onto Front View",
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
TRI_SIZE = 3 * SIZE

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Arrow.v3.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_arrow_v3 = bpy.data.meshes.new(name + '.mesh')
object_arrow_v3 = bpy.data.objects.new(name, mesh_arrow_v3)

vertex_arrow_v3 = [
	(origin.x - SIZE, origin.y, origin.z - SIZE), # P0
	(origin.x - SIZE, origin.y, origin.z + SIZE), # P1
	(origin.x - SIZE, origin.y, origin.z + DBL_SIZE), # P2
	(origin.x, origin.y, origin.z + DBL_SIZE), # P3
	(origin.x, origin.y, origin.z + SIZE), # P4
	(origin.x + DBL_SIZE, origin.y, origin.z + TRI_SIZE), # P5
	(origin.x + (DBL_SIZE + .5), origin.y, origin.z + (TRI_SIZE - .5)), # P6
	(origin.x + (SIZE - .5), origin.y, origin.z + (SIZE - .5)), # P7
	(origin.x + SIZE, origin.y, origin.z), # P8
	(origin.x + TRI_SIZE, origin.y, origin.z + DBL_SIZE), # P9
	(origin.x + DBL_SIZE, origin.y, origin.z), # P10
	(origin.x + DBL_SIZE, origin.y, origin.z - SIZE), # P11
	(origin.x + SIZE, origin.y, origin.z - SIZE)  # P12
]

edges_arrow_v3 = [
	(0, 1), (1, 2), (2, 3), (3, 4),
	(4, 5), (5, 6), (6, 7), (7, 8),
	(8, 9), (8, 10), (10, 11), (11, 12),
	(12, 0), (8, 12), (4, 7)
]

faces_arrow_v3 = [
	(1, 4, 3, 2), (0, 7, 4, 1),
	(0, 12, 8, 7), (12, 11, 10, 8),
	(7, 6, 5, 4), (8, 9, 6, 7)
]
mesh_arrow_v3.from_pydata(vertex_arrow_v3, edges_arrow_v3, faces_arrow_v3)

object_arrow_v3.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_arrow_v3.update(calc_edges=True)
mesh_arrow_v3.update()

bpy.context.scene.collection.objects.link(object_arrow_v3)
