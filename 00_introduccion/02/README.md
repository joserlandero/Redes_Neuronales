# Regularización: Evitando que la Red Memorice

## ¿Qué es el overfitting?

Es cuando una red neuronal tiene **demasiados parametros** para los datos que tiene. En vez de aprender los patrones generales, memoriza cada ejemplo individual del entrenamiento, incluyendo el ruido y las excepciones.

El resultado: accuracy altísimo en training, pero pésimo en datos nuevos.

---

## ¿Cómo se detecta?

Se separa una parte de los datos que la red **nunca ve durante el entrenamiento** — el conjunto de validación. En cada epoch se mide el loss en ambos conjuntos:

- **Loss de training baja constantemente** — la red aprende (o memoriza)
- **Loss de validación baja y luego sube** — la red dejó de generalizar y empezó a memorizar

El punto donde el loss de validación empieza a subir es donde debería detenerse el entrenamiento. Eso es exactamente lo que hace **early stopping**.

Si ambas curvas bajan juntas y se mantienen cercanas, la red está generalizando bien.

---

## ¿Qué es la regularización?

Regularización es cualquier técnica que dificulta la memorización para forzar a la red a aprender patrones generales. Las principales son:

---

## Regularización L1 y L2

Ambas agregan un **castigo extra al loss** basado en el tamaño de los pesos. La idea es simple: pesos grandes permiten que la red se ajuste demasiado a cada detalle del training. Si la penalizamos por tener pesos grandes, se ve obligada a usar pesos más pequeños y encontrar soluciones más simples.

**L2 (Ridge)** agrega la suma de los pesos al cuadrado:

$$\mathcal{L}_{total} = \mathcal{L}_{original} + \lambda \sum w_i^2$$

Los pesos grandes reciben un castigo mucho mayor que los pequeños (por el cuadrado), así que L2 tiende a hacer todos los pesos pequeños pero sin eliminar ninguno.

**L1 (Lasso)** agrega la suma del valor absoluto de los pesos:

$$\mathcal{L}_{total} = \mathcal{L}_{original} + \lambda \sum |w_i|$$

L1 tiende a llevar muchos pesos exactamente a cero, efectivamente eliminando conexiones. Esto produce redes más "simples" donde solo quedan las conexiones importantes.

El hiperparámetro $\lambda$ controla qué tan fuerte es el castigo. Un $\lambda$ demasiado alto perjudica el aprendizaje porque la red no puede tener pesos lo suficientemente grandes para capturar ni siquiera los patrones reales.

---

## Dropout

Durante el entrenamiento, en cada paso se "apagan" neuronas al azar con una cierta probabilidad (por ejemplo, 30%). Cada vez que la red procesa un batch, un conjunto diferente de neuronas está activo.

¿Por qué funciona? Porque la red no puede depender de ninguna neurona individual. Si la neurona 5 siempre se encarga de detectar cierto patrón, ¿qué pasa cuando la apagan? Otras neuronas tienen que aprender a cubrir ese trabajo. El resultado es una red más robusta donde el conocimiento está distribuido.

Es como un equipo de trabajo donde rotativamente algunos miembros faltan — el equipo aprende a funcionar sin depender de nadie en particular.

**Importante:** durante la evaluación (predicción), dropout se desactiva y todas las neuronas están activas. Las salidas se escalan automáticamente para compensar.

---

## Batch Normalization

A medida que la red entrena, la distribución de los valores que entran a cada capa va cambiando (porque los pesos de las capas anteriores están cambiando). Esto se llama **internal covariate shift** y puede hacer que el entrenamiento sea inestable o lento.

Batch Normalization resuelve esto normalizando las entradas de cada capa para que tengan media 0 y desviación estándar 1 dentro de cada mini-batch. Es como aplicar `StandardScaler` no solo a los datos de entrada, sino a la entrada de cada capa interna.

Además, incluye dos parámetros aprendibles ($\gamma$ y $\beta$) que le permiten a la red reescalar y desplazar los valores si la normalización estricta no es óptima. Estos parámetros se ajustan automáticamente durante el entrenamiento.

Beneficios prácticos:
- Permite usar learning rates más grandes sin que el entrenamiento diverja
- Actúa como regularizador leve (reduce la necesidad de dropout)
- Generalmente hace que el entrenamiento sea más rápido y estable

---

## Early Stopping

La idea más simple: monitorear el loss de validación y dejar de entrenar cuando empiece a subir. Se guarda una copia de los pesos del mejor momento (el que tuvo menor loss de validación) y se usa esa copia como modelo final.

En la práctica se le da un margen de "paciencia" — por ejemplo, si el loss de validación no mejora en 10 epochs seguidos, ahí se detiene. Esto evita parar prematuramente por una fluctuación momentánea.

---

## ¿Cuándo usar cada técnica?

No hay una regla fija, pero en la práctica moderna el punto de partida más común es:

- **Batch Normalization** se usa casi siempre después de cada capa oculta
- **Dropout** se agrega si hay overfitting, típicamente con probabilidad entre 0.2 y 0.5
- **L2** se usa con frecuencia, L1 es menos común en deep learning
- **Early stopping** se usa siempre — no hay razón para no usarlo

Estas técnicas se pueden combinar. Un modelo típico podría tener batch normalization + dropout + early stopping trabajando juntos.
