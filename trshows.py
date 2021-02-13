import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
headers = {"Accept-Language": "en-US, en;q=0.5"}
results = requests.get(url, headers=headers)


soup = BeautifulSoup(results.text, "html.parser")

titles = []
years = []

show_td = soup.find_all('td', class_='titleColumn')

for container in show_td:

  #Name
  name = container.a.text
  titles.append(name)

  #Year
  year = container.find('span', class_='secondaryInfo').text
  years.append(year)



#building our Pandas dataframe
shows = pd.DataFrame({
'Show': titles,
'Year': years,
})

print (shows)
shows.to_csv('trshows.csv')
