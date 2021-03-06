import json
import requests
from PIL import Image, ImageColor, ImageDraw, ImageFont

with open('artists.json') as f:
  data = json.load(f)


def process_artists_response():

	artist_thumbnail_uris = []

	for item in data["items"]:
		artist_thumbnail_uris.append(item["images"][0]['url'])
		for images in item["images"]:
			print(len(images))

		print(" ")
	return artist_thumbnail_uris

def get_artist_thumbnails():

	uris = process_artists_response()
	print("$$$")
	print(uris)

	for uri in uris:
		uri_id_truncated = uri[-8:-1]
		request = requests.get(uri).content
		with open(f'test_downloads/{uri_id_truncated}.jpg', 'wb') as handler:
			handler.write(request)

	return None


# get_artist_thumbnails()

def create_base():
	img = Image.new('RGB', (1080, 1920), ImageColor.getrgb("#F1C3ED"))
	img.save('base_image.jpeg')

	return img

def generate_image():

	# create base

	# create header and footer

	# create song names text

	# create artist names text

	# resize and create song images
	return None

def generate_artist_image():

	W, H = (1080, 1920)
	message = "May Top Artists"

	# create base
	base = Image.new('RGB', (W, H), ImageColor.getrgb("#F1C3ED"))
	d = ImageDraw.Draw(base)

	# create header
	font = ImageFont.truetype('Library/Fonts/CircularStd-Bold.ttf' , 70)
	text_width, text_height = font.getsize(message)
	d.text(((W-text_width)/2, 107), message, font=font, fill=(0, 0, 0))

	# create footer
	font = ImageFont. truetype('Library/Fonts/CircularStd-Bold.ttf' , 60)
	d.text((231, 1695), "monthlywrapped.com", font=font, fill=(0, 0, 0))

	base.save('test.jpeg')
	base.show()

	# create grid



	return None

generate_artist_image()


