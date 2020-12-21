import requests
from bs4 import BeautifulSoup

#accessing locally saved website
def open_html(path):
    with open(path, 'rb') as f:
        return f.read()
html = open_html('local_registration_html')

soup = BeautifulSoup(html, 'html.parser')

#storing all names in list
tempProfNames = []
for professor in soup.select('.email'):
    tempProfNames.append(professor.text)

#removing duplicate names
profNames = []
for professor in tempProfNames:
    if professor not in profNames:
        profNames.append(str(professor))

#getting rateMyProf links for each found professors
try:
    from googlesearch import search
except:
    print("No moduel named 'google' found")

possWebsites = []
rateMyProfWeb = []
for prof in profNames:
    for i in search(prof + " rate my professor", tld = "com", num = 1, start = 0, stop = 1, pause = 2):
        possWebsites.append(i)
    for i in possWebsites:
        if (i.find("ratemyprofessors") and i.find("ShowRatings")):
            rateMyProfWeb.append(i)
            possWebsites.clear()
        else:
            print("results not found for " + prof)

ratings = []
for url in rateMyProfWeb:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    ratings.append(soup.select_one('.RatingValue__Numerator-qw8sqy-2.liyUjw').text)

print(rateMyProfWeb)
print(ratings)





