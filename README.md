# clipboard-to-color
This is a Python plugin for Krita that copies the color code (hexcode, rgb, etc) in your clipboard to your current Foreground Color.

### Supported Formats:[^1]
* Hexcode:                ffaa00
* Hexcode with alpha[^2]:     #ffaa0011 
* RGB:                    rgb(239, 104, 255)
* RGBA:                   rgba(239, 104, 255, 0.3)

[^1]: Scans for first regex match for these formats. It would match asflkdsABABCD, kahds#692738, etc. as a hexcode.
[^2]: Opacity is not supported for Foreground Colors, so the Opacity of the current Brush Preset is changed instead.

## Installation

<!-- ### Recommended Method:
### Manual Method: -->

Put the .action file (``ClipboardToColor.action``) in KRITA/actions 

Put everything else (the ``clipboard_to_color`` folder) in KRITA/pykrita

where KRITA is the krita's resource folder.

## Usage

After enabling this plugin, restart Krita. 
Then, go to the 
``Settings / Configure Krita / Keyboard Shortcuts: Scripts / My Scripts``
section and look for the keyboard shortcut labelled ``Clipboard to Color``.

Then, assign a keyboard binding to the shortcut.

To test this, go ahead and copy some sort of color code (ex. ``#696969``) 
and then use the shortcut while focused on the Krita window. 
It should be your new foreground color!