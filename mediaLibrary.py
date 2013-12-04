#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import media 
import dbConnection as dbcon
import re
import timeit

def importMedia():
	#A foler name as a parameter and if it's TV or Movies
	if len(sys.argv) != 3:
		return
	directoryPath = sys.argv[1]
	mediaOption = sys.argv[2]

	mediaDB = dbcon.Database('Media1')
	
	#Get a list of all of the media 
	if mediaOption == '-t':
		print 'Tv Shows'
		tvShows, tvSeasons, tvEpisodes = allTVShows1(directoryPath)
		
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
		#print 'Inserting: ', item.__dict__
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
		showName = showSeason[showPosition]
		print showSeason
		#Get all of the seasons that are available for the current show
		if files == [] and showName in tempShowList: 
			seasonCount = len(dirs)
			#look for folder.jpg ignore anything else Thumbs.db or *.ini 
			showList.append(media.TVShow(showName,seasonCount))
			

		# Only deal with episodes and use the path from the root
		elif files != []: 
			season = (showSeason[7].split(' '))[1] # Gets the season number
			seasonList.append(media.TVSeason(showName, season)) # maybe this should be done after or a search to see if there is a folder.jpg			
			for f in files:
				seasonNumber,episodeNumber, quality, fileName, fileExtension = stripFileInformation(f)
				if int(seasonNumber) == int(season): #confirm that the episode is from the current season
					episodeList.append(media.TVEpisode('',episodeNumber,showName, seasonNumber,'',fileName,quality,fileExtension))	
				#else TODO if the episode is in the wrong directory something should be done.. 
	print 'Done Reading files'
	return showList, seasonList, episodeList

def allTVShows1(directoryPath):
	print 'Starting to read files'
	#initialize vars
	showPosition = len(directoryPath.split('/'))
	seasonPosition = showPosition + 1
	
	showList = []
	seasonList = []
	episodeList = []
	currentShow = ''
	
	for root, dirs, files in os.walk(directoryPath):
		if root == directoryPath:
			tempShowList = dirs
			continue
		
		newShow = root.split('/')
		showName = newShow[showPosition]
		
		if showName == currentShow:	#Get show season episides and folder.jpg
			#See if there is a folder.jpg 
			seasonFolderImage = os.path.join(root,[f for f in files if f == 'folder.jpg'][0])			
			#Number of episodes is the number of files unless there is a folder.jpg
			if seasonFolderImage == '': numberOfEpisodes = len(files)
			else: numberOfEpisodes = len(files) - 1
			#if this is in fact a season of a show the season number will be the seasonPosition in the newShow (7)
			season = (newShow[seasonPosition].split(' '))[1] # Gets the season number
			#Create a new Season with above
			seasonList.append(media.TVSeason(showName, season,seasonFolderImage, numberOfEpisodes))		
			#Go through each file of the current season except folder.jpg
			for f in files:				
				#stripFileInformation from the file 
				if f != 'folder.jpg' and f != 'Thumbs.db': 					
					seasonNumber,episodeNumber, quality, fileName, fileExtension = stripFileInformation(f)
					#Create new Epsiode 
					if int(seasonNumber) == int(season): #confirm that the episode is from the current season
						episodeList.append(media.TVEpisode('',episodeNumber,showName, seasonNumber,'',fileName,quality,fileExtension))
						
					
		elif showName != currentShow:	#New show get folder.jpg
			#Number of season is the length of the dirs 
			numberOfSeason = len(dirs)
			#folder.jpg should be the only file if not ditch the rest.
			showFolderImage = os.path.join(root,[f for f in files if f == 'folder.jpg'][0])
			#Create new show with newShow name
			showList.append(media.TVShow(showName,numberOfSeason,showFolderImage))
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

def dbSizeTest():
	testDB = dbcon.Database ('dbSizeTest')
	testDB.createTable('Episode', dir(media.TVEpisode()))
	test = media.TVEpisode('Test',0,'Some Name',12,'testes','tetset','testes','testes')
	for i in xrange(1000):
		test.episodeNumber = i
		testDB.insertInto('Episode', test.__dict__)

if __name__ == '__main__':
	importMedia()

#	print(timeit.timeit("dbSizeTest()", setup="from __main__ import dbSizeTest", number=10))

#tvshowdir = '/home/jay/Documents/MediaPlayer/Tv Shows'
#allTVShows(tvshowdir)
