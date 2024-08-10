CREATE TABLE movies(
movie_id SERIAL,
movie_title VARCHAR (50) NOT NULL,
movie_story TEXT,
actor_playing_id INTEGER,
PRIMARY KEY (movie_id),
FOREIGN KEY (actor_playing_id) REFERENCES actors (actor_id)
);

INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
    ( 'Good Will Hunting', 
    'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
    (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon')),
    ( 'Oceans Eleven', 
    'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
    (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'));

--Create another table producers, with a foreign key : the id of a movie. The producers table is linked to the movies table
--Insert some record
--Display with INNER JOIN
CREATE TABLE producers (
  producer_id serial PRIMARY KEY,
  producer_name VARCHAR(50) NOT NULL,
  FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
); 

INSERT INTO producers (name, movie_id)
VALUES ()
