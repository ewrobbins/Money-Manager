import datetime

# gets account from its corresponding unique id
def getAccountByID(db, id):

   db.execute('SELECT * FROM Accounts WHERE Id=?', (id,))
   return db.fetchone()

#  returns a list of all accounts
def getAllAccounts(db):

   acctList = []
   db.execute('SELECT * FROM Accounts')
   for row in db:
      acctList.append(row)
   return acctList

# returns unique id from last entered account
def getLastAccountId(db):
   
   db.execute('SELECT Id FROM Accounts ORDER BY Id DESC LIMIT 1')
   return db.fetchone()[0]

# returns all money in all accounts
def getTotalAcctBalance(db):

   bal = 0.0
   db.execute('SELECT * FROM Accounts')
   for row in db:
      bal += row[3]
   return bal

#  gets a specific account's balance
def getBalanceByAccount(db, id):

   db.execute('SELECT Balance FROM Accounts WHERE Id=?', (id,))
   #if db.fetchone() == None: return 0.0
   return db.fetchone()[0]

def getTransactionById(db, id):

   idTup = (id,)
   db.execute('SELECT * FROM Transactions WHERE Id=?', idTup)
   return db.fetchone()

def getAllTransactions(db):

   transList = []
   db.execute('SELECT * FROM Transactions ORDER BY Date DESC')
   for row in db:
      transList.append(row)
   return transList

# not efficient but it works for now
# gets last 4 transactions
def getRectTransactions(db):

   transList = []
   db.execute('SELECT * FROM Transactions ORDER BY Date DESC LIMIT 4')
   for row in db:
      transList.append(row)
   
   return transList

# again, not efficient because I am lousy at SQL
# calculates month-to-date spending
def getMTDSpending(db):
   
   transList = []
   mtdSpend = 0.0
   def isThisMonth(dt):
      today = datetime.datetime.today()
      sDate = str(dt)
      if today.year == int(sDate[0:4]) and today.month == int(sDate[4:6]): return True
      return False
      
   db.execute('SELECT * FROM Transactions ORDER BY Date DESC')
   for row in db:
      transList.append(row)
   
   if len(transList) == 0: return 0.0
   
   x = 0   
   while isThisMonth(transList[x][2]):
      mtdSpend += transList[x][6]
      x += 1
   
   return mtdSpend

def getBillById(db, id):

   db.execute('SELECT * FROM Bills WHERE Id=?', (id,))
   return db.fetchone()

def getAllBills(db):

   billList = []
   db.execute('SELECT * FROM Bills ORDER BY Day_Of_Month ASC')
   for row in db:
      billList.append(row)
   return billList

# again, could be more efficient (unlikely to matter unless you have way too many bills to pay)
def getUpcomingBills(db):

   billList = []
   db.execute('SELECT * FROM Bills ORDER BY Day_Of_Month ASC')
   for row in db:
      billList.append(row)

   currDay = datetime.datetime.today().day
   upcomingBills = []
   for x in billList:
      if x[5] >= currDay and x[5] < currDay + 6:
         upcomingBills.append(x)

   return upcomingBills

# returns a list of all bills due on today's date of the month
def getTodaysBills(db):

   billList = []
   db.execute('SELECT * FROM Bills ORDER BY Day_Of_Month ASC')
   for row in db:
      billList.append(row)
      
   currDay = datetime.datetime.today().day
   todaysBills = []
   for x in billList:
      if x[5] == currDay:
         todaysBills.append(x)
         
   return todaysBills

def getIncomeById(db, id):

   idTup = (id,)
   db.execute('SELECT * FROM Income WHERE Id=?', idTup)
   return db.fetchone()

def getAllIncomes(db):

   riList = []
   db.execute('SELECT * FROM Income')
   for row in db:
      riList.append(row)
   return riList

# returns a list of all jobs(incomes) that pay out today
def getJobsPayingToday(db):
   
   jobList = []
   db.execute('SELECT * FROM Income WHERE Payday=?', (datetime.datetime.today().day,))
   for row in db:
      jobList.append(row)
   return jobList

def getGoalById(db, id):

   idTup = (id,)
   db.execute('SELECT * FROM Goals WHERE Id=?', idTup)
   return db.fetchone()

def getAllGoals(db):

   goalList = []
   db.execute('SELECT * FROM Goals')
   for row in db:
     goalList.append(row)
   return goalList

# only function used for goals for now, until multi-goal functionality implemented
def getTopGoalValue(db):
   val = db.execute('SELECT * FROM Goals ORDER BY Id DESC LIMIT 1').fetchone()
   if val == None:
      return 0.0
   else: 
      return val[2]
