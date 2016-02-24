import consts as CONSTS


class MasteryPageParsing(object):

    def __init__(self, page):
        self.page = page

    def tree_divider(self):
        length_page = len(self.page['masteries'])
        for x in range(0, length_page):
            mastery_id = str(self.page['masteries'][x]['id'])
            print CONSTS.MASTERIES[mastery_id]
