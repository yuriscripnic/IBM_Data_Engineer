CREATE KEYSPACE training  
WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};

use training;

CREATE TABLE movies(
movie_id int PRIMARY KEY,
movie_name text,
year_of_release int
);

insert into movies (movie_id, movie_name, year_of_release) values (1,'Toy Story',1995);

select * from movies;

select movie_name from movies where movie_id = 1;
update movies set year_of_release=1996 where movie_id = 4;
select * from movies where movie_id = 4;

--  movie_id | movie_name | year_of_release
-- ----------+------------+-----------------
--         4 |       null |            1996

delete from movies where movie_id =5;


INSERT into movies(
movie_id, movie_name, year_of_release)
VALUES (6,'Twister',1997);

UPDATE movies
SET year_of_release = 1996
WHERE movie_id = 6;

DELETE from movies
WHERE movie_id = 6;

ALTER TABLE movies
ADD genre text;

