import tkinter as tk

f = open("Fuel.txt", "r")
textArray = f.readlines()
index = int(textArray[0])
lines = textArray[1:]


root = tk.Tk()
deli = 300           # milliseconds of delay per character
svar = tk.StringVar()
labl = tk.Label(root, textvariable=svar, height=100, width=100, fg='pink', bg='black', anchor='center', font=('Courier 400') )

def shif():
    shif.msg = shif.msg[1:] + shif.msg[0]
    svar.set(shif.msg)
    root.after(deli, shif)


shif.msg = lines[index]
shif()
labl.pack()
root.mainloop()