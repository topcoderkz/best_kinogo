import requests
from pprint import pprint
from bs4 import BeautifulSoup


films = []

for i in range(2, 100000000):
    url = "http://kinogo.cc/page/{}/".format(i)
    page = requests.get(url)
    contents = page.content
    soup = BeautifulSoup(contents, 'html.parser')

    titles_li = soup.find_all(attrs={"class": "zagolovki"})

    if titles_li:
        titles = [title.contents[0].contents[0] for title in titles_li]
        for i, unit_rating in enumerate(soup.find_all(attrs={"itemprop": "rating"})):
            li = unit_rating.find_all('li')[0]
            average = float(li.contents[0])
            if average > 4.0:
                films.append((-average, titles[i]))
    else:
        break
        
films = sorted(films)

file = open("kinogo_movies.csv", "w")

for film in films:
    file.write("{},{}\n".format(-film[0], film[1]))

file.close()
