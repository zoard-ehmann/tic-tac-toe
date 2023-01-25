class Table:
    """Table class to set up a new board.
    """
    def __init__(self) -> None:
        """Initializes a table for rendering.
        """
        self.table_data = {
            'a': [' ', ' ', ' '],
            'b': [' ', ' ', ' '],
            'c': [' ', ' ', ' '],
        }
    
    def set_table_field(self, row:str, col:int, symbol:str) -> None:
        """Sets a field of the table with the proper symbol based on the actual player.

        Args:
            row (str): User-selected row.
            col (int): User-selected column.
            symbol (str): Symbol of the user.
        """
        self.table_data[row][col] = symbol

    def print_table(self) -> None:
        """Prints the actual board.
        """
        print(
            f'''
                1   2   3
              -------------
            A | {self.table_data["a"][0]} | {self.table_data["a"][1]} | {self.table_data["a"][2]} |
              -------------
            B | {self.table_data["b"][0]} | {self.table_data["b"][1]} | {self.table_data["b"][2]} |
              -------------
            C | {self.table_data["c"][0]} | {self.table_data["c"][1]} | {self.table_data["c"][2]} |
              -------------
            '''
        )

    def clear_table(self) -> None:
        """Clears the game board and sets an empty space for each field.
        """
        for row, fields in self.table_data.items():
            for field in range(len(fields)):
                self.table_data[row][field] = " "