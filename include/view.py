# THIS DISPLAYS IN THE GREEK ALPHABET ON SOME SYSTEMS
# I HAVE NO IDEA WHY

import Tkinter as tk
import ttk
import tkMessageBox
import tkFont
import windows.acctWindow
import windows.billWindow
import windows.goalWindow
import windows.incomeWindow
import windows.transWindow

GEOMETRY='1366x768+10+10'

class View(object):

   def __init__(self, controller):
      self.ctrl = controller
      self.root = tk.Tk()
      self.root.resizable(width=False, height=False)
      self.root.geometry(GEOMETRY)
      self.root.title('Money Manager')

      self.totalFunds = tk.DoubleVar()
      self.totalFunds.set(0.0)
      self.mainAcctFunds = tk.DoubleVar()
      self.mainAcctFunds.set(0.0)
      self.limitLeft = tk.DoubleVar()
      self.limitLeft.set(0.0)

      self.currUnit = tk.StringVar()
      self.currUnit.set('$')


      f = tkFont.Font(family='times', size=-18)
      s = ttk.Style()
      s.configure('.', font=f)
      
      self.tabBase = ttk.Notebook(self.root)
      self.mainPage = ttk.Frame(self.tabBase)

      self.topFrame = tk.Frame(self.mainPage)
      self.topFrame.config(bg='#b0c4de',bd=5,relief=tk.GROOVE)
      self.topFrame.pack(expand=1,fill=tk.BOTH,side=tk.TOP)
      self.topLeftFrame = tk.Frame(self.topFrame)
      self.topLeftFrame.config(bg='#b0c4de')
      self.topLeftFrame.pack(expand=1,side=tk.LEFT, padx = 15)
      self.topRightFrame = tk.Frame(self.topFrame)
      self.topRightFrame.config(bg='#b0c4de')
      self.topRightFrame.pack(expand=1,side=tk.RIGHT)

      self.vSep = ttk.Separator(self.root, orient="horizontal")
      self.vSep.pack(side="top", fill="x", padx=0)

      self.bottomFrame = tk.Frame(self.mainPage)
      self.bottomFrame.config(bg='#b0c4de', bd=5,relief=tk.GROOVE)
      self.bottomFrame.pack(expand=1,fill=tk.BOTH,side=tk.BOTTOM)
      self.bottomLeftFrame = tk.Frame(self.bottomFrame)
      self.bottomLeftFrame.pack(expand=1,side=tk.LEFT, padx = 15)
      self.bottomLeftFrame.config(bg='#b0c4de')

      self.bottomRightFrame = tk.Frame(self.bottomFrame)
      self.bottomRightFrame.config(bg='#b0c4de')
      self.bottomRightFrame.pack(expand=1,side=tk.RIGHT)
      self.textFont = ('symbol', 14, 'bold')
      self.labelFont = ('symbol', 18, 'bold')
      #self.menu()
      self.BigButtons()
      self.Buttons()
      self.ListBoxes()
      self.labels()
      self.chartBox()
      self.boxFont = ('times', 12)
      self.buttFont = ('times', 13, 'bold')
      
      # transactions frame
      self.transPage = ttk.Frame(self.tabBase)
      self.transTop = tk.Frame(self.transPage)
      self.transTop.pack(side=tk.TOP)
      self.transBottom = tk.Frame(self.transPage)
      self.transBottom.pack(side=tk.BOTTOM)
      
      self.transBox = tk.Listbox(self.transTop)
      self.transBox.config(font=self.boxFont, width=150, height=30)
      self.transBox.pack()
      
      self.transRemoveButton = tk.Button(self.transBottom, text="Remove Selection",
         command=self.removeTrans)
      self.transRemoveButton.config(relief=tk.RAISED, bd=6, height=4, width=15, font=self.buttFont)
      self.transRemoveButton.pack(side=tk.LEFT)
      
      self.transExitButton = tk.Button(self.transBottom, text="Exit Program", command=self.finish)
      self.transExitButton.config(relief = tk.RAISED, bd=6, height=4, width=15, font=self.buttFont)
      self.transExitButton.pack(side=tk.RIGHT, padx = 50)
      
      # bills frame
      self.billsPage = ttk.Frame(self.tabBase)
      self.billsTop = tk.Frame(self.billsPage)
      self.billsTop.pack(side=tk.TOP)
      self.billsBottom = tk.Frame(self.billsPage)
      self.billsBottom.pack(side=tk.BOTTOM)
      
      self.billsBox = tk.Listbox(self.billsTop)
      self.billsBox.config(font=self.boxFont, width=150, height=30)
      self.billsBox.pack()
      
      self.billsRemoveButton = tk.Button(self.billsBottom, text="Remove Selection", 
         command=self.removeBill)
      self.billsRemoveButton.config(relief=tk.RAISED, bd=6, height=4, width=15, font=self.buttFont)
      self.billsRemoveButton.pack(side=tk.LEFT)
      
      self.billsExitButton = tk.Button(self.billsBottom, text="Exit Program", command=self.finish)
      self.billsExitButton.config(relief = tk.RAISED, bd=6, height=4, width=15, font=self.buttFont)
      self.billsExitButton.pack(side=tk.RIGHT, padx = 50)
      
      # income frame
      self.incomePage = ttk.Frame(self.tabBase)
      self.incomeTop = tk.Frame(self.incomePage)
      self.incomeTop.pack(side=tk.TOP)
      self.incomeBottom = tk.Frame(self.incomePage)
      self.incomeBottom.pack(side=tk.BOTTOM)
      
      self.incomeBox = tk.Listbox(self.incomeTop)
      self.incomeBox.config(font=self.boxFont, width=150, height=30)
      self.incomeBox.pack()
      
      self.incomeRemoveButton = tk.Button(self.incomeBottom, text="Remove Selection", 
         command=self.removeIncome)
      self.incomeRemoveButton.config(relief=tk.RAISED, bd=6, height=4, width=15, font=self.buttFont)
      self.incomeRemoveButton.pack(side=tk.LEFT)
      
      self.incomeExitButton = tk.Button(self.incomeBottom, text="Exit Program", command=self.finish)
      self.incomeExitButton.config(relief = tk.RAISED, bd=6, height=4, width=15, font=self.buttFont)
      self.incomeExitButton.pack(side=tk.RIGHT, padx = 50)
      
      # account frame
      self.acctPage = ttk.Frame(self.tabBase)
      self.acctTop = tk.Frame(self.acctPage)
      self.acctTop.pack(side=tk.TOP)
      self.acctBottom = tk.Frame(self.acctPage)
      self.acctBottom.pack(side=tk.BOTTOM)
      
      self.acctBox = tk.Listbox(self.acctTop)
      self.acctBox.config(font=self.boxFont, width=150, height=30)
      self.acctBox.pack()
      
      self.acctRemoveButton = tk.Button(self.acctBottom, text="Remove Selection", 
         command=self.removeAcct)
      self.acctRemoveButton.config(relief=tk.RAISED, bd=6, height=4, width=15, font=self.buttFont)
      self.acctRemoveButton.pack(side=tk.LEFT)
      
      self.acctExitButton = tk.Button(self.acctBottom, text="Exit Program", command=self.finish)
      self.acctExitButton.config(relief = tk.RAISED, bd=6, height=4, width=15, font=self.buttFont)
      self.acctExitButton.pack(side=tk.RIGHT, padx = 50)
      
      self.tabBase.add(self.mainPage, text='Main')
      self.tabBase.add(self.transPage, text='Transactions' )
      self.tabBase.add(self.billsPage, text='Bills' )
      self.tabBase.add(self.incomePage, text='Income' )
      self.tabBase.add(self.acctPage, text='Account' )
      self.tabBase.pack(expand=1, fill="both")

   def BigButtons(self):
      buttFont = ('times', 13, 'bold')
   
      frame = tk.Frame(self.bottomLeftFrame)
      frame.config(bg='#b0c4de')
      frame.pack(side=tk.TOP)

      transButton = tk.Button(frame, text='Add Purchase',
         command=self.createTransWindow)
      transButton.config(relief = tk.RAISED, bd=6, font=buttFont)
      transButton.pack(side = tk.LEFT)
      transButton.config( height = 5, width = 20)

      billsButton = tk.Button(frame, text='Add Bills',
         command=self.createBillWindow)
      billsButton.config(relief = tk.RAISED, bd=6)
      billsButton.pack(side = tk.LEFT, padx=15)
      billsButton.config( height = 5, width = 20, font=buttFont)

   def Buttons(self):
      buttFont = ('times', 13)

      frame = tk.Frame(self.bottomLeftFrame)
      frame.config(bg='#b0c4de')
      frame.pack(side=tk.BOTTOM, pady = 25)

      exitButton = tk.Button(frame, text='Exit', command=self.finish)
      exitButton.config(relief=tk.RAISED, bd=4, height = 4, width = 12)
      exitButton.pack(side=tk.RIGHT, padx=7)

      incomeButton = tk.Button(frame, text = 'Add Income',
         command=self.createIncomeWindow)
      incomeButton.config(relief=tk.RAISED, bd=4, height = 4, width = 14)
      incomeButton.pack(side = tk.LEFT)

      acctButton = tk.Button(frame, text = 'Account Management',
         command=self.createAcctWindow)
      acctButton.config(relief=tk.RAISED, bd=4, height = 4, width = 18)
      acctButton.pack(side = tk.LEFT, padx=7)

      goalsButton = tk.Button(frame, text = 'Set Goal',
         command=self.createGoalWindow)
      goalsButton.config(relief=tk.RAISED, bd=4, height = 4, width = 12)
      goalsButton.pack(side = tk.LEFT, padx=7)

      # yes...I know
      #analButton = tk.Button(frame, text = 'Analysis')
      #analButton.config(relief=tk.RAISED, bd=4, height = 4, width = 12)
      #analButton.pack(side = tk.LEFT, padx=7)

   ''' no functionality to use this for right now
   def menu(self):
      ourmenu = tk.Menu(self.root)
      ourmenu.config(bg = 'gray')
      filemenu = tk.Menu(ourmenu, tearoff=1)
      filemenu.add_command(label='Load')
      filemenu.add_command(label='Save')
      filemenu.add_command(label='Exit')
      ourmenu.add_cascade(menu=filemenu, label='File')
      editmenu = tk.Menu(ourmenu, tearoff=1)
      editmenu.add_command(label='Cut')
      editmenu.add_command(label='Copy')
      editmenu.add_command(label='Paste')
      ourmenu.add_cascade(menu=editmenu, label='Edit')
      helpmenu = tk.Menu(ourmenu)
      helpmenu.add_command(label='Get Help')
      ourmenu.add_cascade(menu=helpmenu, label='Help')
      self.root.config(menu=ourmenu)
   '''

   def ListBoxes(self):

      labelFont = ('times', 16, 'bold')
      boxFont = ('times', 12)

      self.recTransLabel = tk.Label(self.topLeftFrame, bg='#b0c4de', text="Recent Transactions:",
         font=labelFont)
      self.recTransLabel.pack(side=tk.TOP)
      self.rectTransBox = tk.Listbox(self.topLeftFrame, width=60, height=5)
      self.rectTransBox.config(font=boxFont)
      self.rectTransBox.pack(expand=1, side=tk.TOP, pady=5)
      self.rectTransBox.bind('<Double-1>', self.PrintrectTransBox)

      self.upcomingBillsLabel = tk.Label(self.topLeftFrame, bg='#b0c4de', text="Upcoming Bills:",
         font=labelFont)
      self.upcomingBillsLabel.pack(side=tk.TOP, pady=15)
      self.upcomingBillsBox = tk.Listbox(self.topLeftFrame, width=60, height=5)
      self.upcomingBillsBox.config(font=boxFont)
      self.upcomingBillsBox.pack(expand=1,side=tk.TOP, pady=5)
      self.upcomingBillsBox.bind('<Double-1>', self.PrintupcomingBillsBox)

   def PrintrectTransBox(self, event):
      index = self.rectTransBox.curselection()
      item = self.rectTransBox.get(index)
      print "You selected:", item

   def PrintupcomingBillsBox(self, event):
      index = self.upcomingBillsBox.curselection()
      item = self.upcomingBillsBox.get(index)
      print "You selected:", item

   def labels(self):

      labelFont = ('times', 24, 'bold')

      self.f1 = tk.Frame(self.topRightFrame)
      self.f1.pack(side=tk.TOP)
      label1 = tk.Label(self.f1, bg='#b0c4de', text="Total Funds:", width=25, 
         font=labelFont, padx = 20)
      label1.pack(side=tk.LEFT)

      self.totalFundsLabel = tk.Label(self.f1, text=self.currUnit.get() + 
         str(self.totalFunds.get()), width=12, font=labelFont)
      #self.totalFundsLabel = tk.Label(f, text=str(self.totalFunds, width=20, font=labelFont))
      self.totalFundsLabel.pack(side=tk.LEFT)

      self.f2 = tk.Frame(self.topRightFrame)
      self.f2.pack(side=tk.TOP)
      label2 = tk.Label(self.f2, bg='#b0c4de', text=" Main Account Funds:", width=25, 
         font=labelFont, padx = 20)
      label2.pack(side=tk.LEFT)

      self.mainAcctLabel = tk.Label(self.f2, bg='#b0c4de',text=self.currUnit.get() + 
         str(self.mainAcctFunds.get()), width=12, font=labelFont)
      self.mainAcctLabel.pack(side=tk.LEFT)

      self.f3 = tk.Frame(self.topRightFrame)
      self.f3.pack(side=tk.TOP)
      label3 = tk.Label(self.f3, bg='#b0c4de', text="Spending Limit Left:", width=25, 
         font=labelFont, padx = 20)
      label3.pack(side=tk.LEFT)

      self.limitLeftLabel = tk.Label(self.f3, bg='#b0c4de', text=self.currUnit.get() + 
         str(self.limitLeft.get()), width=12, font=labelFont)
      self.limitLeftLabel.pack(side=tk.LEFT)

   def chartBox(self):
      def slice(n): return 360. * n / 500


      frame = tk.Frame(self.bottomFrame)
      frame.pack(side=tk.RIGHT, padx=50)
      c = tk.Canvas(frame, width=300, height=300, bg='#b0c4de', highlightthickness = 0)
      c.pack(side=tk.TOP)
      c.create_arc((2,2,298,298), fill="red", start=slice(0), extent = slice(100))
      c.create_arc((2,2,298,298), fill="blue", start=slice(100), extent = slice(400))
      c.create_arc((2,2,298,298), fill="green", start=slice(400), extent = slice(100))

      #pieChartPH = tk.Listbox(frame, width=60, height=20)
      #pieChartPH.pack(side=tk.TOP)
      #pieChartPH.insert(tk.END, "Placeholder for pie/bar/whatever chart")

   def notify(self, recentTrans, upcomingBills, totalFunds, mainAcctFunds, limitLeft):

      if self.rectTransBox.size() is not 0:
         self.rectTransBox.delete(0, self.rectTransBox.size() - 1)
      if self.upcomingBillsBox.size() is not 0:
         self.upcomingBillsBox.delete(0, self.upcomingBillsBox.size() - 1)

      for x in recentTrans:
         self.rectTransBox.insert(tk.END, x)
      for x in upcomingBills:

         self.upcomingBillsBox.insert(tk.END, x)

      self.totalFunds.set(totalFunds)
      self.mainAcctFunds.set(mainAcctFunds)
      self.limitLeft.set(limitLeft)

      # the following is an ugly workaround until I can get the labels updating right
      self.totalFundsLabel.pack_forget()
      labelFont = ('times', 24, 'bold')
      self.totalFundsLabel = tk.Label(self.f1, bg='#b0c4de', text=self.currUnit.get() + 
         str(self.totalFunds.get()), width=20, font=labelFont)
      self.totalFundsLabel.pack(side=tk.LEFT)
      
      self.mainAcctLabel.pack_forget()
      self.mainAcctLabel = tk.Label(self.f2, bg='#b0c4de',text=self.currUnit.get() + 
         str(self.mainAcctFunds.get()), width=12, font=labelFont)
      self.mainAcctLabel.pack(side=tk.LEFT)
      
      self.limitLeftLabel.pack_forget()
      self.limitLeftLabel = tk.Label(self.f3, bg='#b0c4de', text=self.currUnit.get() + 
         str(self.limitLeft.get()), width=12, font=labelFont)
      self.limitLeftLabel.pack(side=tk.LEFT)
      
   def acctNotify(self, dispList):
      if self.acctBox.size() is not 0:
         self.acctBox.delete(0, self.acctBox.size() - 1)
      
      self.acctDispList = dispList
      for x in dispList:
         self.acctBox.insert(tk.END, x)
         
   def transNotify(self, dispList):
      if self.transBox.size() is not 0:
         self.transBox.delete(0, self.transBox.size() - 1)
      
      self.transDispList = dispList
      for x in dispList:
         self.transBox.insert(tk.END, x)
         
   def billNotify(self, dispList):
      if self.billsBox.size() is not 0:
         self.billsBox.delete(0, self.billsBox.size() - 1)
      
      self.billsDispList = dispList
      for x in dispList:
         self.billsBox.insert(tk.END, x)
         
   def incomeNotify(self, dispList):
      if self.incomeBox.size() is not 0:
         self.incomeBox.delete(0, self.incomeBox.size() - 1)
      
      self.incomeDispList = dispList
      for x in dispList:
         self.incomeBox.insert(tk.END, x)

   def removeTrans(self):
      self.ctrl.delTrans(self.transBox.curselection()[0])
      
   def removeBill(self):
      self.ctrl.delBill(self.billsBox.curselection()[0])
    
   def removeIncome(self):
      self.ctrl.delIncome(self.incomeBox.curselection()[0])

   def removeAcct(self):
      self.ctrl.delAccount(self.acctBox.curselection()[0])

   def createTransWindow(self):
      windows.transWindow.createTransWindow(self.ctrl)

   def createBillWindow(self):
      windows.billWindow.createBillWindow(self.ctrl)
      
   def createAcctWindow(self):
      windows.acctWindow.createAcctWindow(self.ctrl)
    
   def createIncomeWindow(self):
      windows.incomeWindow.createIncomeWindow(self.ctrl)
    
   def createGoalWindow(self):
      windows.goalWindow.createGoalWindow(self.ctrl)

   def finish(self):
      self.ctrl.commitAndClose()
      self.root.quit()
   
   def mainloop(self):
      self.root.mainloop()

#if name = "__main__"
#view = View(NotAController)
#view.mainloop()
