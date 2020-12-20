import requests
from bs4 import BeautifulSoup

url = 'https://registrationssb.ucr.edu/StudentRegistrationSsb/ssb/classRegistration/classRegistration'
r = requests.get(url)

#locally saving website
def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)
save_html(r.content, 'local_registration_html')

#accessing locally saved website
def open_html(path):
    with open(path, 'rb') as f:
        return f.read()
html = open_html('local_registration_html')

print(html)
#soup = BeautifulSoup(r.content, 'html.parser')

#professors = soup.select_one('td a .email')

#print(professors)

