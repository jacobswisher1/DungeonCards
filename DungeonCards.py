import random
# import pyCardDeck
# from pyCardDeck.cards import BaseCard

class Player:

    def __init__(self):
        self.hand = []
        self.deck = []
        self.energy = 3
        self.health = 10
    
    def isDead(self):
        return self.health.equals(0)
    
class Dungeon:

    def __init__(self):
        self.playerSide = []
        self.botSide = []

class Card:

    def __init__(self, name : str, cost : int, playText : str, playEffect : str):
        self.cost = cost
        self.name = name
        self.playText = playText
        self.playEffect = playEffect

class UnitCard(Card):

    classType = 'unit'
    def __init__(self, name :str, power : int, heart : int):
        properties = []
        self.power = power
        self.heart = heart
        super().__init__(name)

class SpellCard(Card):

    classType = 'spell'
    def __init__(self, name :str):
        super().__init__(name)

class Game:

    def __init__(self, player : Player, bot : Player, dungeon : Dungeon):
        pass