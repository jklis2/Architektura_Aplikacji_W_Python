import mysql.connector
from getpass import getpass

class DatabaseManager:
    """
    Class to manage MySQL database operations.
    
    Attributes:
        host (str): Database host address.
        user (str): Database username.
        password (str): Database password.
        database (str): Database name.
    """
    
    def __init__(self, host: str, user: str, password: str, database: str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def execute_query(self, query: str):
        """
        Executes a query and fetches the result.
        
        Args:
            query (str): SQL query to be executed.
        
        Returns:
            result: Result of the query execution.
        """
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            return result
   
def main():
    host = "35.242.205.66"
    user = "student1"
    password = getpass("Input password: ")
    database = "database_os_system_eu_lab"

    db_manager = DatabaseManager(host, user, password, database)

    query = """
    SELECT 
        h.nr_of_households_with_comp * w.windows * v.win10 AS households_with_win10
        
    FROM eu_households_with_desktop_computer h
    JOIN windows_vs_other_os w ON h.month = w.month
    JOIN windows_os_versions v ON w.month = v.month
    WHERE h.month = '2016-07';
    """
    
    result = db_manager.execute_query(query)
    print(f"Estimated number of European households using  Windows 10 in July 2016: {int(result[0])}")

if __name__ == "__main__":
    main()