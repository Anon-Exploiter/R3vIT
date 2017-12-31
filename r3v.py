from insides	import *
from modules 	import *
from bs4 		import BeautifulSoup
from time 		import time, sleep
from sys 		import argv
import re
import requests
print(Banner)

website = argv[1]

print findAdminPanel(website)