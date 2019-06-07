import requests
import json
# Define test JSON
input_sentiment = {'input':
                  [{'text' : 'Today was a great day!'},
                   {'text' : 'Happy with the end result!'},
                   {'text': 'Terrible service and crowded. Would not recommend.'} ]}
input_json = json.dumps(input_sentiment)
# Define your api URL here
print(input_json)
api_url = 'https://txmikdru77.execute-api.ap-south-1.amazonaws.com/api/'
res = requests.post(api_url, json=input_json)
print(res)
output_api = res.text
print(output_api)
