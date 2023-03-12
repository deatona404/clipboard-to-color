# This script converts the current clipboard text to the foreground color
# in Krita. If the clipboard text is formatted incorrectly, it will not
# succeed.
#
# This script uses regex matching to find the first valid color format
# in the clipboard text string. 
#
# Supported color formats:
#       Hexcode: AAAAAA
#       Hexcode with #: #AAAAAA


from PyQt5.QtGui import (
        QColor,
        QPen,
        QBrush,
        QPainter,
        QClipboard)

from krita import *

# -----------------------------------------------------------------------------
# Some function definitions for code cleanup
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
    Returns a ManagedColor color constructed from a text string in the hexcode
    format.

    ARGUMENTS: text (string in hexcode form)

    RETURNS: color (ManagedColor)
'''
def hexCodeToManagedColor(text) -> ManagedColor:
    color = ManagedColor("RGBA", "U8", "")
    colorComponents = color.components()

    print(int((text[0:2]), 16)/255)
    print(int((text[2:4]), 16)/255)
    print(int((text[4:6]), 16)/255)

    colorComponents[2] = int((text[0:2]), 16)/255
    colorComponents[1] = int((text[2:4]), 16)/255
    colorComponents[0] = int((text[4:6]), 16)/255
    colorComponents[3] = 1.0

    color.setComponents(colorComponents)

    return color

'''
    Returns a ManagedColor color based on the input text string.

    ARGUMENTS: text (string in a valid color format)

    RETURNS: color (ManagedColor)
'''
def textToColor(text) -> ManagedColor:
    # TODO: there will be an if-stack here for rgb and hsl and other conversions
    # but for now it will just call hexcode
    return hexCodeToManagedColor(text)


# -----------------------------------------------------------------------------
# Main script
# -----------------------------------------------------------------------------


# get clipboard color

text = getClipboardText()


# convert to ManagedColor color

color = textToColor(text)


# set to the foreground color
Application.activeWindow().activeView().setForeGroundColor(color)