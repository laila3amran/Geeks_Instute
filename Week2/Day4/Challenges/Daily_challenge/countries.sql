CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    capital VARCHAR(255),
    flag VARCHAR(10),
    subregion VARCHAR(255),
    population BIGINT
);

