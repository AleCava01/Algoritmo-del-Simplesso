# Fase II

![Untitled](Fase%20II%20fe9c94ff22fa4e6a875f8d4a37b8e70d/Untitled.png)

# 1. Verifica dell’ottimalità della soluzione di base

## Condizioni di ottimalità

**Per il problema di massimo**

$$
z^*=max\ \ z=z_B+\vec r'_D\vec x_D
$$

La soluzione di base ammissibile e non degenere $\vec x = (\vec x_B,\vec x_D)$ è ottimale se

$$
\vec r^T\le\vec 0
$$

Dato che $\vec r'=\vec r'_B+\vec r'_D$ e $\vec r'_B=\vec 0$ ⇒ la condizione necessaria e sufficiente diventa

$$
\vec r'_D\le \vec 0\\\Rightarrow \vec c'_D-\vec c'_B \times B^{-1}\times D\le\vec 0
$$

Se la soluzione di base è degenere, la condizione sopra riportata non è necessaria ma solo sufficiente.

**Per il problema di minimo**

La soluzione di base ammissibile e non degenere $\vec x = (\vec x_B,\vec x_D)$ è ottimale se

$$
\vec r^T\ge\vec 0
$$

---

Se la solzione di base risulta ottimale, l’algoritmo del simplesso si arresta e restituisce la soluzione di base ottimale e il valore ottimo associato.

---

**Se la soluzione $\vec x = (\vec x_B,\vec x_D)$ non è ottimale, allora esiste almeno una variabile non basica $x_t$ per cui $r_t>0$.**

### Limite superiore della variabile entrante

$$
A\vec x=\vec b \\ B\vec x_B+D \vec x_D = \vec b \\ B\vec x_B = \vec b -D \vec x_D \\ \vec x_B = B^{-1}\vec b -B^{-1}D \vec x_D
$$

Quindi per ogni variabile in base $x_i$ con $i\in(1,..., m)$:

$$
x_i=(B^{-1}\vec b)_i -(B^{-1}D )_i x_t\ge 0 \\   x_t\le \frac{(B^{-1}\vec b)_i}{(B^{-1}D )_i}
$$

Si definisce limite superiore della variabile entrante $x_t$, la quantità:

$$
\frac{(B^{-1}\vec b)_i}{(B^{-1}D )_i}
$$

---

# 2. Verifica illimitatezza

Dato un problema in forma standard e una soluzione di base ammissibile $\vec x=(\vec x_B,\vec x_D)$ associata a $B$, se

$$
(B^{-1}A_t)_i\le0 \ \ \ \ \ \forall i
$$

Allora il problema dato è illimitato.

Infatti ne conseguirebbe che:

$$
x_t\ge\frac{(B^{-1}\vec b)_i}{(B^{-1}A_t)_i} \ \ \ \ \ \forall i
$$

E quindi non esisterebbe un limite superiore per la variabile $x_t$.

Dal momento che $z^*=max \ \ z_B+\vec r'_Dx_D$ e per qualche variabile $x_t$  fuori base vale $r_t>0$, la quantità

$$
r_t\cdot x_t
$$

potrebbe crescere illimitatamente al crescere di $x_t$ generando sempre soluzioni migliori.

---

# 3. Cambio di base - generazione nuova soluzione di base ammissibile

Si definisce l’insieme $I=\{i\in\{1,2,...,m\}: (B^{-1}A_t)_i>0\}$,

Si seleziona la variabile entrante $x_t$ 

### Criteri di selezione per la variabile entrante

- **I° Criterio:** Si seleziona $x_t$ a cui è associato il coefficiente $r_t$ più alto.
    
    Difetti: possibile ciclaggio infinito su soluzioni di base degeneri
    
- **II° Criterio**: Per ogni possibile $x_t$ (quindi a cui è associato $r_t>0$), si calcola il limite superiore e si sceglie $x_t=\underset{t|r_t>0}\max \underset{i\in I} \min \frac{(B^{-1}\vec b)_i}{(B^{-1}A_t)_i}$.
    
    Difetti: molto oneroso, potrebbe ciclare all’infinito su soluzioni di base degeneri
    
- **Regola di Blend**: Viene selezionata $x_t\ \ \ t.c \ \ r_t>0$ con pedice più piccolo e non ancora transitata dalla base.
    
    Permette di evitare il fenomento del ciclaggio in presenza di soluzioni di base degeneri.
    

una volta selezionata $x_t$, il massimo valore a cui posso farla entrare senza violare i vincoli del problema è:

$$
x_t=\underset{i\in I} \min \frac{(B^{-1}\vec b)_i}{(B^{-1}A_t)_i}
$$

Si indica con $k$ il pedice $\in I$ che restituisce il minimo dei rapporti. $x_k$ prenderà il nome di variabile uscente.

La nuova soluzione di base sarà:

$$
\vec x=(\vec x_B,\vec x_D)\\\vec x_B=(... ,x_t)\\ \vec x_D=(...,x_k)=\vec 0
$$

A questo punto si riprende dal punto 1.

---

[Fase II - Procedimento pratico](Fase%20II%20fe9c94ff22fa4e6a875f8d4a37b8e70d/Fase%20II%20-%20Procedimento%20pratico%2028b1abbc95ef410baae40f5435a3e54f.md)