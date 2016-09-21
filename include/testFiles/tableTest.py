
def insertDummies(db):

   insertDummyAccounts(db)
   insertDummyTransactions(db)
   insertDummyBills(db)
   insertDummyIncomes(db)
   insertDummyGoals(db)

def insertDummyAccounts(db):

   db.execute("INSERT INTO Accounts (Id,Name,Type,Balance) \
      VALUES (1, 'BofA', 'Checking', 15000.00)");
   db.execute("INSERT INTO Accounts (Id,Name,Type,Balance) \
      VALUES (2, 'Wells Fargo', 'Savings', 6000.00)");
   db.execute("INSERT INTO Accounts (Id,Name,Type,Balance) \
      VALUES (3, 'SCCU', 'Retirement', 25020.60)");

def insertDummyTransactions(db):

   db.execute("INSERT INTO Transactions (Id,Name,Date,Payee,Import,Amount) \
      VALUES (1,'New shoes','20090624','Foot Locker',1,84.99)");
   db.execute("INSERT INTO Transactions (Id,Name,Date,Payee,Import,Amount) \
      VALUES (2,'Beer','20090824','Bilo',0,14.99)");
   db.execute("INSERT INTO Transactions (Id,Name,Date,Payee,Import,Amount) \
      VALUES (3,'Food','20090724','Chickfila',0,8.25)");
   db.execute("INSERT INTO Transactions (Id,Name,Date,Payee,Import,Amount) \
      VALUES (4,'Textbooks','20150724','Bookstore',1,484.99)");

def insertDummyBills(db):

   db.execute("INSERT INTO Bills (Id,Name,Payee,Import,Day_Of_Month,Amount,Account) \
      VALUES (1,'Electricity','Duke Power',1,15,100.15,1)");
   db.execute("INSERT INTO Bills (Id,Name,Payee,Import,Day_Of_Month,Amount,Account) \
      VALUES (2,'Water','City of Clemson',1,18,26.35,1)");
   db.execute("INSERT INTO Bills (Id,Name,Payee,Import,Day_Of_Month,Amount,Account) \
      VALUES (3,'Internet','Northland',1,01,49.99,1)");
   db.execute("INSERT INTO Bills (Id,Name,Payee,Import,Day_Of_Month,Amount,Account) \
      VALUES (4,'Cable','AT&T',1,21,100.15,1)");

def insertDummyIncomes(db):
   db.execute("INSERT INTO Income (Id,Source,Payday,Amount,Dep_Acct) \
      VALUES (1,'Google',15,2300.06,1)");

def insertDummyGoals(db):
   db.execute("INSERT INTO Goals (Id,Time_Period,Amount) \
      VALUES (1,30,1000)");


