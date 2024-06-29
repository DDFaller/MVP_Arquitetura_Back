import os
from dotenv import load_dotenv
import requests
import json 
load_dotenv()

S3_COMMUNICATION_API = os.getenv('S3_COMMUNICATION_API')

def getModelUrl(user_id,model_name):
  endpoint = 'get'
  headers= {'Content-Type':'application/json'}
  data = {
    'user_id':user_id,
    'model_name': model_name,
    'model_bytes':''
  }
  files=[('model_bytes',('test'))]
  res = requests.post(S3_COMMUNICATION_API + endpoint,data = data, files=files)
  print('Generating request')
  print(S3_COMMUNICATION_API + endpoint)
  res.raise_for_status()
  if res.status_code != 204:
    return res.json()['data']
