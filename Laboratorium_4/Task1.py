import requests
import mysql.connector
from getpass import getpass
import pandas as pd
import logging 

logging.basicConfig(level = logging.INFO)

class RandomUserDataIngestor:
    """
    Class to fetch random user data from the Random User API and save it into a MySQL table.

    Attributes:
        host (str): Database host address.
        user (str): Database username.
        password (str): Database password.
        database (str): Database name.
        table_name (str): Name of the table in the database.
    """
    
    def __init__(self, host: str, user: str, password: str, database: str, table_name: str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table_name = table_name

    def fetch_random_users(self, count: int) -> pd.DataFrame:
        """
        Fetches random users from the Random User API.

        Args:
            count (int): Number of users to fetch.

        Returns:
            pd.DataFrame: DataFrame containing user data.
        """
        response = requests.get(f"https://randomuser.me/api/?results={count}")
        response.raise_for_status()
        data = response.json()["results"]

        users_data = {
            "imie": [user["name"]["first"] for user in data],
            "nazwisko": [user["name"]["last"] for user in data],
            "adres": [f'{user["location"]["street"]["number"]} {user["location"]["street"]["name"]}, '
                      f'{user["location"]["city"]}, {user["location"]["state"]}, '
                      f'{user["location"]["country"]}, {user["location"]["postcode"]}' for user in data],
            "plec": [user["gender"] for user in data],
            "wiek": [user["dob"]["age"] for user in data],
            "email": [user["email"] for user in data]
        }

        return pd.DataFrame(users_data)

    def create_table(self, connection):
        """
        Creates a table in the database if it does not exist.

        Args:
            connection: Database connection object.
        """
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            imie VARCHAR(255) NOT NULL,
            nazwisko VARCHAR(255) NOT NULL,
            adres VARCHAR(255) NOT NULL,
            plec VARCHAR(50) NOT NULL,
            wiek INT NOT NULL,
            email VARCHAR(255) NOT NULL
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
            connection.commit()

    def insert_users(self, connection, users_data: pd.DataFrame):
        """
        Inserts user data into the table.

        Args:
            connection: Database connection object.
            users_data (pd.DataFrame): DataFrame containing user data.
        """
        insert_query = f"""
        INSERT INTO {self.table_name} (imie, nazwisko, adres, plec, wiek, email)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        data_tuples = list(users_data.itertuples(index=False, name=None))

        with connection.cursor() as cursor:
            cursor.executemany(insert_query, data_tuples)
            connection.commit()

    def get_user_count(self, connection) -> int:
        """
        Returns the number of users in the table.

        Args:
            connection: Database connection object.

        Returns:
            int: Number of users in the table.
        """
        query = f"SELECT COUNT(*) FROM {self.table_name}"
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            return result[0]

    def run(self, user_count: int):
        """
        Main method to run the process of fetching user data and saving it to the database.

        Args:
            user_count (int): Number of users to fetch and save.
        """
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

        try:
            self.create_table(connection)
            users_data = self.fetch_random_users(user_count)
            self.insert_users(connection, users_data)
            user_count_in_db = self.get_user_count(connection)
            print(f"Number of users saved: {user_count_in_db}")
        finally:
            connection.close()

if __name__ == "__main__":
    host = "35.242.205.66"
    user = "student1"
    password = getpass("Input password: ")
    database = "python_wsei_db"
    table_name = "przemyslaw_niedziela"  
    
    ingestor = RandomUserDataIngestor(host, user, password, database, table_name)
    ingestor.run(user_count=30)
