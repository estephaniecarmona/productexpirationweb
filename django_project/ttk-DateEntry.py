import tkinter  as tk 
from tkcalendar import DateEntry
my_w = tk.Tk()
my_w.geometry("380x200")  
sel=tk.StringVar() 

cal=DateEntry(my_w,selectmode='day',textvariable=sel)
cal.grid(row=1,column=1,padx=20)

def my_upd(*args): 
    l1.config(text=sel.get()) 

l1=tk.Label(my_w,bg='yellow') 
l1.grid(row=1,column=2)

sel.trace('w',my_upd) 
my_w.mainloop()