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
        self.client = None

    def run(self):
        try:
            serial_devs = serial.Serial(self.port, self.baud)
            while True:
                for serial_dev in serial_devs:
                    # if the content is not empty and the client is defined
                    if serial_dev != "" and self.client is not None:
                        print(serial_dev)
                        # publish the value on the reserved channel
                        self.client.publish("iot/fridge_temperature/" + self.fridgeName, serial_dev)
                continue
        except SerialException:
            print("Device not found on port " + self.port)
