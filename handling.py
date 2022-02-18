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
            pass
        if userInput == "3":
            pass
        if userInput == "4":
            pass
        if userInput == "5":
            pass
        if userInput == "6":
            pass
        if userInput == "7":
            pass
        if userInput == "0":
            print("Ending software...")
    db.close()        
    return

############ Copied from week 6 homework ends ##########
def printAllBooks():
    pass

main()