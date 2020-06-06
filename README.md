# Nakano
Autonomous Temperature Screener

# Description:
Imagine a world post covid , where you want to step out of the house , grab a coffee or simply go to the office. These were things we took for granted before the mighty COVID struck us and left us to think of a  new normal where wearing a mask, carrying a sanitizer and regular temperature checks are the new normal. Just as after the bomb blasts , metal screeners were installed in public spaces we believe devices like Nakano will normalize temperature checks in a post COVID era.
Traditionally there is a person at the point of entry of a public space like airports , restaurants, office buildings, hotels, that normally screens for temperature with the help of a temperature gun before allowing you in. Our solution Nakano makes it possible for you to autonomously screen for temperature and thus not risking the person or guard at possible infections. Nakano measures human body temperature by collecting infrared thermal radiation from the human forehead. The operation is simple, hygienic and the measurement is fast & accurate. The user only needs to point His/Her forehead in front of the (Infrared sensor) and the human body temperature can be quickly and accurately measured within 0.5 seconds. The products are mainly composed of infrared temperature sensor, signal receiving main control board, Power ON/OFF Switch, buzzer, 7-Segment display etc.

![1](https://user-images.githubusercontent.com/54938773/83952653-b75a7000-a857-11ea-9fcb-f2dbc99a6131.png)

![2](https://user-images.githubusercontent.com/54938773/83952668-d1944e00-a857-11ea-83cc-267eff15ac7d.png)


![3](https://user-images.githubusercontent.com/54938773/83952673-e1ac2d80-a857-11ea-96cb-cad044fbf905.png)

![4](https://user-images.githubusercontent.com/54938773/83952682-f983b180-a857-11ea-9b86-6de1466e6d91.png)

![5](https://user-images.githubusercontent.com/54938773/83952767-d4437300-a858-11ea-8d71-3d21060a75e7.png)


# Circuit

![Glorious Lahdi-Leelo](https://user-images.githubusercontent.com/54938773/83952772-e8877000-a858-11ea-91be-2c867947c97e.png)

# Product Architecture and Roadmap

![Nakano](https://user-images.githubusercontent.com/54938773/83952794-0b198900-a859-11ea-9b21-b3eb8b598994.png)

## Streaming temperature sensor data to the IOT platform
#### (Data is simulated sensor data in this case)
![temperature](https://user-images.githubusercontent.com/54938773/83952801-1d93c280-a859-11ea-8be5-a50182c47c25.PNG)

## IBM Watson IOT Platform  

![IOT](https://user-images.githubusercontent.com/54938773/83952824-5338ab80-a859-11ea-8e3c-d1cc7551e48d.PNG)

## Streamed Device data on the IOT platform

![IOTStream](Assets/IBMIoTDataStream.PNG)

## Application listening to IOT device data with relevant console logs 

![app](https://user-images.githubusercontent.com/54938773/83952813-4025db80-a859-11ea-9f54-545ecb7c2ab8.PNG)

## Sample User Text Alert

![textalert](Assets/textalert.jpeg)
