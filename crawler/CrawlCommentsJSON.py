# -*- coding: utf-8 -*-
import urllib2
import time
import re
import json as simplejson
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
#from bs4 import UnicodeDammit
#from bs4 import CData

# Fastest way to uniqify a list in Python
# http://www.peterbe.com/plog/uniqifiers-benchmark
def f1(seq):
   # not order preserving
   set = {}
   map(set.__setitem__, seq, [])
   return set.keys()

# Create/open a file
f = open('comments-crawl.json', 'w')
f.write('{\n')

# Iterate through pages
#y = 1
for y in range(1, 4):
	#print "ID: " + str(y) 
	op_id = y

	# Open url
	url = "http://newz.dk/anonymous-tager-afstand-fra-angreb-paa-fagforeningen-3f-s-hjemmeside/page"+str(op_id)
	##page = urllib2.urlopen(url)
	page = open("Raw/page"+str(op_id)+".html").read()

	# Get data from page
	soup = BeautifulSoup(page)
	
	if y == 1:
		articleTitle = soup.h1.a.string
		articleLink = url
		articleDate = soup.find("span", {"class": "date"}).string
		articleImage = soup.find("a", {"class": "image"}).img["src"]
		
		f.write('\t"articleTitle": "'+articleTitle.encode("UTF-8")+'",\n\t"articleLink": "'+str(articleLink)+'",\n\t"articleDate": "'+str(articleDate)+'",\n\t"articleImage": "'+str(articleImage)+'",\n')	
		f.write('\t"comments": [')
	
	# Global Search Pattern:
	comments = soup.find("div", {"id": "comments"}).findAll("div", {"class": "comment"})
	
	# Item (repeatable) Search Pattern:
	comments_items = []
	for i, comments_item in enumerate(comments):
		
		num = comments_item.h2.findAll("a")[0]["name"]
		page = op_id
		post = comments_item["id"]
		image = comments_item.img["src"]
		user = comments_item.h2.findAll("a")[2]["title"]
		rating = comments_item.div.p.span.string
		date = comments_item.find("p", {"class": "comment_date"}).string
		#datestructured = time.strptime(date, "%d. %b. %Y %H:%M") #dd. MMM. yyyy h:mm
		content = comments_item.find("div", {"class": "comment_content"}).div.renderContents().decode('utf-8')
		citeslist = map(int, re.findall(r'#([0-9]\d*)', content.encode("UTF-8"))) # find all numbers that have a '#'-sign in front; used when citing/refering to other comments. Remove encoding and convert to numbers.
		cites = str(f1(citeslist))[1:-1] # Uniqify list and remove brackets.
		#print datestructured
		
		#print simplejson.dumps(content.encode("UTF-8")[4:-3])
		line = '\n\t\t{\n\t\t\t"num": "'+str(num)+'",\n\t\t\t"page": "'+str(page)+'",\n\t\t\t"post": "'+str(post)+'",\n\t\t\t"image": "'+str(image)+'",\n\t\t\t"user": "'+str(user)+'",\n\t\t\t"rating": "'+str(rating)+'",\n\t\t\t"date": "'+str(date)+'",\n\t\t\t"contents": '+simplejson.dumps(content.encode("UTF-8")[4:-3])+',\n\t\t\t"cites": "'+cites+'"\n\t\t},'
		# remove last ,
		if op_id == 3 and i == len(comments)-1:
			line = line[:-1]
			print "#"+ str(i) +" " + str(len(comments))
		f.write(line)

	# Don't kill the server!		
	time.sleep(0.3)

f.write('\n\t]\n')	
f.write('}')
# Done getting data! Close file.
f.close()

