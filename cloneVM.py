import requests
from requests.auth import HTTPBasicAuth
import json
file = open('account.txt', 'r') 
filelines = file.readlines() 
username=filelines[0].rstrip()
password=filelines[1].rstrip()
vmname=filelines[2].rstrip()
numclone=int(filelines[3].rstrip())
vmsource=''
file.close()
print(vmname)
print(numclone)
response = requests.get("http://127.0.0.1:8697/api/vms",auth = HTTPBasicAuth(username, password))
for i in response.json():
	if(vmname in i['path']):
		vmsource=i['id']
print(vmsource)
headers = {'Content-type': 'application/vnd.vmware.vmw.rest-v1+json','Accept': 'application/vnd.vmware.vmw.rest-v1+json'}
params = (
    ('priority', 'normal'),
)
for i in range(1,numclone+1):
	vmnew=vmname+'_clone_'+str(i)
	print(vmnew)

	datapost={}
	datapost['name']=vmnew
	datapost['parentid']=vmsource
	print(type(datapost))
	response = requests.post("http://127.0.0.1:8697/api/vms", headers=headers, auth = HTTPBasicAuth(username, password), params=params,json=datapost)
	print(response)