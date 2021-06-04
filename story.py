import os
import json
import requests
from time import strftime
from PIL import Image, ImageColor, ImageDraw, ImageFont, ImageOps

import settings
from test_named_tuple import create_song_story_data, create_artist_story_data
from test_named_tuple import make_api_request

class Story:
	def __init__(self):
		self.W = 1080
		self.H = 1920

	def create_header(self, draw, header_text, font_color):
		font = ImageFont.truetype(settings.HEADER_FONT, settings.HEADER_FONT_SIZE)
		text_width, text_height = font.getsize(header_text)
		draw.text(((self.W-text_width)/2, settings.HEADER_POSITION_HEIGHT), header_text, font=font, fill=font_color)

	def create_footer(self, draw, font_color):
		font = ImageFont. truetype(settings.FOOTER_FONT, settings.FOOTER_FONT_SIZE)
		draw.text((settings.FOOTER_POSITION), settings.FOOTER_TEXT, font=font, fill=font_color)

	def create_mask(self, x, y):
		bigsize = (x * 3, y * 3)
		mask = Image.new('L', bigsize, 0)
		draw = ImageDraw.Draw(mask) 
		draw.ellipse((0, 0) + bigsize, fill=255)
		mask = mask.resize((x, y), Image.ANTIALIAS)
		return mask

class SongStory(Story):

	def __init__(self, artists, songs, images):
		super(SongStory, self).__init__()
		self.songs = songs
		self.artists = artists
		self.images = images
		self.header = f"{strftime('%B')} Top Songs"
		self.font_color = settings.SONG_STORY_FONT_COLOR

	def create_image(self):
		base = Image.new('RGB', (self.W, self.H), ImageColor.getrgb(settings.SONG_BASE_COLOR))
		draw = ImageDraw.Draw(base)

		self.header = self.create_header(draw, self.header, self.font_color)
		self.footer = self.create_footer(draw, self.font_color)
		# todo
		self.mask = self.create_mask(128, 130)
		self.thumbnails = self.create_song_thumbnails(self.mask, base)
		self.text = self.create_song_and_artist_text(draw)
		# base.show()
		base.save("song_story_test.jpg")

	def create_song_thumbnails(self, mask, base):
		# todo, fix i
		i = 0
		for filename in self.images:
			if filename.endswith(".jpg"):
				img = Image.open(filename)
				#todo
				new_img = img.resize((128,130))
				new_img.putalpha(mask)
				base.paste(new_img, settings.SONG_THUMBNAIL_POSITION[i], mask)
				i+=1

	def create_song_and_artist_text(self, draw):

		song_font = ImageFont.truetype(settings.SONG_TEXT_FONT, settings.SONG_TEXT_SIZE)
		artist_font = ImageFont.truetype(settings.ARTIST_TEXT_FONT , settings.ARTIST_TEXT_SIZE)

		for i in range(10):
			# draw.text(settings.SONG_RANK_POSITION[i], f"#0{i+1}", font=song_font, fill=settings.SONG_STORY_FONT_COLOR)
			if i < 9:
				draw.text(settings.RANK_POSITION[i], f"#{i+1}", font=song_font, fill=settings.SONG_STORY_FONT_COLOR)
			else:
				draw.text(settings.RANK_POSITION[i], f"#{i+1}", font=song_font, fill=settings.SONG_STORY_FONT_COLOR)

			draw.text(settings.SONG_TEXT_POSITION[i], self.songs[i], font=song_font, fill=settings.SONG_STORY_FONT_COLOR)
			draw.text(settings.SONG_STORY_ARTIST_TEXT_POSITION[i], self.artists[i], font=artist_font, fill=settings.SONG_STORY_FONT_COLOR)


class ArtistStory(Story):

	def __init__(self, artists, images):
		super(ArtistStory, self).__init__()
		self.artists = artists
		self.images = images
		self.header = f"{strftime('%B')} Top Artists"
		self.font_color = settings.ARTIST_STORY_FONT_COLOR

	def create_image(self):
		base = Image.new('RGB', (self.W, self.H), ImageColor.getrgb(settings.ARTIST_BASE_COLOR))
		draw = ImageDraw.Draw(base)

		self.header = self.create_header(draw, self.header, self.font_color)
		self.footer = self.create_footer(draw, self.font_color)
		self.mask = self.create_mask(128, 130)
		self.thumbnails = self.create_thumbnails(self.mask, base)
		self.text = self.create_artist_text(draw)
		# base.show()
		base.save("artist_story_test.jpg")

	def create_thumbnails(self, mask, base):

		i = 0
		for filename in self.images:
			if filename.endswith(".jpg"):
				img = Image.open(filename)
				new_img = img.resize((128,130))

				new_img.putalpha(mask)
				base.paste(new_img, settings.SONG_THUMBNAIL_POSITION[i], mask)
				i+=1

	def create_artist_text(self, draw):
		artist_font = ImageFont.truetype(settings.SONG_TEXT_FONT, settings.SONG_TEXT_SIZE)

		for i in range(10):
			draw.text(settings.RANK_POSITION[i], f"#{i+1}", font=artist_font, fill=settings.ARTIST_STORY_FONT_COLOR)
			draw.text(settings.ARTIST_TEXT_POSITION[i], self.artists[i], font=artist_font, fill=settings.ARTIST_STORY_FONT_COLOR)


response = make_api_request()
s = SongStory(response[0].artists, response[0].songs, response[0].images)
a = ArtistStory(response[1].artists, response[1].images)
a.create_image()
s.create_image()



