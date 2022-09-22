import os

from table import Table
from player import Player
from game import Game

# TODO: add single-player mod

def main():
    table = Table()
    game = Game()


    def clear_console():
        os.system('clear')


    def ask_user_input() -> tuple:
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


    def switch_player(player:Player) -> Player:
        if player == p1:
            return p2
        return p1


    clear_console()
    player1 = input('Please enter the name of Player 1 (X): ').capitalize()
    player2 = input('Please enter the name of Player 2 (O): ').capitalize()

    p1 = Player(player1, 1)
    p2 = Player(player2, 2)
    curr_player = p1

    table.print_table()
    game_is_on = True
    while game_is_on:
        player_loop = True
        while player_loop:
            field = None
            print(f'\n{curr_player.name}\'s turn ({curr_player})\n')

            while field == None:
                field = ask_user_input()

            row = field[0]
            col = field[1]
            
            if table.set_table_field(row=row, col=col, player=curr_player.player_nr):
                curr_player.set_field(row=row, col=col)
                player_loop = False

        if game.check_state(player=curr_player):
            print(f'{curr_player.name} have won!')
            game_is_on = False
        elif not table.field_available():
            print('All the fields have been taken. It\'s a draw.')
            game_is_on = False
        else:
            curr_player = switch_player(player=curr_player)

        table.print_table()

main()