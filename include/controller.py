import model
import view

class Controller(object):

   def __init__ (self, isTest):

      self.model = model.Model(None, isTest)
      self.view = view.View(self)
      self.view.notify(self.getRectTransactions(), self.getUpcomingBills(), 
         self.getTotalAcctBalance(), self.getMainAcctBalance(), self.getSpendLimitLeft())
      #self.model.processBillsAndIncome()
      self.view.acctNotify(self.model.acctDispList)
      self.view.transNotify(self.model.transDispList)
      self.view.billNotify(self.model.billsDispList)
      self.view.incomeNotify(self.model.incomeDispList)

   # get last 4 transactions from model
   def getRectTransactions(self):
      return self.model.getRectTransactions()
   # get bills due within the next six days from model
   def getUpcomingBills(self):
      return self.model.getUpcomingBills()

   # get total funds from all accounts combined
   def getTotalAcctBalance(self):
      return self.model.getTotalAcctBalance()
   # get balance from the designated main account
   def getMainAcctBalance(self):
      return self.model.getMainAcctBalance()
   # get the amount of money remaining against the monthly spending limit
   def getSpendLimitLeft(self):
      return self.model.getSpendLimitLeft()
   
   # get dictionaries mapping display representations of accounts and incomes to their unique Ids
   def getIndexedAccountsDict(self):
      return self.model.getIndexedAccountsDict()
   def getIndexedIncomesDict(self):
      return self.model.getIndexedIncomesDict()
   
   # self-explanatory
   def insertNewAccount(self, list):
      self.model.insertNewAccount(list)
      self.view.notify(self.getRectTransactions(), self.getUpcomingBills(), 
         self.getTotalAcctBalance(), self.getMainAcctBalance(), self.getSpendLimitLeft())
      self.view.acctNotify(self.model.acctDispList)
   def insertNewTrans(self, list):
      self.model.insertNewTrans(list)
      self.view.notify(self.getRectTransactions(), self.getUpcomingBills(), 
         self.getTotalAcctBalance(), self.getMainAcctBalance(), self.getSpendLimitLeft())
      self.view.transNotify(self.model.transDispList)
      self.view.acctNotify(self.model.acctDispList)
   def insertNewBill(self, list):
      self.model.insertNewBill(list)
      self.view.notify(self.getRectTransactions(), self.getUpcomingBills(), 
         self.getTotalAcctBalance(), self.getMainAcctBalance(), self.getSpendLimitLeft())
      self.view.billNotify(self.model.billsDispList)
   def insertNewIncome(self, list):
      self.model.insertNewIncome(list)
      self.view.incomeNotify(self.model.incomeDispList)
   def insertNewGoal(self, list):
      self.model.insertNewGoal(list)
      
   # changes the monthly goal limit
   def setMonthlyGoal(self, amt):
      self.model.setMonthlyGoal(amt)
      self.view.notify(self.getRectTransactions(), self.getUpcomingBills(), 
         self.getTotalAcctBalance(), self.getMainAcctBalance(), self.getSpendLimitLeft())

   # edits existing objects - currently unused
   def editAccount(self, list):
      self.model.editAccount(list)
   def editTrans(self, list):
      self.model.editTrans(list)
   def editBill(self, list):
      self.model.editBill(list)
   def editIncome(self, list):
      self.model.editIncome(list)
   def editGoal(self, list):
      self.model.editGoal(list)

   # tells the controller to set last entered account as main - unused, I believe
   def setMainAccount(self):
      self.model.setLastAcctAsMain()
      
   # self-explanatory - deletes the specified object based on the their index in the last and
   #    updates the view accordingly
   def delAccount(self, ndx):

      self.model.delAccount(ndx)
      self.commit()
      self.view.notify(self.getRectTransactions(), self.getUpcomingBills(), 
         self.getTotalAcctBalance(), self.getMainAcctBalance(), self.getSpendLimitLeft())
      self.view.acctNotify(self.model.acctDispList)
      
   def delTrans(self, ndx):
      
      self.model.delTrans(ndx)
      self.commit()
      self.view.notify(self.getRectTransactions(), self.getUpcomingBills(), 
         self.getTotalAcctBalance(), self.getMainAcctBalance(), self.getSpendLimitLeft())
      self.view.transNotify(self.model.transDispList)
      
   def delBill(self, ndx):
      
      self.model.delBill(ndx)
      self.commit()
      self.view.notify(self.getRectTransactions(), self.getUpcomingBills(), 
         self.getTotalAcctBalance(), self.getMainAcctBalance(), self.getSpendLimitLeft())
      self.view.billNotify(self.model.billsDispList)
      
   def delIncome(self, ndx):
      self.model.delIncome(ndx)
      self.commit()
      self.view.incomeNotify(self.model.incomeDispList)
      
   def delGoal(self, id):
      self.model.delGoal(id)
      self.commit()

   # tells model to commit changes to Sqlite DB
   def commit(self):
      self.model.commit()
   def commitAndClose(self):
      self.model.commitAndClose()
