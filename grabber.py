
from bs4 import BeautifulSoup
import requests

latitudes = []
longitudes = []
page = 0
place = 'Minnesota'

while(page<50):
    url = 'http://www.geonames.org/advanced-search.html?q=' + place + '&startRow=' + str(page*50)

    web = requests.get(url)

    data = web.text

    soup = BeautifulSoup(data)
    i=0
    for row in soup.find_all('tr'):
        for col in row.find_all('td'):
            for span in col.find_all('span'):
                if(span.text.find('l')==1):
                    i=i+1
                elif (i%3)==1:
                    i=i+1
                elif (i%3)==0:
                    longitudes.append(span.text)
                    i=i+1
                elif(i%3)==2:
                    latitudes.append(span.text)
                    i=i+1
                else:
                    print('invalid')
    page=page+1

f = open(place + 'Pulled.txt',"w+")
print('Ensuring lat and long lists are even')
print(len(latitudes))
print(len(longitudes))
if(len(latitudes) == len(longitudes)):

    for z in range(page*50):
        f.write(str(latitudes[z]) + ',' + str(longitudes[z]) + '\n')

    print("Finished printing file")
f.close()
