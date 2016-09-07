import applescript

class KeyboardWriter:

    def __init__(self):
        print "Keyboard Init"

    def writeKey(self, key):
        if key is "return":
            scpt = applescript.AppleScript('''
                tell application "System Events"
                key code 36
                end tell
            ''')
        else:
            scpt = applescript.AppleScript('''
                tell application "System Events"
                    keystroke "''' + key + '''"
                end tell
            ''')
        scpt.run()

    def write(self, code):
        for c in code:
            self.writeKey(c)
        self.writeKey("return")
