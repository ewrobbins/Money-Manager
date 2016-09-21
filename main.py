#!/usr/bin/python

import Tkinter as tk
import include.controller
import sys

if __name__ == "__main__":
   
   isTest = False
   if len(sys.argv) == 2 and sys.argv[1] == 'test':
      isTest = True
      
   c = include.controller.Controller(isTest)
   tk.mainloop()
