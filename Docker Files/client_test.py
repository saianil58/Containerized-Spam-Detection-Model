# this piece of code is to test the model deployed on container
import requests
import json

# url on which the container is hosted
url="http://localhost:1722/predict"

# input data to continer as a Json 
data=json.dumps({'msg':'please stop going out to stop the spread of covid'})

#sending the request
r=requests.post(url,data)

# get the reponse from server
print('the prediction is')
print(r.json())
