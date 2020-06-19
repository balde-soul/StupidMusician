#In[]:
import requests
headers = {"Content-Type": "application/json"}
params = {'access_token': "5L8twZILM2qDBwSY3J0okkIEhVRp8Fp3Nt3SUFbTcbuYyTsuuLGyNHIk79t8"}
r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions',
               params=params,
               json={},
               # Headers are not necessary here since "requests" automatically
               # adds "Content-Type: application/json", because we're using
               # the "json=" keyword argument
               # headers=headers, 
               headers=headers
               )
r.status_code
print(r.json())

#In[]:
import json

with open('/data2/process_data/caojihua/data/MedleyDB/curl.json', 'r') as fp:
    con = json.loads(fp.read())
    pass
print(con.keys())