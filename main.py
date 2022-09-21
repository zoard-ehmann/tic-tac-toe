from table import Table
from player import Player
from game import Game


def main():
    table = Table()
    game = Game()

    player1 = input('Please enter the name of Player 1: ').capitalize()
    player2 = input('Please enter the name of Player 2: ').capitalize()

    p1 = Player(player1, 1)
    p2 = Player(player2, 2)
    curr_player = p1


    def sanitize_input(inp:str):
        if len(inp) == 2:
            row = inp[0].lower()
            try:
                col = int(inp[1]) - 1
                return (row, col)
            except ValueError:
                print('Invalid input! Please try again.')
        return None


    def switch_player(player:Player) -> Player:
        if player == p1:
            return p2
        return p1


    game_is_on = True
    while game_is_on:
        player_loop = True
        while player_loop:
            print(f'\n{curr_player.name}\'s turn\n')
            # TODO: add single-player mod
            table.print_table()
            field = input('Choose field (row and column, eg.: a1): ')
            inp = sanitize_input(field)

            if inp:
                row = inp[0]
                col = inp[1]
                
                if table.set_table_field(row=row, col=col, player=curr_player.player_nr):
                    curr_player.set_field(row=row, col=col)
                    player_loop = False

        if game.check_state(player=curr_player):
            print(f'{curr_player.name} have won!')
            game_is_on = False
        else:
            curr_player = switch_player(player=curr_player)

main()