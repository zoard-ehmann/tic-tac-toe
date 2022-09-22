class Player:
    def __init__(self, player_nr) -> None:
        self.number = player_nr
        self.symbol = self._set_symbol()
        self.name = self._set_name()
        self.table = {
            "a": [0, 0, 0],
            "b": [0, 0, 0],
            "c": [0, 0, 0],
        }

    def _set_symbol(self):
        if self.number == 1:
            return 'X'
        return 'O'

    def _set_name(self):
        name = None
        while not name:
            name = self._sanitize_name(input(f'Please enter the name of Player {self.number} ({self.symbol}): '))
        return name
        
    def _sanitize_name(self, name):
        if len(name) != 0:
            return name.strip().capitalize()
        print('Name cannot be empty. Please try again.')
        return

    def set_field(self, row:str, col:int):
        self.table[row][col] = 1