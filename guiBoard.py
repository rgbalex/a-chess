from tkinter import *
from board import Board

class GameWindow():
    """docstring for GameWindow."""

    def __init__(self):

        #board setup
        self.chessboard = Board()


        # tkinter setup
        self.win = Tk()
        self.win.title("a-chess-game")
        self.win.geometry("1000x1000")
        # self.win.resizable(False,False)
        self.win.minsize(900,910)

        frame = Frame(self.win)
        Grid.rowconfigure(self.win, 0)
        Grid.columnconfigure(self.win, 0)
        frame.grid(row=0, column=0)

        self.grid = Frame(frame)
        self.grid.grid(column=0, row=1)
        Grid.rowconfigure(frame, 1)
        Grid.columnconfigure(frame, 0)

        frame.place(anchor="c", relx=.5, rely=.5)

        headerLabel = Label(frame, text="Chess")
        headerLabel.grid(column=0, row=0)
        startButton = Button(frame, text="Start", command=self.chessboard.start)
        startButton.grid(column=1, row=0)
        refreshButton = Button(frame, text="Refresh", command=self.refresh)
        refreshButton.grid(column=2, row=0)

        color = True
        # Moved out of for loop as buttons became unresponsive as image was destroyed.
        pixel = PhotoImage(width=1, height=1)

        for i in range(8):
            for j in range(8):
                button = Button(self.grid)
                # button.config(state=NORMAL,image = pixel, height = 100, width = 100, bg=("white" if color else "black"), fg=("white" if color else "black"))
                button.config(state=NORMAL, text="", height = 5, width = 10, bg=("white" if color else "black"), fg="#e67300")
                button.grid(column=j, row=i)
                color = not color
            color = not color

        self.chessboard.start()
        self.refresh()

        self.win.mainloop()

    def refresh(self):
        loading = self.chessboard.chessboard
        for i in range(8):
            for j in range(8):
                # https://stackoverflow.com/questions/8369560/finding-widgets-on-a-grid-tkinter-module
                if loading[i][j].__class__.__name__ != "NoneType":
                    self.grid.grid_slaves(column=j, row=i)[0].config(text=loading[i][j].__class__.__name__+str(loading[i][j].color))
                else:
                    self.grid.grid_slaves(column=j, row=i)[0].config(text=" ")
