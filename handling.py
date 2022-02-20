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
    #SELECT Name, Series, Genre, ReleaseYear, Pages FROM Book;
    #SELECT FisrtName Lastname FROM 
    #'SELECT FirstName, LastName, Name, Series, Genre, ReleaseYear, Pages FROM AuthorBookJoin INNER JOIN Author ON AuthorBookJoin.AuthorID = Author.AuthorID INNER JOIN Book ON AuthorBookJoin.BookID = Book.BookID'
    for row in cur.execute('SELECT FirstName, LastName, Name, Series, Genre, ReleaseYear, Pages FROM AuthorBookJoin INNER JOIN Author ON AuthorBookJoin.AuthorID = Author.AuthorID INNER JOIN Book ON AuthorBookJoin.BookID = Book.BookID'):
        print(row)

    return

def printAuthor():
    
    for row in cur.execute('SELECT FirstName, LastName, ReleasedBooks, Name FROM AuthorBookJoin INNER JOIN Author ON AuthorBookJoin.AuthorID = Author.AuthorID INNER JOIN Book ON AuthorBookJoin.BookID = Book.BookID'):
        print(row)
    return

def addBook():
    
    bookname = input('Give the name of the book: ')
    series = input('Give the series of the book: ')
    genre = input('Give the Genre of the book: ')
    year = int(input('Give the release year of the book: '))
    pages = int(input('Give number of pages in the book: '))

    cur.execute("SELECT EXISTS('SELECT 1 FROM Book WHERE Name = (?) AND Series = (?)')", (bookname, series, ))
    found = cur.fechone()
    if (found == '1'):
        print("Book is already in the library")
    else:
        inbooksh = input('Is it in a bookshelf[y/n]: ')
        if inbooksh == 'y':
            booksh = input('Give the bookshelf: ')
            shelf = int(input('Give the shelf: '))
        
        wantQuote = input('Want to add a quote?[y/n]: ')
        if wantQuote == 'y':
            quote = input('Write the quote: ')
            wantReview = input('Want to give review?[y/n]: ')
        
        wantRating = input('Want to give a review[y/n]: ')
        if wantRating == 'y':
            rating = int(input('Give the rating(1-5): '))
            review = input('Small written review: ')
        
        wantReading = input('Want to add reading status?[y/n]: ')
        if wantReading == 'y':
            status = input('Status(not started/started/complete): ')
            whereAt = input('What page are you at: ')
        
        authorFirst = input('First name of the author: ')
        authorLast = input('Last name of the author (can be empty): ')
        released = int(input('Number of released books': ))

        
        cur.execute("SELECT EXISTS('SELECT 1 FROM Author WHERE fistName = (?) AND lastName = (?)')", (authorFirst, authorLast, ))
        found2 = cur.fetchone()
        if found2 == '0':
            cur.execute('INSERT INTO Author VALUES (?), (?), (?);', (authorFirst, authorLast, released, ))

        if found == '1' and found2 == '1':
            return
    
    cur.execute('INSERT INTO BookAuthorJoin VALUES (?), (?):', (('SELECT BookID FROM Book WHERE Name = (?) AND series = (?)', (bookname, series)), ('SELECT AuthorID FROM Author WHERE fistName = (?) AND lastName = (?)', (authorFirst, authorLast))))

    return


def changeReading():
    pass
    #input('Status(not started/started/complete): ')
    #input('What page are you at: ')

def deleteFromShelf():
    pass

def modifyReview():
    pass
    #input('Give the rating(1-5): ')
    #input('Small written review: ')

def printBook():
    pass
    #'SELECT Name, Series, Genre, ReleaseYear, Pages FROM Book'
    #cur.execute('SELECT FirstName, LastName, Name, Series, Genre, ReleaseYear, Pages FROM AuthorBookJoin INNER JOIN Author ON AuthorBookJoin.AuthorID = Author.AuthorID INNER JOIN Book ON AuthorBookJoin.BookID = Book.BookID')

main()