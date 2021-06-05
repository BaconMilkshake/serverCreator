import psycopg2



conn = psycopg2.connect(
    host="db",
    database="backend",
    user="postgres",
    password="Mv3qCSJwMkRr9FPzTsRehc5MxewQYC9",
    port="5432")

cursor = conn.cursor()

def initialise(): #does adds needed tables if does not already exist
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS accounts (
   username VARCHAR(50) UNIQUE NOT NULL,
   password VARCHAR(50) NOT NULL,
   user_id VARCHAR(50) UNIQUE NOT NULL
);
    ''')
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS servers (
   owner_user_id VARCHAR(50) NOT NULL,
   aws_server_id VARCHAR(50) UNIQUE NOT NULL

);
    ''')
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS time_stamps (
   user_id VARCHAR(50) NOT NULL,
   start_time TIMESTAMP  NOT NULL,
   stop_time TIMESTAMP
);
    ''')
    conn.commit()
    