
from distutils.command.clean import clean
import requests
from bs4 import BeautifulSoup

link1 = 'https://dl3.3rver.org'
link2 = 'https://dl3.3rver.org/cdn2/'




link3 = 'https://dl3.3rver.org/cgi-bin/'
link4 = 'https://dl3.3rver.org/hex/'
link5 = 'https://dl3.3rver.org/hex1/'
link6 = 'https://dl3.3rver.org/hex2/'
link7 = 'https://dl3.3rver.org/hex3/'
link8 = 'https://dl3.3rver.org/hex4/'


# takes link if server and returns list of movies availible

def getting_dirs(link):
    data = requests.get(link).text
    soup = BeautifulSoup(data, 'html.parser')
    list_yr = []

    texts = soup.find_all('a')
    for text in texts:
        dirs = text.get_text()
        if dirs != '../':
            list_yr.append(dirs)
    print(list_yr)
    return list_yr


# cleans movies by removing '.' returns list of cleaned movies

def cleaning_movie(movies):
    cleaned = []
    for i in movies:
        cleaned.append(i.replace('.', ' '))
    return cleaned

# finds the needed movie

def finding(movies_cleaned, to_find):
    for i in movies_cleaned:
        words = i.lower().split()
        if to_find in words:
            print(i)



# for i in range(1,8):
#     link = link2+ '0'+str(i) + '/film/'
#     try:
#         years = getting_dirs(link)
#         print(years)
#     except:
#         print("Error in link: ", link)


# getting_dirs('https://dl3.3rver.org/cdn2/01/film/2020/')
m = ['Babyteeth.2020.720p.WEB-DL.x264-GalaxyRG.mkv', 'Babyteeth.2020.Trailer.mp4', 'Feel.the.Beat.2020.720p.NF.WEB-DL.x264-GalaxyRG..>', 'Feel.the.Beat.2020.Trailer.mp4', 'Lost.Bullet.2020.FRENCH.720p.NF.WEB-DL.x264-Gal..>']


a = cleaning_movie(m)
finding(a, "babyteeth")