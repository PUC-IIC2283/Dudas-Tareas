## Ayuda para el cálculo de $X_i$  

- Para resolver este ejercicio hay que notar que, dado cada uno de los $N$ nodos, este tiene como máximo $N-1$ aristas saliendo de él. Dado que no sabemos a priori cuantos vecinos tiene cada nodo, iniciaremos con que nuestra tabla tiene del orden de $N \times N$ entradas (podría ser $(N+1)^2$,  $(N-1)^2$, $N\times (N + 1)$, etc. dependiendo de su implementación).

- Dado que los nodos del árbol son numerados de 1 a $N$, se puede asumir que el nodo 1 es la raíz del árbol, y que su padre es el nodo 0 (que no existe).

- Desde la raíz, recorreremos de forma recursiva sus hijos hasta llegar a las hojas, las cuales formarán la base de los subárboles. Notar que no todo nodo es una hoja, por lo que la cantidad de subárboles es cualquier número entre 1 y $N - 1$.

- Desde los subárboles, hay que avanzar en dirección a la raíz. En cada paso se debe considerar solo una nueva arista, o lo que es equivalente, un nuevo nodo.

- Al agregar el nuevo nodo, hay que combinar los resultados provenientes de los subárboles. Para esto, hay que relacionar al nodo con todos sus vecinos.

- Una vez que se vuelve a la raíz, la tabla debería estar con todos los valores necesarios. Dado que la tabla tiene más entradas de las necesarias, esta podría tener valores no usados.

- Finalmente, a partir de la tabla se calcula el valor para cada $X_i$.

### Conceptos clave

- DFS
- Combinatoria (usar inversos modulares)
- Tamaño de un subárbol
