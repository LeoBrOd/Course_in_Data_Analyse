CREATE TABLE Authors (
  AuthorID INT PRIMARY KEY,
  Name VARCHAR(255) NOT NULL
);

CREATE TABLE Publishers (
  PublisherID INT PRIMARY KEY,
  Name VARCHAR(255) NOT NULL
);

CREATE TABLE Books (
  BookID INT PRIMARY KEY,
  Title VARCHAR(255) NOT NULL,
  PublisherID INT NOT NULL,
  FOREIGN KEY (PublisherID) REFERENCES Publishers(PublisherID)
);

CREATE TABLE AuthorBook (
  AuthorID INT NOT NULL,
  BookID INT NOT NULL,
  FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID),
  FOREIGN KEY (BookID) REFERENCES Books(BookID),
  PRIMARY KEY (AuthorID, BookID)
);

CREATE TABLE BookDetails (
  BookID INT PRIMARY KEY,
  PublicationDate DATE,
  Pages INT,
  FOREIGN KEY (BookID) REFERENCES Books(BookID)  
  ON DELETE CASCADE  
);

INSERT INTO Authors (AuthorID, Name) VALUES (3, 'Charles Dickens');
INSERT INTO Authors (AuthorID, Name) VALUES (4, 'Virginia Woolf');
INSERT INTO Authors (AuthorID, Name) VALUES (5, 'George Orwell');
-- More Publishers
INSERT INTO Publishers (PublisherID, Name) VALUES (3, 'Oxford University Press');
INSERT INTO Publishers (PublisherID, Name) VALUES (4, 'HarperCollins');
-- More Books
INSERT INTO Books (BookID, Title, PublisherID) VALUES (3, '1984', 4);
INSERT INTO Books (BookID, Title, PublisherID) VALUES (4, 'A Tale of Two Cities', 3);
INSERT INTO Books (BookID, Title, PublisherID) VALUES (5, 'Mrs Dalloway', 4);
INSERT INTO Books (BookID, Title, PublisherID) VALUES (6, 'Animal Farm', 4);
-- More AuthorBook links
INSERT INTO AuthorBook (AuthorID, BookID) VALUES (3, 4);
INSERT INTO AuthorBook (AuthorID, BookID) VALUES (4, 5);
INSERT INTO AuthorBook (AuthorID, BookID) VALUES (5, 3);
INSERT INTO AuthorBook (AuthorID, BookID) VALUES (5, 6);
-- More BookDetails
INSERT INTO BookDetails (BookID, PublicationDate, Pages) VALUES (3, '1949-06-08', 328);
INSERT INTO BookDetails (BookID, PublicationDate, Pages) VALUES (4, '1859-04-30', 544);
INSERT INTO BookDetails (BookID, PublicationDate, Pages) VALUES (5, '1925-05-14', 296);
INSERT INTO BookDetails (BookID, PublicationDate, Pages) VALUES (6, '1945-08-17', 112);

--Query 1: Find the total number of books published by each publisher and the average number of pages for their books.
select Publishers.name, count(Books.BookID) as TotalBooks, avg(BookDetails.pages) as AvgPages
from Publishers
join Books on Publishers.PublisherID=Books.PublisherID
join BookDetails on Books.BookID=BookDetails.BookID
group by Publishers.Name

--Query 2: List all authors who have written more than one book, including the titles of these books.
select Authors.Name, string_agg(Books.Title, ',') as Titles
from Authors
join AuthorBook on Authors.AuthorID=AuthorBook.AuthorID
join Books on AuthorBook.BookID=Books.BookID
group by Authors.Name
having count(Books.BookID)>1

--Query 3: Find publishers who have published books with more than 300 pages but none of their books are older than 1950.
SELECT DISTINCT Publishers.Name, Books.Title
FROM Publishers 
JOIN Books ON Publishers. PublisherID = Books. PublisherID 
JOIN BookDetails ON Books. BookID = BookDetails. BookID 
WHERE BookDetails.Pages > 100 
AND NOT EXISTS ( 
	SELECT 1 FROM BookDetails bd 
	WHERE bd. BookID = Books. BookID AND bd. PublicationDate < '1930-01-01'
)