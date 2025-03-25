bl_info = {
	"name": "Rectangular Corner",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 1),
	"blender": (4, 2, 7),
	"description": "",
	"warning": "Use under ur own risk!",
	"category": "Scripting"
}

import bpy
from random import randint
from mathutils import Vector

# Deselect any object 
bpy.ops.object.select_all(action='DESELECT')

# Dimensions like constants
SIZE = 2.0

# Set the reference POINT to build mesh
origin_location = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Rectangular-Corner.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_rect_corner = bpy.data.meshes.new(name + '.mesh')
object_rect_corner = bpy.data.objects.new(name, mesh_rect_corner)

vertex_rect_corner = [
	(origin_location.x - SIZE, origin_location.y, origin_location.z + SIZE),  # P0
	(origin_location.x + SIZE, origin_location.y, origin_location.z + SIZE),   # P1
	(origin_location.x + SIZE, origin_location.y, origin_location.z),  # P2
	(origin_location.x, origin_location.y, origin_location.z), # P3
	(origin_location.x, origin_location.y, origin_location.z - SIZE),  # P4
	(origin_location.x - SIZE, origin_location.y, origin_location.z - SIZE),  # P5
]

edges_rect_corner = [
	(0, 1), (1, 2), (2, 3), 
	(3, 4), (4, 5), (5, 0), (0, 3)
]

faces_rect_corner = [
	(0, 1, 2, 3), (0, 3, 4, 5)
]

mesh_rect_corner.from_pydata(vertex_rect_corner, edges_rect_corner, faces_rect_corner)

object_rect_corner.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_rect_corner.update(calc_edges=True)
mesh_rect_corner.update()

bpy.context.scene.collection.objects.link(object_rect_corner)