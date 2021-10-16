from threading import Thread
import serial
from serial import SerialException


class SerialReaderThread(Thread):

    def __init__(self, fridge_name, max_temperature, port, baud):
        Thread.__init__(self)
        self.fridgeName = fridge_name
        self.maxTemperature = max_temperature
        self.port = port
        self.baud = baud

    def run(self):
        try:
            serial_dev = serial.Serial(self.port, self.baud)
            # TODO register the device in a channel on MQTT
            while True:
                # TODO publish the value on the reserved channel
                continue
        except SerialException:
            print("Device not found on port " + self.port)
