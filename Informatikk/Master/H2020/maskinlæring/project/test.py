import pandas as pd

df = pd.read_csv('genre_songs.csv', engine='python', quotechar='"')

print(df.head(1))

print(list(sorted(df['track.album.release_date']))[1])
print(list(sorted(df['track.album.release_date'], reverse=True))[0])