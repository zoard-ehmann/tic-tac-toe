class Player:
    def __init__(self, name, player_nr) -> None:
        self.name = name
        self.player_nr = player_nr
        self.table = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]


    def set_table(self, table):
        self.table = table