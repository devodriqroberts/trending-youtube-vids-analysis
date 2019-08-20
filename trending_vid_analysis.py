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
from datetime import datetime
import dateutil.parser
import seaborn as sns 
sns.set_style('whitegrid')
init_notebook_mode(connected=True)



#%%
def load_data(path):
    return pd.read_csv(path)

# Convert timestamp strings to datetime object.
def convert_date(timestamp, date_format='%Y-%m-%d'):
    '''
    Converts timestamp to datetime object with specified format.
    default format: '%Y-%m-%d'
    '''
    if 'Z' not in timestamp: # trending_date has format 'yy.dd.mm'
        parsed_date = datetime.strptime(timestamp, '%y.%d.%m')
        return parsed_date
    else:               # publish_time has format 'yyyy-mm-ddThh:mm:ss.000Z'
        d = dateutil.parser.parse(timestamp)
        parsed_date = d.strftime('%Y-%m-%d')
        return d.strptime(parsed_date, date_format)


# Map category labels, add category_label column.
def map_categories(df, column='category_label', map_dict=category_dict):
    '''
    Adds category label column to dataframe.
    Accepts df: Dataframe to perform map on.
            column: Column name in df to perform map on. (default='category_label')
            map_dict: Dictionary containing map items. (default=category_dict)
    '''
    df[column] = df.category_id.map(map_dict)
    return df

# Find top youTube video producers for specified year.
def top_video_producing_for_yr(df, year, top_range=5):
    '''
    Finds top video producers for specified year.
    Accepts df: Dataframe.
            year: Year to filter by.
            top_range: Number of top entries to print / return. (default=5)
    '''

    year_filter = [date.year == year for date in df['publish_time']]
    sliced_df = df[year_filter]

    channel_vid_groups = sliced_df.groupby(['channel_title'])['video_id'].count()
    sorted_groups = channel_vid_groups.sort_values(ascending=False)
    top_producers = sorted_groups[:top_range]

    print('#'*30)
    print(f'Top {top_range} video producers in {year} were:')
    print()
    i = 0
    for vid_count in top_producers:
        print('\t', f'{str(i+1)}) {top_producers.index[i]} : {vid_count} videos.', end='')
        print('\n')
        i += 1

    print('#'*30)

    return top_producers


#%% [markdown]
# ### Load Dataset
#%%
df = load_data('data/USvideos.csv')

#%%
date_columns = ['trending_date', 'publish_time']

for col in date_columns:
    df[col] = [convert_date(ts) for ts in df[col]]

#%%
# Take a peak at the first 5 rows (head).
df.head()

#%%
# Take a peak at the dataframes info function.
df.info()

# 40,949 total entries.
# Every column looks complete with the exception of the video descriptions.

#%%
# Take a peak at the dataframes describe function.
df.describe()

#%% [markdown]
# ## Exploring video category.

'''
- Which category was assigned the most?
- Which category was assigned the least?
- Which creator uploaded the most videos?
>- Which were thier most assigned video category?
'''
#%%
# Let add category labels to the dataframe.
category_dict = {
    
    1 :  'Film & Animation',
    2 : 'Autos & Vehicles',
    10 : 'Music',
    15 : 'Pets & Animals',
    17 : 'Sports',
    18 : 'Short Movies',
    19 : 'Travel & Events',
    20 : 'Gaming',
    21 : 'Videoblogging',
    22 : 'People & Blogs',
    23 : 'Comedy',
    24 : 'Entertainment',
    25 : 'News & Politics',
    26 : 'Howto & Style',
    27 : 'Education',
    28 : 'Science & Technology',
    29 : 'Nonprofits & Activism',
    30 : 'Movies',
    31 : 'Anime/Animation',
    32 : 'Action/Adventure',
    33 : 'Classics',
    34 : 'Comedy',
    35 : 'Documentary',
    36 : 'Drama',
    37 : 'Family',
    38 : 'Foreign',
    39 : 'Horror',
    40 : 'Sci-Fi/Fantasy',
    41 : 'Thriller',
    42 : 'Shorts',
    43 : 'Shows',
    44 : 'Trailers',
}


#%%
# Store new dataframe in a new variable.
mapped_df = map_categories(df)

# Rearrange columns so that category_id 
# and category_label are next to one another.
mapped_df = mapped_df[['video_id', 'trending_date', 'title', 'channel_title', 'category_id',
                    'category_label', 'publish_time', 'tags', 'views', 'likes', 'dislikes', 
                    'comment_count', 'thumbnail_link', 'comments_disabled', 'ratings_disabled',
                    'video_error_or_removed', 'description']]

#%%
category_counts = mapped_df.category_label.value_counts()
category_counts

#%%
i = 0
for count in category_counts:
    print(f'Of the {mapped_df.shape[0]} videos uploaded, {count} ({(count/mapped_df.shape[0]) * 100:0.2f}%) videos were of the {category_counts.index[i]} category.')
    print()
    i += 1

#%%
channels = mapped_df['channel_title'].unique()
num_of_channels = len(channels)



#%%
top_video_producing_for_yr(mapped_df, 2017)
#%%
# sliced_df = [date.year == 2017 for date in df['publish_time']]
# print(min(sliced_df), max(sliced_df))
# print(df['publish_time'].min(), df['publish_time'].max())

# sliced_df_2 = df[sliced_df]
# #%%
# sliced_df_2.head()
# #%%
# mapped_df['trending_date'][0].year == 2016

# #%%
# df.tail()

# #%%
