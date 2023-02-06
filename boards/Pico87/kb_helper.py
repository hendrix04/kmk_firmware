class Passwords():
    work = ''

class Utils():
    def CreateHotkey(KC, key):
        return KC.LCTL(KC.LSFT(KC.LALT(KC.LGUI(KC[key]))))

    def CreateLockHotkey(KC):
        return KC.LCTL(KC.LGUI(KC['Q']))
