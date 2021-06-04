import psycopg2



conn = psycopg2.connect(
    host="localhost",
    database="backend",
    user="postgres",
    password="Abcd1234",
    port="5432")