from riotwatcher import RiotWatcher
from request_champion_mastery import ChampionMastery
from Mastery_page_parser import MasteryPageParsing
from champgg_scraper import championggAPI
from winrate_difference_calculator import winrate_calcuations
from rune_page_parser import RunePageParsing
import consts as CONSTS


def main():
    #my_riot_api_key = str(raw_input('\nPaste Riot API Key: '))
    #my_championgg_api_key = str(raw_input('\nPaste champion.gg API Key: '))
    my_riot_api_key = '8792f2e9-2e9e-4f23-81bd-a219f81ea98f'
    my_championgg_api_key = '3f9e409bd58bc1868f8bfc4a3a75d40c'
    w = RiotWatcher(my_riot_api_key)
    c = championggAPI(my_championgg_api_key)

    #print('\nInput API Key can make requests?')
    #print(w.can_make_request())

    summoner_to_check = str(raw_input('\nWhat summoner do you want to know about? '))
    summoner = w.get_summoner(name=summoner_to_check)
    #print(summoner)

    my_mastery_pages = w.get_mastery_pages([summoner['id'], ])[str(summoner['id'])]
    show_masteries = str(raw_input('Show current masteries? '))
    len_mastery_data = len(my_mastery_pages['pages'])

    if show_masteries == 'Yes':
        for x in range(0, len_mastery_data):
            if my_mastery_pages['pages'][x]['current']:
                current_mastery_page = my_mastery_pages['pages'][x]
                print ('Current masteries: ')
        print '\"{name}\"'.format(name=current_mastery_page['name'])
        mastery = MasteryPageParsing(current_mastery_page)
        m = mastery.tree_divider()
        print m

    elif show_masteries == 'yes':
        for x in range(0, len_mastery_data):
            if my_mastery_pages['pages'][x]['current']:
                current_mastery_page = my_mastery_pages['pages'][x]
        print ('Current mastery page: ')
        print '\"{name}\"'.format(name=current_mastery_page['name'])
        mastery = MasteryPageParsing(current_mastery_page)
        m = mastery.tree_divider()
        print m

    my_rune_pages = w.get_rune_pages([summoner['id'], ])[str(summoner['id'])]
    show_runes = str(raw_input('Show current runes? '))
    len_rune_data = len(my_rune_pages['pages'])

    if show_runes == 'Yes':
        for x in range(0, len_rune_data):
            if my_rune_pages['pages'][x]['current']:
                current_rune_page = my_rune_pages['pages'][x]
                print ('Current rune page: ')
        print '\"{name}\"'.format(name=current_rune_page['name'])
        runes = RunePageParsing(current_rune_page)
        r = runes.rune_descriptions()
        print r

    elif show_runes == 'yes':
        for x in range(0, len_rune_data):
            if my_rune_pages['pages'][x]['current']:
                current_rune_page = my_rune_pages['pages'][x]
        print ('Current runes: ')
        print '\"{name}\"'.format(name=current_rune_page['name'])
        runes = RunePageParsing(current_rune_page)
        r = runes.rune_descriptions()
        print r

    champ_to_check = str(raw_input('\nWhat champion are they on? '))
    role_of_champ = str(raw_input('What role are they in? (Valid inputs: Top, Jungle, Middle, ADC, Support) '))

    championID = CONSTS.CHAMPION_ID[champ_to_check]
    #print ('{cha}\'s championID: {id}').format(cha=champ_to_check, id=championID)

    champion_mastery = ChampionMastery(my_riot_api_key)
    r = champion_mastery.get_champion_mastery(summoner['id'], championID)
    print'{name} is level {level} on {champ}'.format(name=summoner['name'], level=r['championLevel'], champ=champ_to_check)

    ranked_champion_stats = w.get_ranked_stats(summoner['id'])

    length_ranked_data = len(ranked_champion_stats['champions'])

    champ_found = False

    for x in range(0, length_ranked_data):
        if ranked_champion_stats['champions'][x]['id'] == int(championID):
            champ_games_won = float(ranked_champion_stats['champions'][x]['stats']['totalSessionsWon'])
            #print 'champ games won', champ_games_won
            champ_games_lost = float(ranked_champion_stats['champions'][x]['stats']['totalSessionsLost'])
            #print 'games lost', champ_games_lost
            champ_games_played = float(ranked_champion_stats['champions'][x]['stats']['totalSessionsPlayed'])
            winrate = round((champ_games_won / champ_games_played) * 100, 3)

            if champ_games_played > 5:
                if 60 <= winrate:
                    winrate_reaction = 'strong'
                elif 50 <= winrate < 60:
                    winrate_reaction = 'good'
                elif 40 <= winrate < 50:
                    winrate_reaction = 'bad'
                else:
                    winrate_reaction = 'ebolAIDS-causing, cancer-giving, hope-sundering'
            else:
                winrate_reaction = 'unreliable'

            print '{name} on {champ} has a {reac} winrate of {rate}% with {num} games played.'.format(name=summoner['name'], champ=champ_to_check, reac=winrate_reaction, rate=winrate, num=champ_games_played)

            champ_found = True

            champ_stats = c.request_by_champion(champ_to_check)
            champ_winrate = 'unable to be found.'
            length_champion_ranked_data = len(champ_stats)

            for y in range(0, length_champion_ranked_data):
                if champ_stats[y]['role'] == role_of_champ:
                    champ_winrate = float(champ_stats[y]['general']['winPercent'])

            print 'Average winrate for {champ} as {role} is {winrate}.'.format(champ=champ_to_check, role=role_of_champ, winrate=champ_winrate)

            calc = winrate_calcuations(summoner['name'])
            calc.winrate_difference(winrate, champ_winrate)

    if champ_found is False:
        print 'No ranked champion data found for {champ}\n'.format(champ=champ_to_check)


if __name__ == "__main__":
    main()
