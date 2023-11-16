from fastapi import FastAPI
from pydantic import BaseModel
import xml.etree.ElementTree as ET
from sendMail import sendEmail
import datetime

app = FastAPI()


class SensorData(BaseModel):
    temperature: int
    movement: int
    humidity: int


@app.post("/uploadData")
async def root(sensorData: SensorData):
    tree = ET.parse('./sensorData.xml')
    treeRoot = tree.getroot()
    entry = ET.Element("Measurement")
    ET.SubElement(entry, "Temperature").text = str(sensorData.temperature)
    ET.SubElement(entry, "Movement").text = str(sensorData.movement)
    ET.SubElement(entry, "Humidity").text = str(sensorData.humidity)
    ET.SubElement(entry, "TimeStamp").text = str(datetime.datetime.now())
    if sensorData.humidity >3000:
        print("merge")
        sendEmail()

    treeRoot.append(entry)
    tree.write('./sensorData.xml')
    return sensorData
