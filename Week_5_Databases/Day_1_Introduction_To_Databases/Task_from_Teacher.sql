create table products (
product_id SERIAL PRIMARY KEY,
product_name VARCHAR (100) NOT NULL,
category VARCHAR (50) NOT NULL,
price DECIMAL NOT NULL,
stock_quantity INT NOT NULL,
supplier VARCHAR (100))

INSERT INTO products (product_name, category, price, stock_quantity, supplier)
VALUES ('laptop', 'Electronics', 1200, 50, 'TechSupplier Inc'),
('smartphone', 'Electronics', 800, 200, 'MobileWorld'),
('office chair', 'Furniture', 150, 100, 'Furniture Co'),
('coffee maker', 'Appliances', 90, 150, 'HomeGoods'),
('headphones', 'Electronics', 200 ,75, 'AudioHub')

select * from products where category='Electronics' and price>
	(select avg(price) from products where category ='Electronics')
order by product_name asc

select product_name, price*stock_quantity as total_value, supplier from products where (price*stock_quantity)>= 10000
order by supplier asc, total_value desc

