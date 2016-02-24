import consts as CONSTS
import requests
from riotwatcher import LoLException, error_400, error_404, error_401, error_429, error_500, error_503


#Usually RiotWatcher handles this URL formatting, but it doesn't have champ mastery yet
#Champ-Mastery is formatted differently from all other API URL's
class ChampionMastery(object):
    #Hard-coded to NA region, calling for the NA code from consts file
    #Similarly, RiotWatcher defaults to NA region, so shouldn't be a problem
    def __init__(self, api_key, region=CONSTS.REGIONS['north_america']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        try:
            response = requests.get(
            CONSTS.URL['champion_mastery_base'].format(
                proxy=self.region,
                url=api_url
                ),
                params=args
           )
            return response.json()

        except LoLException as e:
            if e == error_429:
                print('WE should retry in {} seconds.'.format(e.headers['Retry-After']))
            elif e == error_404:
                print('Summoner not found.')
            elif e == error_503:
                print('Service unavailible.')
            elif e == error_500:
                print('Internal server error.')
            elif e == error_401:
                print('Unauthorized, check API Key.')
            elif e == error_400:
                print('Bad request')

#   REFERENCE CHAMPION MASTERY API CALL URL
    # /championmastery/location/{platformId}/player/{playerId}/champion/{championId}

    def get_champion_mastery(self, playerId, champId):
        api_url = CONSTS.URL['champion_mastery'].format(
            platformId=CONSTS.LOCATION['north_america'],
            playerId=playerId,
            championId=champId
        )
        return self._request(api_url)
