from flask import Blueprint, render_template, request, jsonify
import pandas as pd
from app.services.service import optimize_portfolio

bp = Blueprint("main", __name__)

# permite subir archivo por formulario html 
@bp.route("/")
def home():
    return render_template("index.html")

# ejecucion de servicio por POST
@bp.route("/optimize-portfolio", methods=["POST"])
def optimize():
    file = request.files.get("file")
    
    # valores para efectos de prueba
    risk_level = float(request.form.get("risk_level", 0.002))
    max_weight = float(request.form.get("max_weight", 0.15))

    # si no se adjuntó archivo
    if not file:
        return jsonify({"error": "Missing file"}), 400

    try:
        df = pd.read_csv(file)
        result = optimize_portfolio(df, risk_level, max_weight)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
