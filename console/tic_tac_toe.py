import sys


class TicTacToeGame:
    global board_dict, user_dict, current_player, current_player_symbol, winner
    board_dict = {
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
    }
    winner = None

    def display_board():
        print("\n")
        for i in board_dict.keys():
            if int(i) % 3 == 0:
                print(f" {board_dict[i]} ")
                if int(i) != 9:
                    print("═══╬═══╬═══")
            else:
                print(f" {board_dict[i]} ", end="║")

    def user_register():
        msg = "Enter your in-game name"
        player1 = (input(f"{msg} (Player 1) : ")).strip() or 'Player 1'
        player2 = (input(f"{msg} (Player 2) : ")).strip() or 'Player 2'
        print(f"Player 1: {player1}\t=>  [O]\nPlayer 2: {player2}\t=>  [X]")
        print(f"\033[94m{player1} Vs. {player2}\033[39m")
        user_dict = {
            player1: 'O',
            player2: 'X',
        }
        return player1, player2, user_dict

    def get_user_choice(current_player, symbol):
        while True:
            try:
                user_input = int(
                    input(f"\n{current_player}, Enter your choice : "))
                if user_input not in [i for i in range(1, 10)]:
                    print(
                        "\033[91mInvalid input. Please enter a number between 1 and 9!\033[39m")
                elif board_dict[str(user_input)] in ['O', 'X']:
                    print(
                        "\033[91mThis spot is already taken. Please choose another spot!\033[39m")
                else:
                    break
            except ValueError:
                print(
                    "\033[91mERROR::You aren't allowed to enter characters/words/symbols!\033[39m")
            except KeyboardInterrupt:
                print(
                    f"\nGame ended by player: \"{current_player}\". Bye Bye 😞️")
                sys.exit()
        board_dict[str(user_input)] = symbol

    def switch_turn():
        next_player = [i for i in user_dict if i != current_player][0]
        return next_player, user_dict[next_player]

    def check_result():
        winning_condition_li = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),
            (1, 4, 7), (2, 5, 8), (3, 6, 9),
            (1, 5, 9), (3, 5, 7)
        ]
        for i in winning_condition_li:
            if board_dict[str(i[0])] == board_dict[str(i[1])] == board_dict[str(i[2])] == current_player_symbol:
                winner = current_player
                return winner
        if all(i in ['O', 'X'] for i in board_dict.values()):
            winner = 'Tie'
            return winner

    ########## Game Play START ##########
    try:
        player1, player2, user_dict = user_register()
        current_player = player1
        current_player_symbol = user_dict[current_player]
        display_board()
        while winner is None:
            get_user_choice(current_player, current_player_symbol)
            winner = check_result()
            if winner:
                msg = "\033[33mNo one wins. Game Over! 😢️" if winner == 'Tie' else f"\033[92mThe winner is {winner}"
                display_board()
                print(f"\n{msg}")
                break
            display_board()
            current_player, current_player_symbol = switch_turn()
    except KeyboardInterrupt:
        print(f"\nGame ended by player. Bye Bye 😞️")
        sys.exit()
    ########## Game Play END ##########
