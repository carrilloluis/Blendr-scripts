bl_info = {
	"name": "Corner Plane 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Corner Plane 2D onto Front View",
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
DOUBLE_SIZE = 2 * SIZE
SHARP = 0.5

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Corner.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_corner = bpy.data.meshes.new(name + '.mesh')
object_corner = bpy.data.objects.new(name, mesh_corner)

vertex_corner = [
	(origin.x, origin.y, origin.z + DOUBLE_SIZE), # P0
	(origin.x + DOUBLE_SIZE, origin.y, origin.z + DOUBLE_SIZE), # P1
	(origin.x + DOUBLE_SIZE, origin.y, origin.z + SIZE), # P2
	(origin.x + (SIZE - SHARP), origin.y, origin.z + SIZE), # P3
	(origin.x, origin.y, origin.z + SHARP), # P4
	(origin.x, origin.y, origin.z - SIZE), # P5
	(origin.x - SIZE, origin.y, origin.z - SIZE), # P6
	(origin.x - SIZE, origin.y, origin.z + SIZE) # P7
]

edges_corner = [
	(0, 1), (1, 2), (2, 3), (3, 4), 
	(4, 5), (5, 6), (6, 7), (7, 0),
	(0, 3), (4, 7)
]

faces_corner = [
	(0, 3, 2, 1), (0, 7, 4, 3), (7, 6, 5, 4)
]
mesh_corner.from_pydata(vertex_corner, edges_corner, faces_corner)

object_corner.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_corner.update(calc_edges=True)
mesh_corner.update()

bpy.context.scene.collection.objects.link(object_corner)