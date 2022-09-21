class Player:
    def __init__(self, name, player_nr) -> None:
        self.name = name
        self.player_nr = player_nr
        self.table = {
            "a": [0, 0, 0],
            "b": [0, 0, 0],
            "c": [0, 0, 0],
        }

    def set_field(self, row:str, col:int):
        self.table[row][col] = 1