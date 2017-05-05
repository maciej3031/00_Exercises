import requests
import json

# getting json from website

url = 'https://api.um.warszawa.pl/api/action/datastore_search/?resource_id=53ef6c4b-8025-4008-a268-916a66de4cfc'

requests_object = requests.get(url)
requests_object.raise_for_status()

# text_file = open('web_page.txt', 'wb')       # write downloaded page to a file (for loop -> memory save for big files
# for i in requests_object.iter_content():
#     text_file.write(i)

json_string_data = requests_object.text
json_python_data = json.loads(json_string_data)

# creating json string from python object

json_string_data_2 = json.dumps(json_python_data)



