QUERY_TABELA_2024 = """
                SELECT Razao_Social,
                Nome_Fantasia,
                REPLACE(VL_SALDO_INICIAL, ',', '.')::NUMERIC - REPLACE(VL_SALDO_FINAL, ',', '.')::NUMERIC AS DESPESA
                FROM operadoras_ativas 
                JOIN tabela_2024
                    ON tabela_2024.REG_NS = operadoras_ativas.Registro_ANS
                WHERE tabela_2024.DESCRICAO ='EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
                AND tabela_2024.DATA >= '2024-01-01'
                AND tabela_2024.DATA < '2025-01-01'
                ORDER BY DESPESA DESC
                LIMIT 10
            """

QUERY_TRIMESTRE_2024 = """
                            SELECT Razao_Social,
                            Nome_Fantasia,
                            REPLACE(VL_SALDO_INICIAL, ',', '.')::NUMERIC - REPLACE(VL_SALDO_FINAL, ',', '.')::NUMERIC AS DESPESA
                            FROM operadoras_ativas 
                            JOIN tabela_2024
                                ON tabela_2024.REG_NS = operadoras_ativas.Registro_ANS
                            WHERE tabela_2024.DESCRICAO ='EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
                            AND tabela_2024.DATA >= '2024-10-01'
                            AND tabela_2024.DATA < '2025-01-01'
                            ORDER BY DESPESA DESC
                            LIMIT 10
                        """


QUERY_TRIMESTRE_2023 = """
                           SELECT  Razao_Social,
                            Nome_Fantasia,
                            REPLACE(VL_SALDO_INICIAL, ',', '.')::NUMERIC - REPLACE(VL_SALDO_FINAL, ',', '.')::NUMERIC AS DESPESA
                            FROM operadoras_ativas 
                            JOIN tabela_2023
                                ON tabela_2023.REG_NS = operadoras_ativas.Registro_ANS
                            WHERE tabela_2023.DESCRICAO ='EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
                            AND tabela_2023.DATA >= '2023-10-01' AND tabela_2023.DATA < '2024-01-01'
                            ORDER BY DESPESA DESC
                            LIMIT 10
                        """