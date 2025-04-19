bl_info = {
	"name": "Sphinx 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 1),
	"blender": (4, 2, 7),
	"description": "Sphinx (quads) onto front view",
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

# Set the reference POINT to build mesh
center = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Sphinx.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_sphinx = bpy.data.meshes.new(name + '.mesh')
object_sphinx = bpy.data.objects.new(name, mesh_sphinx)

vertex_sphinx = [
	(center.x - SIZE, center.y, center.z + (SIZE - (SIZE / 4))), # P0
	(center.x - (SIZE / 2), center.y, center.z), # P1
	(center.x + (SIZE / 2), center.y, center.z), # P2

	(center.x + SIZE, center.y, center.z - SIZE), # P3
	(center.x - SIZE, center.y, center.z - SIZE), # P4
	(center.x - (2 * SIZE), center.y, center.z - SIZE) # P5
]

edges_sphinx = [
	(0, 1), (1, 2), (2, 3), 
	(3, 4), (4, 5), (5, 0), (1, 4) 
]

faces_sphinx = [
	(0, 5, 4, 1), (1, 4, 3, 2)
]

mesh_sphinx.from_pydata(vertex_sphinx, edges_sphinx, faces_sphinx)

object_sphinx.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_sphinx.update(calc_edges=True)
# mesh_sphinx.update()

bpy.context.scene.collection.objects.link(object_sphinx)