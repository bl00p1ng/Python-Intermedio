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