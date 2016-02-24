# riven-rater
Some Python for pulling data on your lane opponent(s) for League of Legends. Heavily uses the Riot Games API, Champion.gg API, and the RiotWatcher library. Relies on requests library for API calls, and on scipy for some statistical analysis.

The whole thing over-all is far from pythonic, to be frank. My variable/class/file naming conventions are all over the place. I'm doing this in bursts during lunch breaks and free time. The main idea is to be able to use statistical analysis consisting of:
  - Comparing a player's win-rate on a champion to the average winrate of the champion.
  - Comparing a player's win-rate on a champion to the average winrate of the champion at their elo.
  - Analysing this difference to determine proficiency on a champion (ideally here would be something like seeing where on the bell curve     they fall for win-rate).
  - Pulling champion health, armor, and damage statistics to provide an appropriate estimate of damage they could deal at different
    points in the laning phase.


These are the main points - analysing champion proficiency - are where I'd be doing anything even remotely new. A lot of guys who like to code like to play League of Legends, and there's a plethora of websites and applications to pull and present basic matchup data, and even more advanced analysis like checking item winrates on individual champions or across elo divisions. 

Ideally, getting this to a prototype would help ALOT. Riot's API limits the number of requests you can make until you register a product, and getting access to the most recent ranked data is out of my reach for now. Riot does provide 1000 ranked games' worth of data, so I'll develop my stat-chewing on that to build a prototype, register it, and hopefully get access to the useful stuff.

Index:

consts.py
  file holding constant values for easier access, imported as "CONSTS" whenever needed.
  contents:
    - URL formats for making API calls to Riot and Champion.gg
    - Version numbers of the Riot API for various sections, required for API calls currently
    - Region names required for Riot API calls
    - Location names for Riot API calls (only champion mastery)
    - Summoner ID's. I included my own and that of a friend for testing purposes.
    - Season name required for match history Riot API calls
    - Mastery ID's paired with brief descriptions. Heavily truncuated from the Riot API's output and saved locally to minimize API calls.
    - Champion ID's paired with champion names, required for champion stat Riot API calls, and saved locally to minimize calls.

request_champion_mastery.py
  RiotWatcher at the moment does not support Riot's Champion Mastery API, so this I implement it myself here.
  For some reason the Champion Mastery API handles calls completely differently from all others, so this helps to keep calls consistent    in the main
  Uses RiotWatcher's LoLException to handle requests errors.
  
Mastery_page_parser.py
  Small class used to parse RiotAPI's JSON output of mastery page ID's into a list of mastery names and descriptions from consts.py
  The JSON is taken from the current mastery page of an input summoner ID.

champgg_scraper.py
  Simple class that implements calling champion.gg's API. The necessary URL formats are stored in consts.py, and errors are handled by
  LoLException.
  It is used to return a JSON that's assigned to a variable so data can be pulled from it.
  
winrate_difference_calculator.py
  The supposed heart of the project. Object class that takes a playername to make a print statement look nicer (why did I do this?)
  It accepts two winrates (player and public) in percent notation (aka 56 not 0.56) and uses them to calculate two values: A percent
  difference between the two and a pvalue obtainied from a Fisher's Exact Test (scipy used here). The idea is to give a clue as to a
  player's skill on a champion compared to the population. Problem is, without modern ranked data, I'm forced to approximate numbers of
