-- All items, ordered by price (lowest to highest)
select * from items order by item_price asc

--Items with a price above 80 (80 included), ordered by price (highest to lowest).
select * from items where item_price>=80  order by item_price desc

--The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
select customer_name, customer_lastname from customers order by customer_name limit 3

--All last names (no other columns!), in reverse alphabetical order (Z-A)
select customer_lastname from customers order by customer_lastname desc