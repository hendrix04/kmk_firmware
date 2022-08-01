import board
<<<<<<< HEAD

from kb import KMKKeyboard

from kmk.extensions.lock_status import LockStatus
from kmk.extensions.stringy_keymaps import StringyKeymaps
from kmk.keys import KC
from kmk.modules.layers import Layers

Pico87 = KMKKeyboard()


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

# Make this for better looking formatting...
______ = 'NO'

Pico87.keymap = [[
  # Layer 0 QWERTY
    'ESC', ______,   'F1',   'F2',   'F3',   'F4', ______,   'F5',   'F6',   'F7',   'F8',   'F9',  'F10',  'F11',  'F12', 'PSCR', 'SLCK', 'PAUS',
    'GRV',   'N1',   'N2',   'N3',   'N4',   'N5',   'N6',   'N7',   'N8',   'N9',   'N0', 'MINS',  'EQL', ______, 'BSPC',  'INS', 'HOME', 'PGUP',
    'TAB', ______,    'Q',    'W',    'E',    'R',    'T',    'Y',    'U',    'I',    'O',    'P', 'LBRC', 'RBRC', 'BSLS',  'DEL',  'END', 'PGDN',
   'CAPS', ______,    'A',    'S',    'D',    'F',    'G',    'H',    'J',    'K',    'L', 'SCLN', 'QUOT',  'ENT', ______, ______, ______, ______,
   ______, 'LSFT',    'Z',    'X',    'C',    'V',    'B',    'N',    'M', 'COMM',  'DOT', 'SLSH', ______, 'RSFT', ______, ______,   'UP', ______,
   'LCTL', 'LGUI', ______, 'LALT', ______, ______,  'SPC', ______, ______, ______, 'RALT', 'RGUI', ______,  MOLYR, 'RCTL', 'LEFT', 'DOWN', 'RGHT',
], [
  # Layer 1
    'ESC', ______,   'F1',   'F2',   'F3',   'F4', ______,   'F5',   'F6',   'F7',   'F8',   'F9',  'F10',  'F11',  'F12', 'PSCR', 'SLCK', 'PAUS',
    'GRV',   'N1',   'N2',   'N3',   'N4',   'N5',   'N6',   'N7',   'N8',   'N9',   'N0', 'MINS',  'EQL', ______, 'BSPC',  'INS', 'HOME', 'PGUP',
    'TAB', ______,    'Q',    'W',    'E',    'R',    'T',    'Y',    'U',    'I',    'O',    'P', 'LBRC', 'RBRC', 'BSLS',  'DEL',  'END', 'PGDN',
   'CAPS', ______,    'A',    'S',    'D',    'F',    'G',    'H',    'J',    'K',    'L', 'SCLN', 'QUOT',  'ENT', ______, ______, ______, ______,
   ______, 'LSFT',    'Z',    'X',    'C',    'V',    'B',    'N',    'M', 'COMM',  'DOT', 'SLSH', ______, 'RSFT', ______, ______,   'UP', ______,
   'LCTL', 'LGUI', ______, 'LALT', ______, ______,  'SPC', ______, ______, ______, 'RALT', 'RGUI', ______,  MOLYR, 'RCTL', 'LEFT', 'DOWN', 'RGHT',
]]
=======
from kb import KMKKeyboard
from kmk.modules.layers import Layers
from kmk.keys import KC

Pico87 = KMKKeyboard()

layers = Layers()
Pico87.modules = [layers]

Pico87.keymap = [
   
  [ # Layer 0 QWERTY
KC.ESC,   KC.NO, KC.F1, KC.F2,  KC.F3,  KC.F4, KC.NO,  KC.F5, KC.F6, KC.F7,   KC.F8,   KC.F9,    KC.F10,   KC.F11,  KC.F12, KC.PSCREEN, KC.SCROLLLOCK, KC.PAUSE,
KC.GRAVE, KC.N1, KC.N2, KC.N3,  KC.N4,  KC.N5, KC.N6,  KC.N7, KC.N8, KC.N9,   KC.N0,   KC.MINUS, KC.EQUAL, KC.NO,     KC.BSPC, KC.INS,  KC.HOME,       KC.PGUP,
KC.TAB,   KC.NO,  KC.Q,  KC.W,   KC.E,   KC.R,  KC.T,   KC.Y,  KC.U,  KC.I,    KC.O,    KC.P,     KC.LBRC,  KC.RBRC,   KC.BSLS, KC.DEL, KC.END,       KC.PGDN,
KC.CAPS,  KC.NO,    KC.A,  KC.S,   KC.D,   KC.F,  KC.G,   KC.H,  KC.J,  KC.K,    KC.L,    KC.SCLN,  KC.QUOT,  KC.ENT,    KC.NO, KC.NO,      KC.NO,      KC.NO,
KC.NO,    KC.LSHIFT, KC.Z,  KC.X,   KC.C,   KC.V,  KC.B,   KC.N,  KC.M,  KC.COMM, KC.DOT,  KC.SLSH,  KC.NO,    KC.RSHIFT, KC.NO,    KC.NO,   KC.UP,   KC.NO,
KC.LCTL,  KC.LGUI,   KC.NO, KC.LALT, KC.NO, KC.NO, KC.SPC, KC.NO, KC.NO, KC.NO,   KC.RALT, KC.RGUI,  KC.NO,    KC.MO(1),     KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT,
  ],
  
    [# Layer 1
KC.ESC,   KC.NO, KC.F1, KC.F2,  KC.F3,  KC.F4, KC.NO,  KC.F5, KC.F6, KC.F7,   KC.F8,   KC.F9,    KC.F10,   KC.F11,  KC.F12, KC.PSCREEN, KC.SCROLLLOCK, KC.PAUSE,
KC.GRAVE, KC.N1, KC.N2, KC.N3,  KC.N4,  KC.N5, KC.N6,  KC.N7, KC.N8, KC.N9,   KC.N0,   KC.MINUS, KC.EQUAL, KC.NO,     KC.BSPC, KC.INS,  KC.HOME,       KC.PGUP,
KC.TAB,   KC.NO,  KC.Q,  KC.W,   KC.E,   KC.R,  KC.T,   KC.Y,  KC.U,  KC.I,    KC.O,    KC.P,     KC.LBRC,  KC.RBRC,   KC.BSLS, KC.DEL, KC.END,       KC.PGDN,
KC.CAPS,  KC.NO,    KC.A,  KC.S,   KC.D,   KC.F,  KC.G,   KC.H,  KC.J,  KC.K,    KC.L,    KC.SCLN,  KC.QUOT,  KC.ENT,    KC.NO, KC.NO,      KC.NO,      KC.NO,
KC.NO,    KC.LSHIFT, KC.Z,  KC.X,   KC.C,   KC.V,  KC.B,   KC.N,  KC.M,  KC.COMM, KC.DOT,  KC.SLSH,  KC.NO,    KC.RSHIFT, KC.NO,    KC.NO,   KC.UP,   KC.NO,
KC.LCTL,  KC.LGUI,   KC.NO, KC.LALT, KC.NO, KC.NO, KC.SPC, KC.NO, KC.NO, KC.NO,   KC.RALT, KC.RGUI,  KC.NO,    KC.MO(1),     KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT,
  ],
]

>>>>>>> ea474c5 (Create main.py)

if __name__ == '__main__':
    Pico87.go()
