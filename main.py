from bs4 import BeautifulSoup
import requests
from datetime import date

response  = requests.get("https://timesofindia.indiatimes.com/india")
soup = BeautifulSoup(response.text,'html')
temp = soup.selector('.WavNE ')
with open(filename, 'a') as file:
    today = date.today()
    file.write(today+'\n')
    for i in temp.contents:
        file.write(i+'\n')
        file.write(data + '\n')
