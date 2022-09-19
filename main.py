import requests, re
from bs4 import  BeautifulSoup as BS

url = "https://www.tutorialspoint.com/assembly_programming/index.htm"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

req= requests.get(url,headers=headers)
data= req.content
data= BS(data,"html.parser")
Topics = []
#print (data.find_all("li").get("href"), end= " ")
lists= data.findAll("ul",attrs={"class":re.compile("^toc")})

for link in lists:
    if link.findAll("a",attrs={"href":re.compile("^/assembly")}):

#GETTING THE TOPIC'S NAMES
        Topics.append(link.text.strip())

#GETTING THE TOPICS DIRECTORY
##        print (help(link))
        '''
        if link.has_attr("href"):
            print(link)'''

        print (link)
        
#print (Topics)
