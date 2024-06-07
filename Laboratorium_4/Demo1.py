from getpass import getpass 
import mysql.connector
import logging

logging.basicConfig(level = logging.INFO)

try: 
    with mysql.connector.connect(
        host="35.242.205.66",
        user= "student1",
        password= getpass("input password: "),
        database="python_wsei_db",
    ) as connection:
        
        with connection.cursor() as cursor:
            query = """
            SELECT * FROM wsei_student
            WHERE ocena_aap >= 4.5 AND rok_rozpoczecia = 2024;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            
            for row in results:
                logging.info(row)
                
except Exception as e:
    logging.warning(f"Connection with exception: {e}")
    
    
    
    