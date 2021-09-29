A 'scraper' pulling all music tracks available on the composer's website, and renaming them to suit the upcoming situational music in Unciv:

- [Civ5 soundtrack](https://www.geoffknorr.com/sid-meiers-civilization-v)
- [G&K soundtrack](https://www.geoffknorr.com/civvgodsandkings)

Instructions:
- `chmod 775 LeaderPortraitScraper.py`
- `./LeaderPortraitScraper.py`
- If you get an http 429 error (limited by server), just try again after a pause. The script will skip already downloaded tracks.
- move the generated mod's folder to your assets and activate as permanent audiovisual mod in the mod manager

Caveats:
- Needs python3
- You might need to `pip install cssselect` and/or lxml
