import bpy
import os
abcPath = os.environ["Unity_Alembic_Path"] #改abc文件绝对路径
resultPath = abcPath[:len(abcPath)-3] + "txt" # 这里的意思是指该文件夹下同名txt文件

for obj in bpy.context.scene.objects:
    obj.select_set(True)
    bpy.ops.object.delete(use_global=False)

bpy.ops.wm.alembic_import(filepath=abcPath)

bpy.context.scene.objects[0].select_set(True)
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.separate(type="LOOSE")

lengths = []

for obj in bpy.context.scene.objects:
    mesh = obj.data
    counts = sum([(len(p.vertices) - 2) for p in mesh.polygons])
    lengths.append(counts)

f = open(resultPath, "w")  #如果无法运行，可改txt绝对路径
f.write('\n'.join(str(e) for e in lengths))

# os.environ["Unity_Alembic_Path_Result"]=
bpy.ops.wm.quit_blender()
