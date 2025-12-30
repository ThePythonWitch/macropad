import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

layers = Layers()
macros = Macros()
keyboard.modules.append(macros)
keyboard.modules.append(layers)

PINS = [board.D3, board.D4, board.D2, board.D1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.MACRO("git status\n"),
     KC.MACRO("git add .\n"),
     KC.MACRO("git pull\n"), 
     KC.LT(1, Macro("git push\n")),
    ],
    [KC.MACRO("ls\n"),
     KC.MACRO("pwd\n"),
     KC.MACRO("cd ..\n"),
     KC.MACRO("clear\n"),
    ] 
]


if __name__ == '__main__':
    keyboard.go()
