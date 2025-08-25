-- Q1
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
-- Subquery: SELECT id FROM SecondTab WHERE id IS NULL → returns {NULL}.

-- Condition becomes: ft.id NOT IN (NULL)

-- But x NOT IN (NULL) is always UNKNOWN in SQL.

-- Result: no rows qualify.

--  Answer: 0



-- Q2
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- Subquery: SELECT id FROM SecondTab WHERE id = 5 → returns {5}.

-- Condition: ft.id NOT IN (5)

-- id=5 → False

-- id=6 → True

-- id=7 → True

-- id=NULL → UNKNOWN (excluded)

-- Rows that qualify: (6, Sharlee), (7, Krish).

--  Answer: 2


-- Q3
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft 
-- WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

-- Subquery: SELECT id FROM SecondTab → returns {5, NULL}.

-- Condition: ft.id NOT IN (5, NULL)

-- Because NULL is present in the list, every comparison becomes UNKNOWN.

-- So no rows qualify.

-- Answer: 0

-- Q4
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

-- Subquery: SELECT id FROM SecondTab WHERE id IS NOT NULL → returns {5}.

-- Condition: ft.id NOT IN (5)

-- id=5 → False

-- id=6 → True

-- id=7 → True

-- id=NULL → UNKNOWN (excluded)

-- Rows that qualify: (6, Sharlee), (7, Krish).

-- Answer: 2


