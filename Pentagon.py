bl_info = {
	"name": "Pentagon 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Pentagon 2D with quads",
	"warning": "Use under ur own risk!!",
	"category": "Scripting"
}

import bpy
from random import randint
from mathutils import Vector
import math

# Deselect any object
bpy.ops.object.select_all(action='DESELECT')

# Dimensions like constants
SIZE = 2.0
RADIANS = math.pi / 180
BASE_Z = SIZE * math.sin(234 * RADIANS)

# Set the reference POINT to build mesh
center = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Pentagon.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_pentagon = bpy.data.meshes.new(name + '.mesh')
object_pentagon = bpy.data.objects.new(name, mesh_pentagon)

vertex_pentagon = [
	(center.x, center.y, center.z), # P0
	(center.x + (SIZE * math.cos(18 * RADIANS)), center.y, center.z + (SIZE * math.sin(18 * RADIANS))), # P1
	(center.x, center.y, center.z  + SIZE), # P2
	(center.x + (SIZE * math.cos(162 * RADIANS)), center.y, center.z + (SIZE * math.sin(162 * RADIANS))), # P3
	(center.x + (SIZE * math.cos(234 * RADIANS)), center.y, center.z + BASE_Z), # P4
	(center.x + (SIZE * math.cos(306 * RADIANS)), center.y, center.z + BASE_Z), # P5
	(center.x, center.y, center.z + BASE_Z), # P6
]

edges_pentagon = [
	(0, 1), (1, 2), (2, 3), (3, 0), (3, 4),
	(4, 6), (6, 0), (6, 5), (5, 1) 
]

faces_pentagon = [
	(2, 3, 0, 1), (3, 4, 6, 0), (0, 6, 5, 1)
]
mesh_pentagon.from_pydata(vertex_pentagon, edges_pentagon, faces_pentagon)

object_pentagon.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_pentagon.update(calc_edges=True)
mesh_pentagon.update()

bpy.context.scene.collection.objects.link(object_pentagon)
