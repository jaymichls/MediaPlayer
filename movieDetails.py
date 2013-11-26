#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess as sub

movie = raw_input("What Movie are you looking for? ")

print 'Movie List'
p = sub.Popen('grep "%s" movies.list'%(movie),shell=True, stdout=sub.PIPE, stderr=sub.PIPE, stdin=sub.PIPE)
stdout=p.communicate()[0]
print stdout

print 'Rating List'
p = sub.Popen('grep "%s" ratings.list'%(movie),shell=True, stdout=sub.PIPE, stderr=sub.PIPE, stdin=sub.PIPE)
stdout=p.communicate()[0]
print stdout
#p.terminate()

plot = raw_input("try to view the plot? ")

if plot == "yes" or plot == "y":
  print 'Plot List'
  p = sub.Popen('grep "%s" plot.list'%(movie),shell=True, stdout=sub.PIPE, stderr=sub.PIPE, stdin=sub.PIPE)
  stdout=p.communicate()[0]
  print stdout
  #p.terminate()


print 'Enjoy!'