import requests
import six
import argparse
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

API_ENDPOINT = 'https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk'
API_KEY = 'DZZwb8Ewgr6sbBvkfu5TmWOMF8DWr8jN'
ANALYZE_ENDPOINT = 'https://language.googleapis.com/v1/documents:analyzeEntities'
API_KEY_FOR_GOOGLE = 'AIzaSyAxpnlAoQ7QcpejbnTK8XEVmHv7nZdjLlM'

class NlpService:
    def __init__(self, answer):
        self.answer = answer

    def get_response_answer(self):
        api_and_input_text = {
            'apikey': (None, API_KEY),
            'query': (None, self.answer),
        }
        req = requests.post(API_ENDPOINT, files=api_and_input_text)
        if not req.status_code == 200 and not req.json()['results']:
            return
        return req.json()['results'][0]['reply']

    def get_analized_answer(self):
        url = f"{ANALYZE_ENDPOINT}?key={API_KEY_FOR_GOOGLE}"
        header = {'Content-Type': 'application/json'}
        body = {
            "document": {
                "type": "PLAIN_TEXT",
                "language": "JA",
                "content": self.answer
            },
            "encodingType": "UTF8"
        }
        return requests.post(url, headers=header, json=body).json()


