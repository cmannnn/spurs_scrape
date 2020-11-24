import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Premier League Stats
page = requests.get('https://fbref.com/en/comps/9/Premier-League-Stats')

# making soup
soup = BeautifulSoup(page.content, 'html.parser')

site = soup.find(class_='fb') 

title_f1 = site.find(id='wrap')

title_f2 = title_f1.find(id='meta')

title_p = title_f2.find(itemprop='name').get_text().strip()

# most goals (but not efficient)
#most_goals_f2 = title_f2.p.nextSibling.nextSibling.nextSibling.get_text()


# print block
#print(
	# title_p,
	# most_goals_f2


