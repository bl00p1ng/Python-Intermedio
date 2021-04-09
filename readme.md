# Curso de Python Intermedio

Apuntes y código del Curso de Python Intermedio de Platzi

[Repositorio Oficial del Curso](https://github.com/facmartoni/curso-intermedio-python)

- [Curso de Python Intermedio](#curso-de-python-intermedio)
  - [📚 Módulo 1. Preparación antes de empezar](#-módulo-1-preparación-antes-de-empezar)
    - [Clase 2. El Zen de Python](#clase-2-el-zen-de-python)
  - [📚 Módulo 2. Entorno virtual](#-módulo-2-entorno-virtual)
    - [Clase 5. El primer paso profesional: creación de un entorno](#clase-5-el-primer-paso-profesional-creación-de-un-entorno)
    - [Clase 6. Instalación de dependencias con pip](#clase-6-instalación-de-dependencias-con-pip)
  - [📚 Módulo 3. Alternativa a los ciclos: comprehensions](#-módulo-3-alternativa-a-los-ciclos-comprehensions)
    - [Clase 8. Listas y diccionarios anidados](#clase-8-listas-y-diccionarios-anidados)
    - [Clase 9. List Comprehensions](#clase-9-list-comprehensions)
    - [Clase 10. Dictionary comprehensions](#clase-10-dictionary-comprehensions)
  - [📚 Módulo 4. Conceptos avanzados de funciones](#-módulo-4-conceptos-avanzados-de-funciones)
    - [Clase 11. Funciones anónimas: lambda](#clase-11-funciones-anónimas-lambda)
    - [Clase 12. High order functions: filter, map y reduce](#clase-12-high-order-functions-filter-map-y-reduce)
      - [Filter](#filter)
      - [Map](#map)
      - [Reduce](#reduce)
    - [Clase 13. Proyecto: filtrando datos](#clase-13-proyecto-filtrando-datos)
  - [📚 Módulo 5. Manejo de errores](#-módulo-5-manejo-de-errores)
    - [Clase 14. Los errores en el código](#clase-14-los-errores-en-el-código)
      - [Syntax Error](#syntax-error)
      - [Exception](#exception)
    - [Clase 15. Debugging](#clase-15-debugging)
    - [Clase 16. Manejo de excepciones](#clase-16-manejo-de-excepciones)
      - [Try/Except](#tryexcept)
      - [raise](#raise)
    - [Finally](#finally)

## 📚 Módulo 1. Preparación antes de empezar

### Clase 2. El Zen de Python

Son los 20 principios del desarrollo de software más importantes de este lenguaje, permiten escribir código de forma correcta y precisa. Fueron creados en 1999.

**Cómo ver el Zen de Python**

1. Abrir la consola interactiva de PythonClase 6. Instalación de dependencias con pip
![Zen de Python en Español parte 4](https://i.ibb.co/3zz1xMv/zen-python-4.png)

## 📚 Módulo 2. Entorno virtual

### Clase 5. El primer paso profesional: creación de un entorno

1. Crear el entorno virtual
    ```bash
    python3 -m venv venv
    ```
2. Activar el entorno virtual (en sistema tipo UNIX o Linux)
    ```bash
    source venv/bin/activate
    ```

Para salir del entorno virtual se usa el comando `deactivate`

### Clase 6. Instalación de dependencias con pip

**Compartir dependencias de un proyecto**

```bash
pip freeze > requeriments.txt
```

Esto guardará en el archivo `requeriments.txt` las dependencias del proyecto con sus respectivas versiones.

Luego para que la persona a la que se comparta el proyecto pueda instalar las dependencias tiene que usar el comando:

```bash
piṕ install -r requeriments.txt
```

## 📚 Módulo 3. Alternativa a los ciclos: comprehensions

### Clase 8. Listas y diccionarios anidados

Se pueden tener listas que guarden diccionarios y diccionarios que guarden listas.

```python
super_list = [
        {"firstname": "Andrés", "lastname": "López"},
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

**Cómo funcionan**

![Cómo funcionan los list comprehensions](https://i.ibb.co/3vvyp12/1-z-J0-Xf-N1fk-WSvll2-Bg8o46g.png)

[Más información sobre el funcionamiento de los List Comprehensions](https://towardsdatascience.com/all-about-python-list-comprehension-14dd979ec0d1)

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

## 📚 Módulo 4. Conceptos avanzados de funciones

### Clase 11. Funciones anónimas: lambda

Son funciones que **no tienen un identificador**. No es necesario usar `return` en este tipo de funciones.

**Sintaxis**

`lambda arguments: expression`

**ℹ Nota:** en Python las funciones lambda sólo pueden tener *una sola línea de código*.

Dado que las funcione anónimas no tienen un identificador, para invocarlas se guardan en una variable que va a contener un objeto de tipo `function`.

_**Ejemplo:**_

![Ejemplo lambda](https://i.ibb.co/6HQBS6H/ejemplo-lambda.png)


### Clase 12. High order functions: filter, map y reduce

Una función de orden superior es *una función que recibe por parámetro otra función.*

Existen 3 tipos de funciones de orden superior que son muy importantes en una gran cantidad de lenguajes de programación:

#### Filter

Como su nombre lo indica, permite filtrar los elementos de una lista en base a la condición que se defina en una función lambda. Básicamente lo que hace `filter()` es tomar por parámetro una función que devuelve true o false indicando si nos interesa el elemento o no, el segundo parámetro es el objeto iterable al que se quiere aplicar el "filtro".

_**Ejemplo:**_

En el siguiente ejemplo se usa `filter()` para filtrar una lista de números y obtener los números que son impares.

![Ejemplo de filter](https://i.ibb.co/nMnSLs2/ejemplo-filter.png)

#### Map

Transforma los elementos de una lista, en base a una *función transformadora* que se le pasa por parámetro. A diferencia de `filter()`, `map()` siempre retorna la misma cantidad de elementos del array inicial independientemente de la transformación que apliquemos. Es posible también no modificar ningún elemento utilizando una *función de identidad* que no es más que una función que siempre devuelve su parámetro como resultado, así en vez de `a=>b` tenemos `a=>a`.

_**Ejemplo:**_

En el siguiente ejemplo se usa `map()` para elevar al cuadrado a cada uno de los números de una lista.

![Ejemplo de map](https://i.ibb.co/gMQk1rC/ejemplo-map.png)

#### Reduce

Permite reducir los valores de una lista a un único valor. A diferencia de las funciones de orden superior anteriores esta necesita ser importada: 

```python
from functools import reduce
```

_**Ejemplo:**_

En el siguiente ejemplo se usa reduce para multiplicar todos los elementos de una lista.

![Ejemplo reduce](https://i.ibb.co/hBnPPGd/ejemplo-reduce.png)

**ℹ Nota:** map, filter y reduce nunca modifican el array original, sino que devuelven una copia que debe ser almacenada en otra variable.

**Explicación gráfica**

![Ejemplo gráfico de filter, map y reduce](https://i.ibb.co/tQQ7f4V/1-Dree-F8a4h2pvx-Rly39-Hj-AA.jpg)


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


## 📚 Módulo 5. Manejo de errores

### Clase 14. Los errores en el código

**Tipos de errores**

![Tipos de errores](https://i.ibb.co/V2m6Qck/tipos-errores-python.png)

#### Syntax Error

Ocurren cuando el código esta mal escribir. Por ejemplo si en lugar de escribir `for` se escribe `far`. Cuando ocurren este tipo de errores el código nunca alcanza a ejecutarse pues cuando Python encuentra un error de sintaxis en el código no ejecuta el código y en su lugar muestra un mensaje de error en la pantalla.


#### Exception

En este tipo de errores el código que esta antes de la excepción si se alcanza a ejecutar y dicha ejecución se interrumpe cuando se lanza una excepción. Cuando se "lanza" dicha dicha excepción Python muestra muestra un menaje de error llamado **traceback** que se lee de abajo hacia arriba.

Si ocurre una excepción y esta no se maneja, Python "eleva" dicha excepción a un scope superior tratando de encontrar un punto en que se le haga manejo a la excepción. Si no lo encuentra muestra el Traceback.


### Clase 15. Debugging

Es una técnica que se usa para encontrar la fuente de los **errores de lógica** en el código. Estos son anomalías en el comportamiento del software que a diferencia de los errores de sintaxis y las excepciones, el interprete de Python no alerta sobre este tipo de errores pues estos no están relacionados con el lenguaje de programación sino con la implementación del algoritmo en el código.

**Step Over:** ejecutar la línea que sigue.

**Step Into:** permite "entrar" en una función para revisar su ejecución línea por línea.

### Clase 16. Manejo de excepciones

#### Try/Except

Permiten manejar excepciones y ejecutar un fragmento de código determinado en caso de que ocurra una excepción. La forma en que funciona es que se pone dentro de `try` el código que puede ser susceptible a lanzar excepciones y luego se maneja la excepción con `except`. Lo que hace `except` es que si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.

_**Ejemplo:**_

![Ejemplo de try/except](https://i.ibb.co/C5JZkBN/try-except-ejemplo.png)

#### raise

Cuando Python no nos informa de un error se puede usar `raise` para elevar una excepción de acuerdo al caso.

_**Ejemplo:**_

![Ejemplo de raise](https://i.ibb.co/zFFcykb/raise-ejemplo.png)

### Finally

Se usa al final de una estructura try/except para hacer cosas como por ejemplo:

- Cerrar un archivo.
- Cerrar una conexión a una base de datos.
- Liberar recursos externos.

Estos usos se deben a que si ocurre una excepción y se interrumpe abruptamente el programa mientras se trabajaba un archivo u se efectuá una conexión con una DB, dicho archivo y DB puede dañarse.

_**Ejemplo:**_

![Ejemplo finally](https://i.ibb.co/2K0F1XQ/finally-ejemplo.png)

`finally` se ejecuta sin importar que ocurra o no una excepción, además no se usa mucho.



