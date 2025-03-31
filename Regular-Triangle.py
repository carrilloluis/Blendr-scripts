bl_info = {
	"name": "Regular Triangle 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Regular Triangle 2D with quads onto Front View",
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
SQR_3 = 3 ** .5

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Arrow.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_triangle = bpy.data.meshes.new(name + '.mesh')
object_triangle = bpy.data.objects.new(name, mesh_triangle)

vertex_triangle = [
	(origin.x, origin.y, origin.z + SQR_3), # P0
	(origin.x + SIZE, origin.y, origin.z + ((SQR_3 - SIZE) / 2)), # P1
	(origin.x + DBL_SIZE, origin.y, origin.z - SIZE), # P2
	(origin.x, origin.y, origin.z - SIZE), # P3
	(origin.x - DBL_SIZE, origin.y, origin.z - SIZE), # P4
	(origin.x - SIZE, origin.y, origin.z + ((SQR_3 - SIZE) / 2)), # P5
	(origin.x, origin.y, origin.z) # P6
]

edges_triangle = [
	(0, 1), (1, 2), (2, 3), (3, 4),
	(4, 5), (5, 0), (5, 6), (1, 6)
]

faces_triangle = [
	(0, 5, 6, 1), (5, 4, 3, 6), (1, 6, 3, 2)
]
mesh_triangle.from_pydata(vertex_triangle, edges_triangle, faces_triangle)

object_triangle.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_triangle.update(calc_edges=True)
mesh_triangle.update()

bpy.context.scene.collection.objects.link(object_triangle)
