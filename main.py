import pandas as pd
from ytinspector.youtube import YouTube
from ytinspector import convert_duration, locate_channel_id

def add_report(channenl_id):
    try:
        response = yt.retrieveChannelVideos(channel_id, 'by id')
        df = pd.DataFrame(response)

    except Exception as e:
        print(e)


CLIENT_FILE = 'desktop.json'


yt = YouTube(CLIENT_FILE)
yt.initService()

channel_id = locate_channel_id('GizsSo-EevA')
response = yt.retrieveChannelVideos(channel_id, 'by id')
df = pd.DataFrame(response)
df = pd.concat([df['id'], df['snippet'].apply(pd.Series), df['contentDetails'].apply(pd.Series), df['statistics'].apply(pd.Series)], axis=1)
df.fillna('', inplace=True)
df['duration'] = df['duration'].apply(convert_duration)
df['tags'] = df['tags'].str.join(',')
df['video url'] = 'https://www.youtube.com/watch?v={0}'.format(df['id'])
df.drop(['thumbnails', 'localized', 'contentRating'], axis=1, inplace=True, errors='ignore')

df.to_csv("scrape.csv")






