import argparse
import re
import requests
import sys
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
parser.add_argument('-tt', help="List of top ten rated episodes of show", action='store_true')

args = parser.parse_args()

imdbID = [x for x in args.url.split("/") if re.match('tt', x)][0]
api_key = args.key.read().rstrip("\n")

omdb_url = "http://www.omdbapi.com/?i=" + imdbID + "&apikey=" + api_key

omdb_url_req = requests.get(omdb_url)

if omdb_url_req.status_code != 200:
    print "Error: https://http.cat/" + str(omdb_url_req.status_code)
    sys.exit(1)

total_seasons =  omdb_url_req.json()['totalSeasons']

season = None
if args.s:
    season = [args.s]
else:
    season = list(range(1, int(total_seasons) + 1))

summary_list = ["Season", "Episode", "Value", "Name"]
final_df = pd.DataFrame()

for x in season:
    omdb_season_url = "http://www.omdbapi.com/?i=" + imdbID + "&Season=" + str(x) + "&apikey=" + api_key
    omdb_season_url_req = requests.get(omdb_season_url)

    episode = [float(y['Episode']) for y in omdb_season_url_req.json()['Episodes']]
    rating = [y['imdbRating'] for y in omdb_season_url_req.json()['Episodes']]
    title = [y['Title'] for y in omdb_season_url_req.json()['Episodes']]
    local_season = [x] * len(omdb_season_url_req.json()['Episodes'])
    df = pd.DataFrame([local_season, episode, rating, title])

    df = df.transpose()
    df.columns = summary_list

    df = df[df.Value != 'N/A']
    df['Value'] = df['Value'].astype(float)

    df_sorted = df.sort_values(by='Episode')
    x = np.array(df_sorted['Value']).reshape(-1, 1)
    y = np.array(df_sorted['Episode']).reshape(-1, 1)
    if len(df_sorted) > 1:
        reg = linear_model.LinearRegression()
        reg.fit(y, x)
        #output = pd.DataFrame([x.flatten(),y.flatten(),reg.predict(y).flatten()]).transpose()
        #output.columns = ["x", "y", "predict"]
        #output.to_csv("lr_testing.csv", index=False) #, output, delimiter=",")
        df_sorted['Residual'] = x - reg.predict(y)
        final_df = final_df.append(df_sorted)
        df_residuals = final_df.query('Residual > 0.0')
        df_residuals = df_residuals.drop(columns=['Value'])

if args.b:
    print df_residuals[df_residuals['Residual'] == df_residuals['Residual'].max()].to_string(index=False)
if args.tt:
    print df_residuals.sort_values(by=['Residual'], ascending = False)[:10].to_string(index=False)
if args.s:
    print df_residuals[['Season', 'Episode', 'Name', 'Residual']].to_string(index=False)
    #else:
    #    print "Not enough data for this season"
