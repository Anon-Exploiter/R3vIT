from insides 	import *
from requests 	import get as GET

def findAdminPanel(website):
	website = addHTTP(website)

	with open('list.txt', 'r') as f:
		content 	= f.read()
		panels		= content.strip("").split("\n")

	for _panels in panels:
		combo 		= website + "/" + _panels
		response_code 	= GET(combo, headers=functions._headers, timeout=5, allow_redirects=False).status_code
		print(response_code)