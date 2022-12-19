# initialize the players' scores and the number of times they have played
player1_score = 0
player2_score = 0
played = 0

# use a while loop that continues until the players have played 5 times
while True:
    # ask player 1 to choose rock, paper, or scissors
    player1_move = input("Player 1, enter your move (rock, paper, or scissors): ")

    # ask player 2 to choose rock, paper, or scissors
    player2_move = input("Player 2, enter your move (rock, paper, or scissors): ")

    # use if-else statements to check for the different combinations of moves and determine a winner
    if player1_move == player2_move:
        print("It's a tie!")
    elif player1_move == 'rock' and player2_move == 'scissors':
        print("Player 1 wins! Rock beats scissors.")
        player1_score += 1
    elif player1_move == 'scissors' and player2_move == 'paper':
        print("Player 1 wins! Scissors beats paper.")
        player1_score += 1
    elif player1_move == 'paper' and player2_move == 'rock':
        print("Player 1 wins! Paper beats rock.")
        player1_score += 1
    else:
        print("Player 2 wins! {} beats {}.".format(player2_move, player1_move))
        player2_score += 1

    # increment played by 1
    played += 1

    if input('Would you like to play again?(Y/N)').lower() == 'y':
        continue
    else:
        break

# print the final scores
print("Player 1's final score is {}".format(player1_score))
print("Player 2's final score is {}".format(player2_score))
