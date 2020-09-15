from ImpConn import *

def Messaged(info,number,From,To,Date):
	msg = info+" Start: "+From+" To: "+To+" Date: "+Date
	url = "url"
	payload = "payload"+str(msg)+"language and route"+str(number)
	headers = {
	'authorization': "key",
	'Content-Type': "content-type",
	'Cache-Control': "control",
	}
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)

def Messagec(info,number,From,To,Date):
	msg = info+" Name: "+From+" Surname: "+To+" Mobile: "+Date
	url = "url"
	payload = "payload"+str(msg)+"language and numbers"+str(number)
	headers = {
	'authorization': "key",
	'Content-Type': "content-type",
	'Cache-Control': "control",
	}
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)
