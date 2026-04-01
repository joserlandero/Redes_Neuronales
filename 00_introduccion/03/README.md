# Hiperparámetros: Las Decisiones que Tú Tomas

Cuando una red neuronal entrena, hay dos tipos de cosas que cambian:

- **Parámetros** — los pesos y biases. La red los ajusta sola durante el entrenamiento.
- **Hiperparámetros** — todo lo demás. Los decides tú antes de empezar.

El modelo nunca "aprende" el learning rate ni el número de capas. Eso es tuyo. Esta es la lista de los que más importan.

---

## Learning Rate

Controla qué tan grande es cada paso cuando el optimizador actualiza los pesos:

$$w_{\text{nuevo}} = w_{\text{actual}} - \eta \cdot \text{gradiente}$$

Un **learning rate muy alto** hace que los pasos sean tan grandes que el modelo nunca converge — salta de un lado al otro sin llegar al mínimo. Un **learning rate muy bajo** hace que el entrenamiento sea innecesariamente lento, o que se quede atascado en un mínimo local.

El punto de partida más común es **0.001** con Adam. A partir de ahí se ajusta.

---

## Batch Size

Cuántas muestras se procesan antes de actualizar los pesos. No cambia el resultado final de forma drástica, pero sí afecta cómo llega:

- **Batch grande** → gradientes más estables, menos actualizaciones por epoch, pero necesita más memoria y tiende a converger a mínimos "afilados" que generalizan menos.
- **Batch pequeño** → más ruido (que actúa como regularización natural), más actualizaciones, y tiende a encontrar mínimos más "planos" que generalizan mejor.

En la práctica, **32 o 64** es el punto de partida más común. A menos que tengas una razón concreta, empieza ahí.

---

## Arquitectura: Capas y Neuronas

Cuántas capas ocultas tiene la red y cuántas neuronas tiene cada una determina su **capacidad** — qué tan complejos son los patrones que puede aprender.

Una red muy simple puede no tener suficiente capacidad para el problema (*underfitting*). Una red muy grande puede memorizar los datos en lugar de aprender (*overfitting*).

No hay fórmula exacta. Las reglas prácticas más comunes son:

- Empieza con 1-2 capas ocultas
- El número de neuronas suele estar entre el tamaño de la entrada y el tamaño de la salida
- Si hay overfitting, regulariza antes de achicar la red

---

## Epochs y Early Stopping

El número de epochs define cuántas veces recorre la red el dataset completo. Más epochs no siempre es mejor — en algún punto la red empieza a memorizar.

Por eso casi siempre se combina con **early stopping**: se monitorea el loss de validación y se detiene el entrenamiento cuando deja de mejorar. Así no importa tanto el número exacto de epochs — puedes poner un número grande y dejar que early stopping decida cuándo parar.

---

## ¿Cómo se busca la combinación correcta?

No hay forma de saber de antemano qué combinación de hiperparámetros va a funcionar mejor. Las estrategias principales son:

**Búsqueda manual** — cambias un hiperparámetro a la vez guiado por intuición y observas el efecto. Aprende mucho pero escala mal.

**Grid Search** — defines una lista de valores posibles para cada hiperparámetro y pruebas todas las combinaciones. Exhaustivo pero caro: si pruebas 5 valores de LR × 4 batch sizes × 3 arquitecturas, son 60 entrenamientos.

**Random Search** — en lugar de probar todas las combinaciones, muestreas al azar del espacio de búsqueda. Sorprendentemente eficiente: muchas veces encuentra buenas soluciones con muchos menos entrenamientos que grid search.

**Búsqueda automática (Keras Tuner)** — frameworks especializados que aprenden de los resultados anteriores para decidir qué combinación probar a continuación. Son la opción más sofisticada y eficiente.

---

## ¿Por dónde empezar?

Un punto de partida sólido para la mayoría de los problemas:

| Hiperparámetro | Valor inicial |
|---|---|
| Learning rate | 0.001 |
| Optimizador | Adam |
| Batch size | 32 |
| Épocas | 100+ con early stopping |
| Capas ocultas | 2 |
| Activación oculta | ReLU |

A partir de este punto se ajusta observando las curvas de entrenamiento y validación.
