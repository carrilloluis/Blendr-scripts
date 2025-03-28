bl_info = {
	"name": "Hexagon Plane 2D (quadrilateral based et **EQUILATERAL**)",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Hexagon Plane 2D onto Front View equilateral with 3 units",
	"warning": "Use under ur own risk!!",
	"category": "Scripting"
}

import bpy
from random import randint
from mathutils import Vector

# Deselect any object
bpy.ops.object.select_all(action='DESELECT')

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Hexagone.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_regular_hexagon = bpy.data.meshes.new(name + '.mesh')
object_regular_hexagon = bpy.data.objects.new(name, mesh_regular_hexagon)

# SQRT_3 = 3 ** .5
SQRT_OF_THREE = 1.73205

vertex_hexagon = [
	(origin.x + 2, origin.y, origin.z), # P0  0°
	(origin.x + 1, origin.y, origin.z + SQRT_OF_THREE), # P1 60°
	(origin.x - 1, origin.y, origin.z + SQRT_OF_THREE), # P2 120°
	(origin.x - 2, origin.y, origin.z), # P3 180°
	(origin.x - 1, origin.y, origin.z - SQRT_OF_THREE), # P4 240°
	(origin.x + 1, origin.y, origin.z - SQRT_OF_THREE) # P5 300°
]

edges_hexagon = [
	(0, 1), (1, 2), (2, 3), (3, 4), 
	(4, 5), (5, 0), (0, 3)
]

faces_hexagon = [
	(0, 1, 2, 3), (3, 4, 5, 0)
]
mesh_regular_hexagon.from_pydata(vertex_hexagon, [], faces_hexagon)

object_regular_hexagon.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_regular_hexagon.update(calc_edges=True)
mesh_regular_hexagon.update()

bpy.context.scene.collection.objects.link(object_regular_hexagon)