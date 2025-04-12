import requests
import json
from response_handler import ResponseHandler


def get(url, headers={}, params={}):
    response = requests.get(url, headers=headers, params=params)

    return ResponseHandler.handle(response)


def post(url, headers={}, params={}, json={}):
    response = requests.post(url, headers=headers, params=params, json=json)

    return ResponseHandler.handle(response)
