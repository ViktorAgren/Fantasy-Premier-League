import pandas as pd
import difflib
def display_history(player,year):
    string = "Fantasy-Premier-League-folder/data/"+year+"/gws/merged_gw.csv"
    df = pd.read_csv(string,index_col = 0)
    df = df.reset_index()
    df = df[df["name"] == difflib.get_close_matches(player, df["name"])[0]]
    df = df[['GW','total_points']]
    df.columns = ['Gameweek','Points']
    return print(df.to_markdown(index=False))


year = str(input('Enter the season (ex. 2022-23):\n'))
player = str(input('Enter the player (ex. Mohamed Salah) :\n'))
display_history(player,year)