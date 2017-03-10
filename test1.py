import tkinter as tk
from tkinter import ttk # label tool

def main():
    win = tk.Tk()
    win.title('Python GUI')
#    win.resizable(0,0)

# Adding a label
    #ttk.Label(win, text='A Label').grid(column=0, row=0)
    aLabel = ttk.Label(win, text='A Label').grid(column=0, row=0)

    def clickMe():
        #action.configure(text='** I have been clicked')
        action.configure(text='hello ' + name.get() + ' ' + numberChosen.get())
       # aLabel.configure(foreground='red')

    # Adding a Button
    action = ttk.Button(win, text='Click Me!', command=clickMe)
    action.grid(column=2,row=1)
    ttk.Label(win, text='Enter a name:').grid(column=0,row=0)

    name = tk.StringVar()
    nameEntered = ttk.Entry(win, width=12, textvariable=name)
    nameEntered.grid(column=0, row=1)
#    nameEntered.focus()

# Combo Box
    ttk.Label(win, text='Choose a number:').grid(column=1, row=0)
    number = tk.StringVar()
    numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
    numberChosen['values'] = (1, 2, 4, 10, 100)
    numberChosen.grid(column=1, row=1)
    numberChosen.current(0)

# Create a check button with different initial states
    chVarDis = tk.IntVar()
    check1 = tk.Checkbutton(win, text='Disable', variable=chVarDis, state='disabled')
    check1.select()
    check1.grid(column=0, row=4, sticky=tk.W)
    chVarUn = tk.IntVar()
    check2 = tk.Checkbutton(win, text='UnChecked', variable=chVarUn)
    check2.deselect()
    check2.grid(column=1, row=4, sticky=tk.W)

    chVarEn = tk.IntVar()
    check3 = tk.Checkbutton(win, text='Enabled', variable=chVarEn)
    check3.select()
    check3.grid(column=2, row=4, sticky=tk.W)
     
    


    win.mainloop()

if __name__ == '__main__':
    main()
