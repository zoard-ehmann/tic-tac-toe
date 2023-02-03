import os
import time
import random

from table import Table
from player import Player


def clear_console() -> None:
    """Clears the console output.
    """
    os.system('clear')


def generate_field() -> tuple:
    """Chooses a random field from the free fields for the computer.

    Returns:
        tuple: Row (alphabetical) and column (numeric) as a tuple.
    """
    best_fields = curr_player.get_recommended_fields()
    return random.choice(best_fields)


def mark_field(row:str, col:int) -> bool:
    """Marks the field both in player table and game table. Returns 'True' if the marking is valid.

    Args:
        row (str): Row to select.
        col (int): Column to select.

    Returns:
        bool: Returns 'True' if the marking of the desired field is successful.
    """
    if curr_player.set_field(row=row, col=col, val=1):
        if second_player.set_field(row=row, col=col, val=-1):
            table.set_table_field(row=row, col=col, symbol=curr_player.symbol)
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

    clear_console()

    single_player = False
    if input('Single player mode? (enter \'y\' if yes): ').lower() == 'y':
        single_player = True

    if single_player:
        p1 = Player(player_nr=1, is_computer=True)
        p2 = Player(player_nr=2)
    else:
        p1 = Player(player_nr=1)
        p2 = Player(player_nr=2)

    while p1.name == p2.name:
        print('This name has been taken. Please choose another one.')
        p2 = Player(player_nr=2)

    curr_player = p1
    second_player = p2

    table.print_table()
    game_is_on = True
    while game_is_on:
        print(f'\n{curr_player.name}\'s turn ({curr_player.symbol})\n')
        if not curr_player.is_computer:
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
                for dot in range(3):
                    time.sleep(.5)
                    print('.', end='', flush=True)
                    dot += 1
                if mark_field(row=field[0], col=field[1]):
                    computer_loop = False
            print('')

        if curr_player.check_win():
            print(f'{curr_player.name} have won!')
            curr_player.increment_score()
            game_is_on = False
        elif not curr_player.has_field_to_take():
            print('All the fields have been taken. It\'s a draw.')
            game_is_on = False
        else:
            if curr_player.number == 1:
                curr_player = p2
                second_player = p1
            else:
                curr_player = p1
                second_player = p2

        table.print_table()

        if not game_is_on:
            if input('Would you like to play again? (enter \'y\' if yes): ').lower() == 'y':
                game_is_on = True
                curr_player = p1
                second_player = p2
                clear_console()
                table.clear_table()
                p1.clear_table()
                p2.clear_table()
            print(f'{p1.name}\'s score: {p1.score}')
            print(f'{p2.name}\'s score: {p2.score}')
