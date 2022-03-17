import bs4
import requests
import pandas as pd

url = 'https://www.theguardian.com/football/premierleague/results'
res = requests.get(url)
result_text = res.text
with open('matchday_results.html', 'w') as f:
    f.write(result_text)

parse_results = bs4.BeautifulSoup(result_text, 'html.parser')
team_name = parse_results.find_all('span', class_='team-name__long')
match_result = parse_results.find_all('div', class_='football-team__score')
print(len(team_name))
print(len(match_result))
home_result = team_name[0].text.strip() + " " + match_result[0].text.strip()
away_result = team_name[1].text.strip() + " " + match_result[1].text.strip()
# print(home_result + " " + away_result)

matchday_result = []
for i in range(0, len(team_name), 2):
    x = team_name[i].text.strip() + " " + match_result[i].text.strip()
    y = team_name[i+1].text.strip() + " " + match_result[i+1].text.strip()
    z = x + " " + y
    matchday_result.append(z)

for i in range(0, 10):
    print(matchday_result[i])