--In the dvdrental database write a query to select all the columns from the “customer” table.
select * from customer

--Write a query to display the names (first_name, last_name) using an alias named “full_name”.
select concat(first_name, ' ', Last_name) as full_name from customer

--Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).
select distinct create_date from customer

--Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
select * from customer order by first_name desc

--Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
select film_id, title, description, release_year, rental_rate from film order by rental_rate asc

--Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.
select address, phone from address where district='Texas'

--Write a query to retrieve all movie details where the movie id is either 15 or 150.
select * from film where film_id=15 or film_id=150

--Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.
select film_id, title, description, length, rental_rate from film 
--where title='Three mushketeers'
where title='Alone Trip'
--No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
select film_id, title, description, length, rental_rate from film 
where title like 'Al%'

--Write a query which will find the 10 cheapest movies.
select title, rental_rate from film order by rental_rate asc limit 10

--Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
--Bonus: Try to not use LIMIT.
SELECT title, rental_rate 
FROM (
  SELECT title, rental_rate , ROW_NUMBER() OVER (ORDER BY rental_rate ASC) AS row_num
  FROM film
) AS ranked_data
WHERE row_num between 11 and 20;

--Write a query which will join the data in the customer table and the payment table. You want to get the first name and last name from the curstomer table, as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
select customer.first_name, customer.last_name, payment.amount, payment.payment_date
from customer join payment on payment.customer_id = customer.customer_id
order by customer.customer_id, payment.payment_id

--You need to check your inventory. Write a query to get all the movies which are not in inventory.
SELECT title from film left join inventory on film.film_id=inventory.film_id
where inventory.film_id is null

--Write a query to find which city is in which country.
select DISTINCT country, city from city join country on city.country_id=country.country_id
order by country.country

--Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.
select staff.first_name,staff.last_name, payment.customer_id, customer.first_name, customer.last_name, amount, payment_date 
from customer join payment ON  customer.customer_id=payment.customer_id
join staff ON  staff.staff_id=payment.staff_id
order by payment.staff_id