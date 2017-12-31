from insides 	import *
from requests 	import post  as POST
from json		import loads as Parse

def reverseViaYGT(website):
	website = addHTTP(website)
	webs 	= removeHTTP(website)
	url 	= "https://domains.yougetsignal.com/domains.php"
	post 	= {'remoteAddress' : webs, 'key' : ''}

	try:
		request = POST(url, headers=functions._headers, timeout=5, data=post).text.encode('UTF-8')
		_data	= Parse(request)
		status 	= _data['status']
		_sites 	= _data['domainArray']
	except Exception:
		return("sedlyf")
		
	_list 	= []

	if 	(status == "Fail"):
		return("sedlyf")

	else:
		_res 	  = [websites[0] for websites in _sites]

		for _urls in _res:
			_urls = removeHTTP(_urls)
			_list.append(_urls)

		return(_list)