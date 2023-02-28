


class Utils:
    @staticmethod
    def get_king_pos(board, color):
        #returns king pos (row, column)
        for elt in range(len(board)):
            for case in range(len(board[elt])):
                c=board[elt][case]
                if c != "" and c.color == color and c.piece == "Roi":
                    return (elt, case)

    @staticmethod
    def king_in_danger(board, color):
        #check to see if king can be taken

        p = Utils.get_king_pos(board, color)

        for column in range(len(board)):
            for case in range(len(board[column])):
                c = board[column][case]
                if c != "" and c.color != color:
                    print(column, case)
                    for i in c.can_move((column, case), board):
                        if i == p:
                            return True
        return False
