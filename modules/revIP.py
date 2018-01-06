from insides 	import *
from modules 	import *

def reverseIP(website):
	try:
		res_0x01 	= revHT(website)
		res_0x02	= revYGT(website)

		print(res_0x01)
		print(res_0x02)

		lis_0x01	= []
		lis_0x02	= []

		if res_0x01 == "sedlyf":
			lis_0x01 = []
		else:
			lis_0x01 = res_0x01

		if res_0x02 == "sedlyf":
			lis_0x02 = []
		else:
			lis_0x02 = res_0x02

		if lis_0x01 is not [] and lis_0x02 is not []:
			_res = list(lis_0x01) + list(lis_0x02)
			_res = set(_res)
			
			for domains in res:
				return domains

		elif lis_0x01 is [] and lis_0x02 is []:
			return "sedlyf"

		elif lis_0x01 is []:
			return "sedlyf1"
	
	except Exception:
		return "sedlyf"