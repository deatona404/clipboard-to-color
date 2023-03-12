
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

def getClipboardText():
    clipboard = QGuiApplication.clipboard()
    text = clipboard.text()
    return text


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