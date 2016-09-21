### Intializes a new sqlite database by creating all the necessary tables


def createAll(db, dbConn):

   createAccounts(db, dbConn)
   createTransactions(db, dbConn)
   createBills(db, dbConn)
   createIncome(db, dbConn)
   createGoals(db, dbConn)

def createAccounts(db, dbConn):

   db.execute('''CREATE TABLE Accounts
               (Id      INT   PRIMARY KEY    NOT NULL,
               Name     TEXT                 NOT NULL,
               Type     TEXT                 NOT NULL,
               Balance  REAL                 NOT NULL);''')
   print "Accounts table created."

def createTransactions(db, dbConn):

   db.execute('''CREATE TABLE Transactions
               (Id     INT   PRIMARY KEY     NOT NULL,
               Name    TEXT                  NOT NULL,
               Date    DATETIME              NOT NULL,
               Payee   TEXT                  NOT NULL,
               Cat     TEXT,
               Import  TINYINT               NOT NULL,
               Amount  REAL                  NOT NULL);''')
   print "Transactions table created."

def createBills(db, dbConn):

   db.execute('''CREATE TABLE Bills
               (Id            INT   PRIMARY KEY     NOT NULL,
               Name           TEXT                  NOT NULL,
               Payee          TEXT                  NOT NULL,
               Cat            TEXT,
               Import         TINYINT               NOT NULL,
               Day_Of_Month   INT                   NOT NULL,
               Amount         REAL                  NOT NULL,
               Account        ID                    NOT NULL );''')
   print "Bills table created."

def createIncome(db, dbConn):

   db.execute('''CREATE TABLE Income
               (Id          INT   PRIMARY KEY     NOT NULL,
               Source       TEXT                  NOT NULL,
               Payday       INT                   NOT NULL,
               Amount       REAL                  NOT NULL,
               Dep_Acct     INT                   NOT NULL );''')
   print "Income table created."

def createGoals(db, dbConn):

   db.execute('''CREATE TABLE Goals
               (Id          INT   PRIMARY KEY    NOT NULL,
               Time_Period  INT                  NOT NULL,
               Amount       REAL                 NOT NULL);''')
   print "Goals table created."
