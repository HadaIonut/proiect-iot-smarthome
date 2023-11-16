import xml.etree.ElementTree as E
import json
def convert():
    tree = E.parse('sensorData.xml')
    root = tree.getroot()
    data = {}

    for child in root:
        if child.tag not in data:
            data[child.tag] = []

        child_data = {}
        for child2 in child:
            child_data[child2.tag] = child2.text

        data[child.tag].append(child_data)

    # Serializați dicționarul într-un fișier JSON
    with open('senzorDataJson.json', 'w') as  json_file:
        json.dump(data, json_file, indent=4)

    print("Datele au fost salvate în fișierul 'senzorDataJson.json'.")

