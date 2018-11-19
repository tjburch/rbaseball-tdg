
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import glob
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

sns.set(style="whitegrid")


# In[2]:


# read in the files
json_files = glob.glob('../data/*.json')
sub_dataframes = []
for f in json_files:
    sub_dataframes.append(pd.read_json(f, orient='index'))

game_dataframe = pd.concat(sub_dataframes)
game_dataframe


# In[3]:


# NaNs?
game_dataframe[game_dataframe.isnull().any(axis=1)]


# All Deleted - either over the course of the week or otherwise.

# In[4]:


game_dataframe = game_dataframe.dropna()
game_dataframe.describe()


# In[5]:


original_sub_vc = game_dataframe['original_subreddit'].value_counts()
original_sub_vc


# In[6]:


sns.barplot(y=original_sub_vc.index, x=original_sub_vc.values, palette="viridis")

plt.xticks(rotation='vertical')
#plt.title('Registration Counts')
plt.xlabel('Number of Users', fontsize=12)
plt.ylabel('Original Subreddit', fontsize=12)
#plt.show()
plt.savefig("orignal_users")


# In[7]:


final_sub_vc = game_dataframe['current_subreddit'].value_counts()
final_sub_vc
sns.barplot(y=final_sub_vc.index, x=final_sub_vc.values, palette="viridis")

plt.xticks(rotation='vertical')
#plt.title('Registration Counts')
plt.xlabel('Number of Users', fontsize=12)
plt.ylabel('Final Subreddit', fontsize=12)
#plt.show()
plt.savefig("final_users")


# In[8]:


dValues = final_sub_vc - original_sub_vc
dValues


# In[9]:


dValues.sort_values(inplace=True)

fig = sns.barplot(x=dValues.index, y=dValues.values, palette="viridis")

#ax = plt.gca()

plt.xticks(rotation='vertical')
#plt.title('Registration Counts')
plt.xlabel('Subreddit', fontsize=12)
plt.ylabel('Change in Users', fontsize=12)

#ax.grid(False)

plt.tight_layout()

plt.draw()
plt.savefig("dUsers")
plt.show()


# In[10]:


normalized_dValues = dValues/original_sub_vc
normalized_dValues.sort_values(inplace=True)

fig = sns.barplot(x=normalized_dValues.index, y=normalized_dValues.values, palette="viridis")



plt.xticks(rotation='vertical')
#plt.title('Registration Counts')
plt.xlabel('Subreddit', fontsize=12)
plt.ylabel('Percent Change in Users', fontsize=12)

#ax.grid(False)
ax = plt.gca()
import matplotlib.ticker as plticker
loc = plticker.MultipleLocator(base=0.2)
ax.yaxis.set_major_locator(loc)

plt.tight_layout()

plt.draw()
plt.savefig("dUsers_normed")
plt.show()


# In[11]:


normalized_dValues*100


# In[12]:


game_dataframe['comment_karma'].hist(bins=30)


# In[13]:


game_dataframe[game_dataframe.comment_karma < 200000].comment_karma.hist(bins=100)


# In[14]:


game_dataframe[game_dataframe.comment_karma < 500].comment_karma.hist(bins=100)


# In[15]:


game_dataframe[game_dataframe.comment_karma < 0]


# In[16]:


game_dataframe[game_dataframe.total_karma < 200000].total_karma.hist(bins=100)


# In[17]:


# original_karma_vc = game_dataframe.groupby('original_subreddit')['total_karma'].sum()
# final_karma_vc = game_dataframe.groupby('current_subreddit')['total_karma'].sum()
# original_karma_vc.sort_values(inplace=True)
# final_karma_vc.sort_values(inplace=True)


# # In[18]:


# sns.barplot(x=original_karma_vc.index, y=original_karma_vc.values, palette="viridis")
# plt.xticks(rotation='vertical')
# plt.xlabel('Subreddit')
# plt.ylabel('Sum Original Karma (comment + post)')
# #plt.savefig("total_karma_original")


# # In[19]:


# sns.barplot(x=final_karma_vc.index, y=final_karma_vc.values, palette="viridis")
# plt.xticks(rotation='vertical')
# plt.xlabel('Subreddit')
# plt.ylabel('Sum Final Karma (comment + post)')
# plt.savefig("total_karma_final")


# # In[20]:


# dkarma_vc = original_karma_vc - final_karma_vc
# dkarma_vc.sort_values(inplace=True)

# sns.barplot(x=dkarma_vc.index, y=dkarma_vc.values, palette="viridis")
# plt.xticks(rotation='vertical')
# plt.xlabel('Subreddit')
# plt.ylabel('Change in Net Karma')
# plt.savefig("dKarma")


# # In[21]:


# normed_karma0 = original_karma_vc/original_sub_vc
# normed_karma0.sort_values(inplace=True)

# sns.barplot(x=normed_karma0.index, y=normed_karma0.values, palette="viridis")
# plt.xticks(rotation='vertical')
# plt.xlabel('Subreddit')
# plt.ylabel('Original Karma/User')
# plt.savefig("normed_karma_final")


# # In[22]:


# normed_karmaf = final_karma_vc/final_sub_vc
# normed_karmaf.sort_values(inplace=True)

# sns.barplot(x=normed_karmaf.index, y=normed_karmaf.values, palette="viridis")
# plt.xticks(rotation='vertical')
# plt.xlabel('Subreddit')
# plt.ylabel('Final Karma/User')
# plt.savefig("normed_karma_final")


# # In[23]:


# normed_dkarma = normed_karmaf - normed_karma0
# normed_dkarma.sort_values(inplace=True)

# sns.barplot(x=normed_dkarma.index, y=normed_dkarma.values, palette="viridis")
# plt.xticks(rotation='vertical')
# plt.xlabel('Subreddit')
# plt.ylabel('$\Delta$ Karma/User')
# plt.savefig("normed_dkarma")


# # In[24]:


# #sns.heatmap(game_dataframe.original_subreddit, game_dataframe.current_subreddit)


# # In[32]:


fig = plt.figure(figsize=(2,1))


fig = sns.catplot(x="original_subreddit", y="total_karma", data=game_dataframe, kind="swarm", alpha=0.85)

plt.xticks(rotation='vertical')
plt.xlabel('Subreddit')
plt.ylabel('Karma')
plt.yscale('log')
plt.savefig("karma_dist")


# In[26]:


print sns.__version__
