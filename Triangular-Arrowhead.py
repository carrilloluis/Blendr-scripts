bl_info = {
	"name": "Triangular arrowhead",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "",
	"warning": "Use under ur own risk!!",
	"category": "Scripting"
}

import bpy
from random import randint
from mathutils import Vector

# Deselect any object
bpy.ops.object.select_all(action='DESELECT')

# Dimensions like constants
SIZE = 2.0
SEPARATOR = 0.2

# Set the reference POINT to build mesh
origin_location = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Triangular-Arrowhead.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_triangular_arrow = bpy.data.meshes.new(name + '.mesh')
object_triangular_arrow = bpy.data.objects.new(name, mesh_triangular_arrow)

# Geometry
vertex_triangular_arrow = [
	(cursor_3d.x, cursor_3d.y, cursor_3d.z + SIZE), # P0
	(cursor_3d.x + SIZE, cursor_3d.y, cursor_3d.z), # P1
	(cursor_3d.x, cursor_3d.y, cursor_3d.z - SIZE),   # P2
	(cursor_3d.x, cursor_3d.y, cursor_3d.z - ((SIZE / 2) - SEPARATOR)), # P3
	(cursor_3d.x - (SIZE + SEPARATOR), cursor_3d.y, cursor_3d.z),   # P4
	(cursor_3d.x, cursor_3d.y, cursor_3d.z + ((SIZE / 2) - SEPARATOR)), # P5
	(cursor_3d.x + (SIZE / 2), cursor_3d.y, cursor_3d.z)    # P6
]

edges_triangular_arrow = [
	(0, 1), (1, 2), (2, 3), (3, 4),
	(4, 5), (5, 0), (5, 6), (3, 6)
]

faces_triangular_arrow = [
	(0, 5, 6, 1), (6, 3, 2, 1), (5, 4, 3, 6)
]
mesh_triangular_arrow.from_pydata(vertex_triangular_arrow, edges_triangular_arrow, faces_triangular_arrow)

object_triangular_arrow.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_triangular_arrow.update(calc_edges=True)
mesh_triangular_arrow.update()

bpy.context.scene.collection.objects.link(object_triangular_arrow)
