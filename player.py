VALID_ROWS = ['a', 'b', 'c']
VALID_COLUMNS = [0, 1, 2]

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

    def set_field(self, row:str, col:int, val:int) -> bool:
        """Validates the input against the available fields. Sets the corresponding field for the user's
        table at a given location.

        Args:
            row (str): User-selected row.
            col (int): User-selected column.
            val (int): Value of the field. 1 if current player's, -1 if opponent's.

        Returns:
            bool: 'True' if setting the field was success and 'False' otherwise.
        """
        user_turn = True
        if val == -1: user_turn = False
        if row in VALID_ROWS and col in VALID_COLUMNS:
            if self.table[row][col] == 0:
                self.table[row][col] = val
                return True
            elif user_turn:
                print('This field has been already taken, please choose another one.')
        elif user_turn:
            print('Invalid input! Please try again.')
        return

    def increment_score(self) -> None:
        """Increments the user score by 1.
        """
        self.score += 1

    def clear_table(self) -> None:
        """Clears the user's table and sets 0 for each field.
        """
        for row, fields in self.table.items():
            for field in range(len(fields)):
                self.table[row][field] = 0

    def get_best_fields(self, free_fields=list) -> list:
        # Returns the free fields now; WIP
        # TODO: Calculate with least as possible steps, calculate with opponent fields, go for possible wins
        # TODO: is free fields required at all?! (calc w/ -1s instead, should mark opponent's...)
        # TODO: best_fields = []
        # TODO: # Go through all rows
        # TODO: row_weights = {} # Highest should be selected
        # TODO: for row, fields in self.table.items():
        # TODO:     row_sum = 0
        # TODO:     for field in fields:
        # TODO:         row_sum += field
        # TODO:     row_weights[row] = [row_sum]
        # TODO: # Go through all columns
        # TODO: col_weights = {} # Highest should be selected
        # TODO: for row, fields in self.table.items():
        # TODO:     for i in range(3):
        # TODO:         col_weights[i] += fields[i] # FIXME ADDING

        # TODO: print(row_weights)
        # TODO: print(col_weights)

        return free_fields

    def check_state(self) -> bool:
        """Checks the user's table for winning situations.

        Returns:
            bool: Returns 'True' when a winning situation occurs.
        """
        a = self.table['a']
        b = self.table['b']
        c = self.table['c']
        win = False

        # Check for complete rows
        if sum(a) == 3 or sum(b) == 3 or sum(c) == 3:
            win = True
        
        # Check for complete columns
        for i in range(3):
            if (a[i] and b[i] and c[i]) == 1:
                win = True

        # Check for complete diagonals
        if b[1] == 1:
            if (a[0] == 1 and c[2] == 1) or (a[2] and c[0] == 1):
                win = True

        return win

