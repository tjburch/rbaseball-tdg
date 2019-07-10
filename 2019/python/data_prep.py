import pandas as pd
from update_data import update_data

update_data()

df_players = pd.read_json("../data/players.json")
df_info = pd.read_json("../data/mlb_colors.json")

df_info = df_info.drop(["league"],axis=1)
df_players = df_players.drop(["team","id"], axis=1)

# Merge on player
df_players = pd.merge(df_players, df_info, how="left", left_on="original_team_id", right_on="id")

# Rename a bunch of those
renames = {
    "colors": "original_colors",
    "name": "original_team_name",
    "sub": "original_sub_name",
}
df_players = df_players.rename(index=str, columns=renames)

df_players = pd.merge(df_players, df_info, how="left", left_on="current_team_id", right_on="id")
renames = {
    "colors": "current_colors",
    "name": "current_team_name",
    "sub": "current_sub_name",
}
df_players = df_players.rename(index=str, columns=renames)

df_players = pd.merge(df_players, df_info, how="left", left_on="ntc", right_on="id")
df_players = df_players.rename(index=str, columns={"sub":"ntc_sub"})
df_players = df_players.drop(["colors","name","id_x","id_y","id"],axis=1)


df_players.to_pickle("../data/players.pickle")
