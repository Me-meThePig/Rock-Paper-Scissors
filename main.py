import random

user_wins = 0
comp_wins = 0
games = 0

while True:
    user_choice = input('Choose rock, paper, or scissors, or type q to quit (r/p/s/q): ')
    comp_choice = random.randint(0, 2)

    # map computer random numbers to rock, paper, or scissors
    if comp_choice == 0:
        comp_choice = 'r'
    elif comp_choice == 1:
        comp_choice = 'p'
    elif comp_choice == 2:
        comp_choice = 's'

    # handle quitting or invalid input
    if user_choice == 'q':
        break
    elif user_choice != ('r' or 'p' or 's'):
        continue

    # print user and computer choices
    print(f'You chose: {user_choice}.')
    print(f'The computer chose: {comp_choice}.')

    # decide the winner
    if user_choice == comp_choice:
        print("it's a tie!")
    elif user_choice == 'r' and comp_choice == 's':
        print('You win!')
        user_wins += 1
    elif user_choice == 'p' and comp_choice == 'r':
        print('You win!')
        user_wins += 1
    elif user_choice == 's' and comp_choice == 'p':
        print('You win!')
        user_wins += 1
    else:
        print('You lose.')
        comp_wins += 1
    
    games += 1

# display stats
if games > 0:
    print(f'\nOut of {games} games, you had {user_wins} win(s), and the computer had {comp_wins} win(s).')
    print(f'\nYou won {round((user_wins/games)*100)}% of the time.')
    print(f'The computer won {round((comp_wins/games)*100)}% of the time.')
    print(f'It was a tie {round(((games-(comp_wins+user_wins))/games)*100)}% of the time.')
