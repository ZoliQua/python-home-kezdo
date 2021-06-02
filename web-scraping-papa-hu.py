
import urllib.request as rqs
import csv
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import random
import requests
import urllib

def sleep(func):
	def wrapper():
		sleeprandomtime = random.randrange(5, 15)
		print(f"Scrapper is going to sleep {sleeprandomtime} seconds.")
		time.sleep(sleeprandomtime)
		return func()
	return wrapper

@sleep
def SleepWakeUp():
	print("Scrapper woke up and continue the process.")

papa_oldal_base = "http://papa.hu/papa-es-videke-kiadasai-2005-2015/papa-es-videke-kiadasai-"
hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': "Magic Browser"}
# filepath="/Users/Zoli/Downloads/"
filepath = "data/papa/"

# Creating timestamp for output plot filename
now = datetime.now()
current_time_abbrev = now.strftime("%Y%m%d-%H%M%S-%f")

# Export filename
filename_export = filepath + "gamenames-" + current_time_abbrev + ".csv"

# List of pdf-s
list_of_pdf_links = []

for i in range(2005, 2016):

	# if i % 10 == 0 and i > 0:
	# 	SleepWakeUp()

	papa_oldal = papa_oldal_base + str(i)
	page = rqs.Request(papa_oldal, headers=hdr)
	content = rqs.urlopen(page).read()

	soup = BeautifulSoup(content, "html.parser")
	right_class = soup.find_all("a")

	print(f"Scrapper read {len(right_class)} DIV elements from the site page {i}.")

	counter = 0

	for item in right_class:

		this_link = item.get("href")
		if this_link[-4:] == ".pdf":
			list_of_pdf_links.append(this_link)

		counter += 1

for link in list_of_pdf_links:

	pdf_name = link.split("/")[-1]

	if len(pdf_name) > 10:
		continue

	pdf_name = "data/papa/" + pdf_name
	rqs.urlretrieve(link, pdf_name)

	#
	# r = requests.get(link, stream=True)
	#
	# with open('/tmp/metadata.pdf', 'wb') as fd:
	#     for chunk in r.iter_content(chunk_size):
	#         fd.write(chunk)

print(len(list_of_pdf_links))
#
# print(f"Scrapper wrote out {written_lines} line in {filename_export} file.")