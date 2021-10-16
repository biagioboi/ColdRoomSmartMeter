import json
from Initializer.SerialReaderThread import SerialReaderThread

if __name__ == "__main__":
    try:
        fp = open('config.json')
        sensors = json.load(fp)
        serials_reader = list()
        for sensor in sensors:
            serials_reader.append(SerialReaderThread(sensor['fridgeName'], sensor['maxTemperature'], sensor['port'], 9600))
        for reader_thread in serials_reader:
            reader_thread.start()
    except FileNotFoundError:
        print("Configuration file not found.")
