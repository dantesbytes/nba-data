import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from dotenv import load_dotenv
import os
import unidecode
load_dotenv()



def load_data_from_url(url):
    """Load the data from a URL."""
    return pd.read_csv(url)

def create_rolling_averages(df, columns, window=5):
   

def create_team_stats(df):
   

def create_position_stats(df):
   

def create_efficiency_features(df):
 

def scale_features(df, columns_to_scale):
   

def build_features(url, output_filepath=None):
  
    
   

if __name__ == "__main__":
    url = os.getenv('URL')  
    output_filepath = "data/processed/feature_engineered_nba_data.csv"
    feature_engineered_df = build_features(url, output_filepath)
    print(feature_engineered_df.head()) 