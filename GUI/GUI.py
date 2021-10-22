import tkinter as tk
import random as random
import pygame as pg
import sys
import os
sys.path.append("C:/Users/Markus/Desktop/Elsys/Github/div-master/GUI")
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

c1 = "#66545e"
c2 = "#a39193"
c3 = "#aa6f73"
f = ("Times", 56, "bold")
fr1 = ("Times", 12)

# Root
root = tk.Tk()
root.title("Yes | No ")
root.resizable(0, 0)
pg.mixer.init()

Number = tk.IntVar()
ActualNumber = tk.IntVar()
Number.set(random.randint(0, 10))
ActualNumber.set(random.randint(0, 10))
text1 = tk.StringVar()
text1.set("Choose one of the following options")
yes = tk.PhotoImage(file="C:/Users/Markus/Desktop/Elsys/Github/div-master/GUI/Yes.png")
no = tk.PhotoImage(file="C:/Users/Markus/Desktop/Elsys/Github/div-master/GUI/No.png")

# Canvas
canvas = tk.Canvas(root, height=600, width=400, bg=c1)
canvas.pack()

# Frames
f3 = tk.Frame(canvas, bg=c3)
f3.place(relx=0.1, rely=0.05)
l1 = tk.Label(f3, text="Is the number equal to", bg=c3, font=fr1, fg=c1)
l1.place(relx=0.5, rely=0, anchor='center')
l1.pack(side=tk.LEFT, pady=10)
l2 = tk.Label(f3, textvariable=ActualNumber, bg=c3, font=fr1, fg=c1)
l2.place(relx=0.5, rely=0, anchor='center')
l2.pack(side=tk.LEFT, pady=10)
l3 = tk.Label(f3, text="?", bg=c3, font=fr1, fg=c1)
l3.place(relx=0.5, rely=0, anchor='center')
l3.pack(side=tk.LEFT, pady=10)

f0 = tk.Frame(canvas, height=320, width=320, bg=c3)
f0.place(relx=0.1, rely=0.18)
l0 = tk.Label(f0, fg=c1, height=3, width=7,
              font=f, textvariable=Number, bg=c3)
l0.pack()

f4 = tk.Frame(canvas, bg=c3)
f4.place(relx=0.1, rely=0.67)
l4 = tk.Label(f4, textvariable=text1, bg=c3, font=fr1, fg=c1)
l4.pack(side=tk.LEFT, pady=10)


def Yes():
    n1, n2 = ActualNumber.get(), Number.get()
    if(n1 == n2):
        text1.set("Well done!")
        pg.mixer.music.load("C:/Users/Markus/Desktop/Elsys/Github/div-master/GUI/TaDah.mp3")
        pg.mixer.music.play(loops=0)
        pg.mixer.music.set_volume(0.2)
    else:
        text1.set("No! Try again")
    Number.set(random.randint(0, 10))
    ActualNumber.set(random.randint(0, 10))


f1 = tk.Frame(canvas, height=100, width=100, bg="white", cursor="gumby")
f1.place(relx=0.1, rely=0.8)
b1 = tk.Button(f1, bg=c2, activebackground=c3,
               image=yes, height=80, width=120, command=Yes)
b1.pack()


def No():
    Number.set(random.randint(0, 10))
    text1.set("What about now?")


f2 = tk.Frame(canvas, height=100, width=100, bg="white", cursor="gobbler")
f2.place(relx=0.60, rely=0.8)
b2 = tk.Button(f2, bg=c2, activebackground=c3,
               image=no, height=80, width=120, command=No)
b2.pack()

root.mainloop()
