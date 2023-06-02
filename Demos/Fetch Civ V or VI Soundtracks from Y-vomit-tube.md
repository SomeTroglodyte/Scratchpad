# Scope
Download the Civ V and/or Civ VI original soundtracks from a dubious but publicly available source and convert them into a music mod usable by Unciv.

This is brought to you as abstract instructions, not a scraper script, thanks to y🤮ut🤬be being what it is.

You may/will need to interpret and translate - e.g. on Suse obviously don't sudo apt, on Windoze improvise, maybe use avidemux to extract uncompressed audio, maybe use the medieval cue thingy to chapter split.

## Prepare
`sudo apt install -y shntool ffmpeg cuetools vorbis-tools`
- choose / create a working directory
- make sure you have at the very least 2.2GB free in your working directory for Civ V, 3.5 GB for Civ VI

## Download
Civ5 URL: https://www.youtube.com/watch?v=rH-Qw2pbrNk
Civ6 URL: https://www.youtube.com/watch?v=eqJFVg05b8Q
Use any downloader available - don't trust online ones blindly. If in doubt, JDownloader can do it - but use only the Jar version, it runs everywhere you have a JRE, and avoids their malware installer.

Fetch "Civ V Soundtrack.cue" and/or "Civ VI Soundtrack.cue" from here and place it into the same directory.

## Convert to uncompressed
Rename the downloaded y💩be sound file to "Civ V Soundtrack.mp4" or "Civ VI Soundtrack.mp4", respectively.

`ffmpeg -hide_banner -i "Civ V Soundtrack.mp4" -y -vn -metadata creation_time= -metadata compatible_brands= -metadata major_brand= -metadata minor_version= -metadata comment="Civ V Soundtrack" -metadata:s:a:0 handler_name= -metadata:s:a:0 creation_time= "Civ V Soundtrack.wav"`
(starting from here, change for Civ6 as needed, won't be mentioned again)

## Split tracks and convert to playable by Unciv
`shnsplit -f "Civ V Soundtrack.cue" -t "%t" -o "cust ext=ogg oggenc -b 128 -o %f -" "Civ V Soundtrack.wav" ;`

## Deploy
Just create an appropriately named subfolder under your mods folder, a 'music' folder under that, and place all .ogg files in there, clean up, and go and mark that mod as permanent audiovisual in Unciv.

## Notes
(Civ5 only) 
Missing:
* Babylon, Egypt Peace, Korea, Siam, Denmark, Austria, Celts, Ethiopie, Maya - not found
* Candidates to replace a few the above: [Korea - Arirang - Theme](https://en.wikipedia.org/wiki/File:Arirang_(USAS).ogg), [Denmark - Drömde mig en dröm - Theme](https://en.wikipedia.org/wiki/File:Dr%C3%B6mde_mig_en_dr%C3%B6m.ogg), [Austria - Recordare - Peace](https://en.wikipedia.org/wiki/File:W._A._Mozart_-_Requiem,_K._626_(Bruno_Walter,_Wiener_Philharmoniker,_Wiener_Staatsopernchor,_1956)_-_06._Recordare.ogg), [Austria - Dies Irae - War](https://en.wikipedia.org/wiki/File:W._A._Mozart_-_Requiem,_K._626_(Bruno_Walter,_Wiener_Philharmoniker,_Wiener_Staatsopernchor,_1956)_-_03._Dies_irae.ogg) 
* Polynesia (available via [GeoffKnorrMusicScraper.py](./GeoffKnorrMusicScraper.py) - these files are preferrable anyway)
* Byzantium, Carthage, Inca, Mongolia, Spain, Sweden, The Huns, The Netherlands, The Ottomans - same as Polynesia

(Civ6 only)
The resulting names all start with a Civ6 civ name and end with an Era - I've added the"- Ambient" suffix so Unciv loads them. Maybe code a PR to support era specific music?


Track boundaries are as displayed by the source, and as such only have full second resolution. So track beginnings and ends may be off, and if I find any bad case I'll maybe update the cue file.


