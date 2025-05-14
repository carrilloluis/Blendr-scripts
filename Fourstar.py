bl_info = {
	"name": "Fourstar 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Fourstar 2D pointed right onto Front View",
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
LEAF_SIZE = 5 * SIZE

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Fourstar.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_fourstar = bpy.data.meshes.new(name + '.mesh')
object_fourstar = bpy.data.objects.new(name, mesh_fourstar)

vertex_fourstar = [
	(origin.x, origin.y, origin.z + LEAF_SIZE), # P0
	(origin.x + SIZE, origin.y, origin.z + SIZE), # P1
	(origin.x + LEAF_SIZE, origin.y, origin.z), # P2
	(origin.x + SIZE, origin.y, origin.z - SIZE), # P3
	(origin.x, origin.y, origin.z - LEAF_SIZE), # P4
	(origin.x - SIZE, origin.y, origin.z - SIZE), # P5
	(origin.x - LEAF_SIZE, origin.y, origin.z), # P6
	(origin.x - SIZE, origin.y, origin.z + SIZE), # P7
	(origin.x, origin.y, origin.z) # P8
]

edges_fourstar = [
	(0, 1), (1, 2), (2, 3), (3, 4),
	(4, 5), (5, 6), (6, 7), (7, 8),
	(1, 8), (3, 8), (5, 8)
]

faces_fourstar = [
	(0, 7, 8, 1), (7, 6, 5, 8),
	(8, 5, 4, 3), (8, 3, 2, 1)
]
mesh_fourstar.from_pydata(vertex_fourstar, edges_fourstar, faces_fourstar)

object_fourstar.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_fourstar.update(calc_edges=True)
bpy.context.scene.collection.objects.link(object_fourstar)
