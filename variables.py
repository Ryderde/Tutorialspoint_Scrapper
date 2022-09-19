import requests, re
from bs4 import  BeautifulSoup as BS

url = "https://www.tutorialspoint.com/assembly_programming/index.htm"
directory = url[30::]
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

req= requests.get(url,headers=headers)
data= BS(req.content,"html.parser")
Topics = []
Links=[]


for i in data.findAll("ul",{"class":re.compile("^toc chapters")}):
	Topics.append(i.text.strip())
	for link in i.findAll("a",href=True):
		Links.append(link.get("href"))
