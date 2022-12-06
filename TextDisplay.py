import tkinter as tk
f = open("Fuel.txt", "r") 
textArray = f.readlines()
index = int(textArray[0])
lines = textArray[1:]


root = tk.Tk()
deli = 200           
svar = tk.StringVar()
labl = tk.Label(root, textvariable=svar, height=1000, width=1000,
                fg='hot pink', bg='lavender', anchor='center', font=('Courier 100'))
root.attributes('-fullscreen', True)


def shif():
    shif.msg = shif.msg[1:] + shif.msg[0]
    svar.set(shif.msg)
    root.after(deli, shif)
    print("Rotating")


shif.msg = lines[index]
shif()
labl.pack()
result = root.destroy
root.after(6000, result)   # Run for 8 seconds
root.mainloop()
print("Terminated")
