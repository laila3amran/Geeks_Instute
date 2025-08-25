SELECT * FROM customer ;

SELECT first_name,last_name AS full_name FROM customer;

SELECT DISTINCT create_date  FROM customer ; 

SELECT * FROM customer ORDER BY first_name DESC ; 

SELECT film_id,title,description,release_year,rental_rate FROM film ORDER BY rental_rate ASC ; 

SELECT c.first_name,
       c.last_name ,
	   a.address,
	   a.phone,
	   a.district
	   FROM customer c
	   INNER JOIN address a ON c.address_id = a.address_id WHERE a.district='Texas';


SELECT * FROM film WHERE film_id=15 OR  film_id=150; 
SELECT * FROM film WHERE film_id in (15, 150);


SELECT film_id, title, description, length, rental_rate FROM film Where title='Alone Trip ';

SELECT film_id, title, description, length, rental_rate FROM film Where title like 'Al%';

select title,replacement_cost from film  order by replacement_cost ASC limit 10 ;

select title,replacement_cost from film  order by replacement_cost ASC limit 10 offset 10  ;

select c.first_name,
       c.last_name,
	   p.amount,
	   p.payment_date
	   from customer c 
	   INNER JOIN payment p ON c.customer_id = p.customer_id 
	   order by p.customer_id ASC  ;

select f.title,
       f.description,
       i.inventory_id,
       i.last_update
       from film f
	   left JOIN inventory i 
	        ON f.film_id=i.film_id 
			where i.film_id IS NULL ;


select c.city,
       coun.country
	   from city c
	   INNER JOIN country coun ON c.country_id = coun.country_id ;


select c.customer_id,
       c.first_name,
	   c.last_name,
	   p.amount,
	   p.payment_date,
	   p.staff_id
      from customer c 
	  INNER JOIN payment p ON c.customer_id= p.customer_id
	  order by p.staff_id ; 



	   
       
			





