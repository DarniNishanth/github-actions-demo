from bs4 import BeautifulSoup
import requests

response  = requests.get("https://timesofindia.indiatimes.com/india")
soup = BeautifulSoup(response.text,'html')
temp = soup.selector('.WavNE ')
for i in temp.contents:
    print(i)
