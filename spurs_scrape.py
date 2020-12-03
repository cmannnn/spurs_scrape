import requests
from bs4 import BeautifulSoup
import pandas as pd

# Premier League Stats
html_text = requests.get('https://fbref.com/en/comps/9/Premier-League-Stats').text
soup = BeautifulSoup(html_text, 'lxml')

# players stats - most goals
player_goals = soup.find('div', id='wrap')
player_goals2 = player_goals.find('div', id='info')
player_goals3 = player_goals2.find('div', id='meta')
player_goals4 = player_goals3.find_all('div')[1]
player_goals5 = player_goals4.find_all('p')[3].text

# players stats - most assists
player_assists = player_goals4.find_all('p')[4].text

# player stats - most clean sheets
player_clean_sheets = player_goals4.find_all('p')[5].text

#print(f'{player_goals5}')
#print(f'{player_assists}')
#print(f'{player_clean_sheets}')

# current league table
current_league_table = pd.read_html('https://fbref.com/en/comps/9/Premier-League-Stats')[0]
current_league_table = current_league_table.set_index('Rk')
current_league_table = current_league_table.drop(['Notes', 'Attendance'], axis=1)

#print(current_league_table.info())

# squad stats NOT PULLING SECOND TABLE IN CORRECTLY
squad_stats_table = pd.read_html('https://fbref.com/en/comps/9/Premier-League-Stats', header=1)[1]

# dropping necessary columns + cleaning column names
squad_stats_table = squad_stats_table.drop(columns=['MP.1', 'W.1', 'D.1', 'L.1', 'GF.1', 'GA.1', 'GDiff.1', 'Pts.1', 'Pts/G.1', 'xG.1', 'xGA.1', 'xGDiff.1', 'xGDiff/90.1'])
squad_stats_table = squad_stats_table.rename(columns={'Rk': 'Rank', 'MP': 'Matches Played'})


print(squad_stats_table.columns)
