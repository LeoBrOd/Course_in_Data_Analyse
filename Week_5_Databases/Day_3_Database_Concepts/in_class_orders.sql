create table orders (
	id serial primary key,
	customer_id smallint not null,
	order_date date not null, 
	product_name varchar(100) not null, 
	quantity smallint not null, 
	price smallint not null, 
	region varchar(50) not null)

INSERT INTO orders (customer_id, order_date, product_name, quantity, price, region) VALUES
(101, '2024-01-10', 'Laptop', 2, 1200.00, 'North America'),
(102, '2024-01-11', 'Smartphone', 5, 800.00, 'Europe'),
(103, '2024-01-12', 'Office Chair', 1, 150.00, 'Asia'),
(101, '2024-01-13', 'Coffee Maker', 10, 90.00, 'North America'),
(104, '2024-01-14', 'Headphones', 3, 200.00, 'Europe'),
(105, '2024-02-15', 'Laptop', 1, 1200.00, 'Europe'),
(102, '2024-02-16', 'Smartphone', 2, 800.00, 'North America'),
(103, '2024-02-17', 'Office Chair', 5, 150.00, 'Europe'),
(106, '2024-02-18', 'Coffee Maker', 7, 90.00, 'Asia'),
(107, '2024-02-19', 'Headphones', 4, 200.00, 'North America'),
(108, '2024-03-10', 'Laptop', 3, 1200.00, 'Asia'),
(109, '2024-03-11', 'Smartphone', 6, 800.00, 'Europe'),
(110, '2024-03-12', 'Office Chair', 2, 150.00, 'North America'),
(111, '2024-03-13', 'Coffee Maker', 8, 90.00, 'Europe'),
(112, '2024-03-14', 'Headphones', 5, 200.00, 'Asia');

select * from orders

-- *Query 1*: Find the total quantity and total sales for each product in each region, but only include products where the total sales amount is greater than $2000.
SELECT product_name, region, SUM(quantity) AS total_quantity, SUM(quantity*price) AS total_sales 
	FROM orders 
	group by product_name, region
	having SUM(quantity*price)>2000

--*Query 2*: Calculate the average price of products ordered in each month, grouped by product name. Only include products where the average price is higher than $500.
select extract (month from order_date) as order_month, product_name, avg(price) as averag_price
	FROM orders 
	group by order_month, product_name
	having avg(price)>500
	order by order_month,product_name

--*Query 3*: List the total number of orders and the total quantity for each customer in each region, but only include customers who have placed more than 2 orders.
select customer_id, region, count(id) as total_orders, sum(quantity) as total_quantity
	from orders 
	group by customer_id, region
	order by customer_id, region