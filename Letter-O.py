bl_info = {
	"name": "Letter O on 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Letter O onto Front View (2D)",
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
center = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Letter-O.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_letter_o = bpy.data.meshes.new(name + '.mesh')
object_letter_o = bpy.data.objects.new(name, mesh_letter_o)

vertex_letter_o = [
	(center.x - DBL_SIZE, center.y, center.z + DBL_SIZE), # P0
	(center.x + DBL_SIZE, center.y, center.z + DBL_SIZE), # P1
	(center.x + DBL_SIZE, center.y, center.z - DBL_SIZE), # P2
	(center.x - DBL_SIZE, center.y, center.z - DBL_SIZE), # P3
	(center.x - SIZE, center.y, center.z + SIZE), # P4
	(center.x + SIZE, center.y, center.z + SIZE), # P5
	(center.x + SIZE, center.y, center.z - SIZE), # P6
	(center.x - SIZE, center.y, center.z - SIZE) # P7
]

edges_letter_o = [
	(0, 1), (1, 2), (2, 3), (3, 0),
	(4, 5), (5, 6), (6, 7), (7, 4),
	(0, 4), (1, 5), (2, 6), (3, 7)
]

faces_letter_o = [
	(1, 0, 4, 5), (4, 0, 3, 7),
	(1, 5, 6, 2), (7, 3, 2, 6)
]
mesh_letter_o.from_pydata(vertex_letter_o, edges_letter_o, faces_letter_o)

object_letter_o.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_letter_o.update(calc_edges=True)
# mesh_letter_o.update()

bpy.context.scene.collection.objects.link(object_letter_o)