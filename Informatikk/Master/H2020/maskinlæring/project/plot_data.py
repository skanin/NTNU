# import numpy as np
# import matplotlib.pyplot as plt
# import csv

# with open('dataset.csv', 'r') as f:
#     tmpLst = []
#     reader = csv.reader(f, quotechar='"', doublequote=True, escapechar='\\')

#     for row in reader:
#         tmpLst.append(row)

#     f = tmpLst.copy()
#     origheaders = f[0]
#     f = f[1:]
#     headers = origheaders[1:3] + origheaders[4:]
#     attributtes = headers[3:]
#     attributtes.append('count')

#     genres = list(set([elem[3] for elem in f]))

#     tmp = dict(list(map(lambda x: [x, dict(list(map(lambda x: [x.lower(), 0], attributtes)))], genres)))

#     for song in f:
#         for i, head in enumerate(list(map(lambda x: x.lower(), origheaders))):
#             if head in tmp[song[3]] and head.lower() != 'year':
#                 try:
#                     if ',' in song[i] and i != 1:
#                         song[i] = song[i].replace(',', '.')
#                         tmp[song[3]][head] += float(song[i])
#                     else:
#                         tmp[song[3]][head] += int(song[i])
#                 except Exception as e:
#                     print(song)
#                     print(e)
#         tmp[song[3]]['count'] += 1


#     for genre, attrs in tmp.items():
#         for attr, value in attrs.items():
#             if attr != 'count':
#                 if attrs['count'] == 0:
#                     print(attrs)
#                     print(genre)
#                 attrs[attr] = value / attrs['count']

#     tmp = sorted(tmp.items(), key=lambda x: x[1]['count'], reverse=True)

#     # to_plot = [] + tmp[0:2] + tmp[len(tmp) // 2 : len(tmp) // 2 + 2] + tmp[len(tmp) - 2 :]
    
#     to_plot = tmp[:10]
    
#     most_popular_genres = ['pop', 'hip hop', 'modern rock', 'disco']

#     print(list(map(lambda x: x[0], tmp)))

#     objects = [elem.capitalize() for elem in map(lambda x: x[0], to_plot)]
#     lengths = sorted([elem for elem in map(lambda x: x[1]['length (duration)'], to_plot)])

#     y_pos = np.arange(len(objects))

#     plt.bar(y_pos, lengths, align='center', alpha=0.5)
#     plt.xticks(y_pos, objects)
#     plt.ylabel('Length (seconds)')
#     plt.title('Mean lengths for top 10 genres in the dataset')
#     tl = plt.gca().get_xticklabels()
#     maxsize = max([len(t) for t in objects])
#     m = 0.2
#     s = maxsize/plt.gcf().dpi*150+2*m
#     margin = m/plt.gcf().get_size_inches()[0]

#     plt.gcf().subplots_adjust(left=margin, right=1.-margin)
#     plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
#     plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

df = pd.read_csv('genre_songs.csv', engine='python', quotechar='"')

headers = list(df.head(1))
songs = {'genres': {}, 'subgenres': {}}

# "danceability","energy","key","loudness","mode","speechiness","acousticness","instrumentalness",
# "liveness","valence","tempo","duration_ms"

for tmp in set(df['playlist_genre']):
    songs['genres'][tmp] = {
        'danceability': 0,
        'energy': 0,
        'key': 0,
        'loudness': 0,
        'mode': 0,
        'speechiness': {},
        'acousticness': {},
        'instrumentalness': 0,
        'liveness': 0,
        'valence': 0,
        'tempo': 0,
        'duration_ms': 0,
        'track.popularity': 0,
        'track.album.release_date': 0,
        'count': 0
    }

for tmp in set(df['playlist_subgenre']):
    songs['subgenres'][tmp] = {
        'danceability': 0,
        'energy': 0,
        'key': 0,
        'loudness': 0,
        'mode': 0,
        'speechiness': {},
        'acousticness': 0,
        'instrumentalness': 0,
        'liveness': 0,
        'valence': 0,
        'tempo': 0,
        'duration_ms': 0,
        'track.popularity': 0,
        'track.album.release_date': 0,
        'count': 0
    }

print(len(list(songs['genres'].keys())))

for index, row in df.iterrows():
    # print(songs['genres'][row['playlist_genre']]['speechiness'])
    songs['genres'][row['playlist_genre']]['acousticness'][round(row['acousticness'], 3)] = songs['genres'][row['playlist_genre']]['acousticness'].get(round(row['acousticness'], 3), 0) + 1
    # year = row['track.album.release_date'][0:4]
    # songs['genres'][row['playlist_genre']]['danceability'] += row['danceability']
    # songs['genres'][row['playlist_genre']]['energy'] += row['energy']
    # songs['genres'][row['playlist_genre']]['key'] += row['key']
    # songs['genres'][row['playlist_genre']]['loudness'] += row['loudness']
    # songs['genres'][row['playlist_genre']]['mode'] += row['mode']
    # songs['genres'][row['playlist_genre']]['speechiness'] += row['speechiness']
    # songs['genres'][row['playlist_genre']]['acousticness'] += row['acousticness']
    # songs['genres'][row['playlist_genre']]['instrumentalness'] += row['instrumentalness']
    # songs['genres'][row['playlist_genre']]['liveness'] += row['liveness']
    # songs['genres'][row['playlist_genre']]['valence'] += row['valence']
    # songs['genres'][row['playlist_genre']]['tempo'] += row['tempo']
    # songs['genres'][row['playlist_genre']]['duration_ms'] += row['duration_ms']
    # songs['genres'][row['playlist_genre']]['track.popularity'] += row['track.popularity']
    # songs['genres'][row['playlist_genre']]['track.album.release_date'] += int(year)
    # songs['genres'][row['playlist_genre']]['count'] += 1

    # songs['subgenres'][row['playlist_subgenre']]['danceability'] += row['danceability']
    # songs['subgenres'][row['playlist_subgenre']]['energy'] += row['energy']
    # songs['subgenres'][row['playlist_subgenre']]['key'] += row['key']
    # songs['subgenres'][row['playlist_subgenre']]['loudness'] += row['loudness']
    # songs['subgenres'][row['playlist_subgenre']]['mode'] += row['mode']
    # songs['subgenres'][row['playlist_subgenre']]['speechiness'] += row['speechiness']
    # songs['subgenres'][row['playlist_subgenre']]['acousticness'] += row['acousticness']
    # songs['subgenres'][row['playlist_subgenre']]['instrumentalness'] += row['instrumentalness']
    # songs['subgenres'][row['playlist_subgenre']]['liveness'] += row['liveness']
    # songs['subgenres'][row['playlist_subgenre']]['valence'] += row['valence']
    # songs['subgenres'][row['playlist_subgenre']]['tempo'] += row['tempo']
    # songs['subgenres'][row['playlist_subgenre']]['duration_ms'] += row['duration_ms']
    # songs['subgenres'][row['playlist_subgenre']]['track.popularity'] += row['track.popularity']
    # songs['subgenres'][row['playlist_subgenre']]['track.album.release_date'] += int(year)
    # songs['subgenres'][row['playlist_subgenre']]['count'] += 1


# for head in headers:
#     for key, value in songs['genres'].items():
#         if head in value.keys():
#             songs['genres'][key][head] = songs['genres'][key][head] / songs['genres'][key]['count']



# attrs = ['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms','track.popularity','track.album.release_date','count']

# objects = [elem.capitalize() for elem in list(songs['genres'].keys())]
# for attr in attrs:
#     to_plot = []
#     for genre in objects:
#         to_plot.append(songs['genres'][genre.lower()][attr])

#     label = attr.capitalize()
#     if attr == 'track.popularity':
#         label = "Popularity"
#     elif attr == 'track.album.release_date':
#         label = 'Year'

#     y_pos = np.arange(len(objects))

#     plt.bar(y_pos, to_plot, align='center', alpha=0.5)
#     plt.xticks(y_pos, objects)
#     plt.ylabel(label)
#     plt.title(f'Mean {label.lower()} for top genres in the dataset')
#     # tl = plt.gca().get_xticklabels()
#     # maxsize = max([len(t) for t in objects])
#     # m = 0.2
#     # s = maxsize/plt.gcf().dpi*150+2*m
#     # margin = m/plt.gcf().get_size_inches()[0]

#     # plt.gcf().subplots_adjust(left=margin, right=1.-margin)
#     # plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
#     plt.show()


randb = sorted(list(songs['genres']['r&b']['acousticness'].items()), key=lambda x: x[0])
randb = randb[0:len(randb):40]
edm = sorted(list(songs['genres']['edm']['acousticness'].items()), key=lambda x: x[0])[0:-1:40]

counts = list(map(lambda x: x[1], randb))
values = list(map(lambda x: x[0], randb))

fig = plt.figure(figsize=(7, 5))

plt.bar(values, counts, width = 0.03) 

plt.xlabel('Acousticness value', fontsize=14)
plt.ylabel('Number of tracks', fontsize=14)
plt.title('Acousticness values for genre R&B', fontsize=16)

plt.show()

plt.xlabel('Acousticness value', fontsize=14)
plt.ylabel('Number of tracks', fontsize=14)
plt.title('Acousticness values for genre edm', fontsize=16)

counts = list(map(lambda x: x[1], edm))
values = list(map(lambda x: x[0], edm))

plt.bar(values, counts, width = 0.03) 

plt.show()