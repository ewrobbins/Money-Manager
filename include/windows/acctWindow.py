import Tkinter as tk
from Tkinter import *
import tkMessageBox
import Tkinter as tk
GEOMETRY='800x250+300+300'
def createAcctWindow(ctrl):
   
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



   topLabel = tk.Label(topFrame, text = "Account Management", font = "Helvetica 16 bold italic")
   topLabel.pack(side = tk.TOP)
   topLabel.config(bg='#b0c4de', width = 20)

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
   acctNameLabel = tk.Label(upperTopLeftFrame, text = "Account Name:")
   acctNameLabel.pack(side = tk.LEFT, pady = 5)
   acctNameLabel.config(bg='#b0c4de', width = 13)
   acctNameEntry = tk.Entry(upperTopLeftFrame)
   acctNameEntry.config(width=30, font=labelFont)
   acctNameEntry.pack(side=tk.LEFT, pady = 5)
   acctNameEntry.focus()

   lowerTopLeftFrame = tk.Frame(topLeftFrame)
   lowerTopLeftFrame.pack(side=tk.BOTTOM)
   lowerTopLeftFrame.config(bg='#b0c4de')
   balanceFrame = tk.Frame(lowerTopLeftFrame)
   balanceFrame.pack(side=tk.TOP)
   balanceFrame.config(bg='#b0c4de')
   balanceLabel = tk.Label(balanceFrame, text = "Starting Balance:")
   balanceLabel.pack(side = tk.LEFT, pady = 5)
   balanceLabel.config(bg='#b0c4de', width = 13)
   balanceEntry = tk.Entry(balanceFrame)
   balanceEntry.config(width=30, font=labelFont)

   balanceEntry.pack(side=tk.LEFT, pady = 5)
   balanceEntry.focus()

   # category entry and label
   #catFrame = tk.Frame(lowerTopLeftFrame)
   #catFrame.pack(side=tk.TOP)
   #catFrame.config(bg='#b0c4de', width=13)
   #catLabel = tk.Label(catFrame, text = "Category:")
   #catLabel.pack(side = tk.LEFT, pady = 5)
   #catLabel.config(bg='#b0c4de', width = 13)
   #catEntry = tk.Entry(catFrame)
   #catEntry.config(width=30, font=labelFont)
   #catEntry.pack(side=tk.BOTTOM)
   #catEntry.pack(side=tk.LEFT, pady = 5)
   #catEntry.focus()

  

   acctFrame = tk.Frame(lowerTopLeftFrame)
   acctFrame.pack(side = tk.TOP)
   acctFrame.config(bg='#b0c4de')
   acctLabel = tk.Label(acctFrame, text = "Account Type:")
   acctLabel.pack(side = tk.LEFT, pady = 5)
   acctLabel.config(bg='#b0c4de', width = 13)

   acctType = StringVar(acctFrame)
   acctType.set("Select An Account Type")
   option = OptionMenu(acctFrame, acctType, "Checking Account", "Savings Account", 
      "Retirement Account")
   option.config(width = 43)
   option.pack(pady = 5)
   
   mainAccount = IntVar()
   C1 = Checkbutton(acctFrame, text = "Main Account?" , variable = mainAccount, onvalue = 1,
         offvalue = 0, height = 1, width = 10)
   C1.config(bg = '#b0c4de')
   C1.pack(side=tk.BOTTOM,pady = 6 )

   def commitAndClose():
      # to-do: add error checking
      list = []
      list.append(acctNameEntry.get())
      list.append(acctType.get())
      list.append(balanceEntry.get())
      list.append(mainAccount.get())

      ctrl.insertNewAccount(list)
      tw.destroy()

   okButton = tk.Button(buttonFrame, text='OK', command=commitAndClose)
   okButton.config(relief=tk.RAISED, bd=4, height = 4, width = 12)
   okButton.pack(side=tk.LEFT, padx=7)

   cancel = tk.Button(buttonFrame, text='CANCEL', command=tw.destroy)
   cancel.config(relief=tk.RAISED, bd=4, height = 4, width = 12)
   cancel.pack(side=tk.LEFT, padx=7)

