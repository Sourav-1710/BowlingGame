import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def test_spare_game(self):
        self.roll_many(0, 20)
        self.assertEqual(self.game.score(), 0)

    def test_increment(self):
        self.roll_many(1, 20)
        self.assertEqual(self.game.score(), 20)

    def test_decrement(self):
        self.roll_spare()
        self.game.roll(3)
        self.roll_many(0, 17)
        self.assertEqual(self.game.score(), 16)

    def test_anothertest(self):
        self.roll_strike()
        self.game.roll(4)
        self.game.roll(3)
        self.roll_many(0, 16)
        self.assertEqual(self.game.score(), 24)

    def test_perfect_game(self):
        self.roll_many(10, 12)
        self.assertEqual(self.game.score(), 300)

    def test_magic_game(self):
        self.roll_many(5, 21)
        self.assertEqual(self.game.score(), 150)    

    def roll_many(self,pins,rolls):
        for _ in range(rolls):
            self.game.roll(pins) 

    def roll_spare(self):
        self.game.roll(5) 
        self.game.roll(5)  

    def roll_strike(self):
        self.game.roll(10)                   


