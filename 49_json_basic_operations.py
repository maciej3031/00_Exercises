import requests
import json

# getting json from website

url = 'https://api.um.warszawa.pl/api/action/datastore_search/?resource_id=53ef6c4b-8025-4008-a268-916a66de4cfc'

requests_object = requests.get(url)

json_string_data = requests_object.text

json_python_data = json.loads(json_string_data)

# creating json string from python object

json_string_data_2 = json.dumps(json_python_data)



