


class Utils:
    def get_king_pos(self, board, color):
        for elt in range(len(board)):
            for case in range(len(board[elt])):
                c=board[elt][case]
                if c != "" and c.color == color and c.piece == "Roi":
                    return (elt, case)


    def king_in_danger(self, board, color):
        p = self.get_king_pos(board, color)

        for column in range(len(board)):
            for case in range(len(board[column])):
                c = board[column][case]
                if c != "" and c.color != color:
                    for i in case.can_move(board, (column, case)):
                        if i == p:
                            return True
        return False
