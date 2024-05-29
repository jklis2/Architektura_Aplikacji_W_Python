import requests
import mysql.connector

response = requests.get("https://randomuser.me/api/?results=30")
users = response.json()["results"]

db = mysql.connector.connect(
    host="35.242.205.66",
    user="student<numer>",  # Replace <numer> with your student number
    password="pythonwsei",
    database="python_wsei_db"
)

cursor = db.cursor()

table_name = "your_name_or_number"  # Replace this with your name or number
cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        address VARCHAR(255),
        gender VARCHAR(10),
        age INT,
        email VARCHAR(100)
    )
""")

for user in users:
    first_name = user["name"]["first"]
    last_name = user["name"]["last"]
    address = f'{user["location"]["street"]["number"]} {user["location"]["street"]["name"]}, {user["location"]["city"]}, {user["location"]["state"]}, {user["location"]["country"]}'
    gender = user["gender"]
    age = user["dob"]["age"]
    email = user["email"]
    
    cursor.execute(f"""
        INSERT INTO {table_name} (first_name, last_name, address, gender, age, email)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (first_name, last_name, address, gender, age, email))

db.commit()
cursor.close()
db.close()

print("Data has been successfully inserted into the table.")
