import pandas as pd
import os
import unidecode
from dotenv import load_dotenv


load_dotenv()

url = os.getenv('URL')

if url is not None:
    try:
        df = pd.read_csv(url, encoding='utf-8')
        print("Data loaded successfully.")
        
       
        print(df.head())
        
    except UnicodeDecodeError:
        print("UTF-8 encoding failed. Trying ISO-8859-1 encoding...")
        try:
            df = pd.read_csv(url, encoding='ISO-8859-1')
            print("Data loaded successfully with ISO-8859-1 encoding.")
            print(df.head())
        except Exception as e:
            print(f"Failed to load data: {e}")
else:
    print("URL environment variable is not set.")

df = pd.read_csv(url)

df_filter = df[(df['year'] >= 1989) & (df['year'] <= 2024)]

max_years = df_filter['years_active'].max()

top_players = df_filter[df_filter['years_active'] == max_years].sort_values('year')



# issue with player colum
df['player'] = df['player'].apply(lambda x: unidecode.unidecode(x))



## most active years played 

print(f"Player with the most active years from draft classes 1989-2024:")
print(top_players[['player', 'year', 'years_active']])

print('\n')



## player with the most wins 


win_shares = 'win_shares'

max_winshares = df_filter[win_shares].max()

top_windshares_players = df_filter[df_filter[win_shares] == max_winshares].sort_values('year')

print('\n')

print(f"player with the most wins  from 1989 - 2024")
print(top_windshares_players[['player', 'year','years_active']])

print('\n')

## most rebounds 

rebounds = 'average_total_rebounds'

max_rebounds = df_filter[rebounds].max()

top_rebounder = df_filter[df_filter[rebounds] == max_rebounds].sort_values('year')
print("player with the most rebounds")
print(top_rebounder[['player', 'year','years_active']])

print(df.head())
print(df.describe())
print(df.info())

# most points all nba playrs 

points = 'points'

max_points = df_filter[points].max()

most_points = df_filter[df_filter[points] == max_points].sort_values('year')
print("player with the most points ")
print(most_points[['player', 'year', 'years_active']])



## year drafted 


players_2000 = df[(df['year'] == 2015) & (df['overall_pick'].notna()) & (df['team'].notna()) &  (df['college'].notna()) & (df['years_active'].notna())]

players_2000_sorted = players_2000.sort_values('overall_pick')


draft_list = [f"{int(row['overall_pick'])}. - {row['player']} - {row['team']} - {row['college']} - {row['years_active']}"
              for _, row in players_2000_sorted.iterrows()]


for players in draft_list:
    print(players)

with open('draftlist.txt', 'w') as f:

    for playerr in draft_list:
        f.write(f"{playerr}\n")