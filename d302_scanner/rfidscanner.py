
import os
import sys
import serial
import time

from keyboard import KeyboardWriter

class RfidScanner:

    prot = {}
    ser = None
    reader_loc = ''

    def __init__(self):
        ''' Establish connection with scanner '''
        global reader_loc
        global prot
        global ser
        reader_loc = '/dev/cu.wchusbserial1410'
        prot = {
        'initiate_connection': '\x02\x01\x00\x00\x03\x03',
        'read_card': '\x02\x01\xa4\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xac\x03',
        }
        try:
            ser = serial.Serial(reader_loc,4800,timeout=1)
        except:
            print "Failed to locate scanner"
            sys.exit(1)
        ser.write(prot['initiate_connection'])
        resp =  ser.read(6)
        if resp == prot['initiate_connection']:
            print "Connection established"
            time.sleep(1)
            # Initialise keyboard
            self.kb = KeyboardWriter()
        else:
            print "Failed to establish connection to scanner"
            sys.exit(1)

    def readCardLoop(self):
        ''' Read cards forever! '''
        while True:
            ser.write(prot['read_card'])
            resp = ser.read(11)
            if len(resp) != 11:
                #print "failed to read card"
                time.sleep(0.5)
            else:
                tmp = resp[4:9].encode('hex')
                #print int("".join(tmp), 16)
                self.kb.write(str(int("".join(tmp), 16)))
                time.sleep(2)

    def readSingleCard(self):
        ''' Read Single RFID card '''
        ser.write(prot['read_card'])
        resp = ser.read(11)
        if len(resp) != 11:
            print "failed to read card"
            time.sleep(0.5)
        else:
            tmp = resp[4:9].encode('hex')
            print int("".join(tmp), 16)

    def writeCard(self):
        '''TODO'''

    def closeConnection(self):
        try:
            ser.close()
        except:
            e = sys.exc_info()[0]
            print e
