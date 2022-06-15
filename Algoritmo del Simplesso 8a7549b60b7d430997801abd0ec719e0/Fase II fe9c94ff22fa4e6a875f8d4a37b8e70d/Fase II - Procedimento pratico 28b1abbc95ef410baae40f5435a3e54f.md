# Fase II - Procedimento pratico

### 1. Split soluzione di base

$$
\vec x = (\vec x_B,\vec x_D)
$$

$\vec x_B :=$ vettore delle variabili in base

$\vec x_D=\vec 0$ := vettore delle variabili fuori base, tutte uguali a 0.

---

### 2. Forma canonica

Si mettono a sistema i vincoli del problema portando in evidenza le variabili in base.

$$
\begin{cases} x_{B_1}=... \\x_{B_2}=... \\...\\x_{B_m}=...\end{cases}
$$

---

### 3. Verifica ottimalità

**Per il problema di massimo,** le condizioni di ottimalità sono:

$$
\vec r'_D\le \vec 0\\\Rightarrow \vec c'_D-\vec c'_B \times B^{-1}\times D\le\vec 0
$$

Per ricavare il vettore $\vec r'_D$ si può usare la funzione obiettivo:

$$
z=z_B+\vec r'_D\vec c_D
$$

quindi si cerca di esprimere la funzione obiettivo solo rispetto alle variabili fuori base, usando come sostituzione delle variabili in base, le relazioni precedentemente trovate con la relazione canonica.

Si può ora costruire il vettore $\vec r'_D$: i suoi elementi saranno i coefficienti che moltiplicano le variabili fuori base nella F.O.

Se $\vec r'_D \le \vec 0$,  allora la soluzione di base è ottimale, altrimenti di procede al cambio di base.

### 4. Cambio di base (con regola di Blend)

**Regola di Blend**: entra in base la variabile $x_k$ fuori base con $r_k>0$ e pedice più basso che non è mai stata in base.

Si riprendono i vincoli precedentemente espressi in forma canonica e si impongono tutti $\ge 0$.

Si azzerano tutte le altre variabili fuori base.

A questo punto possono accadere diversi scenari:

- Tutte le relazioni sono del tipo $x_k\ge c$   con $c$  costante.
    
    In questo caso, il problema è illimitato
    
- C’è almeno una relazione $x_k\le c$ con $c$ costante.
    
    Si prende il vincolo più stringente per $x_k$ e si vede quale variabile (del sistema espresso in forma canonica) l’ha generato. Quest’ultima prenderà il nome di variabile uscente $x_u$.
    
    Si dice che la variabile $x_k$ entrerà al valore $c$ e la variabile $x_u$ uscirà al valore $c.$
    
    Alla fine si trova la nuova soluzione di base
    
    $\vec x=(\vec x_B,\vec x_D)$
    
    $\vec x_B=(...,x_k)$
    
    $\vec x_D=(...,x_u)=\vec 0$
    
    E si ricomincia dal punto 1.