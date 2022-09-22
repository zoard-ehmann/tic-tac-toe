class Game:
    def check_state(self, table:dict) -> bool:
        a = table["a"]
        b = table["b"]
        c = table["c"]
        win = False

        if 0 not in a or 0 not in b or 0 not in c:
            win = True

        for i in range(3):
            if (a[i] and b[i] and c[i]) == 1:
                win = True

        if b[1] == 1:
            if (a[0] == 1 and c[2] == 1) or (a[2] == 1 and c[0] == 1):
                win = True

        return win