import psycopg2

# Connect to the PostgresSQL database

connection = psycopg2.connect(
    host = "host",
    database = "wifi",
    user = "root",
    password = "password"
)

connection.close()