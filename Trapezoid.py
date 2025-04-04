bl_info = {
	"name": "Trapezoid Base 3D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 2),
	"blender": (4, 2, 7),
	"description": "Trapezoid Base 3D",
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
EXT_SIZE = SIZE + HALF_SIZE

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Trapezoid.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_trapezoid = bpy.data.meshes.new(name + '.mesh')
object_trapezoid = bpy.data.objects.new(name, mesh_trapezoid)

vertex_trapezoid = [
	(origin.x - HALF_SIZE, origin.y - HALF_SIZE, origin.z + HALF_SIZE), # P0
	(origin.x - HALF_SIZE, origin.y + HALF_SIZE, origin.z + HALF_SIZE), # P1
	(origin.x + HALF_SIZE, origin.y + HALF_SIZE, origin.z + HALF_SIZE), # P2
	(origin.x + HALF_SIZE, origin.y - HALF_SIZE, origin.z + HALF_SIZE), # P3

	(origin.x - SIZE, origin.y - HALF_SIZE, origin.z - HALF_SIZE), # P4
	(origin.x - SIZE, origin.y + HALF_SIZE, origin.z - HALF_SIZE), # P5
	(origin.x, origin.y + HALF_SIZE, origin.z - HALF_SIZE), # P6
	(origin.x, origin.y - HALF_SIZE, origin.z - HALF_SIZE) # P7
]

edges_trapezoid = [
	(0, 1), (1, 2), (2, 3), (3, 0),
	(4, 5), (5, 6), (6, 7), (7, 4),
	(0, 4), (5, 1), (6, 2), (7, 3)
]

faces_trapezoid = [
	(0, 3, 2, 1), (4, 5, 6, 7),
	(2, 3, 7, 6), (0, 1, 5, 4),
	(0, 4, 7, 3), (1, 2, 6, 5)
]
mesh_trapezoid.from_pydata(vertex_trapezoid, edges_trapezoid, faces_trapezoid)

object_trapezoid.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_trapezoid.update(calc_edges=True)
mesh_trapezoid.update()

bpy.context.scene.collection.objects.link(object_trapezoid)
