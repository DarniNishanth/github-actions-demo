from bs4 import BeautifulSoup
import requests
from datetime import date

response  = requests.get("https://timesofindia.indiatimes.com/?from=mdr")
soup = BeautifulSoup(response.text,'html.parser')
temp = soup.select('.col_l_6')
with open('data.text', 'a') as file:
    today = date.today()
    file.write(today+'\n')
    for i in temp:
        if i.find('img') is not None:
            file.write(i.find('figcaption').text+'\n')
