# Scope
Download the Civ V original soundtrack from a dubious but publicly available source and convert it into a music mod usable by Unciv.

This is brought to you as abstract instructions, not a scraper script, thanks to y🤮ut🤬be being what it is.

You may/will need to interpret and translate - e.g. on Suse obviously don't sudo apt, on Windoze improvise, maybe use avidemux to extract uncompressed audio, maybe use the medieval cue thingy to chapter split.

## Prepare
`sudo apt install -y shntool ffmpeg cuetools vorbis-tools`
- choose / create a working directory
- make sure you have at the very least 2.2GB free in your working directory

## Download
URL: https://www.youtube.com/watch?v=rH-Qw2pbrNk
Use any downloader available - don't trust online ones blindly. If in doubt, JDownloader can do it - but use only the Jar version, it runs everywhere you have a JRE, and avoids their malware installer.

Fetch "Civ V Soundtrack.cue" from here and place it into the same directory.

## Convert to uncompressed
Rename the downloaded y💩be sound file to "Civ V Soundtrack.mp4"

`ffmpeg -hide_banner -i "Civ V Soundtrack.mp4" -y -vn -metadata creation_time= -metadata compatible_brands= -metadata major_brand= -metadata minor_version= -metadata comment="Civ V Soundtrack" -metadata:s:a:0 handler_name= -metadata:s:a:0 creation_time= "Civ V Soundtrack.wav"`

## Split tracks and convert to playable by Unciv
`shnsplit -f "Civ V Soundtrack.cue" -t "%t" -o "cust ext=ogg oggenc -b 128 -o %f -" "Civ V Soundtrack.wav" ;`

## Deploy
Just create an appropriately named subfolder under your mods folder and place all .ogg files in there, clean up, and go and mark that mod as permanent audiovisual in Unciv.
