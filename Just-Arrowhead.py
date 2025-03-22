bl_info = {
	"name": "Just Arrowhead",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Create a Clasic & minimal arrowhead without arm",
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

# Set the reference POINT to build mesh
origin_location = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Just-Arrowhead.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_just_arrow = bpy.data.meshes.new(name + '.mesh')
object_just_arrow = bpy.data.objects.new(name, mesh_just_arrow)

vertex_just_arrow = [
	(origin_location.x - SIZE, origin_location.y, origin_location.z + SIZE),  # P0
	(origin_location.x, origin_location.y, origin_location.z + SIZE),   # P1
	(origin_location.x + SIZE, origin_location.y, origin_location.z),  # P2
	(origin_location.x, origin_location.y, origin_location.z - SIZE), # P3
	(origin_location.x - SIZE, origin_location.y, origin_location.z - SIZE),  # P4
	(origin_location.x, origin_location.y, origin_location.z),  # P5
]

edges_just_arrow = [
	(0, 1), (1, 2), (2, 3), (3, 4),
	(4, 5), (5, 0), (5, 2)
]

faces_just_arrow = [
	(5, 2, 1, 0), (4, 3, 2, 5)
]
mesh_just_arrow.from_pydata(vertex_just_arrow, [], faces_just_arrow)

object_just_arrow.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_just_arrow.update(calc_edges=True)
mesh_just_arrow.update()

bpy.context.scene.collection.objects.link(object_just_arrow)