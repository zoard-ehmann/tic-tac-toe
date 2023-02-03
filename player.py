VALID_ROWS = ['a', 'b', 'c']
VALID_COLUMNS = [0, 1, 2]

class Player:
    """Main player class to set up a new player.
    """
    def __init__(self, player_nr:int, is_computer:bool=False) -> None:
        """Initialization function for new players, sets the symbol, table, score and prompts for a name.

        Args:
            player_nr (int): Number of the player. Can be 1 (for 'X') or 2 (for 'O').
            is_computer (bool, optional): Marker for computer opponent, 'True' for computer in single player mode.
            Defaults to False.
        """
        self.number = player_nr # TODO: validate player nr.
        self.is_computer = is_computer
        self.symbol = self.__set_symbol()
        self.name = self.__set_name()
        self.score = 0
        self.table = {
            'a': [0, 0, 0],
            'b': [0, 0, 0],
            'c': [0, 0, 0],
        }

    def __set_symbol(self) -> str:
        """Sets the symbol based on the player number.

        Returns:
            str: 'X' for player 1 and 'O' for player 2.
        """
        if self.number == 1:
            return 'X'
        return 'O'

    def __set_name(self) -> str:
        """Prompts for a name and passes it for sanitizing. Sets it to 'Computer' for the opponent in
        single player mode.

        Returns:
            str: Sanitized version of the name.
        """
        name = None
        while not name:
            name = 'Computer'
            if not self.is_computer:
                name = self.__sanitize_name(input(f'Please enter the name of Player {self.number} ({self.symbol}): '))
        return name
        
    def __sanitize_name(self, name:str) -> str:
        """Sanitizes the user input to have a correct name format (capitalized, trimmed).

        Args:
            name (str): Unprocessed version of the name.

        Returns:
            str: Sanitized version of the name. Returns 'None' if empty string is provided as input.
        """
        if len(name) != 0:
            sanitized_name = name.strip().capitalize()
            if sanitized_name == 'Computer':
                print('\'Computer\' is reserved, please choose another one.')
                return
            return sanitized_name
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

    def check_win(self) -> bool:
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
            if a[i] == 1 and b[i] == 1 and c[i] == 1:
                win = True

        # Check for complete diagonals
        if b[1] == 1:
            if (a[0] == 1 and c[2] == 1) or (a[2] == 1 and c[0] == 1):
                win = True

        return win

    def has_field_to_take(self) -> bool:
        """Checks if there is free field on the board to take.

        Returns:
            bool: 'True' if there's at least 1 available field, 'False' otherwise.
        """
        for _, fields in self.table.items():
            if 0 in fields:
                return True
        return

    def __least_to_take(self, fields:list, direction:str) -> list:
        frequency = {}
        res = []
        if direction == 'row':
            field_selector = 0
        elif direction == 'col':
            field_selector = 1
        for field in fields:
            if field[field_selector] not in frequency:
                frequency[field[field_selector]] = 0
            frequency[field[field_selector]] += 1
        target = [identifier for identifier, slots in frequency.items() if slots == min(frequency.values())]
        for field in fields:
            if field[field_selector] in target:
                res.append(field)
        return res

    def __calc_min(self, *lists):
        return min(*lists, key=len)

    def get_recommended_fields(self) -> list:
        # Free fields
        free_fields = []
        for row, fields in self.table.items():
            index = 0
            for field in fields:
                if field == 0:
                    free_fields.append((row, index))
                index += 1

        # Rows
        recommended_rows = []
        for row, fields in self.table.items():
            if not -1 in fields:
                index = 0
                for field in fields:
                    if field == 0:
                        recommended_rows.append((row, index))
                    index += 1
        recommended_rows = self.__least_to_take(fields=recommended_rows, direction='row')

        # Columns
        recommended_columns = []
        for index in range(3):
            skip = False
            for row in self.table:
                if self.table[row][index] == -1:
                    skip = True
                    break
            if not skip:
                for row in self.table:
                    if self.table[row][index] == 0:
                        recommended_columns.append((row, index))
        recommended_columns = self.__least_to_take(fields=recommended_columns, direction='col')

        # Diagonals (Common)
        rows = list(self.table.keys())
        recommended_diagonals_1 = []
        recommended_diagonals_2 = []

        # Diagonals (1)
        skip_1 = False
        for index in range(3):
            if self.table[rows[index]][index] == -1:
                skip_1 = True
                break
        if not skip_1:
            for index in range(3):
                if self.table[rows[index]][index] == 0:
                    recommended_diagonals_1.append((rows[index], index))

        # Diagonals (2)
        skip_2 = False
        for index in range(3):
            if self.table[rows[(len(rows) -1) - index]][index] == -1:
                skip_2 = True
                break
        if not skip_2:
            for index in range(3):
                if self.table[rows[(len(rows) -1) - index]][index] == 0:
                    recommended_diagonals_2.append((rows[(len(rows) -1) - index], index))

        min_query = []
        if recommended_columns:
            min_query.append(recommended_columns)
        if recommended_rows:
            min_query.append(recommended_rows)
        if recommended_diagonals_1:
            min_query.append(recommended_diagonals_1)
        if recommended_diagonals_2:
            min_query.append(recommended_diagonals_2)

        best_fields = free_fields
        lists = [l for l in min_query]
        if lists:
            best_fields = self.__calc_min(lists)

        return best_fields

