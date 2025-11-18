from flask import Flask, jsonify
from flask_cors import CORS
from config import Config

# --- CAMBIO 1: Importa 'db' y los modelos desde 'models.py' ---
from models import db, InstrumentoFinanciero, Usuario, PerfilInversionista, EvaluacionRiesgo, Cuestionario, Pregunta, RespuestaUsuario, Recomendacion

# --- Inicialización ---
app = Flask(__name__)
app.config.from_object(Config)

# --- CAMBIO 2: Conecta 'db' a tu 'app' usando init_app ---
db.init_app(app)
# (La línea 'db = SQLAlchemy(app)' se elimina)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# --- CAMBIO 3: La importación de modelos ya no es necesaria aquí ---
# (La línea 'from models import *' se elimina)

# --- Endpoints de la API ---
# (Esta parte no cambia)
@app.route('/')
def health_check():
    """
    Endpoint de "Health Check" (Verificación de estado).
    """
    return jsonify({"status": "API activa y corriendo"}), 200

@app.route('/api/instrumentos')
def get_instrumentos():
    """
    Endpoint principal para obtener todos los instrumentos financieros.
    """
    try:
        instrumentos_lista = InstrumentoFinanciero.query.all()
        instrumentos_json = [instrumento.to_dict() for instrumento in instrumentos_lista]
        return jsonify({"total": len(instrumentos_json), "instrumentos": instrumentos_json}), 200
    except Exception as e:
        return jsonify({"error": f"Error al consultar la base de datos: {str(e)}"}), 500

# --- Ejecución ---
# (Esta parte no cambia)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug=True, port=5000)