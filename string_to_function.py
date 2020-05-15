import bpy
from bpy.types import NodeTree, Node, NodeSocket
from nodeitems_utils import (
    NodeCategory,
    NodeItem,
    NodeItemCustom,
)

var_index = "1"
a = int(var_index)
b = ""

# Enum items list
modeItems = (
    ('RADIANS', "Radians", "Activate Radians"),
    ('DEGREES', "Degrees", "Activate Degrees"),        
)

my_enum_prop: bpy.props.EnumProperty(
    name="Angle",
    description="Angle in Degrees or Radians",
    items=modeItems,
    default='DEGREES',
)

class StringToFunctionNode(bpy.types.Node):
    bl_idname = "string.to_function"
    bl_label = "String to Function"
    
    mode = bpy.props.EnumProperty(name = "Angle", 
    description="Angle in Degrees or Radians", 
    default = "DEGREES", 
    items = modeItems)
    
    # Angle or Degrees Dropdown
    def draw(self, layout):
        layout.prop(self, "mode")
    
    # Additional buttons displayed on the node.
    def draw_buttons(self, context, layout):
        layout.label(text="Function Input")
    
    # String Input
    def string_input(self):
        pass
    
    # Creating VarXY Input Sockets & Output Socket
    def create(self):
        for i in range (a):
            b = str(i)
            self.inputs.new('NodeSocketFloat', "Var 0" + b)        
        self.outputs.new('NodeSocketFloat', "Value")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

def node_add_menu_draw(self, context):
    self.layout.Operator('string.to_function')

import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem

def register():
    bpy.utils.register_class(StringToFunctionNode)
    bpy.types.NODE_MT_category_SH_NEW_CONVERTOR.append(node_add_menu_draw)
#    nodeitems_utils.register_node_categories('SHADER', NodeItem("ShaderNodeTexCoord"))

def unregister():
    bpy.utils.unregister_class(StringToFunctionNode)
    bpy.types.NODE_MT_category_SH_NEW_CONVERTOR.remove(node_add_menu_draw)

if __name__ == "__main__":
    register()