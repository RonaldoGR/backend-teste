from app.database.database import execute_query
from app.database.queries import QUERY_TABELA_2024, QUERY_TRIMESTRE_2024,QUERY_TRIMESTRE_2023

def get_tabela_2024():
    resultados = execute_query(QUERY_TABELA_2024)

    return [
            {
                'Razao Social': row["razao_social"],
                'Nome Fantasia': row["nome_fantasia"],
                'Despesas': row["despesa"]
            }
            for row in resultados
           ]

def get_trimestre_2024():
    resultados = execute_query(QUERY_TRIMESTRE_2024)

    return [
            {
                'Razao Social': row["razao_social"],
                'Nome Fantasia': row["nome_fantasia"],
                'Despesas': row["despesa"]
            }
            for row in resultados
           ]
def get_trimestre_2023():
    resultados = execute_query(QUERY_TRIMESTRE_2023)

    return [
            {
                'Razao Social': row["razao_social"],
                'Nome Fantasia': row["nome_fantasia"],
                'Despesas': row["despesa"]
            }
            for row in resultados
           ]