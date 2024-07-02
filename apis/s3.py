import os
from dotenv import load_dotenv
import requests
import json 
load_dotenv()

S3_COMMUNICATION_API = os.getenv('S3_COMMUNICATION_API')
# S3_COMMUNICATION_API = 'http://localhost:3003/'
if not S3_COMMUNICATION_API:
  raise ValueError("No EXPRESS_API_URL set for Flask application")
  
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
  print('Generating S3 request')
  print(S3_COMMUNICATION_API + endpoint)
  res.raise_for_status()
  if res.status_code != 204:
    return res.json()


def deleteFileFromS3(user_id,model_name):
  endpoint = 'delete'
  headers= {'Content-Type':'application/json'}
  data = {
    'user_id':user_id,
    'model_name': model_name,
    'model_bytes':''
  }
  files=[('model_bytes',('test'))]
  res = requests.delete(S3_COMMUNICATION_API + endpoint,data = data, files=files)
  print('Generating S3 request')
  print(S3_COMMUNICATION_API + endpoint)
  res.raise_for_status()
  if res.status_code != 204:
    return res.json()


def renameFileFromS3(user_id,old_model_name,model_name):
  endpoint = 'rename'
  headers= {'Content-Type':'application/json'}
  data = {
    'user_id':user_id,
    'model_name': model_name,
    'old_model_name': old_model_name,
    'model_bytes':''
  }
  files=[('model_bytes',('test'))]
  res = requests.put(S3_COMMUNICATION_API + endpoint,data = data, files=files)
  print('Generating S3 request')
  print(S3_COMMUNICATION_API + endpoint)
  res.raise_for_status()
  if res.status_code != 204:
    return res.json()

