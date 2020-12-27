import requests
from bs4 import BeautifulSoup
import cgi
import cgitb

print("python script run")

#opening local file to get list of prof names
def open_html(path):
    with open(path, 'rb') as f:
        return f.read()
html = open_html('list_of_prof.html')

soup = BeautifulSoup(html, 'html.parser')

for r in soup.select('.info'):
    r.extract()

rawProfessorNames = []
rawProfessorNames = soup.select('.name')

profNames = []
for prof in rawProfessorNames:
    profNames.append(prof.text)


#list of prof ids
rawProfIds = []
profIds = []

rawProfIds = soup.select('.remove-this-button')

for prof in rawProfIds:
    profIds.append(prof.attrs['data-id'])

#getting professor name input from user
inputProfessor = input("Enter the name of Professor (LastName, FirstName): ")


#main work
if any(inputProfessor in s for s in profNames):
    print("\n\n" + inputProfessor)
    index = profNames.index(inputProfessor+'\r\n\t\t\t\t\t\n')
    profId = profIds[index]
    
    url = 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=' + profId
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rating = soup.select_one('.RatingValue__Numerator-qw8sqy-2.liyUjw').text
    print("\nRating: " + rating + "/5.0\n")

    Reviews = []
    reviews = soup.select('.Comments__StyledComments-dzzyvm-0.gRjWel')

    print("All Student Reviews\n")
    i = 1
    for review in reviews:
        print("\t " + str(i) + ". " + review.text + "\n")
        i += 1



else:
    print("Rating for " + inputProfessor + " does not exist! Sorry!")




#first way i did it (google searching and getting first 5 urls (inaccurate lol))


#accessing locally saved website
#def open_html(path):
#    with open(path, 'rb') as f:
#        return f.read()
#html = open_html('local_registration_html')

#soup = BeautifulSoup(html, 'html.parser')

#getting rateMyProf links for each found professors
#try:
#    from googlesearch import search
#except:
#    print("No moduel named 'google' found")

#possWebsites = []
#rateMyProfWeb = []
#for prof in profNames:
#    for i in search(prof + " rate my professor", tld = "com", num = 1, start = 0, stop = 1, pause = 2):
#        possWebsites.append(i)
#    for i in possWebsites:
#        if (i.find("ratemyprofessors") and i.find("ShowRatings")):
#            rateMyProfWeb.append(i)
#            possWebsites.clear()
#        else:
#            print("results not found for " + prof)

#ratings = []
#for url in rateMyProfWeb:
#    r = requests.get(url)
#    soup = BeautifulSoup(r.content, 'html.parser')
#    ratings.append(soup.select_one('.RatingValue__Numerator-qw8sqy-2.liyUjw').text)

#print(rateMyProfWeb)
#print(ratings)





