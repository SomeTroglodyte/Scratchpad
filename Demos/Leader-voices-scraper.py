#!/usr/bin/python3

import os
import re

garbage = {
	"thumbs.db": True,
	"desktop.ini": True,
	".ds_store": True,
	"__macosx": True,
	"Background.png": True,
	"box.png": True,
	"button.png": True,
	"button active.png": True,
	"button hover.png": True,
	"button on.png": True,
	"button on hover.png": True,
	"Civ+V+logo_clean+V_onWht.png": True,
	"EscToExit_back.png": True,
	"EscToExit_Text.png": True,
	"horizontal scrollbar.png": True,
	"horizontal scrollbar thumb.png": True,
	"horizontalslider.png": True,
	"Play.png": True,
	"slider thumb.png": True,
	"slider thumb active.png": True,
	"slidert humb hover.png": True,
	"Soft.png": True,
	"Stop.png": True,
	"textfield.png": True,
	"textfield hover.png": True,
	"textfield on.png": True,
	"toggle.png": True,
	"toggle active.png": True,
	"toggle hover.png": True,
	"toggle on.png": True,
	"toggle on active.png": True,
	"toggle on hover.png": True,
	"UIMask.png": True,
	"UnitySplash-cube.png": True,
	"UnitySplash-HolographicTrackingLoss.png": True,
	"UnityWatermark-beta.png": True,
	"UnityWatermark-dev.png": True,
	"UnityWatermark-edu.png": True,
	"UnityWatermarkPlugin-beta.png": True,
	"UnityWatermark-proto.png": True,
	"UnityWatermark-small.png": True,
	"UnityWatermark-trial.png": True,
	"UnityWatermark-trial-big.png": True,
	"vertical scrollbar.png": True,
	"vertical scrollbar thumb.png": True,
	"verticalslider.png": True,
	"WarningSign.png": True,
	"window.png": True,
	"window on.png": True,
}

fixleadernames = {
	"Attila.png": "Attila the Hun.png",
	"Bismarck.png": "Otto von Bismarck.png",
	"Washington.png": "George Washington.png",
	"Kamehameha.png": "Kamehameha I.png",
	"Montezuma.png": "Montezuma I.png",
	"Suleiman.png": "Suleiman I.png",
	"William.png": "William of Orange.png",
}

# Generate: gameInfo.ruleset.nations.values.filter { it.leaderName.isNotBlank() }.sortedBy { it.leaderName }.joinToString("") { "\t\"${it.leaderName}\": \"${it.name}\",\n" }
# ... then add BNW leaders and fix up for apk's naming quirks
leadernameprefixes = {
	"Ahmed Al Mansur": "Morocco",
	"AlMansur": "Morocco",
	"Almansur": "Morocco",
	"Alexander": "Greece",
	"Ashurbanipal": "Assyria",
	"Askia": "Songhai",
	"Attila": "The Huns",
	"Augustus Caesar": "Rome",
	"AugustusCeasar": "Rome",
	"Bismark": "Germany",
	"Bismarck": "Germany",
	"Bluetooth": "Denmark",
	"Boudicca": "Celts",
	"BrazilPedroII": "Brazil",
	"Casimir": "Poland",
	"Catherine": "Russia",
	"Dandolo": "Venice",
	"Darius I": "Persia",
	"Darius": "Persia",
	"Dido": "Carthage",
	"Elizabeth": "England",
	"Enrico Dandolo": "Venice",
	"Gajah": "Indonesia",
	"Gajah Mada": "Indonesia",
	"Gandhi": "India",
	"Genghis_Khan": "Mongolia",
	"GenghisKhan": "Mongolia",
	"GustavusAdolphus": "Sweden",
	"Gustavus Adolphus": "Sweden",
	"Haile Selassie": "Ethiopia",
	"HaraldBluetooth": "Denmark",
	"Harun al-Rashid": "Arabia",
	"HarunAlRashid": "Arabia",
	"Hiawatha": "Iroquois",
	"Isabella": "Spain",
	"Kamehameha": "Polynesia",
	"Maria": "Portugal",
	"Maria I": "Portugal",
	"MariaTheresa": "Austria",
	"Maria Theresa": "Austria",
	"Montezuma": "Aztecs",
	"Napoleon": "France",
	"Nebuchadnezzar": "Babylon",
	"OdaNobunaga": "Japan",
	"Oda Nobunaga": "Japan",
	"Otto von Bismarck": "Germany",
	"Pacal": "The Maya",
	"Pacal The Great": "The Maya",
	"Pachacuti": "Inca",
	"Pedro II": "Brazil",
	"Pocatello": "Shohone",
	"Queen Dido": "Carthage",
	"Ramesses": "Egypt",
	"Ramkhamhaeng": "Siam",
	"Sejong": "Korea",
	"Selassie": "Ethiopia",
	"Shaka": "Zulu",
	"Suleiman": "The Ottomans",
	"Sulieman": "The Ottomans",
	"Theodora": "Byzantium",
	"Washington": "America",
	"WilliamOfOrange": "The Netherlands",
	"William of Orange": "The Netherlands",
	"WuZetian": "China",
	"Wu Zetian": "China",
	"ZuluShaka": "Zulu",
}

soundnamemap = {
	"declarewar": "declaringWar",
	"declarewarb": "declaringWar",
	"declareswar": "declaringWar",
	"attacked": "attacked",
	"attacked1": "attacked",
	"transattacked": "attacked",
	"hateattacked": "attacked",
	"attackedoption1": "attacked",
	"defeat": "defeated",
	"defeated": "defeated",
	"defeated1": "defeated",
	"into": "introduction",
	"intro": "introduction",
	"intro1": "introduction",
	"introduction": "introduction",
	"neutralhello": "neutralHello",
	"neutralgreeting": "neutralHello",
	"greeting": "neutralHello",
	"hatehello": "hateHello",
	"hatehello1": "hateHello",
	"request": "tradeRequest",
	"requests": "tradeRequest",
	"neutralrequest": "tradeRequest",
	"traderequestneutral": "tradeRequest",

	"peaceful": "unused/Peace Treaty",
	"peacful": "unused/Peace Treaty",
	"peace": "unused/Peace Treaty",
	"hatehearit": "unused/Hate Lets Hear It 1",
	"hatehearit1": "unused/Hate Lets Hear It 1",
	"hatehearit2": "unused/Hate Lets Hear It 2",
	"hatehearit3": "unused/Hate Lets Hear It 3",
	"hateletshearit": "unused/Hate Lets Hear It 1",
	"hateletshearit1": "unused/Hate Lets Hear It 1",
	"hateletshearit2": "unused/Hate Lets Hear It 2",
	"hateletshearit3": "unused/Hate Lets Hear It 3",
	"hateno": "unused/Hate No 1",
	"hateno1": "unused/Hate No 1",
	"hateno2": "unused/Hate No 2",
	"hateno3": "unused/Hate No 3",
	"hateyes": "unused/Hate Yes 1",
	"hateyes1": "unused/Hate Yes 1",
	"hateyes2": "unused/Hate Yes 2",
	"hateyes3": "unused/Hate Yes 3",
	"hateyes4": "unused/Hate Yes 4",
	"hateyes5": "unused/Hate Yes 5",
	"neutralhearit": "unused/Neutral Lets Hear It 1",
	"neutralhearit1": "unused/Neutral Lets Hear It 1",
	"neutralhearit2": "unused/Neutral Lets Hear It 2",
	"neutralhearit3": "unused/Neutral Lets Hear It 3",
	"neutralhearit4": "unused/Neutral Lets Hear It 4",
	"neutralletshearit": "unused/Neutral Lets Hear It 1",
	"neutralletshearit1": "unused/Neutral Lets Hear It 1",
	"neutralletshearit2": "unused/Neutral Lets Hear It 2",
	"neutralletshearit3": "unused/Neutral Lets Hear It 3",
	"neutralno": "unused/Neutral No 1",
	"neutralno1": "unused/Neutral No 1",
	"neutralno2": "unused/Neutral No 2",
	"neutralno3": "unused/Neutral No 3",
	"neutralyes": "unused/Neutral Yes 1",
	"neutralyes1": "unused/Neutral Yes 1",
	"neutralyes2": "unused/Neutral Yes 2",
	"neutralyes3": "unused/Neutral Yes 3",
	"demand": "unused/Demand",
	"demands": "unused/Demand",
	"gloat" : "unused/Gloat",
	"gloats" : "unused/Gloat",
	"attackedoption2": "unused/Attacked Variant 2",
	"attacked2": "unused/Attacked Variant 2",
	"defeated2": "unused/Defeated Variant 2",
	"neutralhello2": "unused/Neutral Hello 2",
	"excellent": "unused/Excellent",
	"birdambience": "unused/Bird Ambience",
	"declareswarpt2": "unused/Declare War Part 2",
	"declarewara": "unused/Declare War Variant A",
	"intro2": "unused/Introduction Variant 2",
}

leaderimagefolder = "Images/LeaderIcons"
musicfolder = "music"
soundfolder = "voices"

def getSoundNation(fname):
	name, ext = os.path.splitext(fname)
	returnname = name
	returnnation = ""
	for key, nation in leadernameprefixes.items():
		restname = name[len(key):].strip(" \t_")
		if name.startswith(key) and len(restname) < len(returnname):
			returnname = restname
			returnnation = nation
	return returnnation, returnname

def sortimage(dir, fname):
	"Remove Unity garbage, rename and move Leader Images"
	path = os.path.join(dir,fname)
	if fname in garbage:
		os.remove(path)
		return
	rx = """^([a-zA-Z][a-zA-Z0-9' -]*?) \("""
	match = re.search(rx, fname)
	name = fname if match is None else match.group(1) + ".png"
	if name in fixleadernames:
		name = fixleadernames[name]
	print("{} -> {}/{}".format(fname, leaderimagefolder, name))
	destdir = os.path.join(dir, leaderimagefolder)
	os.makedirs(destdir, exist_ok=True)
	dest = os.path.join(destdir, name)
	os.rename(path, dest)

def sortsound(dir, fname):
	path = os.path.join(dir,fname)
	if os.path.getsize(path) > 500000:
		sortmusic(dir, fname)
		return
	nation, name = getSoundNation(fname)
	if nation == "":
		print("{}: unknown nation: deleted".format(fname))
		os.remove(path)
		return
	name = (name.lower()
		.replace("02b","02")
		.replace("_","").replace(" ","").replace("-","").replace("0","")
		.replace("layer","").replace("gesturebase","")
		.replace("natural","neutral")
		.replace("disagrees","no").replace("agrees","yes")
		)
	if not name in soundnamemap:
		print("{}: nation={}, name={}".format(fname, nation, name))
		return
	name = soundnamemap[name]
	subdir = soundfolder
	if name.startswith("unused/"):
		name = nation + " - " + name[7:] + ".ogg"
		subdir = os.path.join(soundfolder, "unused")
	else:
		name = nation + "." + name + ".ogg"
	print("{} -> {}/{}".format(fname, subdir, name))
	destdir = os.path.join(dir, subdir)
	os.makedirs(destdir, exist_ok=True)
	dest = os.path.join(destdir, name)
	if (os.path.exists(dest)):
		print("Warning: {}/{} already exists.".format(subdir, name))
	os.rename(path, dest)

def sortmusic(dir, fname):
	path = os.path.join(dir,fname)
	nation, name = getSoundNation(fname)
	mood = "Peace" if name.startswith("Peace") else ("War" if name.startswith("War") else "Theme")
	parts = name.split(" - ", 3)
	if len(parts) == 3:
		name = nation + " - " + parts[2].strip(" \t_").replace(";",",").replace(", ",",").replace(",",", ") + " - " + mood
	else:
		name = nation + " - " + mood
	print("{} -> {}/{}".format(fname, musicfolder, name))
	destdir = os.path.join(dir, musicfolder)
	os.makedirs(destdir, exist_ok=True)
	dest = os.path.join(destdir, name + ".ogg")
	os.rename(path, dest)

def sortfiles(dir):
	"Take all files extracted from the civilization-v-soundboard apk and put them in a place suitable for an Unciv mod"
	for fname in sorted(os.listdir(dir)):
		path = os.path.join(dir,fname)
		if os.path.isdir(path):
			continue		# skip dirs
		n, ext = os.path.splitext(fname)
		if ext.lower() == ".png":
			sortimage(dir, fname)
		elif ext.lower() == ".ogg":
			sortsound(dir, fname)
		elif ext.lower() == ".meta":
			os.remove(path)

cdir = os.getcwd()
sortfiles(cdir)

