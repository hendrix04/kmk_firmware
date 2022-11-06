import board

from kb import KMKKeyboard

# Remove this if you need to push up for some reason
from kb_helper import Passwords, Utils

from kmk.consts import UnicodeMode
from kmk.extensions.lock_status import LockStatus
from kmk.extensions.stringy_keymaps import StringyKeymaps
from kmk.handlers.sequences import send_string, compile_unicode_string_sequences as cuss
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.layers import Layers

Pico87 = KMKKeyboard()
pswd = Passwords()

Pico87.unicode_mode = UnicodeMode.OSX
Pico87.extensions.append(MediaKeys())

class LEDLockStatus(LockStatus):
    def set_lock_leds(self):
        if self.get_caps_lock():
            Pico87.leds.set_brightness(50, leds=[0])
        else:
            Pico87.leds.set_brightness(0, leds=[0])

        if self.get_scroll_lock():
            Pico87.leds.set_brightness(50, leds=[1])
        else:
            Pico87.leds.set_brightness(0, leds=[1])

    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)  # Critically important. Removing this will break lock status.

        if self.report_updated:
            self.set_lock_leds()


Pico87.modules.append(Layers())
Pico87.extensions.append(LEDLockStatus())
Pico87.extensions.append(StringyKeymaps())

MOLYR = KC.MO(1)
PASSWD = send_string(pswd.work)

# Unicode stuff
unicodes = cuss({
    'SHRG': '¯\_(ツ)_/¯',
})

# Copy values into variables so that they work better
# in the keyboard layout.
SHRG = unicodes.SHRG
# SHRG = unicode_codepoint_sequence([
#     '00af', '005c', '005f', '0028', '30c4',
#     '0029', '005f', '002f', '00af'
# ])

MUTE = Utils.CreateHotkey(KC, 'N1')
VSCODE = Utils.CreateHotkey(KC, 'N2')
LOCK = Utils.CreateLockHotkey(KC)

# Make this for better looking formatting...
______ = 'NO'

Pico87.keymap = [[
  # Layer 0 QWERTY
    'ESC', ______, VSCODE,   'F2',   MUTE,   'F4', ______,   'F5',   'F6',   'F7',   'F8',   'F9',  'F10',  'F11',  'F12', 'PSCR', 'SLCK', 'PAUS',
    'GRV',   'N1',   'N2',   'N3',   'N4',   'N5',   'N6',   'N7',   'N8',   'N9',   'N0', 'MINS',  'EQL', ______, 'BSPC',  'INS', 'HOME', 'PGUP',
    'TAB', ______,    'Q',    'W',    'E',    'R',    'T',    'Y',    'U',    'I',    'O',    'P', 'LBRC', 'RBRC', 'BSLS',  'DEL',  'END', 'PGDN',
   'CAPS', ______,    'A',    'S',    'D',    'F',    'G',    'H',    'J',    'K',    'L', 'SCLN', 'QUOT',  'ENT', ______, ______, ______, ______,
   ______, 'LSFT',    'Z',    'X',    'C',    'V',    'B',    'N',    'M', 'COMM',  'DOT', 'SLSH', ______, 'RSFT', ______, ______,   'UP', ______,
   'LCTL', 'LALT', ______, 'LGUI', ______, ______,  'SPC', ______, ______, ______, 'RGUI', 'RALT', ______,  MOLYR, 'RCTL', 'LEFT', 'DOWN', 'RGHT',
], [
  # Layer 1
    'ESC', ______, VSCODE,   'F2',   MUTE,   'F4', ______,   'F5',   'F6',   'F7',   'F8',   'F9',  'F10',  'F11',  'F12', 'PSCR', 'SLCK', 'MUTE',
    'GRV',   'N1',   'N2',   'N3',   'N4',   'N5',   'N6',   'N7',   'N8',   'N9',   'N0', 'MINS',  'EQL', ______, 'BSPC', 'MPLY',   LOCK, 'VOLU',
    'TAB', ______,    'Q',    'W',    'E',    'R',    'T',    'Y',    'U',    'I',    'O',    'P', 'LBRC', 'RBRC', 'BSLS', 'MRWD', 'MFFD', 'VOLD',
   'CAPS', ______,    'A',    'S',    'D',    'F',    'G',    'H',    'J',    'K',    'L', 'SCLN', 'QUOT',  'ENT', ______, ______, ______, ______,
   ______, 'LSFT',    'Z',    'X',    'C',    'V',    'B',    'N',    'M', 'COMM',  'DOT', PASSWD, ______,   SHRG, ______, ______,   'UP', ______,
   'LCTL', 'LALT', ______, 'LGUI', ______, ______,  'SPC', ______, ______, ______, 'RGUI', 'RALT', ______, 'TRNS', 'RCTL', 'LEFT', 'DOWN', 'RGHT',
]]

if __name__ == '__main__':
    Pico87.go()
