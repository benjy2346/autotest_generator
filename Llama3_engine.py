import requests
from config import Llama3_token

def Llama3_engine(prompt,token = Llama3_token):
    API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B"
    headers = {"Authorization": "Bearer "+token}


    response = requests.post(API_URL, headers=headers, json={
        "inputs": 'read this prompt in chinese and give back the answer accordingly'+prompt
    })
    print( response.json())