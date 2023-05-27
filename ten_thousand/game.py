try:
    from ten_thousand.game_logic import GameLogic
except:
    from game_logic import GameLogic

class Game(GameLogic):
    
    def play(self):

        total_score = 0
        round_number = 1
        dice_remaining = 6
        all_dice_scored_rounds = 0
        points = 0
        final_points = 0

        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input (">")

        if response.lower() == "y" or response.lower() == "yes":
            while True  :
                check = 0
                if response.lower() == "y" or response.lower() == "yes" or dice_remaining == 6:
                    print(f"Starting round {round_number}")
                print(f"Rolling {dice_remaining} dice...")

                dice = list(self.roll_dice(dice_remaining))
                dice_output = "*** "

                for num in dice:
                    dice_output += f"{num} "
                dice_output += "***"
                print(dice_output)
                points = self.calculate_score(dice)

                if  round_number>20:
                    print(f"Thanks for playing. You earned {total_score} points")
                    break

                while True:
                    if points == 0:
                        print('''
****************************************
**        Zilch!!! Round over         **
****************************************''')
                              
                        check = 1
                        round_number += 1
                        dice_remaining = 6
                        total_score -= final_points
                        final_points = 0

                        print(f"You banked {final_points} points in round {round_number}")
                        print(f"Total score is {total_score} points")
                        break

                    if check == 1 :
                        break
                    print("Enter dice to keep, or (q)uit:")
                    response = input(">")

                    if response.lower() == "q" or response.lower() == "quit" or response.lower() == "b":
                        
                        break
                    dice_to_keep = []
                    invalid_input = False
                    removed_dices = dice[:]

                    for value in response:
                        if value in map(str, dice):
                            dice.remove(int(value))

                        elif value not in map(str, dice) or response == '' :
                            print(f"Cheater!!! Or possibly made a typo...  Please try again.")
                            dice = removed_dices
                            print("***", " ".join(str(num) for num in dice), "***")
                            invalid_input = True
                            break
                        dice_to_keep.append(int(value))

                    if invalid_input:
                        continue
                    k = len(self.get_scorers(dice_to_keep))
                    dice_remaining -= k

                    if dice_remaining == 0 :
                        dice_remaining = 6
                    points = self.calculate_score(dice_to_keep)
                    final_points += points
                    print(f"You have {final_points} unbanked points and {dice_remaining} dice remaining")
                    break

                if check == 0:
                    if response.lower() == "q" or response.lower() == "quit":
                        print(f"Thanks for playing. You earned {total_score} points")
                        break

                    if dice_remaining == 0:
                        dice_remaining = 6
                        all_dice_scored_rounds += 1
                        if all_dice_scored_rounds >= 3:
                            all_dice_scored_rounds = 0
                    if all_dice_scored_rounds > 2:
                        print("You have scored all dice for 3 consecutive rounds. Starting a new game.")
                        break

                    print("(r)oll again, (b)ank your points or (q)uit:")
                    response = input (">")

                    if response.lower() == "r" or response.lower() == "roll":
                        total_score += points
                        continue

                    elif response.lower() == "b" or response.lower() == "bank":
                        total_score += points
                        print(f"You banked {final_points} points in round {round_number}")
                        print(f"Total score is {total_score} points")
                        round_number += 1
                        final_points = 0
                        dice_remaining = 6

                    elif response.lower() == "q" or response.lower() == "quit":
                        print(f"Thanks for playing. You earned {total_score} points")
                        break
        else:
            print("OK. Maybe another time")



if __name__ == "__main__":
    game = Game()
    game.play()