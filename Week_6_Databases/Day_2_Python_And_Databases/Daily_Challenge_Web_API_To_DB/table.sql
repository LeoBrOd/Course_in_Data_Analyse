create table countries (
	id serial primary key, 
	name varchar(255) unique not null, 
	capital varchar(255), 
	flag text not null, 
	subregion varchar(255) not null, 
	population int not null
)

select* from countries