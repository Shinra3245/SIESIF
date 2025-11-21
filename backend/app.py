from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config
from motor_inferencia import calcular_puntaje, clasificar_perfil
from reglas_logicas import aplicar_reglas_recomendacion

# --- CAMBIO 1: Importa 'db' y los modelos desde 'models.py' ---
from models import db, InstrumentoFinanciero, Usuario, PerfilInversionista, EvaluacionRiesgo, Cuestionario, Pregunta, RespuestaUsuario, Recomendacion

# --- Inicialización ---
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})




# --- Endpoints de la API ---

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

# -- nuevo endpoint --
@app.route('/api/evaluar-perfil', methods=['POST'])
def evaluar_perfil():
    """
    Recibe las respuestas del cuestionario, calcula el perfil
    y devuelve recomendaciones personalizadas.
    """
    try:
        # 1. Obtener datos del JSON
        data = request.json
        respuestas = data.get('respuestas')

        if not respuestas:
            return jsonify({"error": "Faltan las respuestas"}), 400

        # 2. Usar el Motor de Inferencia 
        puntaje = calcular_puntaje(respuestas)
        perfil = clasificar_perfil(puntaje)

        # 3. Aplicar Reglas Lógicas para obtener instrumentos 
        recomendaciones_obj = aplicar_reglas_recomendacion(perfil)
        
        # Convertir objetos DB a diccionarios JSON
        recomendaciones_json = [inst.to_dict() for inst in recomendaciones_obj]

        # 4. Responder
        return jsonify({
            "puntaje": puntaje,
            "perfil": perfil,
            "total_recomendaciones": len(recomendaciones_json),
            "recomendaciones": recomendaciones_json
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Error interno: {str(e)}"}), 500
# --- Ejecución ---

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug=True, port=5000)