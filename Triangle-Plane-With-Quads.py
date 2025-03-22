bl_info = {
	"name": "Triangle with quads",
	"author": "Carrillo Gutiérrez, Luis",
	"version": (0, 1),
	"blender": (4, 2, 7),
	"description": "Create a triangle plane (FRONT VIEW), with no  just three vertex or n-gon solution, just Quads (no practical use, just to improve blender scripting in python).",
	"warning": "No professional use, use under own risk!!",
	"category": "Scripting"
}

import bpy
from random import randint
from mathutils import Vector

# Deselect any object 
bpy.ops.object.select_all(action='DESELECT')

# Dimensions like constants
SEMI_BASE = 1.0
SEMI_HEIGHT = 1.0
SEPARATION = 0.2

# Set the reference POINT to build mesh
reference_location = Vector((0, 0, 0))

# 3D Object Name onto OUTLINE PANEL
name = 'Triangle-Quads.' + str(randint(0, 100))

# Current location of Blender's Cursor 3D
cursor_3d = bpy.context.scene.cursor.location

mesh_triangle = bpy.data.meshes.new(name + '.mesh')
object_triangle = bpy.data.objects.new(name, mesh_triangle)

vertex_triangle = [
	(reference_location.x + SEMI_BASE, reference_location.y, reference_location.z + SEMI_HEIGHT),  # P0
	(reference_location.x + SEMI_BASE, reference_location.y, reference_location.z - SEPARATION),   # P1
	(reference_location.x + SEMI_BASE, reference_location.y, reference_location.z - SEMI_HEIGHT),  # P2
	(reference_location.x + SEPARATION, reference_location.y, reference_location.z - SEMI_HEIGHT), # P3
	(reference_location.x + SEPARATION, reference_location.y, reference_location.z - SEPARATION),  # P4
	(reference_location.x - SEMI_BASE, reference_location.y, reference_location.z - SEMI_HEIGHT),  # P5
	(reference_location.x, reference_location.y, reference_location.z)    # P6
]

edges_triangle = [
	(1, 2), (2, 3), (3, 4), (4, 1),
	(4, 6), (0, 6), (0, 1),
	(3, 5), (5, 6)
]

faces_triangle = [
	(0, 1, 4, 6), (1, 2, 3, 4), (6, 4, 3, 5)
]
mesh_triangle.from_pydata(vertex_triangle, [], faces_triangle)

object_triangle.location = cursor_3d
bpy.context.scene.cursor.location.xyz = cursor_3d

mesh_triangle.update(calc_edges=True)
mesh_triangle.update()

bpy.context.scene.collection.objects.link(object_triangle)