import psycopg2

def get_db_connection():
    conn = psycopg2.connect(host="172.17.0.1",
                            database="intranet",
                            user="postgres",
                            password='changeme')
    return conn