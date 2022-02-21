CREATE TABLE Bookshelf (
    BookshelfID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Bookshelf  varchar (20),
    Shelf int
);

CREATE TABLE Book (
    BookID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name varchar (50) NOT NULL,
    Series varchar (50),
    Genre varchar (20) NOT NULL,
    ReleaseYear INTEGER NOT NULL,
    Pages INTEGER NOT NULL,
    BookshelfID INTEGER NOT NULL,
    FOREIGN KEY (BookshelfID) REFERENCES Bookshelf (BookshelfID)
);

CREATE TABLE ReadingStatus (
    StatusID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Status varchar (20),
    WhereAt INTEGER,
    BookID INTEGER NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Book (BookID)
);

CREATE TABLE Quotes (
    QuoteID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Quote varchar (200),
    BookID INTEGER NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Book (BookID)
);

CREATE TABLE OwnReview (
    RatingID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Rating INTEGER,
    SmallReview varchar (500),
    BookID INTEGER NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Book (BookID)
    CHECK (Rating <=5);
);

CREATE TABLE Author (
    AuthorID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    FirstName varchar (20) NOT NULL,
    LastName varchar (20),
    ReleasedBooks INTEGER NOT NULL
);

CREATE TABLE BookAuthorJoin (
    BookID INTEGER NOT NULL,
    AuthorID INTEGER NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Book (BookID),
    FOREIGN KEY (AuthorID) REFERENCES Author (AuthorID)
);