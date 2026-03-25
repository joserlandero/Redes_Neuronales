# Conceptos Básicos

Este directorio contiene la documentación teórica y práctica sobre la fase de compilación de una red neuronal. A continuación se detallan los tres componentes fundamentales que dictan cómo aprende un modelo y cómo se evalúa su rendimiento.

## 1. Funciones de Pérdida (Loss Functions)

La función de pérdida cuantifica el error del modelo. Su propósito es medir la discrepancia entre la predicción generada por la red y el valor real observado en los datos. La elección de esta función depende estrictamente del tipo de problema que se busca modelar.

### Para problemas de Regresión
Se utilizan cuando el objetivo es predecir un valor numérico continuo, como podría ser el cálculo de una reserva técnica, un monto de siniestro o una estimación de costos.

* **Error Cuadrático Medio (MSE):** Penaliza de forma severa los errores grandes al elevar las diferencias al cuadrado. Es la métrica analítica por excelencia.
    $$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
* **Error Absoluto Medio (MAE):** Toma el valor absoluto de las diferencias. Es una métrica más robusta cuando la base de datos contiene valores atípicos, ya que no castiga los extremos de forma desproporcionada.
    $$MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$

### Para problemas de Clasificación Binaria
Se aplican cuando el modelo debe predecir entre dos estados posibles, típicamente representados como 0 o 1, como la probabilidad de ocurrencia de un evento específico.

* **Entropía Cruzada Binaria (Binary Cross-Entropy):** Compara las distribuciones de probabilidad. Penaliza logarítmicamente las predicciones que el modelo clasifica con alta seguridad pero que resultan ser incorrectas.
    $$BCE = -\frac{1}{n} \sum_{i=1}^{n} [y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)]$$

### Para problemas de Clasificación Multiclase
Se emplean cuando la variable objetivo contiene tres o más categorías distintas.

* **Categorical Cross-Entropy:** Utilizada cuando las etiquetas de clasificación están estructuradas en formato de vectores múltiples (One-Hot Encoding).
* **Sparse Categorical Cross-Entropy:** Cumple la misma función matemática que la anterior, pero está optimizada para consumir menos memoria al recibir las categorías directamente como números enteros simples.

## 2. Optimizadores (Optimizers)

Mientras que la función de pérdida calcula el error, el optimizador es el algoritmo matemático encargado de ajustar los parámetros internos de la red neuronal para reducir dicho error al mínimo posible en cada iteración.

* **SGD (Stochastic Gradient Descent):** Es el algoritmo fundamental. Realiza actualizaciones constantes en la dirección del gradiente descendente. Es estable, pero puede requerir más tiempo de convergencia y es susceptible a quedarse atrapado en mínimos locales.
* **Adam (Adaptive Moment Estimation):** Es el estándar actual en la industria. Su principal ventaja es que adapta el tamaño del paso de aprendizaje para cada parámetro de forma individual y conserva un registro de los pasos anteriores. Esto le permite acelerar en áreas de descenso claro y estabilizarse al acercarse al objetivo.
* **RMSprop:** Un optimizador altamente efectivo para datos que presentan variaciones importantes a lo largo del tiempo. Suele ser la opción preferida al trabajar con redes recurrentes y análisis de series temporales.

## 3. Tasa de Aprendizaje (Learning Rate)

La tasa de aprendizaje es el parámetro de control más crítico durante la etapa de entrenamiento. Define la magnitud del ajuste que el optimizador aplica a los pesos de la red en cada actualización.

* **Tasa demasiado alta:** El optimizador da pasos muy grandes, provocando que el modelo salte repetidamente por encima del punto óptimo. El entrenamiento se vuelve inestable y la métrica de pérdida puede divergir en lugar de disminuir.
* **Tasa demasiado baja:** El optimizador da pasos sumamente pequeños. El modelo eventualmente aprenderá, pero consumirá un tiempo de procesamiento excesivo y aumentará la probabilidad de estancarse antes de encontrar el error mínimo real.
* **Tasa óptima:** Permite un descenso constante y estable hacia la solución. En la práctica del modelado, los valores iniciales suelen establecerse entre 0.01 y 0.001, requiriendo calibración empírica según el comportamiento observado en la curva de pérdida.