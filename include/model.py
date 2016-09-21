# CAN BE PROBABLY BE SIMPLIFIED VIA POLYMORPHISM WHEN I HAVE TIME

import sqlite3
import os
import datetime
import dbOps.tableCreate
import dbOps.tableParse
import dbOps.tableEdit
import testFiles.tableTest

class Model(object):

   def __init__(self, initDb, isTest):

      self.recTrans = []
      self.upcomingBills = []
      self.mainAcct = 0    # changing functionality to be added later
      
      self.transDispList = []
      self.transIndexDict = {}
      self.billsDispList = []
      self.billsIndexDict = {}
      self.incomeDispList = []
      self.incomeIndexDict = {}
      self.acctDispList = []
      self.acctIndexDict = {}

      # for future functionality use
      if initDb == None:
         dbFile = "MoneyManager.sqlite"
      else:
         dbFile = initDb

      # creates DB if it doesn't exist already, uses existing if it does
      if not os.path.isfile(dbFile):
         print "Database not found. Creating a new one..."
         self.dbConn = sqlite3.connect(dbFile)
         self.db = self.dbConn.cursor()
         dbOps.tableCreate.createAll(self.db, self.dbConn)
         # testing ONLY
         if isTest:
            testFiles.tableTest.insertDummies(self.db)
            self.dbConn.commit()
      else:
         self.dbConn = sqlite3.connect(dbFile)
         self.db = self.dbConn.cursor()
         print "Database found."
      
      # intializes all the display lists for the use of the view
      self.initDisplayLists()

   # should be moved to tableParse
   # gets bills due within next six days
   def getUpcomingBills(self):

      displayList = []

      rawList = map(list, dbOps.tableParse.getAllBills(self.db))
      
      # sorts the rawList by their next billing date
      finalList = sorted(rawList, key=lambda x: self.nextBillDate(x))

      for x in finalList:
         row = ""
         row += str(self.nextBillDate(x)) + "    "
         row += str(x[1]) + "    "
         row += str(x[2]) + "    "
         row += '$' + str(x[6]) + "    "
         displayList.append(row)

      return displayList

   # gets last four transactions
   def getRectTransactions(self):

      displayList = []

      rawList = map(list, dbOps.tableParse.getRectTransactions(self.db))
      finalList = self.convTransDates(rawList)

      for x in finalList:
         row = ""
         row += str(x[2]) + "    "
         row += str(x[1]) + "    "
         row += str(x[3]) + "    "
         row += '$' + str(x[6])
         displayList.append(row)

      return displayList

   # gets funds across all accounts
   def getTotalAcctBalance(self):
      return dbOps.tableParse.getTotalAcctBalance(self.db)
   # gets funds for main account
   def getMainAcctBalance(self):
      if self.mainAcct > 0:
         return dbOps.tableParse.getBalanceByAccount(self.db, self.mainAcct)
      else:
         return 0.00
   # gets amount remaining within monthly spending limit
   def getSpendLimitLeft(self):
      return dbOps.tableParse.getTopGoalValue(self.db) - dbOps.tableParse.getMTDSpending(self.db)

   # returns a list of tuples, each one representing an object as it appears in the database
   def getAllAccounts(self):
      return dbOps.tableParse.getAllAccounts(self.db)
   def getAllTransactions(self):
      return dbOps.tableParse.getAllTransactions(self.db)
   def getAllBills(self):
      return dbOps.tableParse.getAllBills(self.db)
   def getAllIncomes(self):
      return dbOps.tableParse.getAllIncomes(self.db)
      
   
   # creates a dictionary matching formatting account strings to their Id
   def getIndexedAccountsDict(self):
      
      acctDict = {}
      for acct in dbOps.tableParse.getAllAccounts(self.db):
         key = ""
         key += str(acct[1]) + " - " + str(acct[2])
         acctDict[key] = acct[0]
         
      return acctDict
   
   ### following functions create display-formatted lists of DB objects, and saves a dictionary
   #   matching their index to their unique Id
   
   def updateTransList(self):
      
      self.transIndexDict = {}
      transList = self.getAllTransactions()
      self.transDispList = []
      
      i = 0
      for trans in transList:
         sDate = str(trans[2])
         row = ""
         row += datetime.date(int(sDate[0:4]), int(sDate[4:6]), int(sDate[6:])).strftime('%m/%d/%Y')
         row += "       " + str(trans[1]) + "       " + str(trans[3]) + "       " + str(trans[4])
         row += "       " + '$' + str(trans[6])
         self.transDispList.append(row)
         self.transIndexDict[i] = trans[0]
         i += 1
         
   def updateBillsList(self):
      
      self.billsIndexDict = {}
      billsList = self.getAllBills()
      self.billsDispList = []
      
      i = 0
      for bill in billsList:
         row = ""
         row += str(bill[1]) + "       " + str(bill[2]) + "       " + str(bill[3]) + "       "
         row += "on day " + str(bill[5]) + "       " + '$' + str(bill[6])
         self.billsDispList.append(row)
         self.billsIndexDict[i] = bill[0]
         i += 1
      
   def updateIncomeList(self):
      
      self.incomeIndexDict = {}
      incomeList = self.getAllIncomes()
      self.incomeDispList = []

      i = 0
      for inc in incomeList:
         row = ""
         row += str(inc[1]) + "       paid on day " + str(inc[2]) + "       " + '$' + str(inc[3])
         self.incomeDispList.append(row)
         self.incomeIndexDict[i] = inc[0]
         i += 1
      
   def updateAcctList(self):
      
      self.acctIndexDict = {}
      acctList = self.getAllAccounts()
      self.acctDispList = []

      i = 0
      for acct in acctList:
         row = ""
         row += str(acct[1]) + "    " + str(acct[2]) + "    " + '$' + str(acct[3])
         self.acctDispList.append(row)
         self.acctIndexDict[i] = acct[0]
         i += 1
      
   # returns a dictionary mapping formatted incomes for drop-down boxes to their ids
   def getIndexedIncomesDict(self):
   
      incDict = {}
      for inc in dbOps.tableParse.getAllIncomes(self.db):
         incDict[str(inc[1])] = inc[0]
         
      return incDict
   
   # runs all update functions
   def initDisplayLists(self):
      self.updateTransList()
      self.updateBillsList()
      self.updateIncomeList()
      self.updateAcctList()
   
   ### following functions insert new DB objects and update their lists
   
   def insertNewAccount(self, list):
      dbOps.tableEdit.insertNewAccount(self.db, list)
      if list[3]:
         self.mainAcct = dbOps.tableParse.getLastAccountId(self.db)
      self.commit()
      self.updateAcctList()
      
   def insertNewTrans(self, list):
      price = float(list[5])
      acctId = list[6]
      del list[6]
      dbOps.tableEdit.debitAccount(self.db, acctId, price)
      dbOps.tableEdit.insertNewTrans(self.db, list)
      self.commit()
      self.updateAcctList()
      self.updateTransList()
   def insertNewBill(self, list):
      dbOps.tableEdit.insertNewBill(self.db, list)
      self.commit()
      self.updateBillList()
   def insertNewIncome(self, list):
      dbOps.tableEdit.insertNewIncome(self.db, list)
      self.commit()
      self.updateIncomeList()
      
   def insertNewGoal(self, list):
      dbOps.tableEdit.insertNewGoal(list)
      self.commit()
   def setMonthlyGoal(self, amt):
      dbOps.tableEdit.setMonthlyGoal(self.db, amt)
      self.commit()

   ### edit functions currently unused
   def editAccount(self, list):
      dbOps.tableEdit.editAccount(list)
   def editTrans(self, list):
      dbOps.tableEdit.editTrans(list)
   def editBill(self, list):
      dbOps.tableEdit.editBill(list)
   def editIncome(self, list):
      dbOps.tableEdit.editIncome(list)
   def editGoal(self, list):
      dbOps.tableEdit.editGoal(list)

   ### following functions remove items from DB and from their corresponding list
   def delAccount(self, ndx):
      key = int(ndx)
      if self.acctIndexDict[key] == self.mainAcct:
         print 'Cannot delete main account.'
         return
         
      dbOps.tableEdit.delAccount(self.db, self.acctIndexDict[key])
      self.updateAcctList()
   def delTrans(self, ndx):
      key = int(ndx)
      dbOps.tableEdit.delTrans(self.db, self.transIndexDict[key])
      self.updateTransList()
   def delBill(self, ndx):
      key = int(ndx)
      dbOps.tableEdit.delBill(self.db, self.billsIndexDict[key])
      self.updateBillsList()
   def delIncome(self, ndx):
      key = int(ndx)
      dbOps.tableEdit.delIncome(self.db, self.incomeIndexDict[key])
      self.updateIncomeList()
   def delGoal(self, id):
      dbOps.tableEdit.delGoal(self.db, id)
   
   '''   TODO - create XML flag so this can't run more than once a day on any item
   def processBillsAndIncome(self):
      todaysBills = dbOps.tableParse.getTodaysBills(self.db)
      today = datetime.datetime.today()
      fmtdDate = datetime.date(today.year, today.month, today.day).strftime('%Y%m%d')
      
      # process transactions for all bills debited today
      for bill in todaysBills:
         newTrans = []
         newTrans.append(bill[1])
         newTrans.append(int(fmtdDate))
         newTrans.append(bill[2])
         newTrans.append(bill[3])
         newTrans.append(bill[4])
         newTrans.append(bill[6])
         newTrans.append(bill[7])
         self.insertNewTrans(newTrans)
         print "Debiting account " + str(bill[7]) + " " + str(bill[6])
         
      todaysJobs = dbOps.tableParse.getJobsPayingToday(self.db)
      total = 0.0
      for job in todaysJobs:
         print "Crediting account " + str(job[4]) + " " + str(job[3])
         dbOps.tableEdit.creditAccount(self.db, job[4], job[3])
   '''
   ### UTILITY FUNCTIONS ###

   # changes all dates into American format, and sorts list by them
   def convTransDates(self, rawList):
      rawList = sorted(rawList, key=lambda x:x[2])
      for x in rawList:
         sDate = str(x[2])
         x[2] = datetime.date(int(sDate[0:4]), int(sDate[4:6]), int(sDate[6:])).strftime('%m/%d/%Y')
      return rawList

   # calculates next billing date using American format
   def nextBillDate(self, bill):

      today = datetime.datetime.today()

      if today.day > bill[5]:
         month = (today.month + 1) % 12
         if month == 13: month = 1
      else:
         month = today.month

      return datetime.date(today.year, month, bill[5]).strftime('%m/%d/%Y')

   # commits changes to DB
   def commit(self):
      self.dbConn.commit()

   # same thing but closes program afterwards
   def commitAndClose(self):
      self.dbConn.commit()
      self.db.close()

if __name__ == "__main__":
   m = Model(None)
   dbOps.tableParse.getBalanceByAccount(m.db, 1)
   #print dbOps.tableParse.getAllBills(m.db)
   #print dbOps.tableParse.getUpcomingBills(m.db)
   #print dbOps.tableParse.getAllAccounts(m.db)
