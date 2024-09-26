import pandas as pd
import os
from dotenv import load_dotenv

def preprocess_nba_data(input_url, output_filepath):
    """
    Preprocesses the NBA draft data.
    
    Args:
    input_url (str): URL to the raw data file
    output_filepath (str): Path where the processed data should be saved
    
    Returns:
    None
    """
    # Read the data from the URL
    df = pd.read_csv(input_url)
    print("Data loaded successfully.")
    print(df.head())
    
    # Sort the dataframe by year and overall_pick
    df_sorted = df.sort_values(['year', 'overall_pick'])
    
    # Group by year and get the top 15 picks for each year
    top_15_per_year = df_sorted.groupby('year').head(15)
    
    # Select the columns we want for our players.csv
    columns_to_keep = [
        'id', 'year', 'overall_pick', 'team', 'player', 'college', 
        'years_active', 'games', 'points', 'total_rebounds', 'assists',
        'field_goal_percentage', '3_point_percentage', 'free_throw_percentage',
        'points_per_game', 'average_total_rebounds', 'average_assists',
        'win_shares', 'win_shares_per_48_minutes', 'box_plus_minus', 'value_over_replacement'
    ]
    
    top_15_players = top_15_per_year[columns_to_keep]
    
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
    
    # Save to CSV
    top_15_players.to_csv(output_filepath, index=False)
    
    print(f"Created {output_filepath} with {len(top_15_players)} players.")

if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    
    # Get the URL from the environment variable
    url = os.getenv('URL')
    if not url:
        raise ValueError("URL environment variable is not set. Please check your .env file.")

    # Set the output filepath
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_filepath = os.path.join(current_dir, 'processed', 'players.csv')
    
    # Process the data
    preprocess_nba_data(url, output_filepath)