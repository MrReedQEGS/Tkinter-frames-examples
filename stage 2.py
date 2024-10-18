#Stage 2 - more things
import tkinter as tk
import random,sqlite3

CANVAS_BORDER = 5
filename = "testDB.db"

#Your application must inherit from Frame
class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)  #call parent constructor
        self.grid()  #necessary to make it appear on the screen!
        self.createWidgets()
        self.config(cursor="hand2")
        
    def createWidgets(self):
        #Add stuff to my application
        #bg is background colour
        #canvas bd is border width for canvas
        self.testButton = tk.Button(self,text="Draw stuff",bg="#00ff00",command=self.myTest)
        self.dbTest = tk.Button(self,text="Create test DB",bg="#aa00ff",command=self.create_sqlite_database)
        self.dbReadButton = tk.Button(self,text="Read DB",command=self.myDBRead)
        self.quitButton = tk.Button(self,text="Quit",command=self.myQuit)
        
        self.canvas1 = tk.Canvas(self,height=100,width=60,bd=CANVAS_BORDER,relief=tk.RIDGE)
        self.testButton.grid(column = 0,row=0,padx=20,pady=20) #places the button on the app frame
        self.dbTest.grid(column = 1,row=0,padx=20,pady=20)
        self.dbReadButton.grid(column = 2,row=0,padx=20,pady=20)
        self.quitButton.grid(column = 3,row=0,padx=20,pady=20)
        self.canvas1.grid(row=2)
    
    def create_sqlite_database(self):
        """ create a database connection to an SQLite database """
        #https://www.sqlitetutorial.net/sqlite-python/creating-tables/
        
        self.dbConn = None
        try:
            self.dbConn = sqlite3.connect(filename)
            print(sqlite3.sqlite_version)
            c = self.dbConn.cursor()
            #c.execute("DROP TABLE IF EXISTS tblPeople")
            #find out what tables there are:
            mySQL = "SELECT name FROM sqlite_master WHERE type='table' AND name='tblPeople'"
            r = c.execute(mySQL)
            results = r.fetchall()
            print(results)
            if(len(results)==0):
                print("No table...creating one.")
                c.execute("CREATE TABLE IF NOT EXISTS tblPeople (personID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, firstName TEXT, surname TEXT, form TEXT, password TEXT, userLevel INT)")
                c.execute("INSERT INTO tblPeople VALUES (NULL,?,?,?,?,?,?)", ['mreed','Mark', 'Reed', '9MPR','helloworld',0])
           
            r = c.execute("SELECT * FROM tblPeople")
            results = r.fetchall()
            print(results)
                  
            #c.execute("INSERT INTO tblPeople VALUES (NULL,?,?,?,?,?,?)", ['myarwood','Mike', 'Yarwood', '8JML','bob',0])
            #c.execute("INSERT INTO tblPeople VALUES (NULL,?,?,?,?,?,?)", ['jculshaw','Jon', 'Culshaw', '8JML',"frank",0])
            #c.execute("INSERT INTO tblPeople VALUES (NULL,?,?,?,?,?,?)", ['rbremner','Rory', 'Bremner', '7SAP',"paddy",0])
            #c.execute("INSERT INTO tblPeople VALUES (NULL,?,?,?,?,?,?)", ['scoogan','Steve', 'Coogan', '7SAP',"alan",1])
            self.dbConn.commit()
            
        except sqlite3.Error as e:
            print(e)
        finally:
            print("DB closed")
            if self.dbConn:
                self.dbConn.close()

    def myDBRead(self):
        
        
        
        self.dbConn = None
        try:
            self.dbConn = sqlite3.connect(filename)
            print(sqlite3.sqlite_version)
            
            c = self.dbConn.cursor()
            r = c.execute("SELECT * FROM tblPeople")
            results = r.fetchall()
            print(results)
    
        except sqlite3.Error as e:
            print(e)
        finally:
            print("DB closed")
            if self.dbConn:
                self.dbConn.close()
    
    
    def myTest(self):
        if(self.cursorType == "hand2"):
            self.cursorType = "umbrella"
        else:
            self.cursorType = "hand2"
            
        self.config(cursor=self.cursorType)
        
        #Draw on the canvas1
        self.canvas1.delete("all")
        randx=random.randint(10,20)
        randy=random.randint(10,20)
        theID = self.canvas1.create_rectangle(CANVAS_BORDER+3,CANVAS_BORDER+3,20+randx,30+randy)
        randx=random.randint(10,20)
        randy=random.randint(10,20)
        theID = self.canvas1.create_arc(CANVAS_BORDER+3,CANVAS_BORDER+3,20+randx,30+randy,style=tk.ARC)
        randx=random.randint(10,20)
        randy=random.randint(10,20)
        theID = self.canvas1.create_bitmap(CANVAS_BORDER+3+randx,CANVAS_BORDER+3+randy,bitmap="warning")

         
        print(theID)
        somecoords = self.canvas1.coords(theID)
        print(somecoords)

        somecoords = self.canvas1.bbox(theID)
        print(somecoords)

        someResult = self.canvas1.find_all()
        print(someResult)

        someResult = self.canvas1.type(theID)
        print(someResult)
        
        
    def myQuit(self):
        quit()
        
    cursorType = "hand2"
    
    dbConn = None
        
app = Application()
app.master.title("TK Helloworld")
app.mainloop()