from __future__ import annotations

import pandas as pd
import streamlit as st

from services.data_factory import crear_datos_demo
from services.reporting import (
    construir_ficha_trabajador,
    construir_tabla_trabajadores,
    obtener_indicadores,
)
from utils.helpers import obtener_areas_disponibles, resumir_decision_diseno

st.set_page_config(
    page_title="Business Corporation | RR. HH.",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
)


def mostrar_tabla(df: pd.DataFrame) -> None:
    st.dataframe(df, use_container_width=True, hide_index=True)


st.title("🏢 Sistema de RR. HH. - Business Corporation")
st.caption(
    "Versión rehecha en Python puro para la lógica y Streamlit para la interfaz, "
    "sin renderizado HTML manual ni dependencias de marcado externo."
)

repo = crear_datos_demo()
trabajadores = repo.listar_trabajadores()
areas = obtener_areas_disponibles(trabajadores)

with st.sidebar:
    st.header("Navegación")
    vista = st.radio(
        "Seleccione una vista",
        [
            "Resumen ejecutivo",
            "Listado general",
            "Consulta por área",
            "Ficha individual",
            "Validación de reglas",
            "Explicación técnica",
        ],
    )

if vista == "Resumen ejecutivo":
    indicadores = obtener_indicadores(trabajadores)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total trabajadores", indicadores["total_trabajadores"])
    c2.metric("Gerentes", indicadores["gerentes"])
    c3.metric("Jefes de área", indicadores["jefes_area"])
    c4.metric("Áreas registradas", indicadores["areas"])

    c5, c6, c7 = st.columns(3)
    c5.metric("Asistentes", indicadores["asistentes"])
    c6.metric("Técnicos", indicadores["tecnicos"])
    c7.metric("Trabajadores inactivos", indicadores["inactivos"])

    st.subheader("Lectura directa del caso")
    st.info(
        "Esta reconstrucción mantiene POO, jerarquías, getters/setters, resumen, jefe inmediato y estado, "
        "pero evita HTML manual para respetar tu instrucción de hacerlo en Python."
    )

    st.subheader("Decisiones de diseño")
    for linea in resumir_decision_diseno():
        st.write(f"• {linea}")

    st.subheader("Vista previa del listado general")
    tabla = construir_tabla_trabajadores(trabajadores).head(10)
    mostrar_tabla(tabla)

elif vista == "Listado general":
    st.subheader("Listado completo de trabajadores")
    tabla = construir_tabla_trabajadores(trabajadores)
    mostrar_tabla(tabla)

elif vista == "Consulta por área":
    st.subheader("Consulta filtrada por área")
    area = st.selectbox("Seleccione un área", areas)
    tabla = construir_tabla_trabajadores(repo.listar_por_area(area))
    mostrar_tabla(tabla)

elif vista == "Ficha individual":
    st.subheader("Ficha detallada por trabajador")
    nombres = [trabajador.get_nombre_completo() for trabajador in trabajadores]
    nombre = st.selectbox("Seleccione un trabajador", nombres)
    trabajador = repo.buscar_por_nombre(nombre)

    if trabajador:
        ficha = construir_ficha_trabajador(trabajador)
        c1, c2 = st.columns(2)
        with c1:
            st.write(f"**Nombre completo:** {ficha['Nombre completo']}")
            st.write(f"**Documento:** {ficha['Documento']}")
            st.write(f"**Área:** {ficha['Área']}")
            st.write(f"**Puesto:** {ficha['Puesto']}")
            st.write(f"**Rango:** {ficha['Rango']}")
            st.write(f"**Resumen:** {ficha['Resumen']}")
        with c2:
            st.write(f"**Jefe inmediato:** {ficha['Jefe inmediato']}")
            st.write(f"**Estado:** {ficha['Estado']}")
            st.write(f"**Correo:** {ficha['Correo']}")
            st.write(f"**Teléfono:** {ficha['Teléfono']}")
            st.write(f"**Experiencia (años):** {ficha['Experiencia (años)']}")
            st.write(f"**Activo:** {'Sí' if ficha['Activo'] else 'No'}")
    else:
        st.warning("No se encontró al trabajador seleccionado.")

elif vista == "Validación de reglas":
    st.subheader("Comprobación de reglas del negocio")
    validaciones = repo.validar_reglas_de_negocio()

    for validacion in validaciones:
        if validacion["cumple"]:
            st.success(validacion["mensaje"])
        else:
            st.error(validacion["mensaje"])

    st.subheader("Resumen por área")
    tabla = construir_tabla_trabajadores(trabajadores)
    resumen_area = (
        tabla.groupby("Área")[["Es asistente", "Es técnico"]]
        .sum()
        .rename(columns={"Es asistente": "Asistentes", "Es técnico": "Técnicos"})
        .reset_index()
    )
    mostrar_tabla(resumen_area)

elif vista == "Explicación técnica":
    st.subheader("¿Qué cumple esta solución?")
    st.write("• POO completa con clase base Trabajador y clases derivadas por rol.")
    st.write("• Herencia y polimorfismo mediante la redefinición de get_resumen().")
    st.write("• Encapsulamiento con atributos protegidos por getters y setters.")
    st.write("• Estructuras condicionales con if y match-case para estados y decisiones.")
    st.write("• Estructuras repetitivas para poblar colecciones, filtrar y validar reglas.")
    st.write("• Interfaz hecha con componentes nativos de Streamlit, sin HTML manual.")
    st.write("• Modularización estricta para facilitar mantenimiento y defensa académica.")

    st.subheader("Observación importante")
    st.warning(
        "El enunciado menciona explícitamente cuatro áreas, pero también exige cinco jefes de área. "
        "Por eso se añadió Finanzas como quinta jefatura."
    )
