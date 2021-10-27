import json
from SerialReaderThread import SerialReaderThread
import paho.mqtt.client as mqtt

if __name__ == "__main__":
    try:
        fp = open('config.json')
        sensors = json.load(fp)
        serials_reader = list()
        for sensor in sensors:
            serials_reader.append(SerialReaderThread(sensor['fridgeName'], sensor['maxTemperature'], sensor['port'], 9600))
        try:
            fp = open('mqtt_config.json')
            mqtt_config = json.load(fp)
            client = mqtt.Client("FridgeController")
            client.on_connect = lambda client, userdata, flags, rc: f'Connection established.'
            client.username_pw_set(mqtt_config['username'], password=mqtt_config['password'])
            client.connect(mqtt_config['ip'], mqtt_config['port'], 60)
            for reader_thread in serials_reader:
                reader_thread.client = client
                reader_thread.start()
        except FileNotFoundError:
            print("MQTT configuration file not found.")
    except FileNotFoundError:
        print("Configuration file not found.")
