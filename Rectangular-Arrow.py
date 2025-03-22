bl_info = {
	"name": "Rectangular Arrow (arrowhead visibleless)",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 1),
	"blender": (4, 2, 7),
	"description": "Create a Rectangular Arrow 2D (FRONT VIEW) no n-gon solution with quads. [Update]: to make 3d volumetric object apply SOLIDIFY modifier to this new object!",
	"warning": "Use under own risk!!",
	"category": "Scripting"
}

import bpy
from random import randint
from mathutils import Vector

# Deselect any object 
bpy.ops.object.select_all(action='DESELECT')

# Dimensions like constants
WIDTH = 2.0
SEMI_WIDTH = WIDTH / 2
SEMI_HEIGHT = 1.0

# Set the reference POINT to build mesh
origin_location = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Rectangular-Arrow.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_rect_arrow = bpy.data.meshes.new(name + '.mesh')
object_rect_arrow = bpy.data.objects.new(name, mesh_rect_arrow)

vertex_rect_arrow = [
	(origin_location.x - WIDTH, origin_location.y, origin_location.z + SEMI_HEIGHT),  # P0
	(origin_location.x + SEMI_WIDTH, origin_location.y, origin_location.z + SEMI_HEIGHT),   # P1
	(origin_location.x + WIDTH, origin_location.y, origin_location.z),  # P2
	(origin_location.x + SEMI_WIDTH, origin_location.y, origin_location.z - SEMI_HEIGHT), # P3
	(origin_location.x - WIDTH, origin_location.y, origin_location.z - SEMI_HEIGHT),  # P4
	(origin_location.x - WIDTH, origin_location.y, origin_location.z),  # P5
]

edges_rect_arrow = [
	(0, 1), (1, 2), (2, 5), 
	(5, 0), (2, 3), (3, 4),
	(4, 5)
]

faces_rect_arrow = [
	(0, 5, 2, 1), (5, 4, 3, 2)
]
mesh_rect_arrow.from_pydata(vertex_rect_arrow, [], faces_rect_arrow)

object_rect_arrow.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_rect_arrow.update(calc_edges=True)
mesh_rect_arrow.update()

bpy.context.scene.collection.objects.link(object_rect_arrow)