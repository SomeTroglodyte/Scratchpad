A 'scraper' pulling all music tracks available on the composer's website, and renaming them to suit the upcoming situational music in Unciv:

- [Civ5 soundtrack](https://www.geoffknorr.com/sid-meiers-civilization-v)
- [G&K soundtrack](https://www.geoffknorr.com/civvgodsandkings)

Instructions:
- `chmod 775 LeaderPortraitScraper.py`
- `./LeaderPortraitScraper.py`
- move the generated mods folder to your assets and activate as permanent audiovisual mod in the mod manager

Caveats:
- Needs python3
- You might need to `pip install cssselect` and/or lxml
