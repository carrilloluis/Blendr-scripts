bl_info = {
	"name": "Rounded Plane Base 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 2),
	"blender": (4, 2, 7),
	"description": "Rounded Plane 2D",
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
# HALF_SIZE = SIZE / 2 
# EXT_SIZE = SIZE + HALF_SIZE
# cos 45
ROUNDED = 0.70710

# Set the reference POINT to build mesh
center = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Rounded-Plane.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_plane = bpy.data.meshes.new(name + '.mesh')
object_plane = bpy.data.objects.new(name, mesh_plane)

vertex_plane = [
	(center.x, center.y, center.z), # P0
	(center.x, center.y, center.z + SIZE), # P1
	(center.x + (SIZE * ROUNDED), center.y, center.z + (SIZE * ROUNDED)), # P2
	(center.x + SIZE, center.y, center.z), # P3
	(center.x + (SIZE * ROUNDED), center.y, center.z - (SIZE * ROUNDED)), # P4
	(center.x, center.y, center.z - SIZE), # P5
	(center.x - (SIZE * ROUNDED), center.y, center.z - (SIZE * ROUNDED)), # P6
	(center.x - SIZE, center.y, center.z), # P7
	(center.x - (SIZE * ROUNDED), center.y, center.z + (SIZE * ROUNDED)) # P8
]

edges_plane = [
	(0, 1), (1, 2), (2, 3), (3, 0),
	(0, 5), (5, 4), (4, 3), (0, 7), 
	(7, 6), (6, 5), (1, 8), (8, 7)
]

faces_plane = [
	(1, 0, 3, 2), (0, 5, 4, 3),
	(0, 7, 6, 5), (1, 8, 7, 0)
]
mesh_plane.from_pydata(vertex_plane, edges_plane, faces_plane)

object_plane.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_plane.update(calc_edges=True)
mesh_plane.update()

bpy.context.scene.collection.objects.link(object_plane)
