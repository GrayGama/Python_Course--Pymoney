
# ************    Week 14:    ****************# 
import sys
import datetime 
from tkinter import *
from tkinter import ttk
from pyrecord import *
from pycategory import * 

categories = Categories()
records = Records()

#     elif command == 'delete':
#         records.delete()     
#         records.save()
#         break

#GUI:
temp_reclst = []
flag = False

def moneyEntry():
    records.add(money_var.get(), categories, 1) 
    money_entry.delete(0, END)
    
    total = Label(frame, text=f'Now you have {records._wallet} dolars')
    total.grid(column=0, row=9, columnspan=3)

def addRecord():
    temp_reclst.append(dt_entry.get())
    
    temp_reclst.append(clicked.get())
    temp_reclst[1] = temp_reclst[1].replace('-', '').strip()
    
    temp_reclst.append(dscp_entry.get())
    dscp_entry.delete(0, END)
    
    temp_reclst.append(amnt_entry.get())
    amnt_entry.delete(0, END)
    
    records.add(temp_reclst, categories)
    elem = records._record_lst[-1]
    vw_lsbx.insert(END, '{:<20}{:<30s}{:<40}{:<50}'.format(elem[0], elem[1], elem[2], elem[3]))
    temp_reclst.clear()
    
    total = Label(frame, text=f'Now you have {records._wallet} dolars')
    total.grid(column=0, row=9, columnspan=3)
    
def findButton():
    target_categories = categories.find_subcategories(fd_entry.get())
    records.find(target_categories)
    #clear the box list
    for elem in records._record_lst:
        vw_lsbx.delete(0, END)
    # print the records on the box list
    for elem in records._filtered_records:
        vw_lsbx.insert(END, '{:<20}{:<30s}{:<40}{:<50}'.format(elem[0], elem[1], elem[2], elem[3]))

def clearButton(): 
    fd_entry.delete(0, END)
    for elem in records._record_lst:
        vw_lsbx.delete(0, END)
    for elem in records._record_lst:
        vw_lsbx.insert(END, '{:<20}{:<30s}{:<40}{:<50}'.format(elem[0], elem[1], elem[2], elem[3]))

def Delete():
    selection = vw_lsbx.curselection()
    records.delete(selection[0])
    
    for elem in records._record_lst:
        vw_lsbx.delete(0, END)
    for elem in records._record_lst:
        vw_lsbx.insert(END, '{:<20}{:<30s}{:<40}{:<50}'.format(elem[0], elem[1], elem[2], elem[3]))
    
    total = Label(frame, text=f'Now you have {records._wallet} dolars')
    total.grid(column=0, row=9, columnspan=3)
def saveFile():
    records.save()
    
#>>initialization of gui  
root = Tk()
root.title('Pymoney')
#Frame where all the buttons and boxes are going to be
frame = Frame(root, width=810, height=255)
frame.grid_propagate(0)
frame.grid()

#>>big box (.Listbox)
vw_lsbx = Listbox(frame, width=80, bd=5)
vw_lsbx.grid(column=0, row=1, rowspan=8, columnspan=4)

# temptt = records._wallet 
for elem in records._record_lst:
    vw_lsbx.insert(END, '{:<20}{:<30s}{:<40}{:<50}'.format(elem[0], elem[1], elem[2], elem[3]))
    records._wallet += int(elem[3])

#>>labels1 (top)
fd = Label(frame, text="Find category", pady=10, padx=10).grid(column=0, row=0)
fd_entry = Entry(frame, width=45, bd=2)
fd_entry.grid(column=1, row=0)
#find the target category
fd_btt = Button(frame, text='Find',  width=6, command=findButton)
fd_btt.grid(column=2, row=0)  

clr_btt = Button(frame, text='Clear',  width=6, command=clearButton)
clr_btt.grid(column=3, row=0)

#>>labels2(top left)
money_var = StringVar()

money = Label(frame, text="Initial money").grid(column=4, row=1)
money_entry = Entry(frame, textvariable=money_var, width=35, bd=2)
money_entry.grid(column=5, row=1)

upd_btt = Button(frame, text='Update', command=moneyEntry,  width=8)
upd_btt.grid(column=5, row=3, sticky=E)
               
#>>labels3(middle to buttom left)
sp = Label(frame, text='')
sp.grid(column=4, row=4)

dt = Label(frame, text="Date", justify=CENTER)
dt.grid(column=4, row=5)
dt_entry = Entry(frame, width=35, bd=2)
dt_entry.insert(0, str(datetime.date.today()))
dt_entry.grid(column=5, row=5)   
 
catg = Label(frame, text="Category", justify=CENTER)
catg.grid(column=4, row=6)

clicked = StringVar()
catg_entry = ttk.OptionMenu(frame, clicked, 'Please select the record category', '- expense', '  - food', '    - meal', '    - snack', '    - drink', '  - transportation', '    - bus', '    - railway', '- income', '  - salary', '  - bonus')
# catg_entry = Entry(frame, width=35, bd=2)
catg_entry.grid(column=5, row=6)  #<-- need txo change

dscp = Label(frame, text="Description", justify=CENTER)
dscp.grid(column=4, row=7)
dscp_entry = Entry(frame, width=35, bd=2)
dscp_entry.grid(column=5, row=7)
   
amnt = Label(frame, text="Amount", justify=CENTER)
amnt.grid(column=4, row=8)
amnt_entry = Entry(frame, width=35, bd=2)
amnt_entry.grid(column=5, row=8)   

add_btt = Button(frame, text='Add record',  command=addRecord, width=10)
add_btt.grid(column=5, row=9, sticky=E)  #add record button

#>>label4(buttom)

total = Label(frame, text='Now you have {} dolars'.format(records._wallet))
total.grid(column=0, row=9, columnspan=3)

del_btt = Button(frame, text='Delete', command=Delete,  width=8)
del_btt.grid(column=3, row=9, sticky=E)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=saveFile)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)


root.mainloop()

