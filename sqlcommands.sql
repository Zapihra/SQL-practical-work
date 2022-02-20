CREATE TABLE Bookshelf (
    BookshelfID int NOT NULL PRIMARY KEY UNIQUE AUTOINCREMENT,
    Bookshelf  varchar (20),
    Shelf int
);

CREATE TABLE Book (
    BookID INT NOT NULL PRIMARY KEY UNIQUE AUTOINCREMENT,
    Name varchar (50) NOT NULL,
    Series varchar (50),
    Genre varchar (20) NOT NULL,
    ReleaseYear int NOT NULL,
    Pages int NOT NULL,
    BookshelfID int NOT NULL,
    FOREIGN KEY (BookshelfID) REFERENCES Bookshelf (BookshelfID)
);

CREATE TABLE ReadingStatus (
    StatusID int NOT NULL PRIMARY KEY UNIQUE AUTOINCREMENT,
    Status varchar (20),
    WhereAt int,
    BookID int NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Book (BookID)
);

CREATE TABLE Quotes (
    QuoteID int NOT NULL PRIMARY KEY UNIQUE AUTOINCREMENT,
    Quote varchar (200),
    BookID int NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Book (BookID)
);

CREATE TABLE OwnReview (
    RatingID int NOT NULL PRIMARY KEY UNIQUE AUTOINCREMENT,
    Rating int,
    SmallReview varchar (500),
    BookID int NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Book (BookID)
);

CREATE TABLE Author (
    AuthorID int NOT NULL PRIMARY KEY UNIQUE AUTOINCREMENT,
    FirstName varchar (20) NOT NULL,
    LastName varchar (20),
    ReleasedBooks int NOT NULL
);

CREATE TABLE BookAuthorJoin (
    BookID int NOT NULL,
    AuthorID int NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Book (BookID),
    FOREIGN KEY (AuthorID) REFERENCES Author (AuthorID)
);


