bl_info = {
	"name": "Octagon 3D as Roof/Ceiling/vault",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Octagon 3D (mix Quads et Triangles)",
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
HALF_SIZE = SIZE / 2
LENGTH_ = SIZE + HALF_SIZE

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Octagon_Roof' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_roof = bpy.data.meshes.new(name + '.mesh')
object_roof = bpy.data.objects.new(name, mesh_roof)

vertex_roof = [
	(origin.x - HALF_SIZE, origin.y, origin.z + HALF_SIZE), # P0
	(origin.x + HALF_SIZE, origin.y, origin.z + HALF_SIZE), # P1
	(origin.x + HALF_SIZE, origin.y, origin.z - HALF_SIZE), # P2
	(origin.x - HALF_SIZE, origin.y, origin.z - HALF_SIZE), # P3

	(origin.x - LENGTH_, origin.y - SIZE, origin.z - HALF_SIZE), # P4
	(origin.x - LENGTH_, origin.y - SIZE, origin.z + HALF_SIZE), # P5

	(origin.x - HALF_SIZE, origin.y - SIZE, origin.z + LENGTH_), # P6
	(origin.x + HALF_SIZE, origin.y - SIZE, origin.z + LENGTH_), # P7

	(origin.x + LENGTH_, origin.y - SIZE, origin.z + HALF_SIZE), # P8
	(origin.x + LENGTH_, origin.y - SIZE, origin.z - HALF_SIZE), # P9

	(origin.x + HALF_SIZE, origin.y - SIZE, origin.z - LENGTH_), # P10
	(origin.x - HALF_SIZE, origin.y - SIZE, origin.z - LENGTH_), # P11
]

edges_roof = [
	(0, 1), (1, 2), (2, 3), (3, 0),
	(4, 5), (5, 6), (6, 7), (7, 8),
	(8, 9), (9, 10), (10, 11), (11, 4),
	(3, 4), (0, 5), (0, 6), (1, 7),
	(1, 8), (2, 9), (2, 10), (3, 11)
]

faces_roof = [
	(0, 1, 2, 3), (5, 4, 3, 0), (11, 10, 2, 3),
	(9, 8, 1, 2), (7, 6, 0, 1), (5, 0, 6, 5),
	(4, 11, 3, 4), (10, 9, 2, 10), (7, 1, 8, 7)
]
mesh_roof.from_pydata(vertex_roof, edges_roof, faces_roof)

object_roof.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_roof.update(calc_edges=True)
mesh_roof.update()

bpy.context.scene.collection.objects.link(object_roof)