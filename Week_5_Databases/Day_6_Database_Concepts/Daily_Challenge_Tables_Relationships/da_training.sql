--Create 2 tables : Customer and Customer profile. They have a One to One relationship.
-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)
CREATE TABLE  customer (
id serial primary key,
first_name VARCHAR(255),
last_name VARCHAR(255) NOT NULL
)

CREATE TABLE  customer_profile (
id serial primary key,
isLoggedIn BOOLEAN not NULL DEFAULT false,	
customer_id integer not NULL,
FOREIGN KEY (customer_id) REFERENCES customer(id)
)

--Insert those customers
insert into customer (first_name, last_name)
values ('John', 'Doe'), ('Jerome', 'Lalu'), ('Lea', 'Rive')

--Insert those customer profiles, use subqueries
insert into customer_profile (isLoggedIn, customer_id)
values (true,1), (false,2)

-- Use the relevant types of Joins to display:
-- The first_name of the LoggedIn customers
select first_name from customer join customer_profile on customer_profile.customer_id = customer.id
where isLoggedIn = 'true'
-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
select first_name, isLoggedIn  from customer left outer join customer_profile on customer_profile.customer_id = customer.id
-- The number of customers that are not LoggedIn
select count (isLoggedIn) from customer_profile where customer_profile.isLoggedIn ='false'

--Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL
create table book(
book_id SERIAL PRIMARY KEY, 
title VARCHAR(255) NOT NULL, 
author VARCHAR(255) NOT NULL
)

--Insert those books
insert into book (title, author)
values ('Alice In Wonderland', 'Lewis Carroll'),
		('Harry Potter', 'J.K Rowling'),
		('To kill a mockingbird', 'Harper Lee')

--Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age. Make sure that the age is never bigger than 15 (Find an SQL method);
create TABLE STUDENT (
student_id SERIAL PRIMARY KEY, 
name VARCHAR(255) NOT NULL UNIQUE, 
age INTEGER check (age between 0 and 15)
)

--Insert those students
insert into student (name, age)
VALUES ('John', 12),
		('Lera', 11),
		('Patrick', 10),
		('Bob', 14)

-- Create a table named Library, with the columns :
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date
-- This table, is a junction table for a Many to Many relationship with the Book and Student tables : A student can borrow many books, and a book can be borrowed by many children
-- book_fk_id is a Foreign Key representing the column book_id from the Book table
-- student_fk_id is a Foreign Key representing the column student_id from the Student table
-- The pair of Foreign Keys is the Primary Key of the Junction Table
create table library (
book_fk_id integer,
student_id integer,
borrowed_date date,
FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (student_id) REFERENCES student(student_id)ON DELETE CASCADE ON UPDATE CASCADE,
primary key (book_fk_id, student_id)	
)

--Add 4 records in the junction table, use subqueries
-- insert into library (student_id, book_fk_id, borrowed_date)
-- select student_id from student where name='John',
-- select book_id from book where title='Alice In Wonderland',
-- VALUES('15/02/2022')
insert into library (student_id, book_fk_id, borrowed_date)
VALUES (1,1,'15/02/2022'),(4,3,'03/03/2021'),(2,1,'23/05/2021'),(4,2,'12/08/2021')

-- Display the data
-- Select all the columns from the junction table
select * from library
-- Select the name of the student and the title of the borrowed books
select name, title from student 
join library on student.student_id = library.student_id
join book on book.book_id = library.book_fk_id
-- Select the average age of the children, that borrowed the book Alice in Wonderland
select avg (age) from student
join library on student.student_id = library.student_id
join book on book.book_id = library.book_fk_id
where book.title = 'Alice In Wonderland'
-- Delete a student from the Student table, what happened in the junction table ?
--it will remove data connected to him
delete from student where student.student_id = 1