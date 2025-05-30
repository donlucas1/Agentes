# 📊 Agente Analista Interactivo con LM Studio Local

Este proyecto implementa un agente analista interactivo que utiliza un modelo de lenguaje local (a través de LM Studio) para analizar datos de un CSV y generar visualizaciones y análisis estadísticos automáticamente.

## 🛠 Tecnologías utilizadas
- Python 3.x
- Pandas (para manipulación de datos)
- Matplotlib y Seaborn (para visualizaciones)
- OpenAI API (conectado a LM Studio local)
- Re (expresiones regulares)

## 🔌 Configuración requerida
```python
import openai
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import re

# Configuración para LM Studio local
openai.api_key = "not-needed"
openai.api_base = "http://localhost:1234/v1"  # Asegúrate de usar el puerto correcto
```

## 🚀 Cómo usar el agente

### 1. Inicialización
```python
agente = AgenteAnalistaInteractivo("ruta/a/tu/archivo.csv")
```

### 2. Hacer consultas
El agente puede responder preguntas como:
```python
# Visualización básica
agente.responder_y_ejecutar("¿Podés mostrar un gráfico de barras con las ventas por región?")

# Análisis temporal
agente.responder_y_ejecutar("¿Cómo varían las ventas mensuales?")

# Estadísticas completas
agente.responder_y_ejecutar("Necesito todos los datos estadísticos que puedas generar")
```

## 📈 Funcionalidades principales

### Carga y exploración inicial de datos
- Carga automática del CSV
- Detección de tipos de datos
- Visualización de estructura básica

### Generación de código automático
- Creación de visualizaciones (gráficos de barras, líneas, etc.)
- Análisis temporal (tendencias mensuales)
- Estadísticas descriptivas completas:
  - Media, mediana, moda
  - Desviación estándar y varianza
  - Cuartiles y rango intercuartílico
  - Coeficiente de variación

### Ejecución segura
- Extracción de código mediante expresiones regulares
- Ejecución en entorno controlado
- Manejo de errores

## 📋 Ejemplo de salida
El agente proporciona:
1. Confirmación de carga de datos
2. Estructura de columnas
3. Tiempo de respuesta
4. Código generado
5. Resultados/visualizaciones

## ⚠️ Requisitos previos
1. Tener LM Studio ejecutándose localmente
2. Tener cargado un modelo compatible (ej. Mistral)
3. Instalar las dependencias con:
```bash
pip install pandas matplotlib seaborn openai
```

## 📌 Notas importantes
- El agente solo genera y ejecuta código Python relacionado con análisis de datos
- Para preguntas complejas, el modelo podría necesitar ajustes en el prompt
- Se recomienda verificar siempre el código generado antes de usarlo en producción

Este proyecto demuestra cómo integrar modelos de lenguaje local con análisis de datos para crear herramientas interactivas de análisis.
