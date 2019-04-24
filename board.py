from pieces import *

class Board(object):
    """docstring for Board."""

    def __init__(self):
        super(Board, self).__init__()
        self.chessboard = [ [None for j in range(8)] for i in range(8) ]
        self.turn = True # True is white's turn and false is black's turn.
                         # is true because white always goes first.

    def __str__(self):
        print("========================================================")
        for i in self.chessboard:
            print(i)
        print("========================================================")
        return ""

    def place(self,obj, position):
        pos = position
        x = pos[0]-1
        y = 8-pos[1]
        ret = self.chessboard[y][x]
        self.chessboard[y][x] = obj
        return ret

    def get(self, pos):
        x = pos[0]-1
        y = 8-pos[1]
        return self.chessboard[y][x]

    def move(self, old, new):
        pos = old
        x = pos[0]-1
        y = 8-pos[1]
        old = self.chessboard[y][x]
        pos = new
        p = pos[0]-1
        q = 8-pos[1]
        new = self.chessboard[q][p]

        if new.__class__ != None:
            # Append new to dead pieces
            pass

        # Move Pieces
        self.chessboard[q][p] = self.chessboard[y][x]
        self.chessboard[y][x] = None

    def reset(self):
        line1 = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        countx = 1
        self.__init__()
        for i in line1:
            self.place(i(True),(countx,1))
            self.place(i(False),(countx,8))
            countx += 1
        for i in range(1,9):
            self.place(Pawn(True),(i,2))
            self.place(Pawn(False),(i,7))


    def start(self):
        # Starts a game (i.e. turns and stuff)
        self.reset()
        # Waits for white to make a move
        # white.move()
        while True:

            self.__str__()
            playerTurn = True
            while playerTurn:
                choicex = input("Select the x coordinate of a piece to move: ")
                choicey = input("Select the y coordinate of a piece to move: ")
                movexy = (int(choicex),int(choicey))
                piece = self.get(movexy)
                if piece != None:
                    if piece.color == self.turn:
                        # Show valid moves

                        # Move Piece
                        choicex = input("Select the new x coordinate of a piece to move: ")
                        choicey = input("Select the new y coordinate of a piece to move: ")
                        newmovexy = (int(choicex),int(choicey))
                        self.move(movexy, newmovexy)
                        #Change turn
                        print("Next players turn")
                        playerTurn = False
                        self.turn = not self.turn
                    else:
                        print("Not your piece!")
                else:
                    print("No piece selected.")



            # Are they in check?
            # Has someone won?

            # Waits for black to make a move
            # black.move()

            # Are they in check?
            # Has someone won?
