from player import Player


class Game:
    def check_state(self, player:Player) -> bool:
        a = player.table["a"]
        b = player.table["b"]
        c = player.table["c"]
        
        win = False

        if 0 not in (a or b or c):
            win = True

        for i in range(2):
            if (a[i] and b[i] and c[i]) == 1:
                win = True

        if b[1] == 1 and (a[0] == 1 and c[2]) == 1 or (a[2] == 1 and c[0]):
            win = True

        return win