-- CREATE TABLE actors(
-- actor_id SERIAL PRIMARY KEY,
-- first_name VARCHAR (50) NOT NULL,
-- last_name VARCHAR (100) NOT NULL,
-- age DATE NOT NULL,
-- number_oscars SMALLINT NOT NULL
-- );

-- INSERT INTO actors(first_name,last_name,age,number_oscars)
-- VALUES('Matt','Damon','1996-09-18', 5);
-- INSERT INTO actors(first_name,last_name,age,number_oscars)
-- VALUES('George','Clooney','1996-09-18', 2);
-- INSERT INTO actors(first_name,last_name,age,number_oscars)
-- VALUES ('laila','amran','1996-09-18',10);
-- INSERT INTO actors(first_name,last_name,age,number_oscars)
-- VALUES ('Rachida', 'Ouaghache','1996-09-18',14);
-- INSERT INTO actors(first_name,last_name,age,number_oscars)
-- VALUES 
--       ('kadija','amran','1996-09-18',4),
--       ('laila','amran','1996-09-18',10),
-- 	  ('Rachida','Ouaghache','1996-09-18',1);

-- SELECT * FROM actors;
-- Qusetion 1
SELECT  COUNT(*) AS total_actors FROM actors;
-- Qusetion 2
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Brad', '', '1970-12-18', 3);
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Tom', NULL, '1962-07-03', 2); 

-- If I insert an empty string ('') into last_name, PostgreSQL will accept it (because it’s technically a string, not NULL).

--If I try to insert NULL into any of the NOT NULL fields (first_name, last_name, age, number_oscars), PostgreSQL will throw an error:




	  