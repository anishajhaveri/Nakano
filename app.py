#importing relevant modules
import ibmiotf.application
import time
import json
from twilio.rest import Client

#Application Credentials
options ={
"org": "ds3c1j",
"id": "app1",
"auth-method": "apikey",
"auth-key": "",
"auth-token": "" , #hidden for security purposes
"clean-session": True
}

#Twilio Credentials for text alerts
account_sid = ''
auth_token = ''
textclient = Client(account_sid, auth_token)

#Subscribing to the event temperature for device type sensors :)
sourceDeviceType="Sensors"
sourceEvent = "temperature"


def myEventCallback(event):
    temp_threshold=99.9
    str = "COVID Alert received from device [%s]: %s"
    alert=str % (event.device, json.dumps(event.data))
    #Alerts the user if the temperature is above a certain threshold
    if event.data["Temp"] > temp_threshold:
        message = textclient.messages.create(
                                      from_='+12057368398',
                                      body = alert,
                                      to ='+919999999999'
                                  )

        print(message.sid)

#Connecting to IBM iot application client
client = ibmiotf.application.Client(options)
client.connect()
client.deviceEventCallback = myEventCallback
client.subscribeToDeviceEvents(deviceType=sourceDeviceType,event=sourceEvent)
while True:
    time.sleep(1) #Every 1second
