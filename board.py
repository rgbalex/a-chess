from pieces import *
class Board(object):
    """docstring for Board."""

    def __init__(self):
        super(Board, self).__init__()
        self.chessBoard = [ ["" for j in range(8)] for i in range(8) ]
