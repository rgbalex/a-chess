class ChessPiece(object):
    """docstring for Piece.
    Chess Pieces will be defined using an augment of the algebraic chess
    notaiton defined here: https://en.wikipedia.org/wiki/Algebraic_notation_(chess)

    Types applicable:
    P = Pawn
    B = Bishop
    R = Rook (Castle)
    N = Knight
    Q = Queen
    K = King

    Colours applicable:
    White = True
    Black = False

    Positions are defined using the matrix below:
    [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7)]
    [(0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]
    [(0,5), (1,5), (2,5), (3,5), (4,5), (5,5), (6,5), (7,5)]
    [(0,4), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), (7,4)]
    [(0,3), (1,3), (2,3), (3,3), (4,3), (5,3), (6,3), (7,3)]
    [(0,2), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2)]
    [(0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]
    [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0)]
    (where (3,0) is the white king)
    """
    def __init__(self, color):
        self.color = color # bool
        # self.position = position # tuple of co-ordinates

    def __str__(self):
        return ("White" if self.color else "Black") + " " + self.__class__.__name__
