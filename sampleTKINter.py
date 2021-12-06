import tkinter
from tkinter import*
from tkinter.ttk import*
from tkinter import messagebox
window = tkinter.Tk()
window.title("GUI")

#HEllo
#label=tkinter.Label(window,text="Hello").pack()

#Siddhesh
#l1=tkinter.Label(window,text="SIddhesh",font= ("Arial",20))
#l1.grid(column=0,row=0)


#Geometry
#window.geometry('350*200')
#l1.grid(column=0,row=0)

#BUtton
#bt=tkinter.Button(window,text='Enter',bg='orange',fg='black')
#bt.grid(column=1,row=0)

'''button with command
def clicked():
    l1.configure(text='Button was clicked')
bt=tkinter.Button(window,text='Enter',bg='orange',fg='black',command=clicked)
bt.grid(column=1,row=0)
'''

#Entry
'''
txt=tkinter.Entry(window,width=10)
txt.grid(column=1,row=0)

def clicked():
    res='Welcome to '+txt.get()
    l1.configure(text=res)
bt=tkinter.Button(window,text='Enter',command=clicked)
bt.grid(column=2,row=0)'''

#Combobox
'''
combo=Combobox(window)
combo['values']=(1,2,3,4,5,'Text')
combo.current(3)
combo.grid(column=0,row=0)'''

#checkbutton
'''
chk_state=tkinter.BooleanVar()
chk_state.set(True)
chk=Checkbutton(window,text='select',var=chk_state)
chk.grid(column=0,row=0)'''

#RAdiobutton
'''
rad1=Radiobutton(window,text='Python',value=1)
rad2=Radiobutton(window,text='Java',value=2)
rad3=Radiobutton(window,text='Scala',value=3)
rad1.grid(column=0,row=0)
rad2.grid(column=1,row=0)
rad3.grid(column=2,row=0)'''


#MessageBox
def clicked():
    messagebox.showinfo('Message title','Message content')
btn=Button(window,text='Enter',command=clicked)
btn.pack()

window.tkinter.mainlooop()
