#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, re
import media 
import dbConnection as dbcon
import timeit

def importMedia(mediaOption, databaseName, directoryPath):
	
	mediaDB = dbcon.Database(databaseName)
	print mediaOption
	#Get a list of all of the media 
	#TODO movie option or both.. maybe read the folder name to judge
	if mediaOption == '-t':
		print 'Importing Tv Shows'
		tvShows, tvSeasons, tvEpisodes = readTVShows(directoryPath)		
		importTvShows(mediaDB, tvShows, tvSeasons, tvEpisodes)

	if mediaOption == '-m':
		print 'Importing Movies'
		movies = readMovies(directoryPath)
		importMovies(movies)

#Tv Show Specific
def importTvShows(db, tvShows, tvSeasons, tvEpisodes):
	#Attempt to create the necessary tables if they don't exist
	print 'Attempting to create'	
	db.createTable(media.TVShow.__class__.name__, dir(media.TVShow()), media.TVShow.uniqueColumns())
	db.createTable(media.TVSeason.__class__.name__, dir(media.TVSeason()), media.TVSeason.uniqueColumns())
	db.createTable(media.TVEpisode.__class__.name__, dir(media.TVEpisode()), media.TVEpisode.uniqueColumns())
	
	insertList(db, media.TVShow.__class__.name__, tvShows)
	insertList(db, media.TVSeason.__class__.name__, tvSeasons)
	insertList(db, media.TVEpisode.__class__.name__, tvEpisodes)
		
#Movies specific
def importMovies(db, movies):
	print 'Attempting to create %s table'%(media.Movie.__class__.__name___)
	db.createTable(media.Movie.__class__.__name___, dir(media.Movie()), media.Movie.uniqueColumns())
	for m in movies:
		print m.__dict__
	#insertList(db, media.Movie.__class__.__name___, movies)
	
def insertList(db, tableName, someList):
	#Insert data into tables. 
	print 'Attempting to insert'
	for item in someList:
		#print 'Inserting: ', item.__dict__
		db.insertInto(tableName, item.__dict__)

#Movie Specific
def readMovies(directoryPath):
	print 'Unimplemented'
	movies = []
	
	movieTilePosition = len(directoryPath.split('/'))
	
	newMovie = root.split('/')[movieTilePosition]
	#might have to do a check to see that there aren't any child directories in movie folders
	for f in files:
		if f == 'folder.jpg' and f != 'Thumbs.db':
			movieFolderImage = f
			
		elif f != 'folder.jpg' and f != 'Thumb.db':
			fileName, fileExtension, quality = stripMovieFileInformation(f)
			
	movies.append(media.Movie(title, 0, '', '', '', fileExtension, '',fileName, quality,movieFolderImage, root))
	print 'Done reading files'
	return movies

def readTVShows(directoryPath):
	print 'Starting to read TV files'
	#initialize vars
	showPosition = len(directoryPath.split('/'))
	seasonPosition = showPosition + 1
	
	showList = []
	seasonList = []
	episodeList = []
	currentShow = ''
	
	for root, dirs, files in os.walk(directoryPath):
		newShow = root.split('/')
		showName = newShow[showPosition]
		
		if showName == currentShow:	#Get show season episides and folder.jpg
			#See if there is a folder.jpg 
			seasonFolderImage = [f for f in files if f == 'folder.jpg'][0]
			#Number of episodes is the number of files unless there is a folder.jpg
			if seasonFolderImage == '': numberOfEpisodes = len(files)
			else: numberOfEpisodes = len(files) - 1
			#if this is in fact a season of a show the season number will be the seasonPosition in the newShow (7)
			season = (newShow[seasonPosition].split(' '))[1] # Gets the season number
			#Create a new Season with above
			seasonList.append(media.TVSeason(showName, season,seasonFolderImage, numberOfEpisodes,root))		
			#Go through each file of the current season except folder.jpg
			for f in files:				
				#stripFileInformation from the file 
				if f != 'folder.jpg' and f != 'Thumbs.db': 					
					seasonNumber,episodeNumber, quality, fileName, fileExtension = stripFileInformation(f)
					#Create new Epsiode 
					if int(seasonNumber) == int(season): #confirm that the episode is from the current season
						episodeList.append(media.TVEpisode('',episodeNumber,showName, seasonNumber,'',fileName,quality,fileExtension,root))
						
					
		elif showName != currentShow:	#New show get folder.jpg
			#Number of season is the length of the dirs 
			numberOfSeason = len(dirs)
			#folder.jpg should be the only file if not ditch the rest.
			showFolderImage = [f for f in files if f == 'folder.jpg'][0]
			#Create new show with newShow name
			showList.append(media.TVShow(showName,numberOfSeason,showFolderImage,root))
			#Set currentShow to showName 
			currentShow = showName
			
	print 'Done Reading files'
	return showList, seasonList, episodeList


#Regular expressions and os path used to get meaningful information from the filename	
#TODO account for stupid season and episode number at the start of the file. Eventually... See Entourage
def stripFileInformation(f):
	regexEpisode = re.compile("(?:e|episode|\n)(\d{2})",re.IGNORECASE)
	regexSeason = re.compile("(?:s|season)(\d{2})",re.IGNORECASE)
	regexQuality = re.compile("(?:HDTV|720)",re.IGNORECASE)

	fileName, fileExtension = os.path.splitext(f)
	e = regexEpisode.findall(f)[0]
	s = regexSeason.findall(f)[0]
	q = regexQuality.findall(f)[0]

	return s, e, q, fileName, fileExtension

def stripMovieFileInformation(f):
	regexQuality = re.compile("(?:HDTV|720)",re.IGNORECASE)
	quality = regexQuality.findall(f)[0]
	fileName, fileExtension = os.path.splitext(f)
	return fileName, fileExtension, quality
	
def dbSizeTest():
	testDB = dbcon.Database ('dbSizeTest')
	testDB.createTable('Episode', dir(media.TVEpisode()))
	test = media.TVEpisode('Test',0,'Some Name',12,'testes','tetset','testes','testes')
	for i in xrange(1000):
		test.episodeNumber = i
		testDB.insertInto('Episode', test.__dict__)

if __name__ == '__main__':
	if len(sys.argv) != 3:#TODO fix args
		print "syntax: " + sys.argv[0] + "-t/-m database Name folder path"
		exit()
	importMedia(sys.argv[1],sys.argv[2],sys.argv[2])

#	print(timeit.timeit("dbSizeTest()", setup="from __main__ import dbSizeTest", number=10))

#tvshowdir = '/home/jay/Documents/MediaPlayer/Tv Shows'
#allTVShows(tvshowdir)
