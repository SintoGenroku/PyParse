
import requests
import json
from bs4 import BeautifulSoup

class Cinema:
    def __init__(self, name, country, genre):
        self.name = name
        self.country = country
        self.genre = genre

url = 'https://www.kinopoisk.ru/lists/top250/'
src = requests.get(url)
page = BeautifulSoup(src.text, 'lxml')
links = page.find_all('a', class_="paginator__page-number")
link_list = ['https://www.kinopoisk.ru/lists/top250/?tab=all']
arr = []
data ={"film":[]}

for i in range(1, len(links)):
    link_list.append(link_list[i-1].replace(links[i-1].get('href'),links[i].get('href')))

for i in range(0, len(link_list)):
    src = requests.get(link_list[i])
    page = BeautifulSoup(src.text, 'lxml')
    films = page.find_all('p', class_="selection-film-item-meta__name" )
    list = page.find_all('p', class_="selection-film-item-meta__meta-additional")
    countries = []
    genres = []
    
    for item in list:
        countries.append(item.find("span", class_="selection-film-item-meta__meta-additional-item").text)
        genres.append(item.find("span", class_="selection-film-item-meta__meta-additional-item").find_next().text)
  
    for i in range(0, len(films)):
        film = {"name":films[i].text,"country": countries[i],"genre": genres[i]}
        arr.append(film)
print(len(arr))

with(open("films top250.json","w")) as f:
    top_str = json.dumps(arr)
    f.write(top_str)
