from typing import Dict

# Rangos de clasificación de perfil
RANGO_CONSERVADOR = (13, 25)
RANGO_MODERADO = (26, 45)
RANGO_AGRESIVO = (46, 52)


def calcular_puntaje(respuestas: Dict[str, int]) -> int:
    # Valida que las respuestas estén entre 1 y 4 y calcula el puntaje total
    for pregunta, valor in respuestas.items():
        if not isinstance(valor, int) or not (1 <= valor <= 4):
            raise ValueError(f"Valor inválido en {pregunta}: {valor}")
    return sum(respuestas.values())


def clasificar_perfil(puntaje: int) -> str:
    # Clasifica el perfil según el puntaje
    if 13 <= puntaje <= 25:
        return "conservador"
    elif 26 <= puntaje <= 45:
        return "moderado"
    elif 46 <= puntaje <= 52:
        return "agresivo"
    return "indefinido"
