from tkinter import *


class UserInterface:
    def __init__(self):
        # --------------------------Config--------------------------#
        self.root = Tk()
        self.root.config(height=650, width=1200, bg="black")
        # --------------------------Frames--------------------------#
        # frame for the canvas
        self.frame1 = Frame(self.root, bg="black", width=650, height=1200)
        self.frame1.pack()
        # frame for top 25 company names or tickers w/ market cap under 3b
        self.frame2 = Frame(self.root, bg="red", width=120, height=600)
        self.frame2.place(x=10, y=10)
        # frame for relevant articles list
        self.frame3 = Frame(self.root, bg="blue", width=120, height=600)
        self.frame3.place(x=135, y=10)
        # frame for scrolling breaking news about companies in top 3
        self.frame4 = Frame(self.root, bg="green", width=1150, height=30)
        self.frame4.place(x=10, y=615)
        # frame for top 3
        self.frame5 = Frame(self.root, bg="orange", width=500, height=150)
        self.frame5.place(x=650, y=10)
        # frame for article reader (note to self: remember the text width for wrapping capabilities)
        self.frame6 = Frame(self.root, bg="yellow", width=600, height=400)
        self.frame6.place(x=550, y=175)
        # --------------------------Canvas--------------------------#
        self.bg_img = PhotoImage(file="background_image.png")
        self.canvas1 = Canvas(self.frame1, height=650, width=1200, bg="black")
        self.canvas1.grid(column=1, row=1)
        self.canvas1.create_image(600, 325, image=self.bg_img)



        # --------------------------Labels--------------------------#
        # TODO: CREATE LABEL FOR TOP 25 COMPANIES (TIE TO FRAME1) (COL=0, ROW=0)
        # TODO: CREATE LABEL FOR TOP NEWS ARTICLES (TIE TO FRAME2)  (COL=0, ROW=0)
        # TODO: CREATE LABEL FOR TOP NEWS ARTICLES (TIE TO FRAME2)  (COL=0, ROW=0)

        # TODO: FIGURE OUT SCROLLING TEXT FOR FRAME 4 (THINK SNAKE GAME BUT MOVING TEXT)


        # --------------------------Buttons--------------------------#
        # TODO: CREATE BUTTON FOR ADD TO TOP 3 (TIE TO FRAME5) (COL=0, ROW=0)
        # TODO: CREATE BUTTON FOR REMOVE FROM TOP 3 (TIE TO FRAME5) (COL=1, ROW=0)

        # --------------------------ListBoxes--------------------------#
        # TODO: CREATE LISTBOX FOR TOP 25 COMPANIES (TIE TO FRAME1) (COL=0, ROW=1, MAY NEED ROWSPAN)
        # TODO: CREATE LISTBOX FOR TOP NEWS ARTICLES (TIE TO FRAME2)  (COL=0, ROW=1, MAY NEED ROWSPAN)
        # TODO: CREATE LISTBOX FOR TOP 3 COMPANIES (TIE TO FRAME5) (COL=0, ROW=1)
        # TODO: CREATE LISTBOX FOR TOP 3 NEWS ARTICLES (TIE TO FRAME5)  (COL=1, ROW=1)

        # --------------------------TEXTBOX--------------------------#
        # TODO: CREATE A TEXT BOX (WE COULD EITHER USE A MULTI LINE TEXT ENTRY) OR (WE COULD USE A CANVAS.CREATE_TEXT)
        # TODO: TIE THIS TO FRAME6 OR GET RID OF FRAME6 IF WE USE CANVAS.CREATE_TEXT




        self.root.mainloop()