import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import db
from convertXMLtoJSON import convert

def pushData():
	cred = credentials.Certificate("./iotproject-5823d-firebase-adminsdk-ywc3k-9d0d3270f8.json")
	default_app = firebase_admin.initialize_app(cred, {
		'databaseURL':'https://iotproject-5823d-default-rtdb.europe-west1.firebasedatabase.app/'
		})

	convert() #converie de la xml la json


	ref = db.reference("/")

	# text= {
	#     'name': 'John',
	#     'age': 30,
	#     'email': 'john@example.com'
	# }

	# new_ref= ref.push(text)
	# print("New data key:", new_ref.key)


	with open('senzorDataJson.json', 'r') as json_file:
		data_to_upload = json.load(json_file)

	# Send the JSON data to Firebase
	#new_post_ref = ref.push(data_to_upload)
	new_post_ref = ref.update(data_to_upload)
	print("SEND")

#verificare
# pushData()