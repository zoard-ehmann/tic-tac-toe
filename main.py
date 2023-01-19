import os
import time
import random

from table import Table
from player import Player
from game import Game


def clear_console() -> None:
    """Clears the console output.
    """
    os.system('clear')


def generate_field() -> tuple:
    """Chooses a random field from the free fields for the computer.

    Returns:
        tuple: Row (alphabetical) and column (numeric) as a tuple.
    """
    free_fields = table.check_free_fields()
    # TODO: Implement computer 'logic'
    best_fields = curr_player.get_best_fields(free_fields=free_fields)
    print(best_fields)
    input()
    #################################
    return random.choice(best_fields)


def mark_field(row:str, col:int) -> bool:
    """Marks the field both in player table and game table. Returns 'True' if the marking is valid.

    Args:
        row (str): Row to select.
        col (int): Column to select.

    Returns:
        bool: Returns 'True' if the marking of the desired field is successful.
    """
    valid_mark = table.set_table_field(row=row, col=col, symbol=curr_player.symbol)
    if valid_mark:
        curr_player.set_field(row=row, col=col)
        return True
    return


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
        if curr_player.number != 0:
            player_loop = True
            while player_loop:
                field = None
                while field == None:
                    field = ask_field_input()
                if mark_field(row=field[0], col=field[1]):
                    player_loop = False
        else:
            computer_loop = True
            while computer_loop:
                field = generate_field()
                mark_field(row=field[0], col=field[1])
                for dot in range(3):
                    time.sleep(.5)
                    print('.', end='', flush=True)
                    dot += 1
                computer_loop = False
            print('')

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
