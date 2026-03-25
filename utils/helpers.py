from __future__ import annotations

from models.roles import Gerente
from models.trabajador import Trabajador


def obtener_areas_disponibles(trabajadores: list[Trabajador]) -> list[str]:
    areas = sorted({trabajador.get_area() for trabajador in trabajadores if not isinstance(trabajador, Gerente)})
    return areas


def resumir_decision_diseno() -> list[str]:
    return [
        "Se usó una lista de objetos en Python como equivalente práctico del array solicitado en el enunciado.",
        "Se aplicó herencia para evitar duplicar atributos y métodos comunes entre trabajadores.",
        "Se añadió el área de Finanzas porque el caso pide cinco jefes, aunque solo enumera cuatro áreas por nombre.",
        "Se usó Streamlit para acelerar la entrega web sin perder claridad estructural ni uso de HTML.",
        "Se mantuvo la lógica de negocio en servicios separados para facilitar pruebas y mantenimiento.",
    ]
