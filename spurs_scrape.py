from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime

# Premier League Stats
url = 'https://www.espn.com/soccer/teams'

driver = webdriver.Chrome("/Users/cman/python-virtual-environments/code/spurs_scrape/chromedriver")

driver.get(url)

teams_homepage = driver.find_element_by_xpath('//a[contains(@href,"/fixtures/_/id/367/tottenham-hotspur")]')

teams_homepage.click()

fixtures = driver.find_elements_by_class_name('Table__TBODY')

fixture_list = []

for i in fixtures:
	matches = i.text.split('\n')
	fixture_list += matches
	date_time = fixture_list[4].split(' ', 2)
	time = date_time[0] + ' ' + date_time[1]
	date_time_final = fixture_list[0] + ' ' + time
	teams = fixture_list[1] + ' ' + fixture_list[2] + ' ' + fixture_list[3]


# print(fixture_list)



print(teams)
print(date_time_final)