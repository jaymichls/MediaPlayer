#!/usr/bin/python
# -*- coding: utf-8 -*-

class Movie:		
	def __init__(self, title, rating=0, releaseDate='', genre='', plot='', fileExtension='', filePath='', fileName='', quality='',folderImage='', rootDir=''):
		self.title = title
		self.rating = rating
		self.releaseDate = releaseDate 
		self.genre = genre
		self.plot = plot
		self.folderImage = folderImage
		self.rootDir = rootDir

	def __dir__(self):
		return ['fileExtension','quality','filePath','fileName','rootDir','folderImage','plot','genre','releaseDate','rating','title']
	
	@staticmethod
	def uniqueColumns():
		return ['title', 'quality']	#should also have year eventually. 
		
class TVShow:
	def __init__(self, showName, numberOfSeasons='', folderImage='',rootDir=''):
		self.showName = showName
		self.rating = 0
		self.releaseDate = '' 
		self.plot = ''
		self.genre = ''
		self.numberOfSeasons = numberOfSeasons
		self.folderImage = folderImage
		self.rootDir = rootDir
		
	def __dir__(self):
		return ['rootDir','rating','releaseDate','folderImage','plot','genre','numberOfSeasons', 'showName']

	# Temporary solution to unique rows
	@staticmethod
	def uniqueColumns():
		return ['showName'] #Should add year also
	
class TVSeason:
	def __init__(self, showName, seasonNumber, folderImage='', numberOfEpisodes=0,rootDir=''):
		self.showName = showName
		self.seasonNumber = seasonNumber
		self.folderImage = folderImage
		self.numberOfEpisodes = numberOfEpisodes
		self.rootDir = rootDir
		
	def __dir__(self):
		return ['rootDir','folderImage', 'numberOfEpisodes', 'seasonNumber', 'showName']
	
	@staticmethod
	def uniqueColumns():
		return ['showName','seasonNumber']
	
class TVEpisode:
	def __init__(self, episodeName='', episodeNumber=0,showName='',seasonNumber=0, filePath='', fileName='', quality='', fileExtension='',rootDir=''):
		self.episodeName = episodeName
		self.episodeNumber = episodeNumber
		self.showName = showName
		self.seasonNumber = seasonNumber
		self.filePath = filePath
		self.fileName = fileName
		self.quality = quality
		self.fileExtension = fileExtension
		self.rootDir = rootDir
	
	def __dir__(self):
		return ['rootDir','filePath','fileName','quality','fileExtension', 'seasonNumber', 'showName','episodeNumber','episodeName']
	
	@staticmethod	
	def uniqueColumns():
		return ['episodeNumber','showName','seasonNumber']
	
	