import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.hid import HIDModes

HHK = KMKKeyboard()
HHK.col_pins = (board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10 ,board.GP11,   board.GP12,board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18)
HHK.row_pins = (board.GP21, board.GP22, board.GP26, board.GP27, board.GP28)
HHK.diode_orientation = DiodeOrientation.COLUMNS
HHK.modules.append(Layers())

HHK.keymap = [
    [
        KC.ESC, KC.N1,  KC.N2,          KC.N3,  KC.N4,  KC.N5,  KC.N6,  KC.N7,  KC.N8,  KC.N9,  KC.N0,  KC.MINS,KC.EQL, KC.JYEN,KC.BKSP,    KC.INS, KC.HOME, KC.PGUP,
        KC.ZKHK,KC.Q,   KC.W,           KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,   KC.LBRC,KC.RBRC,KC.BKSP,KC.ENT,     KC.DEL, KC.END,  KC.PGDN,
        KC.CAPS,KC.A,   KC.S,           KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.K,   KC.L,   KC.SCLN,KC.QUOT,KC.BSLS,KC.ENT, KC.N3,      KC.N1, KC.N2, KC.N3,
        KC.LSFT,KC.Z,   KC.X,           KC.C,   KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM,KC.DOT, KC.SLSH,KC.RO,  KC.RSFT,KC.N3,  KC.N4,      KC.N1, KC.UP,   KC.N3,
        KC.LCTL,KC.LWIN,KC.LM(2,KC.LALT),KC.TAB,KC.MHEN,KC.MHEN,KC.HENK,KC.HENK,KC.SPC, KC.KANA,KC.RALT,KC.MO(1),KC.RCTL,KC.DOWN,KC.RIGHT,  KC.LEFT, KC.DOWN, KC.RIGHT,
    ],
        [
        KC.ESC, KC.F1,  KC.F2,          KC.F3,  KC.F4,  KC.F5,  KC.F6,  KC.F7,  KC.F8,  KC.F9,  KC.F10, KC.F11, KC.F12, KC.F13, KC.F14,     KC.F15,KC.F16,KC.F17,
        KC.TAB, KC.Q,   KC.W,           KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,   KC.UP,  KC.RBRC,KC.BKSP,KC.N2,      KC.DEL, KC.END,  KC.PGDN,
        KC.CAPS,KC.A,   KC.S,           KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.K,   KC.L,   KC.SCLN,KC.QUOT,KC.BSLS,KC.ENT, KC.N3,      KC.N1, KC.N2, KC.N3,
        KC.LSFT,KC.Z,   KC.X,           KC.C,   KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM,KC.DOT, KC.SLSH,KC.RO,  KC.RSFT,KC.N3,  KC.N4,      KC.N1, KC.UP,   KC.N3,
        KC.LCTL,KC.LWIN,KC.LALT,        KC.TAB, KC.MHEN,KC.MHEN,KC.HENK,KC.HENK,KC.SPC, KC.KANA,KC.RALT,KC.APP ,KC.RCTL,KC.DOWN,KC.RIGHT, KC.LEFT, KC.DOWN, KC.RIGHT,
    ],
        [
        KC.ZKHK,KC.N1,  KC.N2,          KC.N3,  KC.N4,  KC.N5,  KC.N6,  KC.N7,  KC.N8,  KC.N9,  KC.N0,  KC.MINS,KC.EQL, KC.JYEN,KC.BKSP,    KC.INS, KC.HOME, KC.PGUP,
        KC.TAB, KC.Q,   KC.W,           KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,   KC.LBRC,KC.RBRC,KC.BKSP,KC.ENT,     KC.DEL, KC.END,  KC.PGDN,
        KC.CAPS,KC.A,   KC.S,           KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.K,   KC.L,   KC.SCLN,KC.QUOT,KC.BSLS,KC.ENT, KC.N3,      KC.N1, KC.N2, KC.N3,
        KC.LSFT,KC.Z,   KC.X,           KC.C,   KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM,KC.DOT, KC.SLSH,KC.RO,  KC.RSFT,KC.N3,  KC.N4,      KC.N1, KC.UP,   KC.N3,
        KC.LCTL,KC.LWIN,KC.LALT,        KC.TAB, KC.MHEN,KC.MHEN,KC.HENK,KC.HENK,KC.SPC, KC.KANA,KC.RALT,KC.APP ,KC.RCTL,KC.DOWN,KC.RIGHT,   KC.LEFT, KC.DOWN, KC.RIGHT,
    ],
]

if __name__ == '__main__':
    HHK.go(hid_type=HIDModes.USB)
