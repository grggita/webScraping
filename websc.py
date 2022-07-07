import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/grggi/Desktop/Driver/chromedriver.exe")
driver.get('https://en.wikipedia.org/wiki/Vlog%27')
results = []
content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")

for element in soup.findAll('div', attrs={'class':'vector-body'}):
    name = element.find('span')
    if name not in results:
        results.append(name.text)

df = pd.DataFrame({'Articles':results})
df.to_csv('names.csv',index=False , encoding="utf-8")
print(results)