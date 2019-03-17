import requests
import six
import argparse
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

API_ENDPOINT = 'https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk'
API_KEY_FOR_RECRUIT = 'Your_Key'
ANALYZE_ENDPOINT = 'https://language.googleapis.com/v1/documents:analyzeSentiment'
API_KEY_FOR_GOOGLE = 'Your_Key'

class NlpService:
    def __init__(self, answer):
        self.answer = answer

    def get_response_answer(self):
        api_and_input_text = {
            'apikey': (None, API_KEY_FOR_RECRUIT),
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
        req = requests.post(url, headers=header, json=body)
        if not req.status_code == 200:
            return 'サーバーの問題が発生しました'
        req_json = requests.post(url, headers=header, json=body).json()
        if not req_json['documentSentiment']:
            return '私ちょっといま体調悪いかもです'
        elif req_json['documentSentiment']['magnitude'] > 0.5 and req_json['documentSentiment']['magnitude'] > 0.5:
            return 'なんか良さそうですね'
        elif req_json['documentSentiment']['magnitude'] > 0.5 and req_json['documentSentiment']['magnitude'] < -0.5:
            return '...そうなんですね'
        return 'うんうん'


