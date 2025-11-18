from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

# Tabla 1: usuarios
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    activo = db.Column(db.Boolean, default=True)
    
    # Relaciones
    perfiles = db.relationship('PerfilInversionista', backref='usuario', lazy=True)

# Tabla 2: perfiles_inversionista
class PerfilInversionista(db.Model):
    __tablename__ = 'perfiles_inversionista'
    
    id_perfil = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    tipo_perfil = db.Column(db.Enum('conservador', 'moderado', 'agresivo', name='tipo_perfil_enum'), nullable=False)
    puntaje_total = db.Column(db.Integer, nullable=False)
    tolerancia_riesgo = db.Column(db.String(50))
    capacidad_economica = db.Column(db.Numeric(15, 2))
    horizonte_inversion = db.Column(db.Enum('corto', 'mediano', 'largo', name='horizonte_enum'))
    fecha_evaluacion = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.Enum('activo', 'inactivo', name='estado_perfil_enum'), default='activo')
    
    # Relaciones
    evaluaciones = db.relationship('EvaluacionRiesgo', backref='perfil', lazy=True)
    recomendaciones = db.relationship('Recomendacion', backref='perfil', lazy=True)

# Tabla 3: instrumentos_financieros (PRIORIDAD #1)
class InstrumentoFinanciero(db.Model):
    __tablename__ = 'instrumentos_financieros'
    
    id_instrumento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    tipo = db.Column(db.Enum('renta_fija', 'renta_variable', 'mixto', 'alternativo', name='tipo_instrumento_enum'), nullable=False)
    riesgo = db.Column(db.Enum('bajo', 'bajo_medio', 'medio', 'alto', name='riesgo_enum'), nullable=False)
    descripcion = db.Column(db.Text)
    rendimiento_referencial = db.Column(db.String(50))
    horizonte_recomendado = db.Column(db.Enum('corto', 'mediano', 'largo', name='horizonte_recomendado_enum'))
    liquidez = db.Column(db.Enum('baja', 'media', 'media_alta', 'alta', name='liquidez_enum'))
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    recomendaciones = db.relationship('Recomendacion', backref='instrumento', lazy=True)
    
    def to_dict(self):
        """Método para convertir el objeto a diccionario (útil para JSON)"""
        return {
            'id_instrumento': self.id_instrumento,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'riesgo': self.riesgo,
            'descripcion': self.descripcion,
            'rendimiento_referencial': self.rendimiento_referencial,
            'horizonte_recomendado': self.horizonte_recomendado,
            'liquidez': self.liquidez,
            'fecha_actualizacion': self.fecha_actualizacion.isoformat() if self.fecha_actualizacion else None
        }

# Tabla 4: evaluaciones_riesgo
class EvaluacionRiesgo(db.Model):
    __tablename__ = 'evaluaciones_riesgo'
    
    id_evaluacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_perfil = db.Column(db.Integer, db.ForeignKey('perfiles_inversionista.id_perfil'), nullable=False)
    categoria_riesgo = db.Column(db.String(50))
    puntuacion_total = db.Column(db.Integer)
    observaciones = db.Column(db.Text)
    
    # Relaciones
    respuestas = db.relationship('RespuestaUsuario', backref='evaluacion', lazy=True)

# Tabla 5: cuestionarios
class Cuestionario(db.Model):
    __tablename__ = 'cuestionarios'
    
    id_cuestionario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    version = db.Column(db.String(10))
    activo = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    preguntas = db.relationship('Pregunta', backref='cuestionario', lazy=True)

# Tabla 6: preguntas
class Pregunta(db.Model):
    __tablename__ = 'preguntas'
    
    id_pregunta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_cuestionario = db.Column(db.Integer, db.ForeignKey('cuestionarios.id_cuestionario'), nullable=False)
    numero_pregunta = db.Column(db.Integer, nullable=False)
    texto_pregunta = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.Enum('horizonte', 'financiera', 'conocimiento', 'tolerancia', name='categoria_pregunta_enum'))
    obligatoria = db.Column(db.Boolean, default=True)
    
    # Relaciones
    respuestas = db.relationship('RespuestaUsuario', backref='pregunta', lazy=True)

# Tabla 7: respuestas_usuario
class RespuestaUsuario(db.Model):
    __tablename__ = 'respuestas_usuario'
    
    id_respuesta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_evaluacion = db.Column(db.Integer, db.ForeignKey('evaluaciones_riesgo.id_evaluacion'), nullable=False)
    id_pregunta = db.Column(db.Integer, db.ForeignKey('preguntas.id_pregunta'), nullable=False)
    valor_respuesta = db.Column(db.Integer, nullable=False)  # CHECK: 1-4
    puntuacion = db.Column(db.Integer)

# Tabla 8: recomendaciones
class Recomendacion(db.Model):
    __tablename__ = 'recomendaciones'
    
    id_recomendacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_perfil = db.Column(db.Integer, db.ForeignKey('perfiles_inversionista.id_perfil'), nullable=False)
    id_instrumento = db.Column(db.Integer, db.ForeignKey('instrumentos_financieros.id_instrumento'), nullable=False)
    porcentaje_sugerido = db.Column(db.Numeric(5, 2))
    justificacion = db.Column(db.Text)