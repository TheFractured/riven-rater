import consts as CONSTS
import requests
from riotwatcher import LoLException, error_400, error_404, error_401, error_429, error_500, error_503


class championggAPI(object):

    def __init__(self, api_key):
        self.api_key = api_key

    def request_by_role(self, role):
        try:
            response = requests.get(
                CONSTS.URL['champion.gg']+'/stats/role'+role+'?api_key='+self.api_key
                    )
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

        return response.json()

    def request_by_champion(self, champion):
        try:
            response = requests.get(
                CONSTS.URL['champion.gg']+'/stats/champs/'+champion+'?api_key='+self.api_key
                )

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

        return response.json()
