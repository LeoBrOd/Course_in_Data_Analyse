--Exercise 1: DVD Rental
--Get a list of all the languages, from the language table.
select name from language

--Get a list of all films joined with their languages – select the following details : film title, description, and language name.
select title, description, name from film
join language on film.language_id=language.language_id

--Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
select title, description, name from film
right outer join language on film.language_id=language.language_id

--Create a new table called new_film with the following columns : id, name. Add some new films to the table.
create table new_film (
	id serial primary key,
	name varchar(100) unique not null
)

-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
	-- review_id – a primary key, non null, auto-increment.
	-- film_id – references the new_film table. The film that is being reviewed.
	-- language_id – references the language table. What language the review is in.
	-- title – the title of the review.
	-- score – the rating of the review (1-10).
	-- review_text – the text of the review. No limit on the length.
	-- last_update – when the review was last updated.

create table customer_review(
	review_id serial not null primary key,
	film_id int not null,
	foreign key (film_id) references new_film(id) on delete cascade,
	language_id int not null,
	foreign key (language_id) references language(language_id) on delete set null,
	title varchar(100) not null,
	score float not null check(score between 1 and 10),
	review_text text not null,
	last_update timestamp not null default CURRENT_TIMESTAMP
)

insert into new_film (name)
values ('Fallout'), ('Baby Reindeer'),('The Ministry of Ungentlemanly Warfare')

--Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
insert into customer_review (film_id, language_id, title, score, review_text)
values (1, 1,'The End of the World is Going to be Weird on Prime Video’s Quirky, Clever Adaptation of Fallout', 8.5, 'Adapting open-world games can be a great challenge for film and TV creatives because they don’t have the handy-dandy narrative skeleton to convey what made a game so successful. How do you adapt a game with such little storytelling structure to a genre that requires it? Sometimes it baffles creators and the resulting adaptation feels like the product of someone who never really played the game or understood why it was a hit (see all versions to date of “Hitman.”) The team behind Prime Video’s highly-anticipated adaptation of “Fallout” is too smart for that mistake. Brilliant TV voices like Jonathan Nolan and Lisa Joy have taken the “Fallout” sandbox and populated it with their own toys, producing a show with archetypes, settings, and ideas from the Bethesda games but its own strange voice at the same time, one that somehow gets David Lynch, George Miller, Sergio Leone, and Beaver Cleaver to sing in harmony.' ),
(2,2,'Baby Reindeer 2024 Tv Series Review Trailer',7.9,' The Edinburgh Festival is a captivating but unpredictable melting pot of theatrical experiences. Its a place where you can go from being deeply moved by one performance to laughing uncontrollably at the next. Amid the diverse range of shows, some are undeniably brilliant, while others fall short of expectations.')

delete from new_film where name='Baby Reindeer'
-- it will also remove review from customer_review table

--Exercise 2 : DVD Rental
--Use UPDATE to change the language of some films. Make sure that you use valid languages.
update film set language_id=2 where film_id%2=0

--Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
--customer.address_id references address.address_id

--We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
drop table customer_review

--find out how many rentals are still outstanding (ie. have not been returned to the store yet)
select * from rental where return_date is null

--Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
select title, rental_rate from film join inventory
on film.film_id=inventory.film_id
where inventory.film_id in (Select film_id from inventory 
join rental on inventory.inventory_id=rental.inventory_id
where return_date is null) order by rental_rate desc limit 30
	
--Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
select title from film where lower(film.description) like '%sumo%' and film.film_id in
	(select film_id from film_actor where film_actor.actor_id in (select actor_id from actor
		where actor.first_name='Penelope' and actor.last_name='Monroe'))
-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
select title from film where rating = 'R' and film.length<60 limit 1
-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
select title from film where film.film_id in (select film_id from inventory
where inventory.inventory_id in (select inventory_id from rental
where rental.customer_id in (select customer_id from customer 
where customer.first_name = 'Matthew' and customer.last_name = 'Mahan') 
and rental.return_date between '28.07.2005' and '01.08.2005')) and film.rental_rate>4
-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
select title, replacement_cost from film 
where lower(film.description) like '%boat%' or lower(film.title) like '%boat%'
and film.film_id in (select film_id from inventory 
where inventory.inventory_id in (select inventory_id from rental
where rental.customer_id in (select customer_id from customer 
where customer.first_name = 'Matthew' and customer.last_name = 'Mahan')))
order by replacement_cost desc limit 1