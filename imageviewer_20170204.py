from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import os
import glob
import random
import tkinter as tk
from tkinter import ttk

class ImageViewer(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.master.title('ImageViewer')
        self.master.resizable(width= False, height = False)
        self.pack(fill=BOTH, expand=1)

        self.filename = 'img.jpg'
        self.image = Image.open(self.filename)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(image=self.photo)
        self.label.image = self.photo
        self.label.pack()

        self.image_dir = ''
        self.image_list = []
        self.anno_dir = ''
        self.anno_list = []

# initialize mouse state
        self.STATE = {}
        self.STATE['click'] = 0
        self.STATE['x'], self.STATE['y'] = 0,0

def main():
    root = Tk()
    tool = ImageViewer(master=root)
#    root.resizable(width =  True, height = True)
    root.mainloop()

class tmp(object):
    def __init__(self,master):
        master.title('Kawaii')
        master.geometry('800x450')

        canvas = tkinter.Canvas(master, width=800,height=450)
        canvas.grid(row=0,column=0)
        self.image = Image.open('img.jpg')
        self.photo = ImageTk.PhotoImage(self.image)
        canvas.create_image(0,0, image=self.photo)

def plotimg():
    root = tkinter.Tk()
    canvas = tmp(root)
    root.mainloop()

if __name__ == '__main__':
    from tkinter import scrolledtext
    def clickMe():
        action.configure(text='ohhhhh' + name.get())
#        aLabel.configure(foreground='red')

    win = tk.Tk()
    win.title('Image Label')
    win.resizable(0,0)
    #ttk.Label(win, text='A Label').grid(column=0,row=0)
    aLabel = ttk.Label(win, text='A Label')
    aLabel.grid(column=0, row=0)

    action = ttk.Button(win, text='Click Me.',command=clickMe)
    action.grid(column=2, row=1)

    name = tk.StringVar()
    nameEnterd = ttk.Entry(win, width=12, textvariable=name)
    nameEnterd.grid(column=0, row=1)
    nameEnterd.focus()

    bLabel = ttk.Label(win, text='Choose a number:').grid(column=1, row=0)
    number = tk.StringVar()
    numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
    numberChosen['values'] = (1,2,3,54,100)
    numberChosen.grid(column=1, row=1)
    numberChosen.current(0)

    scrolW = 30
    scrolH = 3
    scr = scrolledtext.ScrolledText(win,width=scrolW, height=scrolH,wrap=tk.WORD)
    scr.grid(column=0, columnspan=3)

    win.mainloop()
