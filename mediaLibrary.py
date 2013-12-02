#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import media 
import dbConnection as dbcon
import re

def importMedia():
	#A foler name as a parameter and if it's TV or Movies
	folder = raw_input("Enter folder path.")
	
	mediaDB = dbcon.Database('Media')
	#Create a table based on the folder if it doesn't exist.
	
	#Get a list of all of the media 
	pass

#Tv Show Specific
def importTvShows(tvDB, tvShows):
	pass


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
			for f in files:
				seasonNumber,episodeNumber, quality, fileName, fileExtension = stripFileInformation(f)
				if int(seasonNumber) == int(season): #confirm that the episode is from the current season
					episodeList.append(media.TVEpisode('',episodeNumber,showName, seasonNumber,'',fileName,quality,fileExtension))	
				#else TODO if the episode is in the wrong directory something should be done.. 
	
	return showList, seasonList,episodeList

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
	
tvshowdir = '/home/jay/Documents/MediaPlayer/Tv Shows'
allTVShows(tvshowdir)