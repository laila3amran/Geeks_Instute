-- Exercice 1
SELECT * FROM language;


SELECT f.title,
       f.description,
       l.name 
 FROM film f 
INNER JOIN language l ON f.language_id= l.language_id;



SELECT f.title,
f.description,
l.name From film f
RIGHT JOIN language l ON f.language_id= l.language_id; 


-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.

CREATE TABLE  new_film(
    id SERIAL PRIMARY KEY ,
    name VARCHAR(100) NOT NULL 

);
INSERT INTO new_film (name) 
VALUES ('Inception'), ('The Matrix'), ('Interstellar');



CREATE TABLE customer_review(
    review_id  SERIAL PRIMARY KEY ,
    film_id INTEGER REFERENCES film(film_id) ON DELETE CASCADE ,
    language_id INTEGER REFERENCES language(language_id) ,
    title VARCHAR(255) NOT NULL,
    score INT CHECK(score BETWEEN 1 AND 5),
    review_text TEXT NOT NULL,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

INSERT INTO customer_review (review_id,film_id,language_id,title,score,review_text,last_update)
VALUES (1, 1, 1, 'Amazing movie!', 5, 'I loved the visual effects and the storyline.', DEFAULT),
       (2, 2, 1, 'Mind-bending!', 4, 'A great sci-fi film with a complex plot.', DEFAULT),
       (3, 3, 1, 'A masterpiece', 5, 'The direction and acting were top-notch.', DEFAULT);

    
DELETE FROM new_film WHERE name='Interstellar'; 

-- Q7
-- When you delete a film from the film table (not new_film), all reviews linked to that film are automatically deleted from customer_review.



-- Exercice 2

-- Q1
UPDATE film SET language_id=1 WHERE film_id=1;

UPDATE film
SET language_id = 1
WHERE film_id IN (15, 20, 30);

-- Q2
-- The customer table has foreign keys:

-- store_id → references store(store_id)

-- address_id → references address(address_id)

--  This means when inserting a new customer, the store_id and address_id must already exist in their respective tables.
-- Otherwise, the insert will fail due to foreign key violation.


-- Q3

DROP TABLE customer_review;

-- Q4
SELECT COUNT(*)
FROM rental
WHERE return_date IS NULL;

-- Q5
SELECT f.film_id, f.title, f.rental_rate
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NULL
ORDER BY f.rental_rate DESC
LIMIT 30;


-- Q6
-- 1
SELECT f.title, f.description
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'PENELOPE'
  AND a.last_name = 'MONROE'
  AND f.description ILIKE '%sumo%';

-- 2
SELECT title, description, length, rating
FROM film
WHERE length < 60
  AND rating = 'R'
  AND description ILIKE '%documentary%';

-- 3
SELECT DISTINCT f.title, f.description
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN payment p ON r.rental_id = p.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'MATTHEW'
  AND c.last_name = 'MAHAN'
  AND p.amount > 4.00
  AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- 4
SELECT DISTINCT f.title, f.description, f.replacement_cost
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'MATTHEW'
  AND c.last_name = 'MAHAN'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1;














