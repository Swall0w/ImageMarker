from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import os
import glob
import random
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter.filedialog import askopenfilename, askdirectory
from PIL import Image, ImageTk

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

class ImageMarker(Frame):
    def __init__(self):
        Frame.__init__(self)
        #self.width=800
        #self.height=600
        self.width=800
        self.height=600
        self.margin=200
# Top Frame setting
        self.master.title('Image Marker')
        #self.master.geometry('800x600')
        self.master.geometry(str(self.width)+'x'+str(self.height))
        self.master.configure(background='grey')
        self.master.resizable(width= False, height = False)
# Menu Bar setting
        self.menuBar = Menu(self.master)
        self.master.config(menu=self.menuBar)
        self.fileMenu = Menu(self.menuBar,tearoff=0)
        self.fileMenu.add_command(label='Open image', command=self._open_file)
        self.fileMenu.add_command(label='Open dir', command=self._open_dir)
        self.fileMenu.add_command(label='Exit', command=self._quit)
        self.menuBar.add_cascade(label='File', menu=self.fileMenu)
        self.helpMenu = Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label='About', command=self._msgBox)
        self.menuBar.add_cascade(label='Help', menu=self.helpMenu)
# Plot Area setting
        self.filename=None
        self.canvas = tkinter.Canvas(self.master,width=str(self.width-self.margin),height=self.height)
        self.canvas.grid(row=0,column=0)

# KeyBinding
        self.canvas.bind('<Motion>', self.motion)

    def _plot_image(self):
        print(self.filename)
        self.image = Image.open(self.filename)
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0,0, image=self.photo, anchor='nw')
    def motion(self,event):
        self.x,self.y = event.x, event.y
        print(self.x,self.y)
    def _quit(self):
        answer = mBox.askyesno('Python Message','Are you sure to quit?')
        if answer is True:
            self.master.quit()
            self.master.destroy()
            exit()
    def _msgBox(self):
        mBox.showinfo('Python Message Info Box','A Python GUI created using tkinter:\n The year is 2017.')
    def _load_image(self):
        pass
    def _open_file(self):
        self.filename = askopenfilename(initialdir=os.getcwd(),filetypes=(('Image File','*.jpg'),('All Files','*.*')),title='Choose a file')
        self._plot_image()
    def _open_dir(self):
        name = askdirectory(initialdir=os.getcwd(),title='Choose a image directory')
        print(name)
        print(os.listdir(name))

def func1():
#    def _quit():
#        answer = mBox.askyesno('Python Message','Are you sure to quit?')
#        if answer is True:
#            win.quit()
#            win.destroy()
#            exit()
#        else:
#            pass
#
#    def _msgBox():
#        mBox.showinfo('Python Message Info Box','A Python GUI created using tkinter:\n The year is 2017.')
#    def _load_image():
#        pass
#    def _open_file():
#        name = askopenfilename(initialdir=os.getcwd(),filetypes=(('Text File','*.txt'),('All Files','*.*')),title='Choose a file')
#        print(name)
#        try:
#            with open(name,'r') as f:
#                print(f.read())
#        except:
#            print('No file exists')
#    def _open_dir():
#        name = askdirectory(initialdir=os.getcwd(),title='Choose a image directory')
#        print(name)
#        print(os.listdir(name))
## Create instance
#    win = tk.Tk()
#    win.geometry('800x600')
#    win.title('Python GUI')
#    win.configure(background='grey')

# We are creating a container frame to hold all other widgets
    monty = ttk.LabelFrame(win,text=' Monty Python ')
    monty.grid(column=0, row=0)

# Modify adding a Label
    aLabel = ttk.Label(monty, text='A Label')
    ttk.Label(monty, text='Enter a name:').grid(column=0, row=0, sticky='W')

    name1 = tk.StringVar()
    nameEnterd = ttk.Entry(monty, width=12, textvariable=name1)
    nameEnterd.grid(column=0, row=1, sticky=tk.W)
    nameEnterd.focus()

    menuBar = Menu(win)
    win.config(menu=menuBar)

    fileMenu = Menu(menuBar,tearoff=0)
    fileMenu.add_command(label='Open image', command=_open_file)
    fileMenu.add_command(label='Open dir', command=_open_dir)
    #fileMenu.add_separator()
    fileMenu.add_command(label='Exit', command=_quit)
    menuBar.add_cascade(label='File', menu=fileMenu)

    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label='About', command=_msgBox)
    menuBar.add_cascade(label='Help', menu=helpMenu)


    win.mainloop()
if __name__ == '__main__':
    ImageMarker().mainloop()
#    root.resizable(width =  True, height = True)
#    from tkinter import scrolledtext
#    def clickMe():
#        action.configure(text='ohhhhh' + name.get())
##        aLabel.configure(foreground='red')
#
#    win = tk.Tk()
#    win.title('Image Label')
#    #ttk.Label(win, text='A Label').grid(column=0,row=0)
#    aLabel = ttk.Label(win, text='A Label')
#    aLabel.grid(column=0, row=0)
#
#    action = ttk.Button(win, text='Click Me.',command=clickMe)
#    action.grid(column=2, row=1)
#
#    name = tk.StringVar()
#    nameEnterd = ttk.Entry(win, width=12, textvariable=name)
#    nameEnterd.grid(column=0, row=1)
#    nameEnterd.focus()
#
#    bLabel = ttk.Label(win, text='Choose a number:').grid(column=1, row=0)
#    number = tk.StringVar()
#    numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
#    numberChosen['values'] = (1,2,3,54,100)
#    numberChosen.grid(column=1, row=1)
#    numberChosen.current(0)
#
#    scrolW = 30
#    scrolH = 3
#    scr = scrolledtext.ScrolledText(win,width=scrolW, height=scrolH,wrap=tk.WORD)
#    scr.grid(column=0, columnspan=3)
#
## Create a container to hold labels
#    labelsFrame = ttk.LabelFrame(win,text=' Labels in a Frame')
#    labelsFrame.grid(column=0,row=7,padx=20, pady=40)
#    ttk.Label(labelsFrame, text='Label1').grid(column=0, row=0)
#    ttk.Label(labelsFrame, text='Label1').grid(column=1, row=0)
#    ttk.Label(labelsFrame, text='Label1').grid(column=2, row=0)
#
#    win.resizable(0,0)
#    win.mainloop()
