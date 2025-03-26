bl_info = {
	"name": "Classical Arrow 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 1),
	"blender": (4, 2, 7),
	"description": "Classical Arrow with quadrilateral shapes (quads) like a plane onto front view",
	"warning": "Use under ur own risk!",
	"category": "Scripting"
}

import bpy
from random import randint
from mathutils import Vector

# Deselect any object 
bpy.ops.object.select_all(action='DESELECT')

# Dimensions like constants 
SIZE = 1.0
TRI_SIZE = 3 * SIZE

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Classical-Arrow.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_classic_arrow = bpy.data.meshes.new(name + '.mesh')
object_classic_arrow = bpy.data.objects.new(name, mesh_classic_arrow)

vertex_classic_arrow = [
	(origin.x, origin.y, origin.z + (2 * SIZE)), # P0
	(origin.x + TRI_SIZE, origin.y, origin.z), # P1
	(origin.x, origin.y, origin.z - (2 * SIZE)), # P2

	(origin.x, origin.y, origin.z - SIZE),  # P3
	(origin.x - TRI_SIZE, origin.y, origin.z - SIZE), # P4
	(origin.x - TRI_SIZE, origin.y, origin.z),  # P5

	(origin.x - TRI_SIZE, origin.y, origin.z + SIZE), # P6
	(origin.x, origin.y, origin.z + SIZE), # P7
	(origin.x + SIZE, origin.y, origin.z) # P8
]

edges_classic_arrow = [
	(0, 1), (1, 2), (2, 3), (3, 4),
	(4, 5), (5, 6), (6, 7), (7, 0),
	(7, 8), (3, 8) 
]

faces_classic_arrow = [
	(0, 7, 8, 1), (6, 5, 8, 7),
	(5, 4, 3, 8), (1, 8, 3, 2)
]

mesh_classic_arrow.from_pydata(vertex_classic_arrow, edges_classic_arrow, faces_classic_arrow)

object_classic_arrow.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_classic_arrow.update(calc_edges=True)
mesh_classic_arrow.update()

bpy.context.scene.collection.objects.link(object_classic_arrow)