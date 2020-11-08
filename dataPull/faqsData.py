import requests 
import json
from bs4 import BeautifulSoup 


# This python code is to scrape data from the given website and write it in a json file
  
URL = "https://undergrad.cs.umd.edu/faq"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 

table = soup.find_all('div', attrs = {'class':'panel panel-default'})

questionsAnswers = {}
completeList = []
for t in table:
    answer = t.find('div', attrs = {'class':'field-content'}).find('p')
    if(answer is not None):
        answer = answer.getText()
        question = t.find('h4', attrs = {'class':'panel-title'}).find('a').text.strip()

        questionsAnswers["Question"] = question
        questionsAnswers["Answer"] = answer

        completeList.append(questionsAnswers)

print(len(completeList))

with open('faqs.json', 'w') as json_file:
    json.dump(completeList,json_file)



