from fastapi import FastAPI
from pydantic import BaseModel
import xml.etree.ElementTree as ET
from sendMail import sendEmail
import datetime
from push_data import pushData

app = FastAPI()
global k
k=0


class SensorData(BaseModel):
    temperature: int
    movement: int
    humidity: int

class TargetData(BaseModel):
    target: int

@app.post("/uploadTarget")
async def root2(targetData: TargetData):
    global targetVal
    targetVal=targetData.target
    global contor
    contor=0
    # return targetData.target

@app.post("/uploadData")
async def root(sensorData: SensorData):
    global contor, k
    tree = ET.parse('./sensorData.xml')
    treeRoot = tree.getroot()
    entry = ET.Element("Measurement")
    ET.SubElement(entry, "Temperature").text = str(sensorData.temperature)
    ET.SubElement(entry, "Movement").text = str(sensorData.movement)
    ET.SubElement(entry, "Humidity").text = str(sensorData.humidity)
    ET.SubElement(entry, "TimeStamp").text = str(datetime.datetime.now())

    
    if sensorData.humidity >targetVal and contor<40: 
         contor+=1
         k+=1
         print(contor)
         print(sensorData.humidity)


    elif sensorData.humidity >targetVal and contor>=40: #asteapta 40 secudne
         print("merge")
         sendEmail()
         contor=0
         k+=1
         print(targetVal)
            

    else:
         contor=0
         k+=1
         print(contor)

    if k>120:
        pushData()
        k=0

   
    treeRoot.append(entry) 
    tree.write('./sensorData.xml')
    return sensorData
