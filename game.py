import random, time

# Showing what each one stands for and all of the options
forOptions = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

# Defining all of the different options, the score, and the current version
def rockPaperScissorsGame():
    options = ['R', 'P', 'S']
    computerScore = 0
    playerScore = 0
    version = 1.01

    # Start of the Loop
    while True:
        try:
            player = input('Please type [R]ock, [P]aper, or [S]cissors ')
            player = player.upper
            if player == 'Q':
                print('See you soon!')
                break
            if player == ['V', 'Version']:
                print('Currently running on ', version)
            if player == 'K':
                print('You found the secret key! You earned 2 extra points')
                playerScore += 1
            elif player in options:
                computer = options[random.randint(0,2)]
                if player == computer:
                    print('You tied!')
                elif (player == 'R' and computer == 'S') or \
                    (player == 'P' and computer == 'R') or \
                    (player == 'S' and computer == 'P'):
                    print('You won the round!')
                    playerScore += 1
                else:
                    print('You lost the round')
                    computerScore += 1

                # Prints the score at the end of each round
                print('Player Score = ', playerScore, 'Computer Score = ', computerScore)

                if playerScore == 3:
                    print('You won this game!')
                    break
                elif computerScore == 3:
                    print('You lost this Game, try again.')
                    break
            # If the player or computer's score reaches 3, the game ends
            if playerScore == 3:
                print('You won this game!')
                break
            elif computerScore == 3:
                print('You lost this Game, try again.')
                break
            else:
                print('Please enter the correct option, try again')
        
        except:
            exit()

rockPaperScissorsGame()


