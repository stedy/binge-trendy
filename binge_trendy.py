import argparse
import re
import requests
import pandas as pd
import numpy as np
from sklearn import linear_model

parser = argparse.ArgumentParser(description="""Command line utility to
determine which TV show episodes are above the norm for a season as rated by IMDb users
for more informed binge watching""")
parser.add_argument('-url', help="IMDb show URL of interest")
parser.add_argument('-key', help="Text file with OMDb API key", type=argparse.FileType("r"))
parser.add_argument('-s', help="Season of interest")
parser.add_argument('-b', help="Episode with the highest residual", action='store_true')

args = parser.parse_args()

imdbID = [x for x in args.url.split("/") if re.match('tt', x)][0]
api_key = args.key.read().rstrip("\n")

omdb_url = "http://www.omdbapi.com/?i=" + imdbID + "&apikey=" + api_key
omdb_url_req = requests.get(omdb_url)
total_seasons = omdb_url_req.json()['totalSeasons']

season = None
if args.s:
    season = list(args.s)
else:
    season = list(range(1, int(total_seasons) + 1))

summary_list = ["Season", "Episode", "Value", "Name"]
episodes = []
final_df = pd.DataFrame()


for x in season:
    omdb_season_url = "http://www.omdbapi.com/?i=" + imdbID + "&Season=" + str(x) + "&apikey=" + api_key
    omdb_season_url_req = requests.get(omdb_season_url)

    episode = [float(y['Episode']) for y in omdb_season_url_req.json()['Episodes']]
    rating = [float(y['imdbRating']) for y in omdb_season_url_req.json()['Episodes']]
    title = [y['Title'] for y in omdb_season_url_req.json()['Episodes']]
    local_season = [list(str(x) * len(omdb_season_url_req.json()['Episodes']))]
    df = pd.DataFrame([local_season[0], episode, rating, title])

    df = df.transpose()
    df.columns = summary_list

    df_sorted = df.sort_values(by='Episode')
    x = np.array(df_sorted['Value']).reshape(-1, 1)
    y = np.array(df_sorted['Episode']).reshape(-1, 1)
    reg = linear_model.LinearRegression()
    reg.fit(y, x)

    df_sorted['Residual'] = x - reg.predict(y)

    final_df = final_df.append(df_sorted)

df_residuals = final_df.query('Residual > 0.0')

if args.b:
    print df_residuals[df_residuals['Residual'] == df_residuals['Residual'].max()].to_string(index=False)
else:
    print df_residuals[['Season', 'Episode', 'Name', 'Residual']].to_string(index=False)
