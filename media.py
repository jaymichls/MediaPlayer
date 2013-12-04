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
	def __init__(self, showName='', numberOfSeasons='', folderImage=''):
		self.showName = showName
		self.rating = 0
		self.releaseDate = '' 
		self.plot = ''
		self.genre = ''
		self.numberOfSeasons = numberOfSeasons
		self.folderImage = folderImage
		
	def __dir__(self):
		return ['showName','rating','releaseDate','plot','genre','numberOfSeasons', 'folderImage']

	# Temporary solution to unique rows
	@staticmethod
	def uniqueColumns():
		return ['showName'] #Should add year also
class TVSeason:
	def __init__(self, showName='', seasonNumber='', folderImage='', numberOfEpisodes=0):
		self.showName = showName
		self.seasonNumber = seasonNumber
		self.folderImage = folderImage
		self.numberOfEpisodes = numberOfEpisodes
		
	def __dir__(self):
		return ['showName','seasonNumber', 'folderImage', 'numberOfEpisodes']
	
	@staticmethod
	def uniqueColumns():
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
	
	@staticmethod	
	def uniqueColumns():
		return ['episodeNumber','showName','seasonNumber']