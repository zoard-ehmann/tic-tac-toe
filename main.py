from table import Table
from player import Player


table = Table()

player1 = input('Please enter the name of Player 1: ')
player2 = input('Please enter the name of Player 2: ')

p1 = Player(player1, 1)
p2 = Player(player2, 2)
curr_player = p1


def switch_player(player:Player) -> Player:
    if player == p1:
        return p2
    return p1


game_is_on = True
while game_is_on:
    player_loop = True
    while player_loop:
        print(f'{curr_player.name}\'s turn\n')
        # TODO: error handling for inputs
        # TODO: implement winner calculation logic
        # TODO: add help function
        row = input('Choose row (a, b, c): ').lower()
        col = int(input('Choose column (1, 2, 3): '))
        if table.set_table_field(row=row, column=col, player=curr_player.player_nr): player_loop = False
        table.print_table()
    curr_player = switch_player(player=curr_player)
