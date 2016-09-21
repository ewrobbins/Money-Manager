# functions that actually modify the database

import tableParse

def insertNewAccount(db, list):
   
   # dynamically calculates id based on previous entries
   if db.execute('SELECT Id from Accounts ORDER BY Id DESC LIMIT 1').fetchone() == None:
      id = 1
   else: 
      id = db.execute('SELECT Id from Accounts ORDER BY Id DESC LIMIT 1').fetchone()[0] + 1
      
   db.execute('''INSERT INTO Accounts (Id,Name,Type,Balance) \
      VALUES(?,?,?,?)''', (id, list[0], list[1], list[2]))

def editAccount(db, id, list):
   pass

#  removes money for an account
def debitAccount(db, id, price):

   balance = tableParse.getBalanceByAccount(db, id) - price
   db.execute('UPDATE Accounts set Balance=? where Id=?', (balance,id,))

#  adds money to an account
def creditAccount(db, id, credit):

   balance = tableParse.getBalanceByAccount(db, id) + credit
   db.execute('UPDATE Accounts set Balance=? where Id=?', (balance,id,))   

def delAccount(db, id):
   db.execute('DELETE from Accounts where Id=?', (id,))

def insertNewTrans(db, list):
   
   if db.execute('SELECT Id from Transactions ORDER BY Id DESC LIMIT 1').fetchone() == None:
      id = 1
   else:
      id = db.execute('SELECT Id from Transactions ORDER BY Id DESC LIMIT 1').fetchone()[0] + 1
      
   db.execute('''INSERT INTO Transactions (Id,Name,Date,Payee,Cat,Import,Amount) \
      VALUES(?,?,?,?,?,?,?)''', (id, list[0], list[1], list[2], list[3], list[4], list[5]))

def editTrans(db, id, list):
   pass
   
def delTrans(db, id):
   db.execute('DELETE from Transactions where Id=?', (id,))

def insertNewBill(db, list):

   if db.execute('SELECT Id from Bills ORDER BY Id DESC LIMIT 1').fetchone() == None:
      id = 1
   else:
      id = db.execute('SELECT Id from Bills ORDER BY Id DESC LIMIT 1').fetchone()[0] + 1
      
   db.execute('''INSERT INTO Bills (Id,Name,Payee,Cat,Import,Day_Of_Month,Amount,Account) \
      VALUES(?,?,?,?,?,?,?,?)''', (id, list[0], list[1], list[2], 
         list[3], list[4], list[5], list[6]))

def editBill(db, id, list):
   pass
   
def delBill(db, id):
   db.execute('DELETE from Bills where Id=?', (id,))

def insertNewIncome(db, list):

   if db.execute('SELECT Id from Income ORDER BY Id DESC LIMIT 1').fetchone() == None:
      id = 1
   else:
      id = db.execute('SELECT Id from Income ORDER BY Id DESC LIMIT 1').fetchone()[0] + 1
      
   db.execute('''INSERT INTO Income (Id,Source,Payday,Amount,Dep_Acct) \
         VALUES (?,?,?,?,?)''', (id, list[0], list[1], list[2], list[3]))

def editIncome(db, id, list):
   pass

def delIncome(db, id):
   db.execute('DELETE from Income where Id=?', (id,))
   
# only goal function in use for now
def setMonthlyGoal(db, amt):

   db.execute('DELETE from Goals where Id=1')
   db.execute('''INSERT INTO Goals (Id,Time_Period,Amount) \
      VALUES (1, 30, ?)''', (amt,))
   
def insertNewGoal(db, list):
   
   if db.execute('SELECT Id from Goals ORDER BY Id DESC LIMIT 1').fetchone() == None:
      id = 1
   else:
      id = db.execute('SELECT Id from Goals ORDER BY Id DESC LIMIT 1').fetchone()[0] + 1
      
   db.execute("INSERT INTO Goals (Id,Time_Period,Amount) \
         VALUES (id, list[0], list[1])")

def editGoal(db, id, list):
   pass

def delGoal(db, id):
   db.execute('DELETE from Goals where Id=?', (id,))
