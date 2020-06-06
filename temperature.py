#importing relevant modules
import sys
import time
import json
import paho.mqtt.client as mqtt
import random
#credentials
host ='ds3c1j.messaging.internetofthings.ibmcloud.com'
clientid ='d:ds3c1j:Sensors:Temperature'
username='use-token-auth'
password =""#hidden for security purposes :D
topic='iot-2/evt/temperature/fmt/json'

#Connecting to a mqtt client

client =mqtt.Client(clientid)
client.username_pw_set(username, password)
client.connect(host, 1883, 60)
#Publishing simulated sensor data to IBM iot server
while True:
    try:
        temp,t = random.uniform(97,100), time.ctime()
        client.publish(topic, json.dumps({'Temp':temp,'Time':t}))
        print ("Data published")
        print(str(temp)+"\t"+str(t))
        time.sleep(3)
    except IOError:
        print ("Error")
client.loop()
client.disconnect()
