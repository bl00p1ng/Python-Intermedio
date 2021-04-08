# Curso de Python Intermedio

Apuntes y código del Curso de Python Intermedio

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

_**Ejemplo:_*

```python
my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
```