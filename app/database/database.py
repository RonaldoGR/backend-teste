import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_CONFIG = {
    "dbname": "db_teste_hl4r",
    "user": "db_teste_hl4r_user",
    "password":os.getenv("DATABASE_PASSWORD"),
    "host":"dpg-cvnr9bpr0fns73ef9olg-a.ohio-postgres.render.com",
    "port":"5432"
}

print("DEBUG - DATABASE_PASSWORD:", os.getenv("DATABASE_PASSWORD"))

def get_connection():
    return psycopg2.connect(**DATABASE_CONFIG)

def execute_query(query, params=None):
    try:
        con = get_connection()
        cur = con.cursor(cursor_factory=RealDictCursor)

        cur.execute(query,params)
        results = cur.fetchall()

        print("Conexão bem-sucedida!")
        cur.close()
        con.close()
        return results
    except  Exception as e:
        print(f"Erro ao executar a consulta: {e}")
        return []
    
