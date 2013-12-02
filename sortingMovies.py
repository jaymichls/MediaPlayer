#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The purpose of this program is to create a master list of 
all currently downloaded movies, along with its rating and release 
date.  

First make a list of all movies with the proper name 

'''
import subprocess as sub

def seperateMoviesAndTVWithRatings():
	
	imdbRatingsFile = open('Lists/ratings.list')

	movieFile = open('Lists/movieRatings.list', 'w')

	tvFile = open('Lists/tvshowRatings.list', 'w')

	imdbReadFile = imdbRatingsFile.read()	
	imdbRatingsFile.close()

	imdbList = imdbReadFile.split('\n')

	readingMedia = False

	for line in imdbList:
		
		if line.startswith('NEW'):
			
			readingMedia = True
			continue
	
		if readingMedia:
			
			if line == '' or line == '\n':
				continue

			#break the line into pieces
			subline = line.split()
			length = len(subline)
		
			#get rating
			rating = subline[2] 

			#combine and merge the title together
			subline[3:length-1] = [' '.join(subline[3:length-1])]

			#strip the brackets from the date 
			releaseDate = str.strip(subline[4],'()')

			if title.startswith('"') or title.startswith("'"):

				#strip the quotes from the title
				title = str.strip(subline[3],'""')

				
				#print 'TvShow: '+line
				tvFile.write(line+'\n')

			else:

				#print 'Movie: '+line
				movieFile.write(line+'\n')

	movieFile.close()
	tvFile.close()

def seperateMoviesAndTV():

	imdbFile = open('Lists/movies.list')

	movieFile = open('Lists/movie.list', 'w')

	tvFile = open('Lists/tvshow.list', 'w')

	imdbReadFile = imdbFile.read()

	imdbFile.close()

	imdbList = imdbReadFile.split('\n')

	readingMedia = False

	for line in imdbList:
		
		if line.startswith('==========='):
			
			readingMedia = True
			continue
	
		if readingMedia:
			
			if line == '' or line == '\n':
				continue

			if line.startswith('"') or line.startswith("'"):

				#print 'TvShow: '+line
				tvFile.write(line+'\n')

			else:

				#print 'Movie: '+line
				movieFile.write(line+'\n')

	movieFile.close()
	tvFile.close()

def movieList():

	f = open('Lists/myMovies.list')

	masterFile = open('Lists/allmovies.list')

	wf = f.read()

	f.close()

	movielist = wf.split('\n')

	for movie in movielist:
		
		if movie == ''  or movie == '\n':
			continue
		
		p = sub.Popen('grep "%s" movies.list'%(movie), shell=True, stdout=sub.PIPE, stderr=sub.PIPE, stdin=sub.PIPE)

		stdout = p.stdout

		print 'Looking for: %s.'%(movie)

		for line in stdout:
			
			choice = raw_input('Movie: '+line)
			
			if choice == 'y':
				print'adding movie: %s'%(line)
				
				break

		#check to rename file

#Main
print 'Seperating movies and tv shows'
seperateMoviesAndTVWithRatings()
	