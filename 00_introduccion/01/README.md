# Redes Neuronales: Fundamentos

Este documento explica de forma intuitiva cómo funciona una red neuronal por dentro, recorriendo cada pieza del proceso con ejemplos numéricos concretos.

---

## ¿Qué calcula una neurona?

Una neurona recibe entradas, las multiplica por sus pesos, suma todo, agrega el bias y produce un solo número. Si tenemos dos entradas $x_1 = 3$ y $x_2 = 5$, con pesos $w_1 = 0.4$, $w_2 = -0.2$ y bias $b = 0.1$, la neurona calcula:

$$z = (0.4)(3) + (-0.2)(5) + 0.1 = 0.3$$

Cada neurona siempre tiene **un peso por cada entrada** que recibe, más su bias. Si le llegan 2 valores, tiene 2 pesos. Si le llegan 50, tiene 50 pesos.

---

## ¿Qué pasa cuando hay varias neuronas en una capa?

Si la capa oculta tiene más de una neurona, todas reciben las mismas entradas pero cada una tiene sus propios pesos y bias. Con tres neuronas:

- Neurona A: $z_A = (0.4)(3) + (-0.2)(5) + 0.1 = 0.3$
- Neurona B: $z_B = (-0.1)(3) + (0.5)(5) + 0.0 = 2.2$
- Neurona C: $z_C = (0.3)(3) + (0.1)(5) + (-0.5) = 0.9$

Cada neurona detecta un "patrón" diferente en los datos porque sus pesos son distintos. La capa produce tres salidas, y esas tres salidas se convierten en las entradas de la siguiente capa.

---

## ¿Cómo se conectan las capas?

La capa de salida recibe lo que produjo la capa anterior. Si la capa oculta tiene 3 neuronas, la neurona de salida necesita 3 pesos — uno por cada valor que recibe:

$$\hat{y} = (0.6)(0.3) + (0.3)(2.2) + (-0.4)(0.9) + 0.0 = 0.48$$

La regla es siempre la misma: **el número de pesos de una neurona es igual al número de salidas de la capa anterior**. Por eso a medida que la red crece en capas y neuronas, la cantidad de parámetros crece rápidamente.

Si la capa de salida tiene más de una neurona (como en clasificación multiclase), se obtienen múltiples salidas, cada una representando algo distinto — por ejemplo, la probabilidad de cada clase.

---

## ¿Para qué sirven las funciones de activación?

Sin funciones de activación, apilar 100 capas lineales es equivalente a tener una sola. Las activaciones transforman la salida de cada neurona para "romper" esa linealidad y permitir que la red modele relaciones complejas como curvas y umbrales.

La activación transforma $z$ en $a$, y ese $a$ es lo que llega como entrada a la siguiente capa. Por ejemplo, con ReLU:

- $z_A = 0.3 \rightarrow a_A = \text{ReLU}(0.3) = 0.3$
- $z_B = -2.2 \rightarrow a_B = \text{ReLU}(-2.2) = 0$

La neurona B fue "silenciada" porque su valor era negativo. Eso es precisamente lo que le da a la red la capacidad de aprender relaciones no lineales.

En las capas ocultas se usa casi siempre **ReLU**. En la capa de salida depende del problema: nada (lineal) para regresión, sigmoid para clasificación binaria, y softmax para clasificación multiclase.

---

## ¿Cómo sabemos qué tan mal estuvo la predicción?

La predicción $\hat{y}$ se compara con el valor real $y$ usando una **función de pérdida (loss)**. Por ejemplo, si la red predijo $\hat{y} = 0.84$ y el valor real es $y = 1.0$, usando MSE:

$$\mathcal{L} = (1.0 - 0.84)^2 = 0.0256$$

Ese número mide el error. Mientras más alto, peor. El objetivo del entrenamiento es minimizarlo ajustando los pesos.

---

## ¿Cómo se ajustan los pesos?

El ajuste ocurre en dos pasos que trabajan juntos:

**Backpropagation** recorre la red de atrás hacia adelante calculando los **gradientes** de cada peso — es decir, averigua en qué dirección y cuánto debería moverse cada peso para reducir el loss. Pero no toca ningún peso todavía.

**El optimizador** toma esos gradientes y actualiza todos los pesos. En su forma más básica (SGD), la regla es simple:

$$w_{\text{nuevo}} = w_{\text{actual}} - \eta \cdot \text{gradiente}$$

El gradiente dice "el loss sube si mueves este peso en esta dirección", entonces el optimizador lo mueve en la dirección contraria. El learning rate ($\eta$) controla qué tan grande es cada paso.

Existen optimizadores más sofisticados como Adam, que adaptan el tamaño del paso individualmente para cada peso según su historial, pero al final todos hacen lo mismo: usar los gradientes para mover los pesos en la dirección que reduzca el loss.

El nuevo loss recién se conoce cuando llega el siguiente batch y se hace un nuevo forward pass con los pesos ya actualizados.

---

## Epochs y Batch Size

**Batch size** define cuántas muestras procesas antes de hacer una actualización de pesos. Si tienes 1,000 muestras y batch_size=100, la red procesa 100 muestras, calcula el loss promedio, hace backprop, actualiza pesos, y luego toma las siguientes 100. Eso son 10 actualizaciones para recorrer todo el dataset.

**Epoch** significa que ya recorriste todo el dataset una vez. En el ejemplo anterior, después de esas 10 actualizaciones completaste 1 epoch. El batch size controla qué pasa **dentro** de cada epoch, y el número de epochs controla cuántas veces repites ese recorrido completo.

Un **batch grande** produce actualizaciones más estables porque el gradiente se calcula con muchas muestras, pero hay menos actualizaciones por epoch y además las GPUs tienen un límite de memoria. Un **batch pequeño** produce más actualizaciones por epoch y el ruido que introduce actúa como regularización natural, pero cada actualización individual es menos precisa. En la práctica, 32 o 64 es el punto de partida más común.

Los pesos nunca se reinician entre epochs. Cada epoch empieza con los pesos que quedaron al final del anterior y los sigue refinando. Lo único que se reinicia es el recorrido del dataset — las muestras se barajan al inicio de cada epoch para que los mini-batches sean diferentes.
