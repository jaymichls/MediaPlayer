#!/usr/bin/python
# -*- coding: utf-8 -*-

class Movie:		
	def __init__(self, title='', rating=0, releaseDate=''):
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
	def __init__(self, showName='', numberOfSeasons=''):
		self.showName = showName
		self.rating = 0
		self.releaseDate = '' 
		self.plot = ''
		self.genre = ''
		self.numberOfSeasons = numberOfSeasons
		
	def __dir__(self):
		return ['showName','rating','releaseDate','plot','genre','numberOfSeasons']

class TVSeason:
	def __init__(self, showName='', seasonNumber=''):
		self.showName = showName
		self.seasonNumber = seasonNumber
		
	def __dir__(self):
		return ['showName','seasonNumber']
	
class TVEpisode:
	def __init__(self, episodeName='', episodeNumber=0,showName='',seasonNumber=0, filePath='', fileName='', quality='', fileExtension=''):
		self.episodeName = episodeName
		self.episodeNumber = episodeNumber
		self.showName = showName
		self.seasonNumber = seasonNumber
		self.filePath = filePath
		self.fileName = fileName
		self.quality = quality
		self.fileExtension = fileExtension
	
	def __dir__(self):
		return ['episodeName','episodeNumber','showName','seasonNumber','filePath','fileName','quality','fileExtension']