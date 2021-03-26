import mysql.connector

mydatabase = mysql.connector.connect(
host ="localhost",
username = "root",
password = "pvi@2020",
database = "phoneDB"
)
mypointer = mydatabase.cursor()

