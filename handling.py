############ Copied from week 6 homework ##########
import sqlite3
db = sqlite3.connect('practical_work.db')
cur = db.cursor()

def initializeDB():
    try:
        f = open("sqlcommands.sql", "r")
        commandstring = ""
        for line in f.readlines():
            commandstring+=line
        cur.executescript(commandstring)
    except sqlite3.OperationalError:
        print("Database exists, skip initialization")
    except:
        print("No SQL file to be used for initialization") 


def main():
    
    initializeDB()

    userInput = -1
    while(userInput != "0"):
        print("\nMenu options:")
        print("1: Print all books")
        print("2: Print author")
        print("3: Add book to the collection")
        print("4: Change reading status")
        print("5: Delete book from bookshelf")
        print("6: Modify the books review")
        print("7: Print individual book information")
        print("0: Quit")
        userInput = input("What do you want to do? ")
        print(userInput)
        if userInput == "1":
            printAllBooks()
        if userInput == "2":
            printAuthor()
        if userInput == "3":
            addBook()
        if userInput == "4":
            changeReading()
        if userInput == "5":
            deleteFromShelf()
        if userInput == "6":
            modifyReview()
        if userInput == "7":
            printBook()
        if userInput == "0":
            print("Ending software...")
    db.close()        
    return

############ Copied from week 6 homework ends ##########
def printAllBooks():
    pass

def printAuthor():
    pass

def addBook():
    pass

def changeReading():
    pass

def deleteFromShelf():
    pass

def modifyReview():
    pass

def printBook():
    pass


main()