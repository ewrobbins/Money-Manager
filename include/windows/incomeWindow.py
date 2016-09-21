from Tkinter import *
import tkMessageBox
import Tkinter as tk
GEOMETRY='800x350+300+300'

def createIncomeWindow(ctrl):

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

   topLabel = tk.Label(topFrame, text = "Add Income or Funds", font = "Helvetica 16 bold italic")
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
   sourceNameLabel = tk.Label(upperTopLeftFrame, text = "Job Name:")
   sourceNameLabel.pack(side = tk.LEFT, pady = 5)
   sourceNameLabel.config(bg='#b0c4de', width = 18)
   sourceEntry = tk.Entry(upperTopLeftFrame)
   sourceEntry.config(width=30, font=labelFont)
   sourceEntry.pack(side=tk.LEFT, pady = 5, padx = 10)
   sourceEntry.focus()

   lowerTopLeftFrame = tk.Frame(topLeftFrame)
   lowerTopLeftFrame.pack(side=tk.TOP)
   lowerTopLeftFrame.config(bg='#b0c4de')
   paydayFrame = tk.Frame(topLeftFrame)
   paydayFrame.pack(side=tk.TOP)
   paydayFrame.config(bg='#b0c4de')
   paydayLabel = tk.Label(paydayFrame, text = "Payday (Day of month):")
   paydayLabel.pack(side = tk.LEFT, pady = 5)
   paydayLabel.config(bg='#b0c4de', width = 18)
   paydayEntry = tk.Entry(paydayFrame)
   paydayEntry.config(width=30, font=labelFont)
   paydayEntry.pack(side=tk.LEFT, pady = 5)
   paydayEntry.focus()

   amtFrame = tk.Frame(topLeftFrame)
   amtFrame.pack(side = tk.TOP)
   amtFrame.config(bg='#b0c4de')
   amtLabel = tk.Label(amtFrame, text = "Amount:")
   amtLabel.pack(side = tk.LEFT, pady = 5)
   amtLabel.config(bg='#b0c4de', width = 18)
   amtEntry = tk.Entry(amtFrame)
   amtEntry.config(width=30, font=labelFont)
   amtEntry.pack(side=tk.BOTTOM)
   amtEntry.pack(side=tk.LEFT, pady = 5, padx = 10)
   amtEntry.focus()

   depositAcctFrame = tk.Frame(topLeftFrame)
   depositAcctFrame.pack(side = tk.TOP)
   depositAcctFrame.config(bg='#b0c4de')
   depositAcctLabel = tk.Label(depositAcctFrame, text = "Deposit into Account:")
   depositAcctLabel.pack(side = tk.LEFT, pady = 5, padx = 5)
   depositAcctLabel.config(bg='#b0c4de', width = 18)
   
   depAcct = StringVar(depositAcctFrame)
   depAcct.set("Select an Account")
   depOption = apply(OptionMenu, (depositAcctFrame, depAcct) + 
      tuple(ctrl.getIndexedAccountsDict().keys()))
   depOption.config(width = 36)
   depOption.pack(pady = 5)
   
   '''
   acctFrame = tk.Frame(topLeftFrame)
   acctFrame.pack(side = tk.TOP)
   acctFrame.config(bg='#b0c4de')
   acctLabel = tk.Label(acctFrame, text = "Current Jobs:")
   acctLabel.pack(side = tk.LEFT, pady = 5)
   acctLabel.config(bg='#b0c4de', width = 18)

   
   currSources = StringVar(acctFrame)
   currSources.set("Select A Job")
   curSrcOption = apply(OptionMenu, (acctFrame, currSources) + 
      tuple(ctrl.getIndexedIncomesDict().keys()))
   curSrcOption.config(width = 36)
   curSrcOption.pack(pady = 5, padx = 7)
   '''

   def commitAndClose():
      # to-do: add error checking
      list = []
      list.append(sourceEntry.get())
      list.append(paydayEntry.get())
      list.append(amtEntry.get())
      list.append(ctrl.getIndexedAccountsDict()[depAcct.get()])

      ctrl.insertNewIncome(list)
      tw.destroy()

   okButton = tk.Button(buttonFrame, text='OK', command=commitAndClose)
   okButton.config(relief=tk.RAISED, bd=4, height = 4, width = 12)
   okButton.pack(side=tk.LEFT, padx=7)

   cancel = tk.Button(buttonFrame, text='CANCEL', command=tw.destroy)
   cancel.config(relief=tk.RAISED, bd=4, height = 4, width = 12)
   cancel.pack(side=tk.LEFT, padx=7)

