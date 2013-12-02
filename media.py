#!/usr/bin/python
# -*- coding: utf-8 -*-

class Movie:
	def __init__(self):
		self.title = ''
		self.rating = 0
		self.releaseDate = '' 
		
	def __init__(self, title, rating, releaseDate):
		self.title = title
		self.rating = rating
		self.releaseDate = releaseDate 

	def setTitle(self, title):
		self.title = title

	def setRating(self, rating):
		self.rating = rating

	def setReleaseDate(self, releaseDate):
		self.releaseDate = releaseDate

	def writeMovie(self):

		retVal = title+','+rating+','+releaseDate
		return retVal

class TVShow:
	def __init__(self):
		self.show = ''
		self.episode = ''
		self.episodeNumber = ''
		self.rating = 0
		self.releaseDate = ''
		self.quality = ''
		self.fileLocation = ''
		
	def __init__(self, show, episode, episodeNumber, rating, releaseDate, quality, fileLocation):
		self.show = show
		self.episode = episode
		self.episodeNumber = episodeNumber
		self.rating = rating
		self.releaseDate = releaseDate 
		self.quality = quality
		self.fileLocation = fileLocation

	def setShow(self, show):
		self.show = show

	def setRating(self, rating):
		self.rating = rating

	def setReleaseDate(self, releaseDate):
		self.releaseDate = releaseDate

	def setEpisode(self, episode):
		self.episode = episode

	def setEpisodeNumber(self, episodeNumber):
		self.episodeNumber = episodeNumber
		
	def setFileLocation(self, fileLocation):
		self.fileLocation = fileLocation

	def writeShow(self):
		
		retVal = show+','+episode+','+episodeNumber+','+rating+','+releaseDate
		return retVal