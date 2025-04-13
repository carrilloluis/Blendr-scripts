bl_info = {
	"name": "Pipe (Z letter shape) 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Pipe (Z letter shape) 2D",
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
EXTENSION = SIZE + HALF_SIZE

# Set the reference POINT to build mesh
center = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Pipe-z.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_pipe = bpy.data.meshes.new(name + '.mesh')
object_pipe = bpy.data.objects.new(name, mesh_pipe)

vertex_pipe = [
	(center.x - EXTENSION, center.y, center.z + EXTENSION), # P0
	(center.x + HALF_SIZE, center.y, center.z + EXTENSION), # P1
	(center.x + HALF_SIZE, center.y, center.z - HALF_SIZE), # P2
	(center.x + EXTENSION, center.y, center.z - HALF_SIZE), # P3
	(center.x + EXTENSION, center.y, center.z - EXTENSION), # P4
	(center.x - HALF_SIZE, center.y, center.z - EXTENSION), # P5
	(center.x - HALF_SIZE, center.y, center.z + HALF_SIZE), # P6
	(center.x - EXTENSION, center.y, center.z + HALF_SIZE)  # P7
]

edges_pipe = [
	(0, 1), (1, 2), (2, 3), (3, 4),
	(4, 5), (5, 6), (6, 7), (7, 0),
	(1, 6), (2, 5)
]

faces_pipe = [
	(0, 7, 6, 1), (1, 6, 5, 2), (2, 5, 4, 3)
]
mesh_pipe.from_pydata(vertex_pipe, edges_pipe, faces_pipe)

object_pipe.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_pipe.update(calc_edges=True)
mesh_pipe.update()

bpy.context.scene.collection.objects.link(object_pipe)
