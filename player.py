class Player:
    """Main player class to set up a new player.
    """
    def __init__(self, player_nr:int) -> None:
        """Initialization function for new players, sets the symbol, table, score and prompts for a name.

        Args:
            player_nr (int): Number of the player. Possible values: 0 (for computer), 1 or 2.
        """
        self.number = player_nr
        self.symbol = self._set_symbol()
        self.name = self._set_name()
        self.score = 0
        self.table = {
            'a': [0, 0, 0],
            'b': [0, 0, 0],
            'c': [0, 0, 0],
        }

    def _set_symbol(self) -> str:
        """Sets the symbol based on the player number.

        Returns:
            str: 'X' for player 1 and 'O' for player 2 / computer.
        """
        if self.number == 1:
            return 'X'
        return 'O'

    def _set_name(self) -> str:
        """Prompts for a name and passes it for sanitizing.

        Returns:
            str: Sanitized version of the name.
        """
        name = None
        while not name:
            name = 'Computer'
            if not self.number == 0:
                name = self._sanitize_name(input(f'Please enter the name of Player {self.number} ({self.symbol}): '))
        return name
        
    def _sanitize_name(self, name:str) -> str:
        """Sanitizes the user input to have a correct name format (capitalized, trimmed).

        Args:
            name (str): Unprocessed version of the name.

        Returns:
            str: Sanitized version of the name. Returns 'None' if empty string is provided as input.
        """
        if len(name) != 0:
            return name.strip().capitalize()
        print('Name cannot be empty. Please try again.')
        return

    def set_field(self, row:str, col:int):
        """Sets a field for the user's table at a given location.

        Args:
            row (str): User-selected row.
            col (int): User-selected column.
        """
        self.table[row][col] = 1

    def increment_score(self):
        """Increments the user score by 1.
        """
        self.score += 1

    def clear_table(self):
        """Clears the user's table and sets 0 for each field.
        """
        for row, fields in self.table.items():
            for field in range(len(fields)):
                self.table[row][field] = 0