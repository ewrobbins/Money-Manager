from Tkinter import *
import tkMessageBox
import Tkinter as tk
import datetime
GEOMETRY='800x350+300+300'
def createTransWindow(ctrl):

   list = []

   checkVariable1 = IntVar()

   tw = tk.Toplevel()
   tw.geometry(GEOMETRY)
   tw.resizable(width=False, height=False)
   tw.wm_title("Add or Modify Transactions")
   labelFont = ('georgia', 12,'bold')

   topFrame = tk.Frame(tw)
   topFrame.config(bg='#b0c4de',bd=5)
   topFrame.pack(expand=1,fill=tk.BOTH,side=tk.TOP)

   topLabel = tk.Label(topFrame, text = "Add a purchase ", font = "Helvetica 16 bold italic")
   topLabel.pack(side = tk.TOP)
   topLabel.config(bg='#b0c4de', width = 20)
   
   warnLabel = tk.Label(topFrame, text = "Must have bank account", font = "Helvetica 12 italic")
   warnLabel.pack(side=tk.TOP, pady = 5)
   warnLabel.config(bg='#b0c4de', width = 20)

   topLeftFrame = tk.Frame(topFrame)
   topLeftFrame.config(bg='#b0c4de')
   topLeftFrame.pack(expand=1,side=tk.LEFT, padx = 15)

   topRightFrame = tk.Frame(topFrame)
   topRightFrame.config(bg='#b0c4de')
   topRightFrame.pack(expand=1,side=tk.RIGHT)

   buttonFrame = tk.Frame(topRightFrame)
   buttonFrame.config(bg='#b0c4de')
   buttonFrame.pack(side=tk.BOTTOM, pady = 25)

   upperTopLeftFrame = tk.Frame(topLeftFrame)
   upperTopLeftFrame.pack(side=tk.TOP)
   upperTopLeftFrame.config(bg='#b0c4de')
   nameLabel = tk.Label(upperTopLeftFrame, text = "Transaction:")
   nameLabel.pack(side = tk.LEFT, pady = 5)
   nameLabel.config(bg='#b0c4de', width = 18)
   nameEntry = tk.Entry(upperTopLeftFrame)
   nameEntry.config(width=30, font=labelFont)
   nameEntry.pack(side=tk.LEFT, pady = 5)
   nameEntry.focus()

   lowerTopLeftFrame = tk.Frame(topLeftFrame)
   lowerTopLeftFrame.pack(side=tk.BOTTOM)
   lowerTopLeftFrame.config(bg='#b0c4de')
   dateFrame = tk.Frame(lowerTopLeftFrame)
   dateFrame.pack(side=tk.TOP)
   dateFrame.config(bg='#b0c4de')
   dateLabel = tk.Label(dateFrame, text = "Date (YYYYMMDD):")
   dateLabel.pack(side = tk.LEFT, pady = 5)
   dateLabel.config(bg='#b0c4de', width = 18)
   dateEntry = tk.Entry(dateFrame)
   dateEntry.config(width=30, font=labelFont)
   today = datetime.datetime.today()
   dateEntry.insert(0, datetime.date(today.year, today.month, today.day).strftime('%Y%m%d'))
   dateEntry.pack(side=tk.LEFT, pady = 5)
   dateEntry.focus()

   fromFrame = tk.Frame(lowerTopLeftFrame)
   fromFrame.pack(side=tk.TOP)
   fromFrame.config(bg='#b0c4de')
   fromLabel = tk.Label(fromFrame, text = "From:")
   fromLabel.pack(side = tk.LEFT, pady = 5)
   fromLabel.config(bg='#b0c4de', width = 18)
   fromEntry = tk.Entry(fromFrame)
   fromEntry.config(width=30, font=labelFont)
   fromEntry.pack(side=tk.BOTTOM)
   fromEntry.pack(side=tk.LEFT, pady = 5)
   fromEntry.focus()

   # category entry and label
   catFrame = tk.Frame(lowerTopLeftFrame)
   catFrame.pack(side=tk.TOP)
   catFrame.config(bg='#b0c4de', width=12)
   catLabel = tk.Label(catFrame, text = "Category:")
   catLabel.pack(side = tk.LEFT, pady = 5)
   catLabel.config(bg='#b0c4de', width = 18)
   catEntry = tk.Entry(catFrame)
   catEntry.config(width=30, font=labelFont)
   catEntry.pack(side=tk.BOTTOM)
   catEntry.pack(side=tk.LEFT, pady = 5)
   catEntry.focus()

   amtFrame = tk.Frame(lowerTopLeftFrame)
   amtFrame.pack(side = tk.TOP)
   amtFrame.config(bg='#b0c4de')
   amtLabel = tk.Label(amtFrame, text = "Amount:")
   amtLabel.pack(side = tk.LEFT, pady = 5)
   amtLabel.config(bg='#b0c4de', width = 18)
   amtEntry = tk.Entry(amtFrame)
   amtEntry.config(width=30, font=labelFont)
   amtEntry.pack(side=tk.BOTTOM)
   amtEntry.pack(side=tk.LEFT, pady = 5)
   amtEntry.focus()

   acctFrame = tk.Frame(lowerTopLeftFrame)
   acctFrame.pack(side = tk.TOP)
   acctFrame.config(bg='#b0c4de')
   acctLabel = tk.Label(acctFrame, text = "Account:")
   acctLabel.pack(side = tk.LEFT, pady = 5)
   acctLabel.config(bg='#b0c4de', width = 18)

   acct = StringVar(acctFrame)
   acct.set("Select An Account")
   option = apply(OptionMenu, (acctFrame, acct) + 
      tuple(ctrl.getIndexedAccountsDict().keys()))
   option.config(width = 42)
   option.pack(pady = 5)

   C1 = Checkbutton(lowerTopLeftFrame, text = "Important?" , variable = checkVariable1, onvalue = 1,
         offvalue = 0, height = 1, width = 10)
   C1.config(bg = '#b0c4de')
   C1.pack(side=tk.LEFT,pady = 6 )

   def commitAndClose():
      # to-do: add error checking
      list.append(nameEntry.get())
      list.append(dateEntry.get())
      list.append(fromEntry.get())
      list.append(catEntry.get())
      list.append(checkVariable1.get())
      list.append(float(amtEntry.get()))
      list.append(ctrl.getIndexedAccountsDict()[acct.get()])

      ctrl.insertNewTrans(list)
      tw.destroy()

   okButton = tk.Button(buttonFrame, text='OK', command=commitAndClose)
   okButton.config(relief=tk.RAISED, bd=4, height = 4, width = 12)
   okButton.pack(side=tk.LEFT, padx=7)

   cancel = tk.Button(buttonFrame, text='CANCEL', command=tw.destroy)
   cancel.config(relief=tk.RAISED, bd=4, height = 4, width = 12)
   cancel.pack(side=tk.LEFT, padx=7)

