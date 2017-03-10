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

class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x, self.y = 0,0
    def showtip(self, text):
        'Display text in tooltip window'
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox('insert')
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry('+%d+%d' % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT, background='#ffffe0', relief=tk.SOLID, borderwidth=1,font=('tahoma','8','normal'))
        label.pack(ipadx=1)

def createToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

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

    def _quit():
        answer = mBox.askyesno('Python Message','Are you sure to quit?')
        if answer is True:
            win.quit()
            win.destroy()
            exit()
        else:
            pass

    def _msgBox():
        mBox.showinfo('Python Message Info Box','A Python GUI created using tkinter:\n The year is 2017.')
    def _load_image():
        pass
    def _open_file():
        name = askopenfilename(initialdir=os.getcwd(),filetypes=(('Text File','*.txt'),('All Files','*.*')),title='Choose a file')
        print(name)
        try:
            with open(name,'r') as f:
                print(f.read())
        except:
            print('No file exists')
    def _open_dir():
        name = askdirectory(initialdir=os.getcwd(),title='Choose a image directory')
        print(name)
        print(os.listdir(name))
# Create instance
    win = tk.Tk()
    win.geometry('800x600')
    win.title('Python GUI')
    win.configure(background='grey')

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
