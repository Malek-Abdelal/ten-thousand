import random
# try:
from ten_thousand.game_logic import GameLogic
# except :
#     from game_logic import GameLogic

class Game() :
    def play(self, round_num):
        # player = GameLogic()
        GameLogic.play_game(round_num)


if __name__ == "__main__":
    # new_game = Game()
    GameLogic.play_game()