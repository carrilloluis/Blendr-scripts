bl_info = {
	"name": "Drop water Plane 2D",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 0, 1),
	"blender": (4, 2, 7),
	"description": "Drop-water shape 2D onto Front View, with additional step : ADD MODIFIER > Subdivision > Level 2 (or hotkey CTRL + 2)",
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
name = 'Drop-Water.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_dropwater = bpy.data.meshes.new(name + '.mesh')
object_dropwater = bpy.data.objects.new(name, mesh_dropwater)

vertex_dropwater = [
	(origin.x + SHARP, origin.y, origin.z + (3 * SIZE)), # P0
	(origin.x + SHARP, origin.y, origin.z + SIZE), # P1
	(origin.x + (SIZE + (SHARP / 2)), origin.y, origin.z), # P2
	(origin.x + (SIZE + SHARP), origin.y, origin.z - SIZE), # P3
	(origin.x, origin.y, origin.z - (2 * SIZE)), # P4
	(origin.x - (SIZE + SHARP), origin.y, origin.z - SIZE), # P5
	(origin.x - (SIZE + (SHARP / 2)), origin.y, origin.z), # P6
	(origin.x - SIZE, origin.y, origin.z + SIZE), # P7
	(origin.x, origin.y, origin.z) # P8
]

edges_dropwater = [
	(0, 1), (1, 2), (2, 3), (3, 4), 
	(4, 5), (5, 6), (6, 7), (7, 0),
	(0, 8), (2, 8), (6, 8), (4, 8)
]

faces_dropwater = [
	(0, 8, 2, 1), (8, 4, 3, 2), 
	(6, 5, 4, 8), (0, 7, 6, 8)
]
mesh_dropwater.from_pydata(vertex_dropwater, edges_dropwater, faces_dropwater)

object_dropwater.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_dropwater.update(calc_edges=True)
mesh_dropwater.update()

bpy.context.scene.collection.objects.link(object_dropwater)