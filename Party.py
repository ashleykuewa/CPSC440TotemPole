from tkinter import *
import time
import random


tk = Tk()
canvas = Canvas(tk, width=1500, height=900, background="grey")
canvas.pack()

def xy(event):
    xm, ym = event.x, event.y

def callback(event):
    if True:
        print("clicked2")
        # 'solve' is used here to stop the after... methods.
        tk.quit()
def task():
    w=random.randint(1,1000)
    h=random.randint(1,1000)
    canvas.create_rectangle(w,h,w+150,h+150)

    canvas.bind("<Button-1>",callback)
    solve = tk.after(1000,task)
# above and below tk.after is set to 'solve' a variable.          
solve = tk.after(1000,task)

tk.mainloop()
print("done")
