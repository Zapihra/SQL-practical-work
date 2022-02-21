############ Copied from week 6 homework ##########
from asyncio.windows_events import NULL
import sqlite3
db = sqlite3.connect('practical_work.db')
cur = db.cursor()

def initializeDB():
    try:
        f = open("SQLqueries.sql", "r")
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
        print("5: Modify the books review")
        print("6: Add quote")
        print("7: Print individual book information")
        print("0: Quit")
        userInput = input("What do you want to do? ")

        if userInput == "1":
            printAllBooks()
        if userInput == "2":
            printAuthor()
        if userInput == "3":
            addBook()
        if userInput == "4":
            changeReading()
        if userInput == "5":
            modifyReview()
        if userInput == "6":
            addQuote()
        if userInput == "7":
            printBook()            
        if userInput == "0":
            print("Ending software...")
    db.close()        
    return

############ Copied from week 6 homework ends ##########
def printAllBooks():
    
    for row in cur.execute('SELECT FirstName, LastName, Name, Series, Genre, ReleaseYear, Pages FROM BookAuthorJoin \
        INNER JOIN Author ON BookAuthorJoin.AuthorID = Author.AuthorID \
        INNER JOIN Book ON BookAuthorJoin.BookID = Book.BookID'):
        
        print("Author: {} {}; Book name {}, series {}, genre {}, release year {} and number of pages {}\
            ".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) )

    return

def printAuthor():

    authorFirst = input('First name of the author: ')
    authorLast = input('Last name of the author (can be empty): ')
    cur.execute('SELECT AuthorID FROM Author WHERE FirstName = (?) AND LastName = (?);', (authorFirst, authorLast, ))
    authorid = cur.fetchone()[0]
    
    for row in cur.execute('SELECT FirstName, LastName, ReleasedBooks, Name, Series FROM BookAuthorJoin  \
        INNER JOIN Author ON BookAuthorJoin.AuthorID = Author.AuthorID \
        INNER JOIN Book ON BookAuthorJoin.BookID = Book.BookID \
        WHERE BookAuthorJoin.AuthorID = (?)', (authorid, )):
        
        print("Author: {} {} number of released books {} book name {} and series {}".format(row[0], row[1], row[2], row[3], row[4]))
    return

def addBook():

    bookname = input('Give the name of the book: ')
    series = input('Give the series of the book: ')
    genre = input('Give the Genre of the book: ')
    year = int(input('Give the release year of the book: '))
    pages = int(input('Give number of pages in the book: '))

    #checks if the book already exists in the database
    cur.execute('SELECT 1 FROM Book WHERE Name = (?) AND Series = (?)', (str(bookname), str(series), ))
    found = cur.fetchone()
    if found:
        print("Book is already in the library")
        anotherAuthor =input("Want to add another author for the book?[y/n] ")
        if anotherAuthor == 'y':

            authorFirst = input('First name of the author: ')
            authorLast = input('Last name of the author (can be empty): ')
            released = int(input('Number of released books: '))

            cur.execute('SELECT 1 FROM Author WHERE FirstName = (?) AND LastName = (?)', (str(authorFirst), str(authorLast), ))
            found2 = cur.fetchone()
            
            if found2 == None:
                cur.execute('INSERT INTO Author (FirstName, LastName, ReleasedBooks)\
                    VALUES (?, ?, ?);', (str(authorFirst), str(authorLast), released, ))
                db.commit()

            cur.execute('SELECT BookID FROM Book WHERE Name = (?) AND Series = (?);', (bookname, series, ))
            bookid = cur.fetchone()[0]
            cur.execute('SELECT AuthorID FROM Author WHERE FirstName = (?) AND LastName = (?);', (authorFirst, authorLast, ))
            authorid = cur.fetchone()[0]

            cur.execute('SELECT 1 FROM BookAuthorJoin WHERE BookID = (?) AND AuthorID = (?)', (bookid, authorid))
            check1 = cur.fetchone()

            if check1:
                print("Book already has this author")
                return

            cur.execute('INSERT INTO BookAuthorJoin VALUES (?, ?);', (bookid, authorid))
            db.commit()
            
        else:#just returns for the menu if nothing is added
            return

    else:
        booksh = None
        shelf = None 
        quote = None
        rating = None
        review = None
        status = None
        whereAt = None
        authorFirst = None
        authorLast = None
        released = None

        inbooksh = input('Is it in a bookshelf[y/n]: ')
        if inbooksh == 'y':
            booksh = input('Give the bookshelf: ')
            shelf = int(input('Give the shelf: '))
        
        authorFirst = input('First name of the author: ')
        authorLast = input('Last name of the author (can be empty): ')
        released = int(input('Number of released books: '))

        #checks if author already exists
        cur.execute('SELECT 1 FROM Author WHERE FirstName = (?) AND LastName = (?)', (str(authorFirst), str(authorLast), ))
        found2 = cur.fetchone()
        
        if found2 == None: #the new writer is created
            cur.execute('INSERT INTO Author (FirstName, LastName, ReleasedBooks)\
                VALUES (?, ?, ?);', (str(authorFirst), str(authorLast), released, ))
            db.commit()


        #extra questions for more information
        wantQuote = input('Want to add a quote?[y/n]: ')
        if wantQuote == 'y':
            quote = input('Write the quote: ')
        
        wantRating = input('Want to give a review[y/n]: ')
        if wantRating == 'y':
            rating = int(input('Give the rating(1-5): '))
            review = input('Small written review: ')
        
        wantReading = input('Want to add reading status?[y/n]: ')
        if wantReading == 'y':
            status = input('Status(not started/started/complete): ')
            whereAt = input('What page are you at: ')

        #bookshelf added to the database
        cur.execute('INSERT INTO Bookshelf \
            (Bookshelf, Shelf) VALUES (?, ?);', (booksh, shelf, ))
        db.commit()

        #bookshelf is defined and added to the book
        cur.execute('SELECT BookshelfID FROM Bookshelf ORDER BY BookshelfID DESC LIMIT 1')
        bookshID = cur.fetchone()
        cur.execute('INSERT INTO Book (Name, Series, Genre, Pages, ReleaseYear, BookshelfID) \
            VALUES (?, ?, ?, ?, ?, ?);', (bookname, series, genre, pages, year, bookshID[0]))
        db.commit()

        #wanted book and author is defined
        cur.execute('SELECT BookID FROM Book WHERE Name = (?) AND Series = (?);', (bookname, series, ))
        bookid = cur.fetchone()[0]
        cur.execute('SELECT AuthorID FROM Author WHERE FirstName = (?) AND LastName = (?);', (authorFirst, authorLast, ))
        authorid = cur.fetchone()[0]

        #adding additional parts to the book
        cur.execute('INSERT INTO Quotes (Quote, BookID) \
           VALUES (?, ?)', (quote, bookid, ))
        db.commit()
        cur.execute('INSERT INTO OwnReview (Rating, SmallReview, BookID) \
            VALUES (?, ?, ?);', (rating, review, bookid))
        db.commit()
        cur.execute('INSERT INTO ReadingStatus (Status, WhereAt, BookID) \
            VALUES (?, ?, ?);', (status, whereAt, bookid))
        db.commit()

        #if the author already exists it is joined with the book here where the new author is also joined
        cur.execute('INSERT INTO BookAuthorJoin VALUES (?, ?);', (bookid, authorid))
        db.commit()

        print('Book added')

    return


def changeReading():
    bookname = input('Give the name of the book: ')
    series = input('Give the series of the book: ')
    status = input('Status(not started/started/complete): ')
    whereAt = int(input('What page are you at: '))

    #bookid was found using the book information
    cur.execute('SELECT BookID FROM Book WHERE Name = (?) AND Series = (?);', ( bookname, series, ))
    bookid = cur.fetchone()

    cur.execute('UPDATE ReadingStatus SET Status = (?), WhereAt = (?) \
        WHERE BookID = (?);', (status, whereAt, bookid[0]))
    db.commit()

    return

def modifyReview():
    
    bookname = input('Give the name of the book: ')
    series = input('Give the series of the book: ')
    rating = int(input('Give the rating(1-5): '))
    review = input('Small written review: ')

    #bookid was found using the book information
    cur.execute('SELECT BookID FROM Book WHERE Name = (?) AND Series = (?);', ( bookname, series, ))
    bookid = cur.fetchone()

    cur.execute('INSERT INTO SET Rating = (?), SmallReview = (?) \
        WHERE BookID = (?);', (rating, review, bookid[0]))
    db.commit()
    return

def addQuote():

    bookname = input('Give the name of the book: ')
    series = input('Give the series of the book: ')
    quote = input("Write the quote here: ")


    cur.execute('SELECT BookID FROM Book WHERE Name = (?) AND Series = (?);', ( bookname, series, ))
    bookid = cur.fetchone()[0]

    cur.execute('INSERT INTO Quotes (Quote, BookID) \
           VALUES (?, ?)', (quote, bookid, ))
    db.commit()

    return

def printBook():

    bookname = input('Give the name of the book: ')
    series = input('Give the series of the book: ')
    cur.execute('SELECT BookID FROM Book WHERE Name = (?) AND Series = (?);', ( bookname, series, ))
    bookid = cur.fetchone()[0]

    
    cur.execute('SELECT Book.Name, Book.Series, Book.Genre, Book.ReleaseYear, Book.Pages FROM BookAuthorJoin \
        INNER JOIN Book ON Book.BookID = BookAuthorJoin.BookID \
        WHERE BookAuthorJoin.BookID = (?);', (bookid, ))
    bookAuthor = cur.fetchone()

    cur.execute('SELECT Bookshelf.Bookshelf, Bookshelf.Shelf, \
            OwnReview.Rating, OwnReview.SmallReview, ReadingStatus.Status, ReadingStatus.whereAt FROM Book \
        INNER JOIN Bookshelf ON Bookshelf.BookshelfID = Book.BookshelfID \
        INNER JOIN ReadingStatus ON ReadingStatus.BookID = Book.BookID \
        INNER JOIN OwnReview ON OwnReview.BookID = Book.BookID \
        WHERE Book.BookID = (?);', (bookid, ))
    bookInfo = cur.fetchone()

    for row in cur.execute('SELECT Author.FirstName, Author.LastName FROM BookAuthorJoin \
        INNER JOIN Author ON Author.AuthorID = BookAuthorJoin.AuthorID \
        INNER JOIN Book ON Book.BookID = BookAuthorJoin.BookID \
        WHERE BookAuthorJoin.BookID = (?);', (bookid, )):
        print("Author: {} {}".format(row[0], row[1], ))


    print("Book name {}, series {} and genre {}".format(bookAuthor[0], bookAuthor[1], bookAuthor[2]))
    print("Book's release year {} and number of pages {}".format(bookAuthor[3], bookAuthor[4]))
    print("Bookmark {} on page {}".format(bookInfo[4], bookInfo[5]))
    print("Shelf placing: {} {} shelf".format(bookInfo[0], bookInfo[1]))
    print("Your quotes of the book: ")

    for row in cur.execute('SELECT Quote FROM Quotes \
        INNER JOIN Book ON Book.BookID = Quotes.BookID \
        WHERE Book.BookID = (?);', (bookid, )):
        print(row[0])

    print("Your review {}/5\n{}".format(bookInfo[2], bookInfo[3]))
    return

main()