bl_info = {
	"name": "Star 2D w/ 8 points",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Star 2D with 8 points onto Front View",
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
# DBL_SIZE = 2 * SIZE

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Star-8p.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_star8p = bpy.data.meshes.new(name + '.mesh')
object_star8p = bpy.data.objects.new(name, mesh_star8p)

vertex_star8p = [
	(origin.x, origin.y, origin.z), # P0

	(origin.x, origin.y, origin.z + LENGTH_), # P1
	(origin.x + HALF_SIZE, origin.y, origin.z + SIZE), # P2
	(origin.x + SIZE, origin.y, origin.z + SIZE), # P3

	(origin.x + SIZE, origin.y, origin.z + HALF_SIZE), # P4
	(origin.x + LENGTH_, origin.y, origin.z), # P5
	(origin.x + SIZE, origin.y, origin.z - HALF_SIZE), # P6

	(origin.x + SIZE, origin.y, origin.z - SIZE), # P7
	(origin.x + HALF_SIZE, origin.y, origin.z - SIZE), # P8
	(origin.x, origin.y, origin.z - LENGTH_), # P9

	(origin.x - HALF_SIZE, origin.y, origin.z - SIZE), # P10
	(origin.x - SIZE, origin.y, origin.z - SIZE), # P11
	(origin.x - SIZE, origin.y, origin.z - HALF_SIZE), # P12

	(origin.x - LENGTH_, origin.y, origin.z), # P13
	(origin.x - SIZE, origin.y, origin.z + HALF_SIZE), # P14
	(origin.x - SIZE, origin.y, origin.z + SIZE),  # P15

	(origin.x - HALF_SIZE, origin.y, origin.z + SIZE)  # P16
]

edges_star8p = [
	(0, 1), (1, 2), (2, 3), (3, 0),
	(0, 3), (3, 4), (4, 5), (5, 0),
	(0, 5), (5, 6), (6, 7), (7, 0),
	(0, 7), (7, 8), (8, 9), (9, 0),
	(9, 0), (9, 10), (10, 11), (11, 0),
	(11, 0), (11, 12), (12, 13), (13, 0),
	(13, 0), (13, 14), (14, 15), (15, 0)
]

faces_star8p = [
	(0, 1, 2, 3), (0, 3, 4, 5),
	(0, 5, 6, 7), (0, 7, 8, 9),
	(0, 9, 10, 11), (0, 11, 12, 13),
	(0, 13, 14, 15), (0, 15, 16, 1)
]
mesh_star8p.from_pydata(vertex_star8p, edges_star8p, faces_star8p)

object_star8p.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_star8p.update(calc_edges=True)
mesh_star8p.update()

bpy.context.scene.collection.objects.link(object_star8p)