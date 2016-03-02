import consts as CONSTS
from collections import Counter


class RunePageParsing(object):

    def __init__(self, page):
        self.page = page

    def rune_descriptions(self):
        length_page = len(self.page['slots'])
        rune_ids = range(0, length_page)

        for x in range(0, length_page):
            rune_ids[x] = str(self.page['slots'][x]['runeId'])

        rune_count = Counter(rune_ids)
        rune_ids = list(set(rune_ids))
        length_ids = len(rune_ids)

        for x in range(0, length_ids):
            print rune_count[rune_ids[x]], CONSTS.RUNES[rune_ids[x]]['name'], CONSTS.RUNES[rune_ids[x]]['description']
