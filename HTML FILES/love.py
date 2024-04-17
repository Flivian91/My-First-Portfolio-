from turtle import *
import time
from tkinter import*
from tkinter import ttk

class Bt():
    def __init__(self, root):
        self.root = root
        self.root.title("Button Clicked Display I Love You")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        btn = ttk.Button(self.root, text="Click Me!", command=self.clicked)
        btn.pack()

    def clicked(self):
                
        begin_fill()
        pensize(3)
        left(50)
        forward(133)
        circle(50, 200)
        right(140)
        circle(50,200)
        forward(133)
        #time.sleep(3)
        color("red")
        end_fill()
        Label(self.root, text="I Love you!!").pack()





if __name__ == "__main__":
    root = Tk()
    Bt(root)
    root.mainloop()