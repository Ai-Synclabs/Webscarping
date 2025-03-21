import requests
from bs4 import BeautifulSoup


user_agent = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7"}

dkd = requests.get("https://aaaa.com/",headers=user_agent)


dkdContent = dkd.content


jobs = BeautifulSoup(dkdContent,"html.parser")


#print(jobs.find("div"))

xy = jobs.findAll("div",{"class":"testimonials-content-heading"})


for x in xy:
    print(x)
