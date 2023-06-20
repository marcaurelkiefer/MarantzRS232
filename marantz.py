import cec
import serial

class Marantz(object):
    
    serial_device = "/dev/ttyUSB0"

    def connect(self):
        self.ser = serial.Serial(self.serial_device)
    
    def write(self, command):
        self.ser.write((command+"\r").encode())

    def command(self, command):
        self.write(command)
        return self.read()

    def read(self):
        return self.ser.read_until(b"\r")
    
    def power_status(self):
        return self.command("@PWR:?")

    def power_on(self):
        return self.command("@PWR:2")
    
    def power_off(self):
        return self.command("@PWR:1")
        