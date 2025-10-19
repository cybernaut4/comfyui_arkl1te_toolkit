from inspect import cleandoc
from comfy.comfy_types.node_typing import IO
import os

class PadZeroes:
    """
    Takes an `int` number and outputs it with padded zeroes as a `string`.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int_field": ("INT", {
                    "default": 0,
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),   
                "quantity": ("INT", {
                    "default": 4,
                    "display": "number"
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "padZeroes"
    CATEGORY = "Arkl1te's Toolkit/string"

    def padZeroes(self, int_field, quantity=None):
        quantity = 4 if quantity is None else quantity
        padded = str(int_field).zfill(quantity)
        return (padded,)
    
class AnythingToString:
    """
    Takes any type of value and outputs it as a `string`.
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required":
            {
                "input": (IO.ANY,)
            }
        }
    
    RETURN_TYPES = ("STRING",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "convertToString"
    CATEGORY = "Arkl1te's Toolkit/string"


    def convertToString(self, input):
        string = str(input,)
        return (string,)
        
class Concatenate:
    """
    Concatenate or join strings, with the optionality to add a **prefix** and a **suffix**.

    NOTE: **prefix** uses the final string as reference, __not__ string_b ! 
    Be mindful if you're using it for *file paths*!
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required":
            {
                "string_a": ("STRING",),
                "string_b": ("STRING",)
            },
            "optional":
            {
                "prefix": ("STRING",),
                "suffix": ("STRING",),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "concatenate"
    CATEGORY = "Arkl1te's Toolkit/string"


    def concatenate(self, string_a, string_b, prefix, suffix):
        concatenated = ""
        concatenated = prefix + string_a if prefix else string_a
        concatenated = concatenated + string_b
        if suffix:
            concatenated = concatenated + suffix
        
        return (concatenated,)
    

class GetNewFileIndex:
    """
    Counts how many files with the **extension** are in the **directory**.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "directory": ("STRING", {
                    "default": "",
                    "file_select": "directory",
                }),
                "extension": ("STRING", {
                    "default": "mp4"
                }),
            }
        }
    
    RETURN_TYPES = ("INT",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "countFilesWithExtension"
    CATEGORY = "Arkl1te's Toolkit/string"

    def countFilesWithExtension(self, directory, extension):
        comfyui_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

        directory = (comfyui_root + "\\output\\" + directory.replace("/", "\\"))
        extension = "." + extension.lower()

        return (len([f for f in os.listdir(directory) if f.lower().endswith(extension)]),)

        

NODE_CLASS_MAPPINGS = {
    "PadZeroes": PadZeroes,
    "AnythingToString": AnythingToString,
    "Concatenate": Concatenate,
    "GetNewFileIndex": GetNewFileIndex,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PadZeroes": "Pad Zeroes",
    "AnythingToString": "Anything To String",
    "Concatenate": "Concatenate",
    "GetNewFileIndex": "Get New File Index",
}
