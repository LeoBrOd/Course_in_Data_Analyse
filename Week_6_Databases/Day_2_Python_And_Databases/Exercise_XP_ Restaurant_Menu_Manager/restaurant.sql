create table Menu_Items (
	item_id SERIAL PRIMARY KEY,
	item_name VARCHAR(30) unique NOT NULL,
	item_price SMALLINT DEFAULT 0
)

select * from Menu_Items

drop table Menu_Items

