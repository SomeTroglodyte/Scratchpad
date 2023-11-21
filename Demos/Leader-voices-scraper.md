# How to get Leader Voices from a public itch.io offer

Goal: Convert said download into a Mod for Unciv, containing Leader Voices for certain diplomativ interactions, Civ war/peace music tracks, and optionally Leader Portraits.

* Get an AssetRipper release from https://github.com/AssetRipper/AssetRipper/releases and unpack (twice!).
* Get CiviVIB.apk from itch.io: https://omegaxp.itch.io/civilization-v-soundboard.
* Set your system to a dark Theme, or endure almost unreadable fonts in AssetRipper for a short while.
* Launch AssetRipper (the executable works standalone, no install necessary beyond unpacking).
* Open file, select the APK, wait patiently until it has built its view.
* Export all files - the ones you don't need are few, and AssetRipper exports a lot of junk you don't need anyway.
* Navigate down to AssetRipperExport***/ExportedProject/Assets/AudioClip.
* Move all files into your future mod's root, and if you want them, those from Texture2D too (only if you're not planning to use a better source for leader portraits).
* Place the [Leader-voices-scraper.py](https://github.com/SomeTroglodyte/Scratchpad/blob/master/Demos/Leader-voices-scraper.py) script into the same folder the extracted files are now in. It's available right where in this repo and folder - follow the link and hit the little download button top right corner, two steps to the right of the "Raw" button.

* Run the Leader-voices-scraper.py script - make sure to use a recent Python 3 interpreter.
* You may remove AssetRipper, the APK, the AssetRipperExport* folder and my script now.

* Run Unciv and mark your mod as permanent audiovisual.
* If you copied the assets from Texture2D, you get Leader Portraits. These are pretty much the same but slightly lower quality, as those from the 'Civ V Leader portraits' mod or those scraped from wikia using my LeaderPortraitScraper.py script.
