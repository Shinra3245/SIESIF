from typing import Dict

# Rangos de clasificación de perfil
RANGO_CONSERVADOR = (13, 25)
RANGO_MODERADO = (26, 45)
RANGO_AGRESIVO = (46, 52)

def calcular_puntaje(respuestas: Dict[str, int]) -> int:
    """
    Calcula el puntaje total del cuestionario.
    Valida que las respuestas estén entre 1 y 4.
    """
    total = 0
    for pregunta, valor in respuestas.items():
        # Convertir a entero por seguridad si viene como string
        try:
            valor_int = int(valor)
        except ValueError:
            raise ValueError(f"Valor no numérico en {pregunta}: {valor}")

        if not (1 <= valor_int <= 4):
            raise ValueError(f"Valor inválido en {pregunta}: {valor_int} (Debe ser 1-4)")
        
        total += valor_int
        
    return total

def clasificar_perfil(puntaje: int) -> str:
    """
    Clasifica el perfil según el puntaje total obtenido.
    """
    if RANGO_CONSERVADOR[0] <= puntaje <= RANGO_CONSERVADOR[1]:
        return "conservador"
    elif RANGO_MODERADO[0] <= puntaje <= RANGO_MODERADO[1]:
        return "moderado"
    elif RANGO_AGRESIVO[0] <= puntaje <= RANGO_AGRESIVO[1]:
        return "agresivo"
    
    return "indefinido"