import requests
from bs4 import BeautifulSoup as bs

#page = requests.get("https://www.imdb.com/title/tt0111161/")
#soup = bs(page.content, 'html.parser')



class Movie:
    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)
        self.soup = bs(self.page.content, 'html.parser')
        self.get_title_yr(self.soup)
        self.get_rating(self.soup)

    def get_title_yr(self, soup):
        self.title_and_yr= soup.find('h1').text
        self.title = self.title_and_yr[:-8]
        self.yr = self.title_and_yr[-6:-2]
        return self.title, self.yr

    def get_rating(self, soup):
        try:
            self.rating = soup.find('span', attrs={'itemprop':'ratingValue'}).text
        except:
            self.rating = 'None'
        return self.rating

    def output_details(self):
        details = "Title: {}, Year: {}, Rating: {}".format(self.title, self.yr, self.rating)
        return details

#m = Movie("https://www.imdb.com/title/tt0111161/")
#print(m.title)
#print(m.yr)
#print(m.rating)

def number_to_url(num):
    missingDigits = 7-len(str(num))
    newNum = str(num)
    if missingDigits>0:
        for x in range(missingDigits):
            newNum = '0'+newNum
    url = "https://www.imdb.com/title/tt"+ newNum + "/"
    return url

movies = []

'''
for x in range(1270767, 1270797):
    try:
        url = number_to_url(x)
        #print('trying:')
        print(url)
        m = Movie(url)
        #print('made movie')
        print(m.output_details())
        movies.append(m)
    except:
        #print('Failed: {}'.format(str(x)))
        pass

'''

url = r"https://www.imdb.com/title/tt2527336/"

m = Movie(url)
print(m.output_details())


'''
missingUrls = []

for x in range(1270767, 1270797):
    try:
        url = number_to_url(x)
        request = requests.get(url)
        if request.status_code != 200:
            missingUrls.append(url)
            print(url)
    except:
        print('woops')

'''