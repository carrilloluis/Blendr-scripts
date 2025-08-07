bl_info = {
	"name": "Octagon Vault v2.0",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Octagon Vault",
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
FIFTH_HALF_SIZE = (2 * SIZE) + (HALF_SIZE / 2)

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'OctagonVault.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_octagon = bpy.data.meshes.new(name + '.mesh')
object_octagon = bpy.data.objects.new(name, mesh_octagon)

vertex_octagon = [
	(origin.x, origin.y - HALF_SIZE, origin.z), # P0
	(origin.x, origin.y, origin.z + LENGTH_), # P1
	(origin.x + SIZE, origin.y, origin.z + SIZE), # P2
	(origin.x + LENGTH_, origin.y, origin.z), # P3
	(origin.x + SIZE, origin.y, origin.z - SIZE), # P4
	(origin.x, origin.y, origin.z - LENGTH_), # P5
	(origin.x - SIZE, origin.y, origin.z - SIZE), # P6
	(origin.x - LENGTH_, origin.y, origin.z), # P7
	(origin.x - SIZE, origin.y, origin.z + SIZE), # P8
	(origin.x, origin.y + HALF_SIZE, origin.z + FIFTH_HALF_SIZE), # P9
	(origin.x + LENGTH_, origin.y + HALF_SIZE, origin.z + LENGTH_), # P10
	(origin.x + FIFTH_HALF_SIZE, origin.y + HALF_SIZE, origin.z), # P11
	(origin.x + LENGTH_, origin.y + HALF_SIZE, origin.z - LENGTH_), # P12
	(origin.x, origin.y + HALF_SIZE, origin.z - FIFTH_HALF_SIZE), # P13
	(origin.x - LENGTH_, origin.y + HALF_SIZE, origin.z - LENGTH_), # P14
	(origin.x - FIFTH_HALF_SIZE, origin.y + HALF_SIZE, origin.z), # P15
	(origin.x - LENGTH_, origin.y + HALF_SIZE, origin.z + LENGTH_) # P16
]

edges_octagon = [
	(0, 1), (1, 2), (2, 3), (3, 0),
	(3, 4), (4, 5), (5, 0), (5, 6),
	(6, 7), (7, 0), (7, 8), (8, 1),
	
	(1, 9), (9, 10), (2, 10), (10, 11),
	(3, 11), (11, 12), (4, 12), (12, 13),
	(5, 13), (13, 14), (6, 14), (14, 15),
	(7, 15), (15, 16), (8, 16), (16, 9)
]

faces_octagon = [
	(0, 3, 2, 1), (5, 4, 3, 0),
	(6, 5, 0, 7), (7, 0, 1, 8),
	(1, 2, 10, 9), (2, 3, 11, 10),
	(3, 4, 12, 11), (4, 5, 13, 12),
	(5, 6, 14, 13), (6, 7, 15, 14),
	(7, 8, 16, 15), (8, 1, 9, 16)
]
mesh_octagon.from_pydata(vertex_octagon, edges_octagon, faces_octagon)

object_octagon.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_octagon.update(calc_edges=True)
mesh_octagon.update()

bpy.context.scene.collection.objects.link(object_octagon)
