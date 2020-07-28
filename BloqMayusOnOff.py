from tkinter import Tk, Label, PhotoImage
from win32api import GetKeyState # pip install pywin32
from win32con import VK_CAPITAL

root = Tk()
root.attributes("-topmost", True)
root.overrideredirect(True)
root.attributes("-transparentcolor", "#F0F0F0")

label = Label(root)
label.pack()

imagen_on = PhotoImage(file="bloq_on.png")
imagen_off = PhotoImage(file="bloq_off.png")

def OnOff():
    estadoBloqMayus = GetKeyState(VK_CAPITAL)
    if estadoBloqMayus == 0:
        label.configure(image=imagen_off)
    elif estadoBloqMayus == 1:
        label.configure(image=imagen_on)
    root.after(1, OnOff)

def mover_root(event):
    root.geometry(f"+{event.x_root}+{event.y_root}")

label.bind("<B1-Motion>", mover_root)

OnOff()

root.mainloop()


