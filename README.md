![LOGO for Clipboard to Color plugin](./.assets/clipboard-to-color-logo.png)

# clipboard-to-color
This is a Python plugin for Krita that copies the color code (hexcode, rgb, etc) in your clipboard to your current Foreground Color.

### Supported Formats:[^1]
| Format | Example |
| ------ | ------ |
Hexcode:         |       ``ffaa00``
Hexcode with alpha[^2]:  |   ``#ffaa0011 ``
RGB:          |          ``rgb(239, 104, 255)``
RGBA:            |       ``rgba(239, 104, 255, 0.3)``

[^1]: Scans for first regex match for these formats. It would match asflkdsABABCD, kahds#692738, etc. as a hexcode.
[^2]: Opacity is not supported for Foreground Colors, so the Opacity of the current Brush Preset is changed instead.

## Installation

<!-- ### Recommended Method:
### Manual Method: -->

Go to the button that says "<> Code" near the top of the page. Click it, then click ``Download ZIP``.

Put the .action file (``actions/ClipboardToColor.action``) in KRITA/actions 

Put everything else (the ``./clipboard_to_color`` folder) in KRITA/pykrita

where KRITA is Krita's Resource Folder.

## Usage

After enabling this plugin, restart Krita. 
Then, go to the 
``Settings / Configure Krita / Keyboard Shortcuts: Scripts / My Scripts``
section and look for the keyboard shortcut labelled ``Clipboard to Color``.

Then, assign a keyboard binding to the shortcut.

To test this, go ahead and copy some sort of color code (ex. ``#042069``, a nice dark blue) and then use the shortcut while focused on the Krita window. 
It should be your new foreground color! 

## Inspiration

I recently installed Microsoft PowerToys and made frequent use of the ColorPicker tool it adds to colorpick various things on my screen and not in Krita. Unfortunately, the only method I could find to get that hexcode into Krita for work was opening up the color palette and manually pasting it in. Obviously, that impedes workflow, so I threw a script together and made it a plugin.


## Limitations

Currently, this plugin has only been made and developed around the RGB color space. Support for CMYK is unlikely at this time.