import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('URL')

df = pd.read_csv(url)

df_filtered = df[(df['year'] >= 2000) & (df['year'] <= 2024)]

max_active_years = df_filtered['years_active'].max()

top_players = df_filtered[df_filtered['years_active'] == max_active_years].sort_values('year')

print(f"Player(s) with the most active years ({max_active_years}) from draft classes 2000-2024:")
print(top_players[['player', 'year', 'years_active']])