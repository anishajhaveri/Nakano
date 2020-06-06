#importing relevant modules
import ibmiotf.application
import time
import json
#Application Credentials
options ={
"org": "ds3c1j",
"id": "app1",
"auth-method": "apikey",
"auth-key": "a-ds3c1j-wdmxph78xn",
"auth-token": "" , #hidden for security purposes
"clean-session": True
}
#Subscribing to the event temperature for device type sensors :)
sourceDeviceType="Sensors"
sourceEvent = "temperature"


def myEventCallback(event):
    temp_threshold=99.5
    str = "%s event received from device [%s]: %s"
    print(str % (event.format, event.device, json.dumps(event.data)))
    if event.data["Temp"] > temp_threshold:
        print("danger")
    else:
        print("fine")

#connecting to IBM iot application client
client = ibmiotf.application.Client(options)
client.connect()
client.deviceEventCallback = myEventCallback
client.subscribeToDeviceEvents(deviceType=sourceDeviceType,event=sourceEvent)
while True:
    time.sleep(1) #refreshes every 1second
