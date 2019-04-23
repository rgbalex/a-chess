from .piece import ChessPiece
class Pawn(ChessPiece):
    """docstring for Pawn."""

    def __init__(self, color, position):
        super(Pawn, self).__init__(color, position)
