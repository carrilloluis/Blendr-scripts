bl_info = {
	"name": "Hexagon Plane 2D (quadrilateral based)",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Hexagon Plane 2D onto Front View, non equilateral",
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
SHARP = 0.5

# Set the reference POINT to build mesh
origin = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Hexagon.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_hexagon = bpy.data.meshes.new(name + '.mesh')
object_hexagon = bpy.data.objects.new(name, mesh_hexagon)

vertex_hexagon = [
	(origin.x, origin.y, origin.z + (SIZE + SHARP)), # P0
	(origin.x + SIZE, origin.y, origin.z + SIZE), # P1
	(origin.x + SIZE, origin.y, origin.z - SIZE), # P2
	(origin.x, origin.y, origin.z - (SIZE + SHARP)), # P3
	(origin.x - SIZE, origin.y, origin.z - SIZE), # P4
	(origin.x - SIZE, origin.y, origin.z + SIZE), # P5
]

edges_hexagon = [
	(0, 1), (1, 2), (2, 3), (3, 4), 
	(4, 5), (5, 0), (0, 3)
]

faces_hexagon = [
	(0, 3, 2, 1), (0, 5, 4, 3)
]
mesh_hexagon.from_pydata(vertex_hexagon, edges_hexagon, faces_hexagon)

object_hexagon.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_hexagon.update(calc_edges=True)
mesh_hexagon.update()

bpy.context.scene.collection.objects.link(object_hexagon)