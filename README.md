# Deep Learning Frameworks: TF, PyTorch & MLX

Este repositorio documenta mi proceso de aprendizaje y experimentación con redes neuronales, comparando la sintaxis, 
el rendimiento y la implementación en tres de los principales frameworks de Deep Learning: **TensorFlow, PyTorch y MLX**. 

El objetivo principal es desarrollar intuición práctica sobre cada herramienta y aprovechar la aceleración por hardware de Apple Silicon (M4), aplicando estos modelos a problemas de ciencia de datos y análisis actuarial.

## Objetivos del Proyecto
- Entender la lógica subyacente de cada framework.
- Traducir arquitecturas de redes neuronales entre TensorFlow, PyTorch y MLX.
- Evaluar el rendimiento y la eficiencia de MLX en procesadores Apple M4.
- Resolver problemas prácticos con diferentes datasets (regresión, clasificación, series de tiempo).

## Estructura del Repositorio
El proyecto está organizado de manera jerárquica: primero por el tipo de arquitectura de red neuronal y, dentro de cada una, por el proyecto o dataset específico.

* `00_introduccion/`: Conceptos básicos, creación de tensores y operaciones fundamentales.
* `01_redes_densas/`: Multilayer Perceptrons (MLP) aplicados a datos tabulares.
* `02_redes_recurrentes_lstm/`: Modelos para pronósticos y series de tiempo.
* `03_redes_convolucionales_cnn/`: Procesamiento de matrices y extracción de características.
* `04_autoencoders/`: Reducción de dimensionalidad y detección de anomalías.

Dentro de cada proyecto, se encuentran los scripts individuales para cada framework (ej. `tf_modelo.py`, `torch_modelo.py`, `mlx_modelo.py`).

## Entorno y Tecnologías
- Hardware: MacBook Air (Chip M4)
- Lenguaje: Python 3.x
- Librerías principales: `tensorflow`, `torch`, `mlx`, `pandas`

## Cómo ejecutar los scripts
1. Clonar este repositorio.
2. Crear un entorno virtual local: `python3 -m venv env`
3. Activar el entorno: `source env/bin/activate`
4. Instalar las dependencias (se agregará un `requirements.txt` próximamente).