from .piece import ChessPiece
class Pawn(ChessPiece):
    """docstring for Pawn."""

    def __init__(self, color):
        super(Pawn, self).__init__(color)

    def findMoves(self, currentPosition):
        pass

    def selectMove(self):
        pass
