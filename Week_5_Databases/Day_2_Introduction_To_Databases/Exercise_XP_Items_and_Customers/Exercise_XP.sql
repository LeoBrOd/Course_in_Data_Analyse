create table items (
	item_id serial primary key,
	item_name varchar (100) not null,
	item_price decimal not null
)
	
create table customers (
	customer_id serial primary key,
	customer_name varchar (30) not null,
	customer_lastname varchar (40) not null
)

insert into items (item_name, item_price)
values ('Small Desk',100 ), ('Large desk', 300), ('Fan', 80)

insert into customers (customer_name,customer_lastname)
values ('Greg', 'Jones'), ('Sandrsa', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'),('Melanie', 'Johnson')

select * from items

select * from items where item_price >80

select * from items where item_price <300

select * from customers where customer_lastname='Smith'

select * from customers where customer_lastname='Jones'

select * from customers where customer_name!='Scott'