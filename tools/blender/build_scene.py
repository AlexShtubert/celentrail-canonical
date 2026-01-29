import bpy
import os
import math

# ========= НАСТРОЙКИ =========
OUT_PATH = "assets/3d/balka/latest/balka.glb"

# Очистка сцены
bpy.ops.wm.read_factory_settings(use_empty=True)

# ========= ПРОСТАЯ ВИЗУАЛЬНАЯ ЗАГЛУШКА БАЛКИ =========
# (это не твоя финальная геометрия — только чтобы pipeline ЗАВЁЛСЯ)

# Создаём балку как прямоугольный брус
bpy.ops.mesh.primitive_cube_add(size=1)
balka = bpy.context.active_object
balka.name = "Balka"

# Масштаб под «балку»
balka.scale = (1.15, 0.12, 0.20)  # длина, ширина, высота

# Материал (металл)
mat = bpy.data.materials.new(name="Steel")
mat.use_nodes = True
nodes = mat.node_tree.nodes
bsdf = nodes.get("Principled BSDF")
bsdf.inputs["Metallic"].default_value = 0.7
bsdf.inputs["Roughness"].default_value = 0.35
balka.data.materials.append(mat)

# ========= КАМЕРА =========
bpy.ops.object.camera_add(
    location=(2.5, -2.5, 1.8),
    rotation=(math.radians(65), 0, math.radians(45))
)
bpy.context.scene.camera = bpy.context.active_object

# ========= СВЕТ =========
bpy.ops.object.light_add(type='AREA', location=(2, -2, 3))
light = bpy.context.active_object
light.data.energy = 1500

bpy.ops.object.light_add(type='AREA', location=(-2, 2, 2))
light2 = bpy.context.active_object
light2.data.energy = 800

# ========= ЭКСПОРТ =========
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

bpy.ops.export_scene.gltf(
    filepath=OUT_PATH,
    export_format='GLB',
    export_apply=True
)

print("GLB собран:", OUT_PATH)
