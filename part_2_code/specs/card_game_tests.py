import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.game = CardGame()

    def test_check_for_ace(self):
        card1 = Card("Hearts", 1)
        card2 = Card("Spades", 2)
        self.assertTrue(self.game.check_for_ace(card1))
        self.assertFalse(self.game.check_for_ace(card2))

    def test_highest_card(self):
        card1 = Card("Hearts", 10)
        card2 = Card("Diamonds", 5)
        self.assertEqual(self.game.highest_card(card1, card2), card1)

    def test_cards_total(self):
        card1 = Card("Hearts", 5)
        card2 = Card("Diamonds", 9)
        card3 = Card("Clubs", 2)
        self.assertEqual(self.game.cards_total([card1, card2]), "You have a total of 14")
        self.assertEqual(self.game.cards_total([card1, card3]), "You have a total of 7")
