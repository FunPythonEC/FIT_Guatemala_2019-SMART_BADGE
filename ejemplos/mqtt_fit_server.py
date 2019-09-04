from umqtt.robust import MQTTClient
import time


MQTT_CLIENT_ID = "ESP32"
MQTT_PORT = 1884
MQTT_TOPIC = "t/Prueba_uPy"
MQTT_HOST = "fit2019.enjambre.ec"
WIFI_SSID = "galielo"
WIFI_PW = ""

mqtt_client = None
def cb(topic, msg):
	print(msg)
    
def pub_msg(msg):
    global mqtt_client
    try:    
        mqtt_client.publish(MQTT_TOPIC, msg)
        print("Sent: " + msg)
    except Exception as e:
        print("Exception publish: " + str(e))
        raise

def sub_msg():
    global mqtt_client
    try:    
        mqtt_client.set_callback(cb)
        mqtt_client.subscribe(bytes(MQTT_TOPIC, 'utf-8'))
        mqtt_client.wait_msg()
        
    except Exception as e:
        print(e)            

def connect_mqtt():    
    global mqtt_client
    mqtt_client = MQTTClient(client_id=MQTT_CLIENT_ID, 
                                 server=MQTT_HOST, 
                                 port=MQTT_PORT, 
                                 ssl=False)
    mqtt_client.connect()
    print('MQTT Connected')

while True:
    #start execution
    try:
        print("Connecting WIFI")
        #connect_wifi(WIFI_SSID, WIFI_PW)
        print("Connecting MQTT")
        connect_mqtt()
        print("Publishing")
        pub_msg("{\"micropython\":" + str(time.time()) + "}")
        print("OK")
        sub_msg()

        time.sleep(10)
    except Exception as e:
        print(str(e))


      