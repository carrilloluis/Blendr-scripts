bl_info = {
	"name": "Rectangular Prism 3D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Rectangular Prism 3D",
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
SEPARATOR = .2

# Set the reference POINT to build mesh
center = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Rect-Prism.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_rect_prism = bpy.data.meshes.new(name + '.mesh')
object_rect_prism = bpy.data.objects.new(name, mesh_rect_prism)

vertex_rect_prism = [
	(center.x - SIZE, center.y + SIZE, center.z + SIZE), # Pa / 0
	(center.x - SIZE, center.y + SIZE, center.z - SIZE), # Pb / 1
	(center.x - SIZE, center.y - SIZE, center.z - SIZE), # Pc / 2

	(center.x + SIZE, center.y + SIZE, center.z + SIZE), # Pd / 3
	(center.x + SIZE, center.y + SIZE, center.z - SIZE), # Pe / 4
	(center.x + SIZE, center.y - SIZE, center.z - SIZE)  # Pf / 5
]

edges_rect_prism = [
]

faces_rect_prism = [
	(0, 3, 4, 1), (0, 2, 5, 3), (2, 1, 4, 5), (0, 1, 2), (3, 5, 4) 
]

mesh_rect_prism.from_pydata(vertex_rect_prism, [], faces_rect_prism)

object_rect_prism.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_rect_prism.update(calc_edges=True)
mesh_rect_prism.update()

bpy.context.scene.collection.objects.link(object_rect_prism)
