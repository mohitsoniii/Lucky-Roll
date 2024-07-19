import random

min_value = 1
max_value = 6

def roll():
    value = random.randint(min_value, max_value)
    return value

while True :
    num_players = input("Enter the Number of players (2-4) : ")
    if num_players.isdigit():
        num_players = int(num_players)
        if 2 <= num_players <= 4 :
            break
        else:
            print("Number of players must be in between 2 - 4 !!")
    else:
        print("Invalid Input, try again")

max_score = 50
player_score = [0 for _ in range(num_players)]

while max(player_score) < max_score:
    for player_idx in range(num_players):
        print("\nPlayer number", player_idx + 1, "turn has just started !")
        print("Your total score is :", player_score[player_idx], "\n")
        cur_score = 0

        while True:
            want_roll = input("Would you like to roll (y) ? ")
            if want_roll.lower() != 'y':
                break
            
            value = roll()
            if value == 1:
                print("\nyou rolled a 1 !!, Turn done !!")
                cur_score = 0
                break
            else:
                cur_score += value
                print("you rolled a : ", value)
            
            print("Your score is : ",cur_score, "\n")

        player_score[player_idx] += cur_score
        print("Your total score is : ", player_score[player_idx])

max_score = max(player_score)
winning_idx = player_score.index(max_score)
print("\nPlayer number", winning_idx + 1, "is the WINNER with a score of: ", max_score, "\n")