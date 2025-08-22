CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
	item_name VARCHAR(100) NOT NULL,
	item_price INTEGER NOT NULL
	
);
INSERT INTO  items (item_name,item_price) 
values 
  ('Small Desk',100),
  ('Large desk ',300 ),
  ('Fan ',80)
  ;

CREATE TABLE customers (
   customer_id SERIAL PRIMARY KEY,
   customer_first_name VARCHAR(100) NOT NULL,
   customer_last_name VARCHAR(100) NOT NULL
   
);

INSERT INTO customers (customer_first_name,customer_last_name)
VALUES 
       ('Greg ',' Jones'),
	   ('Sandra  ',' Jones'),
	   ('Scott  ',' Scott '),
	   ('Trevor  ',' Green'),
	   ('Melanie  ',' Johnson')
	   ;


SELECT * FROM items ;
SELECT * FROM items WHERE item_price>80;
SELECT * FROM items WHERE item_price<=300;
SELECT * FROM customers;
SELECT * FROM customers WHERE customer_last_name='Smith';
SELECT * FROM customers WHERE customer_last_name='Jones';
SELECT * FROM customers WHERE customer_first_name !='Scott  ';



