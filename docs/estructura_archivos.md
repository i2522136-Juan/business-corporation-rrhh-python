# Explicación de archivos del proyecto

## app.py
Punto de entrada de la aplicación Streamlit. Gestiona la interfaz web, la navegación y la visualización de datos con componentes nativos de Streamlit.

## models/trabajador.py
Contiene la clase abstracta `Trabajador`, donde se centralizan los atributos comunes y los métodos getters/setters, además de `get_jefe_inmediato()` y `get_estado()`.

## models/roles.py
Define las clases derivadas `Gerente`, `JefeArea`, `Asistente` y `PersonalTecnico`. Aquí se aplica polimorfismo porque cada tipo implementa su propia versión de `get_resumen()`.

## services/repository.py
Almacena la lista de objetos trabajador, equivalente práctico al array de objetos del caso. También implementa búsquedas y validaciones de reglas del negocio.

## services/data_factory.py
Construye los datos iniciales exigidos por la consigna: 1 gerente, 5 jefes de área, 2 asistentes por área y 5 técnicos por área.

## services/reporting.py
Transforma los objetos en DataFrames de Pandas para visualización, análisis y generación de indicadores dentro de la aplicación.

## utils/constants.py
Define constantes reutilizables del sistema, como estados laborales y áreas base.

## utils/helpers.py
Agrupa funciones auxiliares de soporte, por ejemplo las decisiones de diseño y la extracción de áreas disponibles.

## tests/test_logic.py
Pruebas automáticas básicas para comprobar el cumplimiento de las reglas centrales del problema.

## requirements.txt
Lista las dependencias de Python necesarias para ejecutar el proyecto.

## scripts/setup_env.py
Script en Python para crear el entorno virtual e instalar dependencias sin recurrir a shell script.

## docs/flujograma_pseudocodigo.txt
Describe el flujo del sistema en pseudocódigo y texto estructurado.

## README.md
Documento principal del repositorio. Explica el objetivo, la estructura, la instalación, la ejecución y el enlace del repositorio cuando se publique.

## docs/informe_tecnico.docx
Informe formal en Word con desarrollo, explicación técnica, estructura del proyecto y observaciones sobre la solución.
