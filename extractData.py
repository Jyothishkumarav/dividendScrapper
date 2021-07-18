import requests
from bs4 import BeautifulSoup

url = 'https://www.bseindia.com/corporates/corporates_act.html'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
           "Accept-Encoding": "gzip, deflate",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
           "Connection": "close", "Upgrade-Insecure-Requests": "1"}

page = requests.get(url, headers=headers)
html_soup = BeautifulSoup(page.text, 'html.parser')
security_list = html_soup.findAll("tr", class_="TTRow ng-scope")
print(len(security_list))
