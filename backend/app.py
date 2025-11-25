import os
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy

# --- Importación de Modelos ---
from models import db, InstrumentoFinanciero

# --- Importación de Lógica ---
from motor_inferencia import calcular_puntaje, clasificar_perfil
from reglas_logicas import aplicar_reglas_recomendacion

# --- Configuración de Rutas Estáticas ---
base_dir = os.path.abspath(os.path.dirname(__file__))
frontend_dir = os.path.join(base_dir, '../frontend')

app = Flask(__name__, static_folder=frontend_dir, static_url_path='')
app.config.from_object(Config)

# --- Inicialización de Extensiones ---
db.init_app(app)
cors = CORS(app)

# ==========================================
#  LÓGICA DE AUTO-INICIALIZACIÓN (NUEVO)
# ==========================================
def inicializar_base_datos():
    """Crea tablas e inserta datos si la BD está vacía."""
    with app.app_context():
        # 1. Crear Tablas
        db.create_all()
        
        # 2. Verificar si ya hay datos
        if InstrumentoFinanciero.query.first():
            return # Ya existen datos, no hacemos nada

        print("Inicializando base de datos con 11 instrumentos...")
        
        # 3. Insertar los 11 Instrumentos (Datos Semilla)
        datos = [
            {
                "nombre": "CETES", "tipo": "renta_fija", "riesgo": "bajo",
                "descripcion": "Certificados de la Tesorería de la Federación. Bonos de corto plazo emitidos por el Gobierno Federal; no pagan cupones, se compran con descuento y al vencimiento devuelven el valor nominal.",
                "rendimiento_referencial": "10-11% anual", "horizonte_recomendado": "corto", "liquidez": "alta"
            },
            {
                "nombre": "Bonos M", "tipo": "renta_fija", "riesgo": "bajo_medio",
                "descripcion": "Deuda soberana a tasa fija con cupones semestrales y plazos de 3 a 30 años. Sensibles a cambios en tasas de interés, adecuados para objetivos de mediano y largo plazo.",
                "rendimiento_referencial": "8-10% anual", "horizonte_recomendado": "largo", "liquidez": "alta"
            },
            {
                "nombre": "Udibonos", "tipo": "renta_fija", "riesgo": "bajo",
                "descripcion": "Bonos vinculados a la inflación que pagan una tasa real más la variación de la UDI. Ayudan a preservar el poder adquisitivo en el mediano y largo plazo.",
                "rendimiento_referencial": "4-6% real + inflación", "horizonte_recomendado": "largo", "liquidez": "alta"
            },
            {
                "nombre": "Bondes F", "tipo": "renta_fija", "riesgo": "bajo",
                "descripcion": "Bonos de tasa flotante cuyo cupón se ajusta periódicamente con una tasa de referencia de corto plazo. Minimizan la exposición a cambios de tasas a largo plazo.",
                "rendimiento_referencial": "9-11% anual", "horizonte_recomendado": "mediano", "liquidez": "alta"
            },
            {
                "nombre": "Bonos del IPAB", "tipo": "renta_fija", "riesgo": "bajo",
                "descripcion": "Títulos emitidos por el IPAB (BPAG y BPA) referenciados a CETES o tasa de fondeo. Algunos protegen contra la inflación. Bajo riesgo por respaldo público.",
                "rendimiento_referencial": "8-10% anual", "horizonte_recomendado": "mediano", "liquidez": "media_alta"
            },
            {
                "nombre": "Acciones", "tipo": "renta_variable", "riesgo": "alto",
                "descripcion": "Participación en empresas listadas en BMV o BIVA. Alto potencial a largo plazo con volatilidad en el corto. Algunas pagan dividendos. Requieren diversificación.",
                "rendimiento_referencial": "10-20% anual (variable)", "horizonte_recomendado": "largo", "liquidez": "alta"
            },
            {
                "nombre": "ETFs", "tipo": "mixto", "riesgo": "medio",
                "descripcion": "Fondos cotizados que replican un índice y se operan como acciones. Ofrecen diversificación inmediata y bajas comisiones. El riesgo depende del índice que replican.",
                "rendimiento_referencial": "8-15% anual", "horizonte_recomendado": "largo", "liquidez": "alta"
            },
            {
                "nombre": "Fondos de Inversión (Deuda)", "tipo": "renta_fija", "riesgo": "bajo_medio",
                "descripcion": "Vehículos administrados por profesionales que agrupan recursos en carteras de deuda. Se valoran y ofrecen liquidez diaria.",
                "rendimiento_referencial": "7-10% anual", "horizonte_recomendado": "mediano", "liquidez": "alta"
            },
            {
                "nombre": "Fondos de Inversión (Mixtos)", "tipo": "mixto", "riesgo": "medio",
                "descripcion": "Fondos que combinan instrumentos de renta fija y renta variable. Balance entre seguridad y rendimiento. Administrados profesionalmente.",
                "rendimiento_referencial": "10-15% anual", "horizonte_recomendado": "largo", "liquidez": "alta"
            },
            {
                "nombre": "Fondos de Inversión (Renta Variable)", "tipo": "renta_variable", "riesgo": "alto",
                "descripcion": "Fondos que invierten principalmente en acciones. Mayor potencial de rendimiento con mayor volatilidad. Requieren horizonte de inversión largo.",
                "rendimiento_referencial": "12-20% anual (variable)", "horizonte_recomendado": "largo", "liquidez": "alta"
            },
            {
                "nombre": "FIBRAS", "tipo": "alternativo", "riesgo": "medio",
                "descripcion": "Fideicomisos que invierten en bienes raíces, infraestructura o energía. Pagan distribuciones periódicas de rentas o flujos. Cotizan en bolsa.",
                "rendimiento_referencial": "8-12% anual", "horizonte_recomendado": "largo", "liquidez": "media"
            }
        ]

        for item in datos:
            nuevo_instrumento = InstrumentoFinanciero(**item)
            db.session.add(nuevo_instrumento)
        
        db.session.commit()
        print("Base de datos poblada exitosamente.")

# ¡EJECUTAR AL INICIO! (Esto asegura que Gunicorn corra esto al arrancar)
inicializar_base_datos()

# ==========================================
#  RUTAS
# ==========================================

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/health')
def health_check():
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

if __name__ == '__main__':
    app.run(debug=True, port=5000)