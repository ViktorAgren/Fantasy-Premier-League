import pandas as pd
import difflib
def display_history(player, year):
    """
    Given a player's name and the year, displays the gameweek history of the player.

    Parameters:
    player (str): The name of the player.
    year (str): The year of the season.

    Returns:
    Markdown table: The points per gameweek
    """
    name = player.split()
    id = find_player_id(player, year)
    name_id = "_".join([name[0], name[1], id])
    df = pd.read_csv(f"FPL-Folder/data/{year}/players/{name_id}/gw.csv", index_col=0)
    df = df.reset_index()
    df = df[['round', 'total_points']]
    df.columns = ['Gameweek', 'Points']
    print(df.to_markdown(index=False))

def find_player_id(player,year):
    """
    Given a player's name and the year, returns the ID of the player.

    Parameters:
    player (str): The name of the player.
    year (str): The year of the season.

    Returns:
    str: The ID of the player.
    """
    name = player.split()
    player_id = "FPL-Folder/data/"+year+"/player_idlist.csv"
    df = pd.read_csv(player_id,index_col=False)
    df = df[df["first_name"] == name[0]]
    id = df[df["second_name"] == name[1]]['id'].to_string(index=False)
    return id

def find_team_id(team, year):
    """
    Given a team name and the year, returns the ID of the team.

    Parameters:
    team (str): The name of the team.
    year (str): The year of the season.

    Returns:
    str: The ID of the team.
    """
    teams = "FPL-Folder/data/"+year+"/teams.csv"
    df_id = pd.read_csv(teams,index_col=False)
    id = df_id[df_id["name"] == team]['id'].to_string(index=False)
    return id

def display_players_in_squad(team, year):
    """
    Given a team name and the year, displays the list of players in the team.

    Parameters:
    team (str): The name of the team.
    year (str): The year of the season.

    Returns:
    Markdown table: The first and second name of players in squad
    """
    team_id = int(find_team_id(team,year))
    players_raw = "FPL-Folder/data/"+year+"/players_raw.csv"
    df = pd.read_csv(players_raw,index_col=False)
    df = df[df['team'] == team_id]
    df = df[['first_name','second_name']]
    print(df.to_markdown(index=False))

def display_teams(year):
    """
    Given a year, displays the list of teams in the season.

    Parameters:
    year (str): The year of the season.

    Returns:
    Markdown table: The teams in the given season
    """
    teams = "FPL-Folder/data/"+year+"/teams.csv"
    df = pd.read_csv(teams,index_col=False)['name']
    print(df.to_markdown(index=False))

def display_transfer_history(player, year):
    """
    Given a player's name and the year, displays the transfer history of the player.

    Parameters:
    player (str): The name of the player.
    year (str): The year of the season.

    Returns:
    Markdown table: The transfers per gameweek for a certain player
    """
    name = player.split()
    id = find_player_id(player, year)
    name_id = name[0]+'_'+name[1]+'_'+id
    player_id_string = "FPL-Folder/data/"+year+"/players/"+name_id+"/gw.csv"
    df = pd.read_csv(player_id_string,index_col = 0)
    df = df.reset_index()
    df = df[['round','transfers_balance','transfers_in','transfers_out']]
    df.columns = ['Gameweek','Net transfers','Transfers in', 'Transfers out']
    print(df.to_markdown(index=False))

def main():
    decision = input("What would you like to print?\n 1: Display teams per year\n 2: Display players in team per year\n 3: Display player gameweek history per year\n 4: Display player transfer history per year\n")

    match decision:
        case '1':
            year = input('Enter the season (ex. 2022-23):\n')
            display_teams(year)
        case '2':
            year = input('Enter the season (ex. 2022-23):\n')
            team = input('Enter the team (ex. Liverpool):\n')
            display_players_in_squad(team, year)
        case '3':
            year = input('Enter the season (ex. 2022-23):\n')
            player = input('Enter the player (ex. Mohamed Salah) :\n')
            display_history(player, year)
        case '4':
            year = input('Enter the season (ex. 2022-23):\n')
            player = input('Enter the player (ex. Mohamed Salah) :\n')
            display_transfer_history(player, year)

if __name__ == "__main__":
    main()