import Tkinter as tk
from Tkinter import *
import tkMessageBox
import Tkinter as tk
GEOMETRY='650x250+300+300'

def createGoalWindow(ctrl):
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



   topLabel = tk.Label(topFrame, text = "Set Goal", font = "Helvetica 16 bold italic")
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
   goalAmountLabel = tk.Label(upperTopLeftFrame, text = "Monthly Goal Spending:")
   goalAmountLabel.pack(side = tk.LEFT, pady = 5)
   goalAmountLabel.config(bg='#b0c4de', width = 18)
   goalAmtEntry = tk.Entry(upperTopLeftFrame)
   goalAmtEntry.config(width=15, font=labelFont)
   goalAmtEntry.pack(side=tk.LEFT, pady = 5, padx = 7)
   goalAmtEntry.focus()

   def commitAndClose():

      ctrl.setMonthlyGoal(goalAmtEntry.get())
      tw.destroy()

   okButton = tk.Button(buttonFrame, text='OK', command=commitAndClose)
   okButton.config(relief=tk.RAISED, bd=4, height = 4, width = 12)
   okButton.pack(side=tk.LEFT, padx=7)

   cancel = tk.Button(buttonFrame, text='CANCEL', command=tw.destroy)
   cancel.config(relief=tk.RAISED, bd=4, height = 4, width = 12)
   cancel.pack(side=tk.LEFT, padx=7)
