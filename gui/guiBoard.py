from tkinter import *

# tkinter setup
win = Tk()
win.title("a-chess-game")
win.geometry("1000x1000")
# win.resizable(False,False)
win.minsize(900,910)


frame = Frame(win)
Grid.rowconfigure(win, 0)
Grid.columnconfigure(win, 0)
frame.grid(row=0, column=0)


grid = Frame(frame)
grid.grid(column=0, row=1)
Grid.rowconfigure(frame, 1)
Grid.columnconfigure(frame, 0)


frame.place(anchor="c", relx=.5, rely=.5)
header = Label(frame, text="Chess")
header.grid(column=0, row=0)

white = True
# Moved out of for loop as buttons became unresponsive as image was destroyed.
pixel = PhotoImage(width=1, height=1)

for i in range(8):
    for j in range(8):
        button = Button(grid)
        button.config(image = pixel, height = 100, width = 100,bg=("white" if white else "black"))
        button.grid(column=j, row=i)
        white = not white
    white = not white

win.mainloop()
