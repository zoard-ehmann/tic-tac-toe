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


    def set_table_field(self, row, column, player):
        col = column - 1
        if self.table_data[row][col] == " ":
            self.table_data[row][col] = self._recognize_player(player)
            return 1
        else:
            self._throw_err()
            return 0


    def print_table(self):
        print(
            f'''
            -------------
            | {self.table_data["a"][0]} | {self.table_data["a"][1]} | {self.table_data["a"][2]} |
            -------------
            | {self.table_data["b"][0]} | {self.table_data["b"][1]} | {self.table_data["b"][2]} |
            -------------
            | {self.table_data["c"][0]} | {self.table_data["c"][1]} | {self.table_data["c"][2]} |
            -------------
            '''
        )