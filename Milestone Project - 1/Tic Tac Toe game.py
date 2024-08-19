test_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player_token = []
starting_first = ''
player_one_position = 0
player_two_position = 0
turn = 0
choices = []
next_turn = ''


def player_symbol():
    global player_token

    player_1 = input("Player 1: Do you want to be X or O? ")
    player_1 = player_1.upper()

    while player_1 != 'X' and player_1 != 'O':
        print(f"Please input either 'X' or 'O'")
        player_1 = input("Player 1: Do you want to be X or O? ")

    player_token.append(player_1)

    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'

    player_token.append(player_2)

    return player_token


def game_start():
    global starting_first

    print(f'Player 1 will go first.\n\n')

    start_choice = input('Are you ready to play? Enter Yes or No. ')

    while start_choice != 'Yes' and start_choice != 'No':
        print(f"Please input either 'Yes' or 'No'")
        start_choice = input('Are you ready to play? Enter Yes or No. ')

    if start_choice == 'Yes':
        starting_first = 'Player 1'
    else:
        starting_first = 'Player 2'

    return starting_first


def player_1_position():
    global player_one_position
    player_one_choice = 0

    while player_one_choice not in range(1, 10):
        player_one_choice = int(input('Player One - Choose your next position: (1-9) '))
        if player_one_choice not in range(1, 10):
            print(f'Please input a number between 1 and 9')

    for i in range(0, player_one_choice + 1):
        player_one_position = player_one_choice - 1

    return player_one_position


def player_2_position():
    global player_two_position
    player_two_choice = 0

    while player_two_choice not in range(1, 10):
        player_two_choice = int(input('Player Two - Choose your next position: (1-9) '))
        if player_two_choice not in range(1, 10):
            print(f'Please input a number between 1 and 9')

    for i in range(0, player_two_choice + 1):
        player_two_position = player_two_choice - 1

    return player_two_position


def display_board():
    print(f'\n')
    print(f"   |   |   \n {test_board[6]} | {test_board[7]} | {test_board[8]}\n   |   |   ")
    print(f"-----------  ")
    print(f"   |   |   \n {test_board[3]} | {test_board[4]} | {test_board[5]}\n   |   |   ")
    print(f"-----------  ")
    print(f"   |   |   \n {test_board[0]} | {test_board[1]} | {test_board[2]}\n   |   |   ")


def update_display():
    global turn
    global next_turn
    global choices

    if turn == 0:
        if starting_first == 'Player 1':
            test_board[player_one_position] = player_token[0]
            choices.append(player_one_position)

        elif starting_first == 'Player 2':
            test_board[player_two_position] = player_token[1]
            choices.append(player_two_position)

    if turn > 0:
        if next_turn == 'one':
            if player_one_position not in choices:
                test_board[player_one_position] = player_token[0]
                choices.append(player_one_position)
        else:
            if player_two_position not in choices:
                test_board[player_two_position] = player_token[1]
                choices.append(player_two_position)

    return test_board


def game_check():
    global test_board
    global turn

    if turn == 9:
        for element in test_board:
            if element != ' ':
                print(f'\nThe game is a tie.')
                break


# Bringing everything together
print(f'Welcome to Tic Tac Toe!')

play_again = ''
while True:
    player_symbol()
    game_start()

    if starting_first == 'Player 1':
        player_1_position()
        update_display()
        display_board()
        next_turn = 'two'
    else:
        player_2_position()
        update_display()
        display_board()
        next_turn = 'one'

    turn = 1
    while turn < 9:
        if next_turn == 'one':
            print(f'\n')
            player_1_position()
            update_display()
            display_board()
            next_turn = 'two'
            turn += 1
            if (test_board[0] == test_board[1] == test_board[2] == player_token[0] or test_board[2] == test_board[5] ==
                test_board[8] == player_token[0] or test_board[6] == test_board[7] == test_board[8] == player_token[
                    0] or
                test_board[0] == test_board[3] == test_board[6] == player_token[0] or test_board[2] == test_board[4] ==
                test_board[6] == player_token[0]) or test_board[0] == test_board[4] == test_board[8] == player_token[
                0] or \
                    test_board[3] == test_board[4] == test_board[5] == player_token[0] or test_board[1] == test_board[
                4] == \
                    test_board[7] == player_token[0]:
                print(f"\nCongrats! You have won the game. You defeated Player Two in {turn} turns.")
                break

        elif next_turn == 'two':
            print(f'\n')
            player_2_position()
            update_display()
            display_board()
            next_turn = 'one'
            turn += 1
            if (test_board[0] == test_board[1] == test_board[2] == player_token[1] or test_board[2] == test_board[5] ==
                test_board[8] == player_token[1] or test_board[6] == test_board[7] == test_board[8] == player_token[
                    1] or
                test_board[0] == test_board[3] == test_board[6] == player_token[1] or test_board[2] == test_board[4] ==
                test_board[6] == player_token[1]) or test_board[0] == test_board[4] == test_board[8] == player_token[
                1] or \
                    test_board[3] == test_board[4] == test_board[5] == player_token[1] or test_board[1] == test_board[
                4] == \
                    test_board[7] == player_token[1]:
                print(f"\nCongrats! You have won the game. You defeated Player One in {turn} turns.")
                break

    game_check()
    play_again = input(f'\nWould you like to play again? Yes/No ')
    print(f'\n')
    if play_again == 'Yes':
        test_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        starting_first = ''
        player_token = []
        player_one_position = 0
        player_two_position = 0
        turn = 0
        choices = []
        next_turn = ''
        continue
    else:
        print(f'\nThanks for playing.')
        break
