from rfidscanner import RfidScanner
import sys

class Main:
    '''Main Class'''

    def __init__(self):
        s = RfidScanner()
        s.readCardLoop()

if __name__ == "__main__":
    Main()
