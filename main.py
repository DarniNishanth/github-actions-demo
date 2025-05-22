from bs4 import BeautifulSoup
import requests
from datetime import datetime

response  = requests.get("https://timesofindia.indiatimes.com/?from=mdr")
soup = BeautifulSoup(response.text,'html.parser')
temp = soup.select('.col_l_6')
with open('data.txt', 'a') as file:
    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    file.write(now_str+'\n')
    for i in temp:
        if i.find('img') is not None:
            file.write(i.find('figcaption').text+'\n')
print("Successful")
