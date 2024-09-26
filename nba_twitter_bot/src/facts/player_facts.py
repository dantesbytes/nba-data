import random
from datetime import datetime

def generate_player_fact(players, teams, games, seasons, awards):
    """
    
    Args:
    players (list): List of dictionaries containing player data
    teams (list): List of dictionaries containing team data
    games (list): List of dictionaries containing game data
    seasons (list): List of dictionaries containing season data
    awards (list): List of dictionaries containing awards data
    
    Returns:
    str: A fact about a randomly selected player
    """
    player = random.choice(players)
    fact_types = [
        generate_draft_fact,
        generate_career_stats_fact,
        generate_team_fact,
        generate_award_fact,
        generate_comparison_fact
    ]
    
    chosen_fact_generator = random.choice(fact_types)
    return chosen_fact_generator(player, players, teams, games, seasons, awards)

def generate_draft_fact(player, players, teams, games, seasons, awards):
    return f"{player['player']} was drafted {ordinal(player['overall_pick'])} overall in the {player['year']} NBA draft by the {player['team']}."

def generate_career_stats_fact(player, players, teams, games, seasons, awards):
    stat = random.choice(['points', 'total_rebounds', 'assists'])
    return f"In {player['games']} career games, {player['player']} averaged {player[f'average_{stat}']} {stat.replace('_', ' ')} per game."

def generate_team_fact(player, players, teams, games, seasons, awards):
    team = next((team for team in teams if team['team'] == player['team']), None)
    if team:
        return f"{player['player']} was drafted by the {team['city']} {team['name']}, who play in the {team['conference']} Conference."
    return generate_draft_fact(player, players, teams, games, seasons, awards)

def generate_award_fact(player, players, teams, games, seasons, awards):
    player_awards = [award for award in awards if award['player_id'] == player['id']]
    if player_awards:
        award = random.choice(player_awards)
        return f"{player['player']} won the {award['category']} award in the {award['season_id']} season."
    return generate_career_stats_fact(player, players, teams, games, seasons, awards)

def generate_comparison_fact(player, players, teams, games, seasons, awards):
    comp_player = random.choice(players)
    while comp_player['id'] == player['id']:
        comp_player = random.choice(players)
    
    stat = random.choice(['points_per_game', 'average_total_rebounds', 'average_assists'])
    if float(player[stat]) > float(comp_player[stat]):
        comparison = "higher"
    else:
        comparison = "lower"
    
    return f"{player['player']} has a {comparison} career {stat.replace('_', ' ')} ({player[stat]}) than {comp_player['player']} ({comp_player[stat]})."

def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"
