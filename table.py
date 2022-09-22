class Table:
    def __init__(self) -> None:
        self.table_data = {
            "a": [" ", " ", " "],
            "b": [" ", " ", " "],
            "c": [" ", " ", " "],
        }

    def set_table_field(self, row:str, col:int, symbol:str) -> bool:
        if row in ['a', 'b', 'c'] and col in [0, 1, 2]:
            if self.table_data[row][col] == " ":
                self.table_data[row][col] = symbol
                return True
            print('This field has been already taken, please choose another one.')
        else:
            print('Invalid input! Please try again.')
        return False

    def field_available(self) -> bool:
        for _, fields in self.table_data.items():
            if " " in fields:
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

    def clear_table(self):
        for row, fields in self.table_data.items():
            for field in range(len(fields)):
                self.table_data[row][field] = " "