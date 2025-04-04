from flask import Blueprint, jsonify
from app.services import get_tabela_2024, get_trimestre_2024,get_trimestre_2023


bp = Blueprint("routes", __name__)


@bp.route("/")
def home():
    return jsonify({
         "mensagem": "API teste"
         ""})

@bp.route("/<parametro>")
def teste(parametro):
    if parametro == '2024':
       resultados = get_tabela_2024()
       print(f"DEBUG - Resultados 2024: {resultados}")
       return jsonify({ "TABELA 2024": resultados })
        
    if parametro == 'trimestre2024':
            resultados = get_trimestre_2024()
            return jsonify({ "TRIMESTRE 2024": resultados })
       
    if parametro == 'trimestre2023':
            resultados = get_trimestre_2023()
            return jsonify({ "TRIMESTRE 2023": resultados })
    return jsonify({ "erro": "Parâmetro inválido" }), 400
