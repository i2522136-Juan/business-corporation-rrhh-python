# Caso práctico N.º 01 - Business Corporation (Python + Streamlit)

## 1. Objetivo
Este proyecto resuelve el caso práctico de **Business Corporation** con una solución hecha en **Python**, usando **Streamlit** para la interfaz y una arquitectura modular orientada a objetos. Se rehízo para evitar HTML manual, diagramas embebidos de otros formatos y scripts auxiliares que no fueran Python.

## 2. Qué implementa
- 1 gerente general.
- 5 jefes de área.
- 2 asistentes por área.
- 5 técnicos por área.
- Lista de objetos en memoria como equivalente práctico del array solicitado.
- Métodos obligatorios:
  - `get_resumen()`
  - `get_jefe_inmediato()`
  - `get_estado()`
- Dashboard web en Streamlit.
- Validación de reglas del negocio.
- Pruebas automáticas con Pytest.
- Informe en Word.

## 3. Estructura del proyecto
```text
business_corporation_rrhh_app/
├── app.py
├── models/
│   ├── trabajador.py
│   └── roles.py
├── services/
│   ├── data_factory.py
│   ├── repository.py
│   └── reporting.py
├── utils/
│   ├── constants.py
│   └── helpers.py
├── tests/
│   └── test_logic.py
├── scripts/
│   └── setup_env.py
├── docs/
│   ├── estructura_archivos.md
│   ├── flujograma_pseudocodigo.txt
│   └── informe_tecnico.docx
├── requirements.txt
├── pyproject.toml
├── generate_report.py
└── README.md
```

## 4. Crear entorno virtual
### Opción recomendada en Python
```bash
python scripts/setup_env.py
```

### Opción manual
```bash
python -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
```

## 5. Ejecutar la aplicación
```bash
.venv/bin/streamlit run app.py
```

## 6. Ejecutar pruebas
```bash
.venv/bin/pytest -q
```

## 7. Regenerar el informe Word
```bash
.venv/bin/python generate_report.py
```

## 8. Enlace del repositorio
**Pendiente de publicación remota.**

Cuando se publique en GitHub o GitLab, sustituir esta línea por el enlace real del repositorio.

## 9. Decisión de diseño importante
El enunciado menciona cuatro áreas concretas bajo gerencia, pero también exige cinco jefes de área. Para cumplir el mínimo exigido sin romper la lógica, se añadió el área de **Finanzas**.

## 10. Flujo general del sistema
El flujo del sistema está documentado en `docs/flujograma_pseudocodigo.txt`, también escrito solo en texto para mantener la solución centrada en Python.

## 11. Tecnologías usadas
- Python 3
- Streamlit
- Pandas
- Pytest
- python-docx

## 12. Nota importante
El PDF original pide tablas HTML, pero esta reconstrucción sigue tu instrucción explícita: **hacerlo todo en Python**. Por eso la visualización se resuelve con componentes nativos de Streamlit y estructuras de datos de Python, sin HTML manual.
