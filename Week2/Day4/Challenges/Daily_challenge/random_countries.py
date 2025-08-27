import requests
import random
import psycopg2

# Step 1: Fetch all countries from API
url = "https://restcountries.com/v3.1/all?fields=name,capital,flag,subregion,population"
response = requests.get(url)
countries = response.json()

# Step 2: Choose 10 random countries
random_countries = random.sample(countries, 10)

# Step 3: Connect to PostgreSQL
connection = psycopg2.connect(
    host="localhost",
    database="your_db",
    user="your_user",
    password="your_password"
)
cursor = connection.cursor()

# Step 4: Insert into database
for c in random_countries:
    name = c["name"]["common"]
    capital = c["capital"][0] if "capital" in c and c["capital"] else None
    flag = c.get("flag")
    subregion = c.get("subregion")
    population = c.get("population")

    cursor.execute("""
        INSERT INTO countries (name, capital, flag, subregion, population)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, capital, flag, subregion, population))

# Step 5: Commit and close
connection.commit()
cursor.close()
connection.close()

print("✅ 10 random countries inserted successfully!")
