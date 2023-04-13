# This script converts the current clipboard text to the foreground color
# in Krita. If the clipboard text is formatted incorrectly, it will not
# succeed.
#
# This script uses regex matching to find the first valid color format
# in the clipboard text string. 
#
# Supported color formats:
#       Hexcode:                ffaa00
#       Hexcode with alpha:     #ffaa0011 
#       RGB:                    rgb(239, 104, 255)
#       RGBA:                   rgba(239, 104, 255, 0.3)

# To add support for a new color format, you must:
#   1. add it to the Format enum
#               example: HEXCODE = 1
#   2. add it to the global formatsList (and come up with a regex pattern!)
#               example: [Format.HEXCODE, "([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"]
#   3. make a helper function that returns a ManagedColor with the color format as input
#               example: def hexCodeToManagedColor(text) -> ManagedColor:
#   4. edit the textToColor() if-else stack to have a case for the color format
#               example: if FORMAT == Format.HEXCODE:
#                   return hexCodeToManagedColor(text)
#   5. add it to the list of supported color formats in the comment above and in README.md



from PyQt5.QtGui import (
        QColor,
        QPen,
        QBrush,
        QPainter,
        QClipboard)

from krita import *

import re

from enum import Enum

# Enums for supported color formats:
class Format(Enum):
    HEXCODE = 1
    HEXCODE_ALPHA = 2

    RGB = 3
    RGBA = 4

formatsList = [
    [Format.HEXCODE, "([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"],
    [Format.HEXCODE_ALPHA, "([A-Fa-f0-9]{8})$"],
    [Format.RGB, "rgb\(\d+,\s\d+,\s\d+\)"],
    [Format.RGBA, "rgba\(\d+,\s\d+,\s\d+,\s0?\.\d+\)"]

    ]

# global variable for format of this execution
FORMAT = -1


# --------------------------------------------------------------------------------------
# Below are all the functions we use!!
# --------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Here are the specific format helper functions (all should return ManagedColor)
# -----------------------------------------------------------------------------

'''
    Returns a ManagedColor color constructed from a text string in the hexcode
    format.

    ARGUMENTS: text (string in hexcode form)

    RETURNS: color (ManagedColor)
'''
def hexCodeToManagedColor(text) -> ManagedColor:
    color = ManagedColor("RGBA", "U8", "")
    colorComponents = color.components()

    red = int((text[0:2]), 16)
    green = int((text[2:4]), 16)
    blue = int((text[4:6]), 16)

    colorComponents[2] = red/255
    colorComponents[1] = green/255
    colorComponents[0] = blue/255
    colorComponents[3] = 1.0

    color.setComponents(colorComponents)

    return color

'''
    Returns a ManagedColor color constructed from a text string in the hexcode with alpha
    format.

    ARGUMENTS: text (string in hexcode alpha form)

    RETURNS: color (ManagedColor)
'''
def hexCodeAlphaToManagedColor(text) -> ManagedColor:
    color = ManagedColor("RGBA", "U8", "")
    colorComponents = color.components()

    red = int((text[0:2]), 16)
    green = int((text[2:4]), 16)
    blue = int((text[4:6]), 16)
    alpha = int((text[6:8]), 16)

    colorComponents[2] = red/255
    colorComponents[1] = green/255
    colorComponents[0] = blue/255
    colorComponents[3] = alpha/255

    color.setComponents(colorComponents)

    return color


'''
    Returns a ManagedColor color constructed from a text string in the rgb
    format.

    ARGUMENTS: text (string in rgb form)

    RETURNS: color (ManagedColor)
'''
def rgbToManagedColor(text) -> ManagedColor:
    color = ManagedColor("RGBA", "U8", "")
    colorComponents = color.components()

    splice = re.findall('\d+', text)

    red = int(splice[0])
    green = int(splice[1])
    blue = int(splice[2])


    colorComponents[2] = red/255
    colorComponents[1] = green/255
    colorComponents[0] = blue/255
    colorComponents[3] = 1.0

    color.setComponents(colorComponents)

    return color


'''
    Returns a ManagedColor color constructed from a text string in the rgba
    format.

    ARGUMENTS: text (string in rgba form)

    RETURNS: color (ManagedColor)
'''
def rgbaToManagedColor(text) -> ManagedColor:
    color = ManagedColor("RGBA", "U8", "")
    colorComponents = color.components()

    splice = re.findall('\d+', text)
    alphaval = re.findall("0?\.\d+", text)

    red = int(splice[0])
    green = int(splice[1])
    blue = int(splice[2])
    alpha = float(alphaval[0])


    colorComponents[2] = red/255
    colorComponents[1] = green/255
    colorComponents[0] = blue/255
    colorComponents[3] = alpha

    color.setComponents(colorComponents)

    return color


# -----------------------------------------------------------------------------
# Here are general functions that make it work
# -----------------------------------------------------------------------------

'''
    Returns a text string representing the most recent item in the system 
    clipboard.

    RETURNS: text (string)
'''
def getClipboardText():
    clipboard = QGuiApplication.clipboard()
    text = clipboard.text()
    return text



'''
    Returns a ManagedColor color based on the input text string.

    ARGUMENTS: text (string in a valid color format)

    RETURNS: color (ManagedColor)
'''
def textToColor(text) -> ManagedColor:

    if FORMAT == Format.HEXCODE:
        return hexCodeToManagedColor(text)
    elif FORMAT == Format.HEXCODE_ALPHA:
        return hexCodeAlphaToManagedColor(text)
    elif FORMAT == Format.RGB:
        return rgbToManagedColor(text)
    elif FORMAT == Format.RGBA:
        return rgbaToManagedColor(text)

    print("error converting filtered text to color")
    return None # error



'''
    Returns a Match object relating to the first valid color format found
    in the input text string.

    ARGUMENTS: text (string hopefully with a valid color format)

    RETURNS: match (Match)
             FORMAT global variable is also set accordingly
'''
def findFormat(text):
    match = None

    # iterate through every supported format and try to find a match
    # then, our match is the currMatch with the lowest index found
    for item in formatsList:
        # perform the search
        pattern = item[1]
        currMatch = re.search(pattern, text, flags=re.IGNORECASE)
        # update our return value if this is the new minimum index
        if(currMatch):
            if(not match or currMatch.span()[0] <= match.span()[0]):
                match = currMatch
                global FORMAT
                FORMAT = item[0] # return the format to the global var
    
    return match


# --------------------------------------------------------------------------------------
# Main script
# --------------------------------------------------------------------------------------


# get clipboard text

text = getClipboardText()

# find format

match = findFormat(text)
if match == None:
    print("no match found in clipboard text string; do nothing")
else:
    lowerBound = int(match.span()[0])
    upperBound = int(match.span()[1])
    filteredText = text[lowerBound:upperBound]

    # convert to ManagedColor color
    color = textToColor(filteredText)
    
    if(color): # if it didnt error, then set it!

        # set to the foreground color
        Application.activeWindow().activeView().setForeGroundColor(color)
        print("changed color successfully") # TODO: delete this later; for debugging rn
        
        # we can't actually impact color opacity so change the brush opacity
        Application.activeWindow().activeView().setPaintingOpacity(color.components()[3])
