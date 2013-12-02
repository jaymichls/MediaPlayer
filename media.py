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
		self.showName = ''
		self.rating = 0
		self.releaseDate = ''
		self.plot = ''
		self.genre = '' 
		self.numberOfSeasons = 0
		
	def __init__(self, showName, numberOfSeasons):
		self.showName = showName
		self.rating = 0
		self.releaseDate = '' 
		self.plot = ''
		self.genre = ''
		self.numberOfSeasons = numberOfSeasons
		
	def setShowname(self, showName):
		self.showName = showName

	def setRating(self, rating):
		self.rating = rating

	def setReleaseDate(self, releaseDate):
		self.releaseDate = releaseDate

class TVSeason:
	def __init__(self):
		self.showName = ''
		self.seasonNumber = 0
		self.seasonLocation = ''
		
	def __init__(self, showName, seasonNumber):
		self.showName = showName
		self.seasonNumber = seasonNumber
		self.sesasonLocation = ''
	
class TVEpisode:
	def __init__(self):
		self.episodeName = ''
		self.episodeNumber = ''
		self.showName = ''
		self.seasonNumber = 0
		self.filePath = ''
		self.fileName = ''
		self.quality = ''
		self.fileExtension = ''
		
	def __init__(self, episodeName, episodeNumber,showName,seasonNumber, filePath, fileName, quality, fileExtension):
		self.episodeName = episodeName
		self.episodeNumber = episodeNumber
		self.showName = showName
		self.seasonNumber = seasonNumber
		self.filePath = filePath
		self.fileName = fileName
		self.quality = quality
		self.fileExtension = fileExtension
		
	def setEpisodeName(self, episodeName):
		self.episodeName = episodeName

	def setEpisodeNumber(self, episodeNumber):
		self.episodeNumber = episodeNumber		
	
	def setFilePath(self, filePath):
		self.filePath = filePath
		
	def setFileName(self, fileName):
		self.fileName = fileName
		
	def setQuality(self, quality):
		self.quality = quality
		