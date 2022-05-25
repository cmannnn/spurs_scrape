matches = ['Sat,', 'Apr', '16', 'Tottenham', 'Hotspur', 'v', 'Brighton', '&', 'Hove', 'Albion', '7:30', 'AM', 'English', 'Premier', 'League', 'Sat,', 'Apr', '23', 
'Brentford', 'v', 'Tottenham', 'Hotspur', '12:30', 'PM', 'English', 'Premier', 'League', 'Sat,', 'Apr', '30', 'Tottenham', 'Hotspur', 'v', 'Leicester', 'City', '10:00', 
'AM', 'English', 'Premier', 'League']

other_matches = ['Sat, Apr 16', 'Tottenham Hotspur', 'v', 'Brighton & Hove Albion', '7:30 AM English Premier League', 'Sat, Apr 23', 'Brentford', 'v',
'Tottenham Hotspur', '12:30 PM English Premier League', 'Sat, Apr 30', 'Tottenham Hotspur', 'v', 'Leicester City', '10:00 AM English Premier League']

# date_time = other_matches[4].split(' ', 2)
# print(date_time)
date = other_matches[::5]
time = other_matches[4::5]

hour_am_pm = []
league = []

for p in time:
	time_split = p.split(' ', 2)
	# print(time_split)
	hour_am_pm_split = time_split[0] + ' ' + time_split[1]
	hour_am_pm.append(hour_am_pm_split)
	league_split = time_split[2]
	league.append(league_split)
	# print(league)

# print(date)
# print(hour_am_pm)

date_time = []

for d in date:
	for t in hour_am_pm:
		time_time = d + ' ' + t
		date_time.append(time_time)

# print(date_time)
# print(league)

print(other_matches)

home_split = other_matches[1::5]
vs_split = other_matches[2::5]
away_split = other_matches[3::5]

home_away = []

for a in home_split:
	home_away.append(a
			# home_away_grab = h + ' ' + v + ' ' + a
			# home_away.append(home_away_grab)

# print(home_away)

# for m in other_matches:
# 	print(m[1])
	# home_split = m[1::5]
	# vs_split =
	# away_split = 
	# print(home_split)














