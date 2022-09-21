class Table:
    def __init__(self) -> None:
        self.table_data = {
            "a": [" ", " ", " "],
            "b": [" ", " ", " "],
            "c": [" ", " ", " "],
        }


    def _recognize_player(self, player):
        if player == 1:
            return "X"
        return "O"

    
    def _throw_err(self):
        print(
            '''
            -----------------------------------------------
            ****** This field has been taken already ******
            ******     Please choose another one     ******
            -----------------------------------------------
            '''
        )


    def set_table_field(self, row, col, player):
        if row[col] == " ":
            row[col] = self._recognize_player(player)
            return 0
        else:
            self._throw_err()
            return 1


    def print_table(self):
        print(
            f'''
            -------------
            | ${self.table_data[0][0]} | ${self.table_data[0][1]} | ${self.table_data[0][2]} |
            -------------
            | ${self.table_data[1][0]} | ${self.table_data[1][1]} | ${self.table_data[1][2]} |
            -------------
            | ${self.table_data[2][0]} | ${self.table_data[2][1]} | ${self.table_data[2][2]} |
            -------------
            '''
        )