class Table:
    def __init__(self) -> None:
        self.table_data = {
            "a": [" ", " ", " "],
            "b": [" ", " ", " "],
            "c": [" ", " ", " "],
        }

    def set_table_field(self, row:str, col:int, symbol:str) -> int:
        if row in ['a', 'b', 'c'] and col in [0, 1, 2]:
            if self.table_data[row][col] == " ":
                self.table_data[row][col] = symbol
                return 1
            print('This field has been already taken, please choose another one.')
        else:
            print('Invalid input! Please try again.')
        return 0

    def field_available(self) -> bool:
        for _, row in self.table_data.items():
            if " " in row:
                return True
        return False

    def print_table(self):
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