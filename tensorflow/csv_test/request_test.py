import requests
import json
import pandas as pd

datas = {'key':'value'}

url= "URL"

response = requests.post(url, data=datas)

if response.status_code == 200 :
    global info            # ?�역변??
    info = json.loads(response.text)

df = pd.json_normalize(info['docs']) 
df.to_csv('sample_test.csv',encoding='utf-8-sig')