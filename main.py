import os

from table import Table
from player import Player
from game import Game

# TODO: add single-player mod

def clear_console():
    os.system('clear')


def ask_field_input() -> tuple:
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


def main():
    table = Table()
    game = Game()

    clear_console()

    p1 = Player(player_nr=1)
    p2 = Player(player_nr=2)
    curr_player = p1

    table.print_table()
    game_is_on = True
    while game_is_on:
        player_loop = True
        while player_loop:
            print(f'\n{curr_player.name}\'s turn ({curr_player.symbol})\n')
            field = None
            while field == None:
                field = ask_field_input()

            row = field[0]
            col = field[1]
            if table.set_table_field(row=row, col=col, player=curr_player.number):
                curr_player.set_field(row=row, col=col)
                player_loop = False

        if game.check_state(player=curr_player):
            print(f'{curr_player.name} have won!')
            game_is_on = False
        elif not table.field_available():
            print('All the fields have been taken. It\'s a draw.')
            game_is_on = False
        else:
            if curr_player.number == 1:
                curr_player = p2
            else:
                curr_player = p1

        table.print_table()

main()