import mysql.connector

student_number = input("Enter your student number: ")

db = mysql.connector.connect(
    host="35.242.205.66",
    user=f"student{student_number}",
    password="pythonwsei",
    database="database_os_system_eu_lab"
)

cursor = db.cursor()

query = """
SELECT 
    (h.nr_of_households_with_comp * w.win10 / 100) AS estimated_win10_households
FROM 
    eu_households_with_desktop_computer h
JOIN 
    windows_vs_other_os o ON h.month = o.month
JOIN 
    windows_os_versions w ON o.month = w.month
WHERE 
    h.month = 'July 2016' AND o.month = 'July 2016' AND w.month = 'July 2016';
"""

cursor.execute(query)
result = cursor.fetchone()

if result:
    print(f"Estimated number of households using Windows 10 in July 2016: {result[0]}")
else:
    print("No data found for July 2016")

cursor.close()
db.close()
