import os
import time

from table import Table
from player import Player
from game import Game

# TODO: add single-player mod

def clear_console():
    """Clears the console output.
    """
    os.system('clear')


def ask_field_input() -> tuple:
    """Prompts the user for a field input (eg.: a1), validates it for length and splits into row and column.
    Returns 'None' if the input is not valid.

    Returns:
        tuple: Row (alphabetical) and column (numeric) as a tuple.
    """
    user_prompt = input('Choose a field (row and column, eg.: a1): ')
    if len(user_prompt) == 2:
        row = user_prompt[0].lower()
        if row.isalpha():
            try:
                col = int(user_prompt[1]) - 1
                return (row, col)
            except ValueError:
                pass

    print('Invalid input! Please try again.')
    return


if __name__ == '__main__':
    table = Table()
    game = Game()

    clear_console()

    single_player = False
    if input('Single player mode? (enter \'y\' if yes): ').lower() == 'y':
        single_player = True

    p1 = Player(player_nr=1)
    if single_player:
        p2 = Player(player_nr=0)
    else:
        p2 = Player(player_nr=2)

    while p1.name == p2.name:
        print('This name has been taken. Please choose another one.')
        p2 = Player(player_nr=2)

    curr_player = p1

    table.print_table()
    game_is_on = True
    while game_is_on:
        print(f'\n{curr_player.name}\'s turn ({curr_player.symbol})\n')
        if curr_player.name != 'Computer':
            player_loop = True
            while player_loop:
                field = None
                while field == None:
                    field = ask_field_input()

                row = field[0]
                col = field[1]
                if table.set_table_field(row=row, col=col, symbol=curr_player.symbol):
                    curr_player.set_field(row=row, col=col)
                    player_loop = False
        else:
            for dot in range(5):
                time.sleep(.5)
                print('.', end='', flush=True)
                dot += 1

        if game.check_state(table=curr_player.table):
            print(f'{curr_player.name} have won!')
            curr_player.increment_score()
            game_is_on = False
        elif not table.has_available_field():
            print('All the fields have been taken. It\'s a draw.')
            game_is_on = False
        else:
            if curr_player.number == 1:
                curr_player = p2
            else:
                curr_player = p1

        table.print_table()

        if not game_is_on:
            if input('Would you like to play again? (enter \'y\' if yes): ').lower() == 'y':
                game_is_on = True
                curr_player = p1
                clear_console()
                table.clear_table()
                p1.clear_table()
                p2.clear_table()
            print(f'{p1.name}\'s score: {p1.score}')
            print(f'{p2.name}\'s score: {p2.score}')
