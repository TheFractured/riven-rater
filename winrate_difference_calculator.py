from scipy import stats
import math


class winrate_calcuations(object):

    def __init__(self, player_name):
        self.player_name = player_name

    def winrate_difference(self, player_winrate, public_winrate):
        winrate_difference = player_winrate - public_winrate
        winrate_average = round((player_winrate + public_winrate)/2, 3)

        winrate_percent_difference = round(winrate_difference / winrate_average * 100, 3)

        player_wins = math.floor(player_winrate/100)*1000
        player_losses = math.floor(1000 - player_wins)

        public_wins = math.floor(public_winrate/100)*1000
        public_losses = math.floor(1000 - public_wins)

        oddsratio, pvalue = stats.fisher_exact([[player_wins, player_losses], [public_wins, public_losses]])
        print 'pvalue =', pvalue
        if pvalue <= 0.05:
            print 'There\'s a statistically significant', winrate_percent_difference, '% difference between', self.player_name,'\'s winrate and the average winrate.'
        else:
            print 'There\'s a statistically insignificant', winrate_percent_difference, '% difference between', self.player_name,'\'s winrate and the average winrate.'
