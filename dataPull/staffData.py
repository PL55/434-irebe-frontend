

import requests 
import json
from bs4 import BeautifulSoup 


# This python code is to scrape data from the given website and write it in a json file
  
URL = "https://www.cs.umd.edu/people/staff"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 

table = soup.find_all('div', attrs = {'class':'media-body'})
# print(table)


completeList = []
allMembers = {}
for t in table:
    temp = t.find('h4', attrs = {'class':'media-heading'}).find('a')

    # Getting the name
    name = temp.string
    allMembers['Name'] = name
    print(allMembers)

    # Getting their personal link
    link = 'https://www.cs.umd.edu' + temp.get('href')
    r2 = requests.get(link) 
    soup2 = BeautifulSoup(r2.content, 'html5lib') 
 
    # Getting title
    title = soup2.find('div',attrs = {'class':'views-field views-field-field-faculty-title col-md-6 col-sm-12 col-xs-12'})
    title = title.find('h2').string
    allMembers['Title'] = title

    # Getting email
    email = soup2.find('div',attrs = {'class':'views-field views-field-contact col-md-6 col-sm-12 col-xs-12'})
    email = email.find('span',{'class': 'field-content'}).text
    if "[at]" in email:
        email = email.replace(" [at] ",'@')
    allMembers['Email'] = email

    # Getting phone
    phone = soup2.find('div',attrs = {'class':'views-field views-field-field-profile-phone col-md-6 col-sm-12 col-xs-12'})
    if phone is not None:
        phone = phone.find('div',attrs = {'class':'field-content'}).string
        allMembers['Phone'] = phone
    else:
        allMembers['Phone'] = "Unavaliable"
    
    # Getting office location
    room = soup2.find('div',attrs = {'class':'views-field views-field-field-profile-location col-md-6 col-sm-12 col-xs-12'})
    if room is not None:
        room = room.find('div',attrs = {'class':'field-content'}).string
        allMembers['Office'] = room
    else:
        allMembers['Office'] = "Unavaliable"

    completeList.append(allMembers)
    allMembers = {}


with open('data.json', 'w') as json_file:
    json.dump(completeList,json_file)



