import pandas as pd
import numpy as np
import glob
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns


sns.set(style="whitegrid")

# read in the files
json_files = glob.glob('../data/*.json')
sub_dataframes = []
for f in json_files:
    sub_dataframes.append(pd.read_json(f, orient='index'))

game_dataframe = pd.concat(sub_dataframes)

game_dataframe[game_dataframe.isnull().any(axis=1)]

game_dataframe = game_dataframe.dropna()

original_sub_vc = game_dataframe['original_subreddit'].value_counts()

sns.barplot(y=original_sub_vc.index, x=original_sub_vc.values, palette="viridis")

plt.xticks(rotation='vertical')
#plt.title('Registration Counts')
plt.xlabel('Number of Users', fontsize=12)
plt.ylabel('Original Subreddit', fontsize=12)
plt.show()

final_sub_vc = game_dataframe['current_subreddit'].value_counts()
final_sub_vc
sns.barplot(y=final_sub_vc.index, x=final_sub_vc.values, palette="viridis")

plt.xticks(rotation='vertical')
#plt.title('Registration Counts')
plt.xlabel('Number of Users', fontsize=12)
plt.ylabel('Final Subreddit', fontsize=12)
plt.show()

dValues = final_sub_vc - original_sub_vc


fig = sns.barplot(x=dValues.index, y=dValues.values, palette="viridis")

plt.xticks(rotation='vertical')
#plt.title('Registration Counts')
plt.xlabel('Subreddit', fontsize=12)
plt.ylabel('Change in Users', fontsize=12)
plt.show()
plt.draw()

plt.savefig("dUsers")
