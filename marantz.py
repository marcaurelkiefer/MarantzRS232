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
    
    def volume_up(self):
        return self.command("@VOL:1")
    
    def volume_down(self):
        return self.command("@VOL:2")
        
    def volume_up_fast(self):
        return self.command("@VOL:3")
    
    def volume_down_fast(self):
        return self.command("@VOL:4")
    
    def volume_status(self):
         return self.command("@VOL:?")
    
    def source_status(self):
        return self.command("@SRC:?")
    
    def source_select(self, source):
        return self.command("@SRC:" + source)