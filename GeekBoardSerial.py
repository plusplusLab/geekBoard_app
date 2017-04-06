import serial
import sys
import struct
import time


class GeekBoard :

    # pin mapping between geekboard and arduino soft

    analogPinMap = {"1":0, "2":1, "3":2, "4":3}
    digitalPinMap = {"5":3, "6":5, "7":6, "8":9}
    activeAnalog = {True, True, False, False}
    activeDigital = {False, False, False, False}
    # get port from command line
    mySerial = None;

    def initGeekBoard(self, serial_port):
        #port is to be passed from : str(sys.argv[1])
        # init serial
        self.mySerial = serial.Serial(serial_port, 115200);
        self.activeAnalog = [True, True, False, False]
        self.activeDigital = [False, False, False, False]
        time.sleep(1)
        print "connected to GeekBoard on port: " + serial_port

    def setActiveAnalog(self, pin):
        self.activeAnalog[pin] = True

    def getActiveAnalog(self, pin):
        return self.activeAnalog[pin]

    def parseAnalogValue(self, val):
        hib = struct.unpack('B', val[0])[0]
        lob =  struct.unpack('B', val[1])[0]
        parsed = (hib<<8) + lob
        return parsed


    def getAnalogValue(self, pin):
        self.mySerial.write("GA"+struct.pack('B', pin))
        resp = self.mySerial.read(4)
        cmd = resp[0:1]

        if cmd == "A":
            print 'analog value'
            print struct.unpack('B', resp[1])[0]
            value =  self.parseAnalogValue(resp[2:4])
            return value

    def getDigitalValue(self, pin):
        self.mySerial.write("GD"+struct.pack('B', pin))
        resp = geekB.read(3)
        cmd = resp[0:1]

        if cmd == "D":
            print 'digital value'
            print struct.unpack('B', resp[1])[0]
            value =  struct_unpack('B', resp[2])[0]
            return value
