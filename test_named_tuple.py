from collections import namedtuple
import json
import requests



ArtistData = namedtuple('ArtistStory', ['artists', 'images'])
SongData = namedtuple('SongStory', ['songs', 'artists', 'images'])


def create_artist_story_data():

	with open('artists2.json') as f:
		data = json.load(f)

	artists = [artist["name"] for artist in data["items"]]
	images = [data["items"][i]["images"][0]['url'] for i in range(len(data["items"]))]

	# more readable to parse image uris from json
	# for item in data["items"]:
		# uri = (item["images"][0]['url'])


	for i, url in enumerate(images):
		url_id_truncated = url[-8:-1]
		request = requests.get(url).content
		with open(f'test_downloads/artist/{url_id_truncated}.jpg', 'wb') as handler:
			images[i] = f'test_downloads/artist/{url_id_truncated}.jpg'
			handler.write(request)

	story = ArtistData(artists=artists, images=images)
	return story



def create_song_story_data():

	with open('songs2.json') as f:
			data = json.load(f)

	songs = [data["items"][i]["name"] for i in range(10)]
	artists = []
	images = []

	for item in data["items"]:
		_artists = item["artists"]
		if len(_artists) > 1:
			multi_artist_string = ", ".join([str(_artists[i]['name']) for i in range(len(_artists))])
			artists.append(multi_artist_string)
		else:
			artists.append(item['artists'][0]['name'])

		images.append(item["album"]["images"][0]["url"])


	for i, url in enumerate(images):
			url_id_truncated = url[-8:-1]
			request = requests.get(url).content
			with open(f'test_downloads/song/{url_id_truncated}.jpg', 'wb') as handler:
				images[i] = f'test_downloads/song/{url_id_truncated}.jpg'
				handler.write(request)


	story = SongData(songs=songs, artists=artists, images=images)
	return story


s = create_song_story_data()
a = create_artist_story_data()
# print(s)
# print(" ")
# print(a)



