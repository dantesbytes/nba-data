import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('URL')

df = pd.read_csv(url)

df_filter = df[(df['year'] >= 2000) & (df['year'] <= 2024)]

max_years = df_filter['years_active'].max()

top_players = df_filter[df_filter['years_active'] == max_years].sort_values('year')

print(f"Player(s) with the most active years ({max_years}) from draft classes 2000-2024:")
print(top_players[['player', 'year', 'years_active']])

print(df.head())


max_winshares = df_filter['win_shares'].max()

top_windshares_players = df_filter[df_filter['win_shares'] == max_winshares].sort_values('year')

print(f"player(s) with the most wind shares ({max_winshares}) from 2000 - 2024")

print(top_windshares_players[['player', 'year','years_active']])