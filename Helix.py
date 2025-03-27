bl_info = {
	"name": "Simulating Helix Shape Plane 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Helix Plane 2D onto Front View",
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
SLACK = .75
BEVEL = .25

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Helix.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_helix = bpy.data.meshes.new(name + '.mesh')
object_helix = bpy.data.objects.new(name, mesh_helix)

vertex_helix = [
	(origin.x + SLACK, origin.y, origin.z + (SIZE - BEVEL)), # P0
	(origin.x + (SIZE + SLACK), origin.y, origin.z + (SIZE - BEVEL)), # P1
	(origin.x + ((2 * SIZE) + SLACK), origin.y, origin.z + (SIZE - BEVEL)), # P2
	(origin.x + ((2 * SIZE) + SLACK), origin.y, origin.z), # P3
	(origin.x + SLACK, origin.y, origin.z), # P4
	(origin.x - SLACK, origin.y, origin.z - (SIZE - BEVEL)), # P5
	(origin.x - (SIZE + SLACK), origin.y, origin.z - (SIZE - BEVEL)), # P6
	(origin.x - ((2 * SIZE) + SLACK), origin.y, origin.z - (SIZE - BEVEL)), # P7
	(origin.x - ((2 * SIZE) + SLACK), origin.y, origin.z), # P8
	(origin.x - SLACK, origin.y, origin.z) # P9
]

edges_helix = [
	(0, 1), (1, 2), (2, 3), (3, 4), 
	(4, 5), (5, 6), (6, 7), (7, 8),
	(8, 9), (9, 4)
]

faces_helix = [
	(0, 9, 4, 1), (1, 4, 3, 2), 
	(9, 6, 5, 4), (9, 8, 7, 6)
]
mesh_helix.from_pydata(vertex_helix, edges_helix, faces_helix)

object_helix.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_helix.update(calc_edges=True)
mesh_helix.update()

bpy.context.scene.collection.objects.link(object_helix)