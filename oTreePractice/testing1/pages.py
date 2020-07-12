from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player


class MyPage(Page):
    form_model = 'player'
    form_fields = ['are_you_ok']
    def js_vars(self):
        return dict(
        speed_method = self.player.speed_method,
        )


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass

page_sequence = [MyPage, ResultsWaitPage, Results]
