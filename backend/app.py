from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config
# Inicializa la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inicializa las extensiones
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) # Habilita CORS para /api/

# --- Dependencia (Modelos) ---
# Esta sección fallará hasta que Gael complete 'backend/models.py'
# Por ahora, puedes crear una clase temporal aquí para probar.
# MÁS ADELANTE, esta importación será: from .models import InstrumentoFinanciero

# --- Bloque Temporal de Prueba (BORRAR LUEGO) ---
# (Pega esto en app.py temporalmente para que el código corra)
class InstrumentoFinanciero(db.Model):
    __tablename__ = 'instrumentos_financieros'
    id_instrumento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    tipo = db.Column(db.String(50))
    riesgo = db.Column(db.String(20))
    
    # Esta función es VITAL para convertir el objeto a JSON
    def to_dict(self):
        return {
            'id': self.id_instrumento,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'riesgo': self.riesgo
        }
# --- Fin del Bloque Temporal ---


# --- Endpoints de la API ---

@app.route('/')
def health_check():
    """
    Endpoint de "Health Check" (Verificación de estado).
    Retorna un JSON simple si la API está activa.
    """
    return jsonify({"status": "API activa y corriendo"}), 200

@app.route('/api/instrumentos')
def get_instrumentos():
    """
    Endpoint principal para obtener todos los instrumentos financieros.
    """
    try:
        # 1. Hacer la consulta a la BD (usando el modelo de Gael)
        instrumentos_lista = InstrumentoFinanciero.query.all()
        
        # 2. Convertir los objetos SQLAlchemy a diccionarios
        #    Usamos la función to_dict() que Gael definirá en models.py
        instrumentos_json = [instrumento.to_dict() for instrumento in instrumentos_lista]
        
        # 3. Retornar la lista en formato JSON
        return jsonify({"total": len(instrumentos_json), "instrumentos": instrumentos_json}), 200

    except Exception as e:
        # Manejo de errores
        return jsonify({"error": f"Error al consultar la base de datos: {str(e)}"}), 500

# --- Ejecución ---

if __name__ == '__main__':
    with app.app_context():
        # Esta línea crea las tablas en tu base de datos (si no existen)
        # Solo necesitas ejecutarlo una vez para crear el archivo siesif_dev.db
        db.create_all()
    
    # Inicia el servidor de desarrollo
    app.run(debug=True, port=5000)