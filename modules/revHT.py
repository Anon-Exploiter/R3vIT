from insides 	import *
from requests 	import get

def reverseViaHT(website):
	website = removeHTTP(website)
	url 	= "https://api.hackertarget.com/reverseiplookup/?q={url}".format(url=website)

	try:
		request = get(url, headers=functions._headers, timeout=5).text.encode('UTF-8')
	except:
		return("sedlyf")

	if "parameter" in request:
		return("sedlyf")

	else:
		lis 	= []
		_lis 	= []
		_rev	= [lis.append(urls) for urls in request.split("\n")]
		lis 	= lis[:-1]
		for _url in lis:
			_url = removeHTTP(_url)
			_lis.append(_url)
		return(_lis)