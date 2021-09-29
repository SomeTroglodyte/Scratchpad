#!/usr/bin/python3
import os
import io
import re
import urllib.request
from lxml.html import parse
from cssselect import HTMLTranslator
from urllib.parse import urljoin

soundtrackUrl1 = 'https://www.geoffknorr.com/sid-meiers-civilization-v'
soundtrackUrl2 = 'https://www.geoffknorr.com/civvgodsandkings'
trackCss = '#mainContent ul.tracks li.track div.track-info div.title a.link'
namePattern = re.compile(r'^.*?\s([^\s]+)\s+-\s*(.+)\s*-\s*"([^"]+)"')
destination = ['mods', 'Civ5 Soundtrack', 'music']
nameXlt = {
	"Hawaii": "Polynesia",
	"Ottoman Empire": "The Ottomans",
	"Huns": "The Huns",
	"Netherlands": "The Netherlands",
	"Civilization V: Gods and Kings - The Medieval World Scenario": "Scenario - The Medieval World",
	"Paradise Found - Polynesian Scenario": "Scenario - Polynesian Paradise Found",
}

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

def fetchTrack(name, href, path):
	match = namePattern.match(name)
	if match:
		nation = match.group(2).rstrip()
		if nation in nameXlt:
			nation = nameXlt[nation]
		name = f"{nation} - {match.group(3)} - {match.group(1)}"
	else:
		if name in nameXlt:
			name = nameXlt[name]
	name = name.replace(';','').replace(',','').replace('.','').replace(':','')
	outPath = os.path.join(path, name) + '.mp3'
	if os.path.exists(outPath):
		print (f"        {name}.mp3 already exists.")
		return

	code, data, msg = download(href)
	if code != 200:
		print (f"Error fetching URL {href}: {msg}")
	else:
		with io.open(outPath,'wb') as file:
			file.write(data)
		print (f"        {name}.mp3: {len(data)} byte")

def scrapePage(url, path):
	code, data, msg = download(url)
	if code != 200:
		print (f"Error fetching URL {url}: {msg}")
		return
	
	doc = parse(io.BytesIO(data)).getroot()
	title = doc.cssselect('head title')[0].text
	encoding = doc.xpath('head/meta/@charset')[0]
	print (f"Title: {title}")

	for link in doc.cssselect(trackCss):
		name = link.text
		href = link.attrib['href']
		print (f"    {name} ({href})")
		fetchTrack(name, href, path)

def main():
	path = makeDestination()
	scrapePage(soundtrackUrl1, path)
	scrapePage(soundtrackUrl2, path)
	print (f"All done, {path} is ready.")
	return

main()
