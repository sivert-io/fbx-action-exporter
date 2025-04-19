bl_info = {
    "name": "FBX Action Exporter (Full Settings)",
    "author": "You",
    "version": (2, 2),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Armature Tools",
    "description": "FBX exporter for all actions with full export settings and collapsible layout",
    "category": "Import-Export",
}

import bpy
import os
from bpy.types import Operator, Panel, PropertyGroup
from bpy.props import *

class FBXExportSettings(PropertyGroup):
    export_path: StringProperty(name="Export Path", subtype="DIR_PATH")

    # Transform
    global_scale: FloatProperty(name="Scale", default=1.0, min=0.001, max=1000.0)
    apply_scale_options: EnumProperty(
        name="Apply Scalings",
        items=[
            ('FBX_SCALE_NONE', "All Local", ""),
            ('FBX_SCALE_UNITS', "FBX Units Scale", ""),
            ('FBX_SCALE_CUSTOM', "FBX Custom Scale", ""),
            ('FBX_SCALE_ALL', "FBX All", "")
        ],
        default='FBX_SCALE_NONE'
    )
    axis_forward: EnumProperty(
        name="Forward",
        items=[(x, x, "") for x in ['X', 'Y', 'Z', '-X', '-Y', '-Z']],
        default='-Z'
    )
    axis_up: EnumProperty(
        name="Up",
        items=[(x, x, "") for x in ['X', 'Y', 'Z', '-X', '-Y', '-Z']],
        default='Y'
    )
    apply_unit_scale: BoolProperty(name="Apply Unit")
    use_space_transform: BoolProperty(name="Use Space Transform", default=True)
    bake_space_transform: BoolProperty(name="Apply Transform")

    # Geometry
    mesh_smooth_type: EnumProperty(
        name="Smoothing",
        items=[('OFF', "Normals Only", ""), ('FACE', "Face", ""), ('EDGE', "Edge", "")],
        default='OFF'
    )
    use_subsurf: BoolProperty(name="Export Subdivision Surface")
    use_mesh_modifiers: BoolProperty(name="Apply Modifiers", default=True)
    use_mesh_edges: BoolProperty(name="Loose Edges")
    use_triangles: BoolProperty(name="Triangulate Faces")
    use_tspace: BoolProperty(name="Tangent Space")
    colors_type: EnumProperty(
        name="Vertex Colors",
        items=[('NONE', "None", ""), ('SRGB', "sRGB", ""), ('LINEAR', "Linear", "")],
        default='SRGB'
    )
    prioritize_active_color: BoolProperty(name="Prioritize Active Color")

    # Armature
    use_armature_deform_only: BoolProperty(name="Only Deform Bones")
    add_leaf_bones: BoolProperty(name="Add Leaf Bones", default=True)
    armature_nodetype: EnumProperty(
        name="Armature FBXNode Type",
        items=[('NULL', "Null", ""), ('ROOT', "Root", ""), ('LIMBNODE', "LimbNode", "")],
        default='NULL'
    )
    primary_bone_axis: EnumProperty(
        name="Primary Bone Axis",
        items=[(x, x, "") for x in ['X', 'Y', 'Z', '-X', '-Y', '-Z']],
        default='Y'
    )
    secondary_bone_axis: EnumProperty(
        name="Secondary Bone Axis",
        items=[(x, x, "") for x in ['X', 'Y', 'Z', '-X', '-Y', '-Z']],
        default='X'
    )

class FBX_PT_export_main(Panel):
    bl_label = "FBX Action Export"
    bl_idname = "FBX_PT_export_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Armature Tools"

    def draw(self, context):
        pass

class FBX_PT_path(Panel):
    bl_label = "Export Path"
    bl_parent_id = "FBX_PT_export_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Armature Tools"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.fbx_export, "export_path")

class FBX_PT_transform(Panel):
    bl_label = "Transform"
    bl_parent_id = "FBX_PT_export_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Armature Tools"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        p = context.scene.fbx_export
        layout = self.layout
        layout.prop(p, "global_scale")
        layout.prop(p, "apply_scale_options")
        layout.prop(p, "axis_forward")
        layout.prop(p, "axis_up")
        layout.prop(p, "apply_unit_scale")
        layout.prop(p, "use_space_transform")
        layout.prop(p, "bake_space_transform")

class FBX_PT_geometry(Panel):
    bl_label = "Geometry"
    bl_parent_id = "FBX_PT_export_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Armature Tools"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        p = context.scene.fbx_export
        layout = self.layout
        layout.prop(p, "mesh_smooth_type")
        layout.prop(p, "use_subsurf")
        layout.prop(p, "use_mesh_modifiers")
        layout.prop(p, "use_mesh_edges")
        layout.prop(p, "use_triangles")
        layout.prop(p, "use_tspace")
        layout.prop(p, "colors_type")
        layout.prop(p, "prioritize_active_color")

class FBX_PT_armature(Panel):
    bl_label = "Armature"
    bl_parent_id = "FBX_PT_export_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Armature Tools"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        p = context.scene.fbx_export
        layout = self.layout
        layout.prop(p, "primary_bone_axis")
        layout.prop(p, "secondary_bone_axis")
        layout.prop(p, "armature_nodetype")
        layout.prop(p, "use_armature_deform_only")
        layout.prop(p, "add_leaf_bones")

class FBX_PT_export_button(Panel):
    bl_label = "Export"
    bl_parent_id = "FBX_PT_export_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Armature Tools"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.operator("export_fbx.actions", text="Export All Actions")

class ExportAllActionsOperator(Operator):
    bl_idname = "export_fbx.actions"
    bl_label = "Export All Actions"

    def execute(self, context):
        obj = context.object
        p = context.scene.fbx_export

        if not obj or obj.type != 'ARMATURE':
            self.report({'ERROR'}, "Select an Armature")
            return {'CANCELLED'}

        if not p.export_path:
            self.report({'ERROR'}, "Set an export directory")
            return {'CANCELLED'}

        if not obj.animation_data:
            obj.animation_data_create()

        scene = context.scene
        old_start = scene.frame_start
        old_end = scene.frame_end
        exported = 0

        for action in bpy.data.actions:
            if not action.use_fake_user:
                continue

            start = int(action.frame_range[0])
            end = int(action.frame_range[1])
            track = obj.animation_data.nla_tracks.new()
            track.name = f"TEMP_{action.name}"
            strip = track.strips.new(action.name, start, action)
            strip.action_frame_start = start
            strip.action_frame_end = end

            scene.frame_start = start
            scene.frame_end = end
            filepath = os.path.join(p.export_path, f"{action.name}.fbx")

            try:
                bpy.ops.export_scene.fbx(
                    filepath=filepath,
                    global_scale=p.global_scale,
                    apply_scale_options=p.apply_scale_options,
                    axis_forward=p.axis_forward,
                    axis_up=p.axis_up,
                    apply_unit_scale=p.apply_unit_scale,
                    use_space_transform=p.use_space_transform,
                    bake_space_transform=p.bake_space_transform,
                    mesh_smooth_type=p.mesh_smooth_type,
                    use_subsurf=p.use_subsurf,
                    use_mesh_modifiers=p.use_mesh_modifiers,
                    use_mesh_edges=p.use_mesh_edges,
                    use_triangles=p.use_triangles,
                    use_tspace=p.use_tspace,
                    colors_type=p.colors_type,
                    prioritize_active_color=p.prioritize_active_color,
                    object_types={'ARMATURE'},
                    use_armature_deform_only=p.use_armature_deform_only,
                    add_leaf_bones=p.add_leaf_bones,
                    armature_nodetype=p.armature_nodetype,
                    primary_bone_axis=p.primary_bone_axis,
                    secondary_bone_axis=p.secondary_bone_axis
                )
                exported += 1
            except Exception as e:
                self.report({'WARNING'}, f"Export failed: {action.name}: {e}")

            obj.animation_data.nla_tracks.remove(track)

        scene.frame_start = old_start
        scene.frame_end = old_end
        self.report({'INFO'}, f"Exported {exported} actions")
        return {'FINISHED'}

classes = [
    FBXExportSettings,
    FBX_PT_export_main,
    FBX_PT_path,
    FBX_PT_transform,
    FBX_PT_geometry,
    FBX_PT_armature,
    FBX_PT_export_button,
    ExportAllActionsOperator
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.fbx_export = PointerProperty(type=FBXExportSettings)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.fbx_export

if __name__ == "__main__":
    register()
