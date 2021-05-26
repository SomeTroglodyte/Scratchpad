#!/usr/bin/python3
import os
import io
import urllib.request
from lxml.html import parse
from cssselect import HTMLTranslator
from urllib.parse import urljoin


leaderListUrl = 'https://civilization.fandom.com/wiki/Leaders_(Civ5)'
leaderTableCss = '#content table.wikitable.sortable tbody tr'
leaderImageCss = '#content figure a.image'
destination = ['mods', 'Wikia Leader Portraits', 'Images','LeaderIcons']

def makeDestination():
	path = ""
	for part in destination:
		path = os.path.join(path,part)
	try: os.makedirs (path)
	except: pass
	return path
	
def download(url):
	rq = urllib.request.urlopen(url)
	code = rq.getcode()
	data = rq.read()
	return (code, data, rq.msg)

def leaderPage(name, href, path):
	url = urljoin(leaderListUrl,href)
	code, data, msg = download(url)
	if code != 200:
		print (f"Error fetching URL {url}: {msg}")
	else:
		page = parse(io.BytesIO(data)).getroot()
		picurl = page.cssselect(leaderImageCss)[0].attrib['href']
		code, pic, msg = download(picurl)
		if code != 200:
			print (f"Error fetching URL {picurl}: {msg}")
		else:
			outPath = os.path.join(path, name) + '.png'
			with io.open(outPath,'wb') as file:
				file.write(pic)
			print (f"        {name}.png: {len(pic)} byte")

def main():
	code, data, msg = download(leaderListUrl)
	if code != 200:
		print (f"Error fetching URL {leaderListUrl}: {msg}")
		return
	
	doc = parse(io.BytesIO(data)).getroot()
	title = doc.cssselect('head title')[0].text
	encoding = doc.xpath('head/meta/@charset')[0]
	print (f"Title: {title}")
	path = makeDestination()

	for tr in doc.cssselect(leaderTableCss):
		if len(tr.getchildren()) < 1 or tr.getchildren()[0].tag != 'td':
			continue		# lxml bug - it includes thead despite specifying tbody
		td1 = tr.getchildren()[0]
		td2 = tr.getchildren()[1]
		name = td1.xpath('a[1]/@title')[0]
		href = td1.xpath('a[1]/@href')[0]
		category = ""
		try: category = td1.xpath('a[3]/@href')[0].split('#')[1]		# third link might have #DLConly
		except: pass
		civ = td2.xpath('a[1]/@title')[0]
		print (f"    {name} ({civ}) ({category})")
		
		leaderPage(name, href, path)
	print (f"All done, {path} is ready.")
	return

main()

