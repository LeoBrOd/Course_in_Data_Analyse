create table students (
	id serial primary key,
	last_name varchar(30) not null,
	first_name varchar(30) not null,
	birth_date date not null)

insert into students (first_name, last_name, birth_date)
values ('Marc',	'Benichou',	'02/11/1998'),
('Yoan',	'Cohen',	'03/12/2010'),
('Lea',	'Benichou',	'27/07/1987'),
('Amelia',	'Dux',	'07/04/1996'),
('David',	'Grez',	'14/06/2003'),
('Omer',	'Simpson',	'03/10/1980')

insert into students (last_name, first_name, birth_date)
values ('Brodskyi', 'Leonid','13/08/1991')

-- Fetch all of the data from the table.
select * from students 

-- Fetch all of the students first_names and last_names.
select first_name, last_name from students 

-- Fetch the student which id is equal to 2.
select first_name, last_name from students where id=2

-- Fetch the student whose last_name is Benichou AND first_name is Marc.
select first_name, last_name from students where last_name='Benichou' and first_name='Marc'

-- Fetch the students whose last_names are Benichou OR first_names are Marc.
select first_name, last_name from students where last_name='Benichou' or first_name='Marc'

--Fetch the students whose first_names contain the letter a.
select first_name, last_name from students where first_name ilike '%a%'

--Fetch the students whose first_names start with the letter a.
select first_name, last_name from students where first_name ilike 'a%'
	
--Fetch the students whose first_names end with the letter a.
select first_name, last_name from students where first_name ilike '%a'

--Fetch the students whose second to last letter of their first_names are a (Example: Leah).
select first_name, last_name from students where first_name ilike '%a_'

--Fetch the students whose id’s are equal to 1 AND 3 .
select first_name, last_name from students where id=1 or id=3

--Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
select * from students where birth_date>'1/01/2000'

-- XP Gold Part
--Fetch the first four students. You have to order the four students alphabetically by last_name.
select first_name, last_name, birth_date from students order by last_name limit 4

select first_name, last_name, birth_date from students where id in (select id from students limit 4) order by last_name

--Fetch the details of the youngest student.
select first_name, last_name, birth_date from students where birth_date=(select max(birth_date) from students)

--Fetch three students skipping the first two students.
select first_name, last_name, birth_date from students offset 2 limit 3