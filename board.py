from pieces import *

class Board(object):
    """docstring for Board."""

    def __init__(self):
        super(Board, self).__init__()
        self.chessBoard = [ ["" for j in range(8)] for i in range(8) ]

    def __str__(self):
        for i in self.chessBoard:
            print(i)
        return ""

    def place(self,obj):
        pos = obj.position
        x = pos[0]-1
        y = 8-pos[1]
        ret = self.chessBoard[y][x]
        self.chessBoard[y][x] = obj
        return ret

    def reset(self):
        line1 = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        countx = 1
        self.__init__()
        for i in line1:
            self.place(i(True,(countx,1)))
            self.place(i(False,(countx,8)))
            countx += 1
        for i in range(1,9):
            self.place(Pawn(True,(i,2)))
            self.place(Pawn(False,(i,7)))
