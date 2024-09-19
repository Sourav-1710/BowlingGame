import pydoc
class BowlingGame:

    """Represent a game of bolwing.

    A game of bowling consists of rolls to knock down pins.
    This class allows tarcking of rolls and scoring according to standard bolwing rules.
    
    Attributes:
    rools (list): alist to store the number of pins knocked down in each roll.
    """
    def __init__(self):

        self.rolls = []

    def roll(self,pins):
        self.rolls.append(pins)

    def score(self):
        result = 0
        roll_index = 0
        for _ in range(10):
            if self.is_strike(roll_index):
                result += self.strike_score(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):
                result += self.spare_score(roll_index)
                roll_index += 2
            else:
                result += self.frame_score(roll_index)
                roll_index += 2 
                return result  
    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def strike_score(self, roll_index): 
        return 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def spare_score(self, roll_index):
        return 10 + self.rolls[roll_index + 2]

    def frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]

documentation = pydoc.render_doc(BowlingGame)
with open("BowlingGame.html", "w") as f:
    f.write(documentation)                   