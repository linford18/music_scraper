import bs4
from urllib.request import urlopen as uReq      #parseing
from bs4 import BeautifulSoup as soup  #grab

my_url= 'http://www.officialcharts.com/new-releases/'

uClient=uReq(my_url)             #grabs the whole content of webpage

page_html = uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
page_soup.h1

container = page_soup.findAll("div" , {"class":"accordion"})

filename = "newSongList.csv"
f = open(filename,"w")


headers = "TITLE,ARTIST\n"
f.write(headers)
singles=container[0]
artist=singles.findAll("div" , {"class":"artist"})
title=singles.findAll("div" , {"class":"title"})


for i in range(len(artist)):
	try:
		print(artist[i].a.text)          #artist_name = artist[i].a.text
		print(title[i].a.text)
		f.write(title[i].a.text+","+artist[i].a.text.replace(",","|")+ "\n")       #f.write(artist_name+ "\n")
	except AttributeError:
		print(artist[i].text.strip())           #artist_name = artist[i].text.strip()
		f.write(title[i].a.text+","+artist[i].text.replace(",","|").strip()+ "\n")  #not needed
		continue
	
	

f.close()
