# Simulación Portuaria con Python

Este proyecto implementa una simulación detallada de las operaciones en un puerto utilizando el entorno de simulación **SimPy**. Está diseñado para analizar y optimizar la eficiencia operativa de un puerto mediante la segmentación de actividades en muelles especializados según el tipo de barco.

## Características Principales
- **Segmentación de muelles:** Divididos por tipo de barco para optimizar tiempos de carga y descarga.
- **Eventos dinámicos:** Simulación de factores como clima, huelgas y otros imprevistos operativos.
- **Estadísticas avanzadas:** Generación y análisis de datos clave para la planificación estratégica.
- **Estructura modular:** Código organizado para facilitar su comprensión y mantenimiento.

## Organización del Proyecto
- **Carpeta principal:**
  - `boats.py`: Gestión de barcos.
  - `ports.py`: Operaciones portuarias.
- **Carpeta `Statistics`:**
  - `csv_analizer.py`: Análisis de datos generados.
  - `statistics_1.py`: Recopilación de datos durante la simulación.
- **Carpeta `Unforeseen`:**
  - `unforeseen.py`: Simulación de eventos inesperados.
  - `weather.py`: Modelado de condiciones climáticas.
- **Carpeta `Terminal Exit`:**
  - `menu.py`: Interfaz para análisis y estadísticas.
  - `formats.py`: Formateo de salidas.
- **Jupyter Notebooks:** Análisis detallado de resultados de simulaciones.

## Cómo Usar
1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la simulación:
   ```bash
   python sim.py
   ```
4. Analiza los resultados con los notebooks disponibles en la carpeta `analysis`.

## Ejemplo de Resultados
- **Simulación 1:**
  - Llegadas cada 10 horas.
  - Tiempo medio de espera: 7 horas.
  - Ingresos generados: 44.7M €.
- **Simulación 3:**
  - Llegadas cada 25 horas.
  - Tiempo medio de espera: <1% de barcos afectados.
  - Ingresos generados: 16M €.

## Objetivo
Utilizar simulaciones para prever situaciones futuras y optimizar la productividad portuaria ajustando variables clave como capacidad de los muelles, condiciones climáticas e imprevistos.

