from models import InstrumentoFinanciero

def aplicar_reglas_recomendacion(perfil: str):
    """
    Aplica las reglas lógicas (R4, R5, R6) para seleccionar instrumentos
    desde la base de datos según el perfil.
    """
    consulta = InstrumentoFinanciero.query

    if perfil == 'conservador':
        # REGLA R4: Riesgo bajo o bajo_medio, Tipo Renta Fija
        return consulta.filter(
            InstrumentoFinanciero.riesgo.in_(['bajo', 'bajo_medio']),
            InstrumentoFinanciero.tipo == 'renta_fija'
        ).all()

    elif perfil == 'moderado':
        # REGLA R5: Riesgo bajo, medio o bajo_medio.
        return consulta.filter(
            InstrumentoFinanciero.riesgo.in_(['bajo', 'medio', 'bajo_medio'])
        ).all()

    elif perfil == 'agresivo':
        # REGLA R6: Riesgo medio o alto, horizonte largo
        return consulta.filter(
            InstrumentoFinanciero.riesgo.in_(['medio', 'alto']),
            InstrumentoFinanciero.horizonte_recomendado.in_(['mediano', 'largo'])
        ).all()

    return []