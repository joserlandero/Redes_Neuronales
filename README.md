# Deep Learning Frameworks: TF, PyTorch & MLX

![Python](https://img.shields.io/badge/Python-3.11-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red)
![MLX](https://img.shields.io/badge/MLX-Apple_Silicon-black)
![Status](https://img.shields.io/badge/Status-En_Progreso-yellow)

Este repositorio documenta mi proceso de aprendizaje y experimentación con redes neuronales, comparando la sintaxis,
el rendimiento y la implementación en tres de los principales frameworks de Deep Learning: **TensorFlow, PyTorch y MLX**.
El objetivo principal es desarrollar intuición práctica sobre cada herramienta y aprovechar la aceleración por hardware de Apple Silicon (M4).

---

## Objetivos del Proyecto

- Entender la lógica subyacente de cada framework.
- Traducir arquitecturas de redes neuronales entre TensorFlow, PyTorch y MLX.
- Resolver problemas prácticos con diferentes datasets (regresión, clasificación, series de tiempo).

---

## Hardware

Todos los experimentos con MLX fueron ejecutados en **Apple M4** (Metal backend), aprovechando la memoria unificada para acelerar el entrenamiento de modelos directamente en CPU/GPU integrada.

---

## Estructura del Repositorio

El proyecto está organizado de manera jerárquica: primero por el tipo de arquitectura de red neuronal y, dentro de cada una, por el proyecto o dataset específico.

```
deep-learning/
│
├── 00_fundamentos/               # Conceptos matemáticos y teóricos base
│   ├── 01_gradiente_y_backprop/
│   ├── 02_funciones_de_activacion/
│   ├── 03_optimizadores/
│   ├── 04_funciones_de_perdida/
│   └── 05_metricas/
│
├── 01_redes_densas/              # Multilayer Perceptrons (MLP) — datos tabulares
├── 02_redes_recurrentes_lstm/    # Modelos para pronósticos y series de tiempo
└── 03_redes_convolucionales_cnn/ # Procesamiento de imágenes y extracción de características
```

Dentro de cada proyecto, se encuentran los scripts individuales por framework:

```
01_redes_densas/
└── 01_clasificacion_iris/
    ├── tf_modelo.py
    ├── torch_modelo.py
    └── mlx_modelo.py
```

---

## Proyectos

| # | Proyecto | Dataset | Tipo | Frameworks |
|---|----------|---------|------|------------|
| — | — | — | — | En construcción |

> La tabla se irá completando conforme se agreguen proyectos al repositorio.

---

## Cómo Ejecutar los Scripts

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/deep-learning.git
   cd deep-learning
   ```
2. Crear un entorno virtual local:
   ```bash
   python3 -m venv env
   ```
3. Activar el entorno:
   ```bash
   source env/bin/activate
   ```
4. Instalar las dependencias del proyecto que deseas ejecutar:
   ```bash
   pip install -r 01_redes_densas/01_clasificacion_iris/requirements.txt
   ```

---

## Roadmap

- [x] Estructura base del repositorio
- [ ] `00_fundamentos` — conceptos teóricos iniciales
- [ ] Primer proyecto en `01_redes_densas`
- [ ] Comparativa de tiempos de entrenamiento entre frameworks
- [ ] Agregar notebooks `.ipynb` como alternativa a los scripts `.py`
