from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random


author = 'Your name here'

doc = """
Your app description
"""

class speed(object):
    def speed_list(player):
        
        participant = player.participant
        # 若不存在就決定並起來，若已存在就直接取出
        if Constants.key_method not in participant.vars:
            randomspeed = random.choice([0.7, 0.8, 0.9])
            #_隨機選擇完放dict
            participant.vars[Constants.key_method] = randomspeed
        method = participant.vars[Constants.key_method]
        return method

class Constants(BaseConstants):
    name_in_url = 'testing1'
    players_per_group = None
    num_rounds = 1
    key_method = 'speed_method'

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.speed_method = speed.speed_list(p)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    speed_method = models.FloatField()
    are_you_ok = models.BooleanField(
            label = '你今天好嗎？',
            choices = [
                [True, '很好'],
                [False, '還好']
            ],
            widget=widgets.RadioSelect,
    )
