import os
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy

# --- Importación de Modelos ---
# Nota: Importamos db aquí para inicializarlo, pero los modelos se importan después
# para evitar errores circulares si fuera necesario, aunque con esta estructura está bien.
from models import db, InstrumentoFinanciero

# --- Importación de Lógica ---
from motor_inferencia import calcular_puntaje, clasificar_perfil
from reglas_logicas import aplicar_reglas_recomendacion

# --- Configuración de Rutas Estáticas ---
# Calculamos la ruta absoluta a la carpeta 'frontend'
base_dir = os.path.abspath(os.path.dirname(__file__))
frontend_dir = os.path.join(base_dir, '../frontend')

# Inicializamos Flask diciéndole dónde está el frontend
app = Flask(__name__, static_folder=frontend_dir, static_url_path='')
app.config.from_object(Config)

# --- Inicialización de Extensiones ---
db.init_app(app)
cors = CORS(app) # CORS permite que el frontend hable con el backend

# ==========================================
#  RUTAS DE LA PÁGINA WEB (FRONTEND)
# ==========================================

@app.route('/')
def serve_index():
    """Ruta raíz: Sirve el archivo index.html del frontend"""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    """
    Ruta comodín: Sirve cualquier otro archivo (css, js, html, imágenes)
    que esté en la carpeta frontend.
    """
    return send_from_directory(app.static_folder, path)

# ==========================================
#  RUTAS DE LA API (BACKEND)
# ==========================================

@app.route('/api/health')
def health_check():
    """(Opcional) Movemos el health check a una ruta de API"""
    return jsonify({"status": "API activa y corriendo"}), 200

@app.route('/api/instrumentos')
def get_instrumentos():
    try:
        instrumentos_lista = InstrumentoFinanciero.query.all()
        instrumentos_json = [instrumento.to_dict() for instrumento in instrumentos_lista]
        return jsonify({"total": len(instrumentos_json), "instrumentos": instrumentos_json}), 200
    except Exception as e:
        return jsonify({"error": f"Error al consultar la base de datos: {str(e)}"}), 500

@app.route('/api/evaluar-perfil', methods=['POST'])
def evaluar_perfil():
    try:
        data = request.json
        respuestas = data.get('respuestas')

        if not respuestas:
            return jsonify({"error": "Faltan las respuestas"}), 400

        puntaje = calcular_puntaje(respuestas)
        perfil = clasificar_perfil(puntaje)
        recomendaciones_obj = aplicar_reglas_recomendacion(perfil)
        
        recomendaciones_json = [inst.to_dict() for inst in recomendaciones_obj]

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

# --- Función Auxiliar para Render (Poblar DB si está vacía) ---
def poblar_base_datos():
    # Verifica si la tabla existe y tiene datos
    try:
        if InstrumentoFinanciero.query.first():
            return
        
        # Si está vacía, insertar datos básicos (EJEMPLO RÁPIDO para que funcione el deploy)
        print("Poblando base de datos...")
        # Aquí podrías poner tu lógica de inserción si usaras PostgreSQL persistente
        # Por ahora, en SQLite de Render se borrará al reiniciar, pero esto sirve de ejemplo.
    except:
        pass

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # poblar_base_datos()
    app.run(debug=True, port=5000)