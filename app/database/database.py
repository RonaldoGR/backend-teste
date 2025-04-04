import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_CONFIG = {
    "dbname": "teste",
    "user": "postgres",
    "password":"sql123",
    "host":"172.23.192.1",
    "port":"5432"
}

def get_connection():
    return psycopg2.connect(**DATABASE_CONFIG)

def execute_query(query, params=None):
    try:
        con = get_connection()
        cur = con.cursor(cursor_factory=RealDictCursor)

        cur.execute(query,params)
        results = cur.fetchall()

        con.close()
        return results
    except  Exception as e:
        print(f"Erro ao executar a consulta: {e}")
        return []
    
