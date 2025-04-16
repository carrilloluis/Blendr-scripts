bl_info = {
	"name": "Zigzag 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Zigzag 2D onto Front View",
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
TRIPLE_SIZE = 3 * SIZE

# Set the reference POINT to build mesh
center = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Zigzag.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_zigzag = bpy.data.meshes.new(name + '.mesh')
object_zigzag = bpy.data.objects.new(name, mesh_zigzag)

vertex_zigzag = [
	(center.x, center.y, center.z + TRIPLE_SIZE), # P0
	(center.x - SIZE, center.y, center.z + TRIPLE_SIZE), # P1
	(center.x + SIZE, center.y, center.z + SIZE), # P2
	(center.x, center.y, center.z + SIZE), # P3
	(center.x, center.y, center.z - SIZE), # P4
	(center.x - SIZE, center.y, center.z - SIZE), # P5
	(center.x + SIZE, center.y, center.z - TRIPLE_SIZE), # P6
	(center.x, center.y, center.z - TRIPLE_SIZE) # P7
]

edges_zigzag = [
	(0, 1), (0, 2), (2, 3), (1, 3),
	(2, 4), (4, 5), (3, 5), (4, 6),
	(6, 7), (5, 7)
]

faces_zigzag = [
	(0, 1, 3, 2), (2, 3, 5, 4), (4, 5, 7, 6)
]
mesh_zigzag.from_pydata(vertex_zigzag, edges_zigzag, faces_zigzag)

object_zigzag.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_zigzag.update(calc_edges=True)
# mesh_arrow.update()

bpy.context.scene.collection.objects.link(object_zigzag)
