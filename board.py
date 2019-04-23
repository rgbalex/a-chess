class Board(object):
    """docstring for Board."""

    def __init__(self):
        super(Board, self).__init__()
        self.chessBoard = [ ["" for j in range(8)] for i in range(8) ]

    def __str__(self):
        for i in self.chessBoard:
            print(i)
        return ""

    def place(self,obj,place):
        x = place[0]-1
        y = place[1]-a
        ret = self.chessBoard[y][x]
        self.chessBoard[y][x] = obj
        return ret
