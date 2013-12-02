#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import media 
import dbConnection as dbcon
import re
import inspect

def importMedia():
	#A foler name as a parameter and if it's TV or Movies
	if len(sys.argv) != 3:
		return
	directoryPath = sys.argv[1]
	mediaOption = sys.argv[2]
	print directoryPath
	print mediaOption
	mediaDB = dbcon.Database('Media')
	
	#Get a list of all of the media 
	if mediaOption == '-t':
		print 'Tv Shows'
		tvShows, tvSeasons, tvEpisodes = allTVShows(directoryPath)
		importTvShows(mediaDB, tvShows, tvSeasons, tvEpisodes)


#Tv Show Specific
def importTvShows(tvDB, tvShows, tvSeasons, tvEpisodes):
	#Attempt to create the necessary tables if they don't exist
	print 'Attempting to create'
	#tv = media.TVShow('','')
	tvDB.createTable('Show', dir(media.TVShow()))
	tvDB.createTable('Season', dir(media.TVSeason()))
	tvDB.createTable('Episode', dir(media.TVEpisode()))
	
	print 'Attempting to insert'
	insertList(tvDB, 'Show',tvShows)
	insertList(tvDB, 'Season',tvSeasons)
	insertList(tvDB, 'Episode',tvEpisodes)
	
def insertList(db, tableName, someList):
	#Insert data into tables. 
	for item in someList:
		print 'Inserting: ', item.__dict__
		db.insertInto(tableName, item.__dict__)
		
#Movie Specific
def importMovies(movieDb, movies):
	pass

def allTVShows(directoryPath):
	#initialize vars
	showPosition = len(directoryPath.split('/'))
	episodeList = []
	showList = []
	seasonList = []
	
	#Go through each entry recursively 
	for root, dirs, files in os.walk(directoryPath):
		if root == directoryPath: #This is the list of shows.
			tempShowList = dirs
			continue #this will skip the folder icon for now
		
		#gets the name of the show from the file path also the season # if there is one
		showSeason = root.split('/')
		showName = showSeason[6]
		
		#Get all of the seasons that are available for the current show
		if files == [] and showName in tempShowList: 
			seasonCount = len(dirs)
			showList.append(media.TVShow(showName,seasonCount))

		# Only deal with episodes and use the path from the root
		elif files != []: 
			season = (showSeason[7].split(' '))[1] # Gets the season number
			seasonList.append(media.TVSeason(showName, season))
			for f in files:
				seasonNumber,episodeNumber, quality, fileName, fileExtension = stripFileInformation(f)
				if int(seasonNumber) == int(season): #confirm that the episode is from the current season
					episodeList.append(media.TVEpisode('',episodeNumber,showName, seasonNumber,'',fileName,quality,fileExtension))	
				#else TODO if the episode is in the wrong directory something should be done.. 
	print 'Done Reading files'
	return showList, seasonList, episodeList

#Regular expressions and os path used to get meaningful information from the filename	
def stripFileInformation(f):
	regexEpisode = re.compile("(?:e|episode|\n)(\d{2})",re.IGNORECASE)
	regexSeason = re.compile("(?:s|season)(\d{2})",re.IGNORECASE)
	regexQuality = re.compile("(?:HDTV|720)",re.IGNORECASE)

	fileName, fileExtension = os.path.splitext(f)
	e = regexEpisode.findall(f)[0]
	s = regexSeason.findall(f)[0]
	q = regexQuality.findall(f)[0]

	return s, e, q, fileName, fileExtension
	
importMedia()
#tvshowdir = '/home/jay/Documents/MediaPlayer/Tv Shows'
#allTVShows(tvshowdir)