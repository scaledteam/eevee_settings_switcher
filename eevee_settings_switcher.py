#
# Created by scaled
#

bl_info = {
    "name":         "Eevee settings switcher",
    "author":       "scaled",
    "blender":      (2,93,0),
    "version":      (0,1,0),
    "location":     "None",
    "description":  "Automaticly turn on and off Ambient Occulution and Screen Space Reflections when viewport mode changed from Material mode to Rendered mode. Useful for slow hardware.",
    "category":     "Render"
}

import bpy
    
handle = object()

def notify_test(*args):
    my_viewport = None

    for area in bpy.context.screen.areas: 
        if area.type == 'VIEW_3D':
            for space in area.spaces: 
                if space.type == 'VIEW_3D':
                    my_viewport = space

    if my_viewport.shading.type == 'MATERIAL':
        bpy.context.scene.eevee.use_gtao = False
        bpy.context.scene.eevee.use_ssr = False
    elif my_viewport.shading.type == 'RENDERED':
        bpy.context.scene.eevee.use_gtao = True
        bpy.context.scene.eevee.use_ssr = True

def register():
	bpy.msgbus.subscribe_rna(
	    key=bpy.types.View3DShading,
	    owner=handle,
	    args=(),
	    notify=notify_test,
	)
	#bpy.msgbus.publish_rna(key=subscribe_to)

def unregister():
	bpy.msgbus.clear_by_owner(handle)
 
if __name__ == "__main__":
    register()
