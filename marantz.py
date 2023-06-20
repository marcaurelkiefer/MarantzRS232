import cec
import serial

class Marantz(object):
    
    serial_device = "/dev/ttyUSB0"

    def connect(self):
        self.ser = serial.Serial(self.serial_device)
    
    def write(self, command):
        self.ser.write((command+"\r").encode())

    def read(self):
        return self.ser.read_until(b"\r")
    
    def test(self):
        self.write("@PWR:?")
        print(self.read())