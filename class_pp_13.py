import sqlite3
"""
connection = sqlite3.connect(r"C:\Users\Emre\Downloads\SQLiteDatabaseBrowserPortable\emre1.db")
command = "INSERT INTO Clients (ID, Name, Surname) VALUES (1, 'Tim ', 'JAMES')"
connection.execute(command)
connection.comit()
connection.close
"""

with sqlite3.connect(r"C:\Users\Emre\Downloads\SQLiteDatabaseBrowserPortable\emre1.db")  as conn:
    command = "INSERT INTO Clients (ID, Name, Surname) VALUES (1, 'Tim ', 'JAMES')"
    conn.execute(command)