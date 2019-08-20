#%% [markdown]
# # Trending YouTube Video Statistics Analysis
# YouTube (the world-famous video sharing website) maintains a 
# list of the top trending videos on the platform. According to 
# Variety magazine, “To determine the year’s top-trending videos, 
# YouTube uses a combination of factors including measuring users interactions 
# (number of views, shares, comments and likes). Note that they’re not the 
# most-viewed videos overall for the calendar year”. Top performers on the 
# YouTube trending list are music videos (such as the famously virile “Gangam Style”), 
# celebrity and/or reality TV performances, and the random dude-with-a-camera viral 
# videos that YouTube is well-known for.
#
# This dataset was collected using the YouTube API.
#
# Columns include:
'''
- video_id
- trending_date
- title
- channel_title
- category_id
- publish_time
- tags
- views (number of views)
- likes (number of likes)
- dislikes (number of dislikes)
- comment_count 
- thumbnail_link
- comments_disabled
- ratings_disabled
- video_error_or_removed
- description
'''

#%% [markdown]
# ### Standard imports.
#%%
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from plotly.offline import iplot, init_notebook_mode
import seaborn as sns 
sns.set_style('whitegrid')
init_notebook_mode(connected=True)


#%% [markdown]
# ### Load Dataset
#%%
def load_data(path):
    return pd.read_csv(path)

df = load_data('data/USvideos.csv')

#%%
# Take a peak at the first 5 rows (head).
df.head()
