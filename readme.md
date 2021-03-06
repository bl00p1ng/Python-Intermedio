# Curso de Python Intermedio

Apuntes y c贸digo del Curso de Python Intermedio de Platzi

[Repositorio Oficial del Curso](https://github.com/facmartoni/curso-intermedio-python)

- [Curso de Python Intermedio](#curso-de-python-intermedio)
  - [馃摎 M贸dulo 1. Preparaci贸n antes de empezar](#-m贸dulo-1-preparaci贸n-antes-de-empezar)
    - [Clase 2. El Zen de Python](#clase-2-el-zen-de-python)
  - [馃摎 M贸dulo 2. Entorno virtual](#-m贸dulo-2-entorno-virtual)
    - [Clase 5. El primer paso profesional: creaci贸n de un entorno](#clase-5-el-primer-paso-profesional-creaci贸n-de-un-entorno)
    - [Clase 6. Instalaci贸n de dependencias con pip](#clase-6-instalaci贸n-de-dependencias-con-pip)
  - [馃摎 M贸dulo 3. Alternativa a los ciclos: comprehensions](#-m贸dulo-3-alternativa-a-los-ciclos-comprehensions)
    - [Clase 8. Listas y diccionarios anidados](#clase-8-listas-y-diccionarios-anidados)
    - [Clase 9. List Comprehensions](#clase-9-list-comprehensions)
    - [Clase 10. Dictionary comprehensions](#clase-10-dictionary-comprehensions)
  - [馃摎 M贸dulo 4. Conceptos avanzados de funciones](#-m贸dulo-4-conceptos-avanzados-de-funciones)
    - [Clase 11. Funciones an贸nimas: lambda](#clase-11-funciones-an贸nimas-lambda)
    - [Clase 12. High order functions: filter, map y reduce](#clase-12-high-order-functions-filter-map-y-reduce)
      - [Filter](#filter)
      - [Map](#map)
      - [Reduce](#reduce)
    - [Clase 13. Proyecto: filtrando datos](#clase-13-proyecto-filtrando-datos)
  - [馃摎 M贸dulo 5. Manejo de errores](#-m贸dulo-5-manejo-de-errores)
    - [Clase 14. Los errores en el c贸digo](#clase-14-los-errores-en-el-c贸digo)
      - [Syntax Error](#syntax-error)
      - [Exception](#exception)
    - [Clase 15. Debugging](#clase-15-debugging)
    - [Clase 16. Manejo de excepciones](#clase-16-manejo-de-excepciones)
      - [Try/Except](#tryexcept)
      - [raise](#raise)
    - [Finally](#finally)
    - [Clase 18. Assert Statements](#clase-18-assert-statements)
  - [馃摎 M贸dulo 6. Manejo de archivos](#-m贸dulo-6-manejo-de-archivos)
    - [Clase 19. 驴C贸mo trabajar con archivos?](#clase-19-c贸mo-trabajar-con-archivos)
      - [Modos de apertura](#modos-de-apertura)
    - [Clase 20. Trabajando con archivos de texto en Python](#clase-20-trabajando-con-archivos-de-texto-en-python)

## 馃摎 M贸dulo 1. Preparaci贸n antes de empezar

### Clase 2. El Zen de Python

Son los 20 principios del desarrollo de software m谩s importantes de este lenguaje, permiten escribir c贸digo de forma correcta y precisa. Fueron creados en 1999.

**C贸mo ver el Zen de Python**

1. Abrir la consola interactiva de PythonClase 6. Instalaci贸n de dependencias con pip
![Zen de Python en Espa帽ol parte 4](https://i.ibb.co/3zz1xMv/zen-python-4.png)

## 馃摎 M贸dulo 2. Entorno virtual

### Clase 5. El primer paso profesional: creaci贸n de un entorno

1. Crear el entorno virtual
    ```bash
    python3 -m venv venv
    ```
2. Activar el entorno virtual (en sistema tipo UNIX o Linux)
    ```bash
    source venv/bin/activate
    ```

Para salir del entorno virtual se usa el comando `deactivate`

### Clase 6. Instalaci贸n de dependencias con pip

**Compartir dependencias de un proyecto**

```bash
pip freeze > requeriments.txt
```

Esto guardar谩 en el archivo `requeriments.txt` las dependencias del proyecto con sus respectivas versiones.

Luego para que la persona a la que se comparta el proyecto pueda instalar las dependencias tiene que usar el comando:

```bash
pi峁? install -r requeriments.txt
```

## 馃摎 M贸dulo 3. Alternativa a los ciclos: comprehensions

### Clase 8. Listas y diccionarios anidados

Se pueden tener listas que guarden diccionarios y diccionarios que guarden listas.

```python
super_list = [
        {"firstname": "Andr茅s", "lastname": "L贸pez"},
        {"firstname": "Tony", "lastname": "Stark"},
        {"firstname": "Peter", "lastname": "Parker"},
        {"firstname": "Hana", "lastname": "Uzaki"},
    ]

super_dict = {
    "natural_nums": [1, 2, 3, 4, 5],
    "integer_nums": [-1, -2, 0, 1, 2],
    "floating_nums": [1.1, 4.5, 6.43]
}
```

### Clase 9. List Comprehensions

**Sintaxis**

![Sintaxis List Comprehensions](https://i.ibb.co/VS1Rmj4/sintaxis-list-comprehensions.png)

**C贸mo funcionan**

![C贸mo funcionan los list comprehensions](https://i.ibb.co/3vvyp12/1-z-J0-Xf-N1fk-WSvll2-Bg8o46g.png)

[M谩s informaci贸n sobre el funcionamiento de los List Comprehensions](https://towardsdatascience.com/all-about-python-list-comprehension-14dd979ec0d1)

_**Ejemplo:**_

```python
squares = [i**2 for i in range(1, 101) if i % 3 != 0]
```

### Clase 10. Dictionary comprehensions

**Sintaxis**

![Sintaxis Dictionary comprehensions](https://i.ibb.co/v1JfBts/sintaxis-Dictionary-comprehensions.png)

_**Ejemplo:**_

```python
my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
```

## 馃摎 M贸dulo 4. Conceptos avanzados de funciones

### Clase 11. Funciones an贸nimas: lambda

Son funciones que **no tienen un identificador**. No es necesario usar `return` en este tipo de funciones.

**Sintaxis**

`lambda arguments: expression`

**鈩? Nota:** en Python las funciones lambda s贸lo pueden tener *una sola l铆nea de c贸digo*.

Dado que las funcione an贸nimas no tienen un identificador, para invocarlas se guardan en una variable que va a contener un objeto de tipo `function`.

_**Ejemplo:**_

![Ejemplo lambda](https://i.ibb.co/6HQBS6H/ejemplo-lambda.png)


### Clase 12. High order functions: filter, map y reduce

Una funci贸n de orden superior es *una funci贸n que recibe por par谩metro otra funci贸n.*

Existen 3 tipos de funciones de orden superior que son muy importantes en una gran cantidad de lenguajes de programaci贸n:

#### Filter

Como su nombre lo indica, permite filtrar los elementos de una lista en base a la condici贸n que se defina en una funci贸n lambda. B谩sicamente lo que hace `filter()` es tomar por par谩metro una funci贸n que devuelve true o false indicando si nos interesa el elemento o no, el segundo par谩metro es el objeto iterable al que se quiere aplicar el "filtro".

_**Ejemplo:**_

En el siguiente ejemplo se usa `filter()` para filtrar una lista de n煤meros y obtener los n煤meros que son impares.

![Ejemplo de filter](https://i.ibb.co/nMnSLs2/ejemplo-filter.png)

#### Map

Transforma los elementos de una lista, en base a una *funci贸n transformadora* que se le pasa por par谩metro. A diferencia de `filter()`, `map()` siempre retorna la misma cantidad de elementos del array inicial independientemente de la transformaci贸n que apliquemos. Es posible tambi茅n no modificar ning煤n elemento utilizando una *funci贸n de identidad* que no es m谩s que una funci贸n que siempre devuelve su par谩metro como resultado, as铆 en vez de `a=>b` tenemos `a=>a`.

_**Ejemplo:**_

En el siguiente ejemplo se usa `map()` para elevar al cuadrado a cada uno de los n煤meros de una lista.

![Ejemplo de map](https://i.ibb.co/gMQk1rC/ejemplo-map.png)

#### Reduce

Permite reducir los valores de una lista a un 煤nico valor. A diferencia de las funciones de orden superior anteriores esta necesita ser importada: 

```python
from functools import reduce
```

_**Ejemplo:**_

En el siguiente ejemplo se usa reduce para multiplicar todos los elementos de una lista.

![Ejemplo reduce](https://i.ibb.co/hBnPPGd/ejemplo-reduce.png)

**鈩? Nota:** map, filter y reduce nunca modifican el array original, sino que devuelven una copia que debe ser almacenada en otra variable.

**Explicaci贸n gr谩fica**

![Ejemplo gr谩fico de filter, map y reduce](https://i.ibb.co/tQQ7f4V/1-Dree-F8a4h2pvx-Rly39-Hj-AA.jpg)


### Clase 13. Proyecto: filtrando datos

**Unir diccionarios**

*En versiones de Python > 3.5 y < 3.9*

Se usa `**` en el diccionario original y en el que se va a concatenar

```python
old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA))
```

*En Python 3.9*

Se usa el operador `|` entre el diccionario original y el que se va a concatenar

```python
old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
```


## 馃摎 M贸dulo 5. Manejo de errores

### Clase 14. Los errores en el c贸digo

**Tipos de errores**

![Tipos de errores](https://i.ibb.co/V2m6Qck/tipos-errores-python.png)

#### Syntax Error

Ocurren cuando el c贸digo esta mal escribir. Por ejemplo si en lugar de escribir `for` se escribe `far`. Cuando ocurren este tipo de errores el c贸digo nunca alcanza a ejecutarse pues cuando Python encuentra un error de sintaxis en el c贸digo no ejecuta el c贸digo y en su lugar muestra un mensaje de error en la pantalla.


#### Exception

En este tipo de errores el c贸digo que esta antes de la excepci贸n si se alcanza a ejecutar y dicha ejecuci贸n se interrumpe cuando se lanza una excepci贸n. Cuando se "lanza" dicha dicha excepci贸n Python muestra muestra un menaje de error llamado **traceback** que se lee de abajo hacia arriba.

Si ocurre una excepci贸n y esta no se maneja, Python "eleva" dicha excepci贸n a un scope superior tratando de encontrar un punto en que se le haga manejo a la excepci贸n. Si no lo encuentra muestra el Traceback.


### Clase 15. Debugging

Es una t茅cnica que se usa para encontrar la fuente de los **errores de l贸gica** en el c贸digo. Estos son anomal铆as en el comportamiento del software que a diferencia de los errores de sintaxis y las excepciones, el interprete de Python no alerta sobre este tipo de errores pues estos no est谩n relacionados con el lenguaje de programaci贸n sino con la implementaci贸n del algoritmo en el c贸digo.

**Step Over:** ejecutar la l铆nea que sigue.

**Step Into:** permite "entrar" en una funci贸n para revisar su ejecuci贸n l铆nea por l铆nea.

### Clase 16. Manejo de excepciones

#### Try/Except

Permiten manejar excepciones y ejecutar un fragmento de c贸digo determinado en caso de que ocurra una excepci贸n. La forma en que funciona es que se pone dentro de `try` el c贸digo que puede ser susceptible a lanzar excepciones y luego se maneja la excepci贸n con `except`. Lo que hace `except` es que si ocurre un error dentro del bloque de c贸digo del try, se deja de ejecutar el c贸digo del try y se ejecuta lo que se haya definido en el Except.

_**Ejemplo:**_

![Ejemplo de try/except](https://i.ibb.co/C5JZkBN/try-except-ejemplo.png)

#### raise

Cuando Python no nos informa de un error se puede usar `raise` para elevar una excepci贸n de acuerdo al caso.

_**Ejemplo:**_

![Ejemplo de raise](https://i.ibb.co/zFFcykb/raise-ejemplo.png)

### Finally

Se usa al final de una estructura try/except para hacer cosas como por ejemplo:

- Cerrar un archivo.
- Cerrar una conexi贸n a una base de datos.
- Liberar recursos externos.

Estos usos se deben a que si ocurre una excepci贸n y se interrumpe abruptamente el programa mientras se trabajaba un archivo u se efectu谩 una conexi贸n con una DB, dicho archivo y DB puede da帽arse.

_**Ejemplo:**_

![Ejemplo finally](https://i.ibb.co/2K0F1XQ/finally-ejemplo.png)

`finally` se ejecuta sin importar que ocurra o no una excepci贸n, adem谩s no se usa mucho.


### Clase 18. Assert Statements

Es una forma de combinar el manejo de excepciones con el control del flujo del programa. El funcionamiento de `assert` es el siguiente:

![Funcionamiento assert](https://i.ibb.co/0j51cMR/funcionamiento-assert.png)

**Sintaxis**

```python
assert <condition>, <error message>
```

_**Ejemplo:**_

![Ejemplo assert](https://i.ibb.co/9ZHs7WH/ejemplo-assert.png)

**鈩? Nota:** `isnumeric()` es un m茅todo que evalu谩 si un string es alg煤n tipo de n煤mero. Si es as铆 retorna True, de lo contrario retorna False.


## 馃摎 M贸dulo 6. Manejo de archivos

### Clase 19. 驴C贸mo trabajar con archivos?

Por general al trabajar con archivos en Python se trabaja con archivos de texto, no archivos binarios.

#### Modos de apertura

![Modos de apertura](https://i.ibb.co/JypF8zb/modos-de-apertura.png)

**R:** permite obtener el contenido de un archivo

**W:** lo que hace es borrar el archivo anterior y reemplazarlo con el archivo modificado.

**A:** en lugar de sobrescribir el archivo lo que hace es agregar las modificaciones al final.

**Sintaxis**

```python
with open('./path/to/archive', 'r') as f:
```

`with` es lo que se conoce en Python como un **manejador contextual**. Lo que hace es controlar el flujo del archivo para que en caso de que el programa se cierre abruptamente el archivo no se da帽e.

`as` permite darle un "alias" al archivo para usarlo de forma m谩s sencilla en el c贸digo.


### Clase 20. Trabajando con archivos de texto en Python

```python
with open('./files/numbers.txt', 'r', encoding='utf-8') as f:
```

`encoding='utf-8'` estable la codificaci贸n del archivo para que no se visualicen mal s铆mbolos como las tildes.

Se pude recorrer cada l铆nea de un archivo usando un ciclo for.

```python
numbers = []

with open('./files/numbers.txt', 'r', encoding='utf-8') as f:
    for line in f:
        numbers.append(int(line))
```
Tambi茅n se pueden usar ciclos para escribir en cada l铆nea de un archivo

```python
names = ['Andr茅s', 'Hana', 'Gabriela', 'Felipe']

with open('./files/names.txt', 'w', encoding='utf-8') as f:
    for name in names:
        f.write(name)
        f.write('\n')
```