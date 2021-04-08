# Curso de Python Intermedio

Apuntes y código del Curso de Python Intermedio

[Repositorio Oficial del Curso](https://github.com/facmartoni/curso-intermedio-python)

- [Curso de Python Intermedio](#curso-de-python-intermedio)
  - [📚 Módulo 1. Preparación antes de empezar](#-módulo-1-preparación-antes-de-empezar)
    - [Clase 2. El Zen de Python](#clase-2-el-zen-de-python)
  - [📚 Módulo 2. Entorno virtual](#-módulo-2-entorno-virtual)
    - [Clase 5. El primer paso profesional: creación de un entorno](#clase-5-el-primer-paso-profesional-creación-de-un-entorno)
    - [Clase 6. Instalación de dependencias con pip](#clase-6-instalación-de-dependencias-con-pip)

## 📚 Módulo 1. Preparación antes de empezar

### Clase 2. El Zen de Python

Son los 20 principios del desarrollo de software más importantes de este lenguaje, permiten escribir código de forma correcta y precisa. Fueron creados en 1999.

**Cómo ver el Zen de Python**

1. Abrir la consola interactiva de Python
2. Importar `this`, este es el módulo que contiene el Zen de Python. Esto se hace ejecutando la siguiente línea en la consola: `import this`

**El Zen de Python en español**

![Zen de Python en Español parte 1](https://i.ibb.co/M2ZHrM7/zen-python-1.png)
![Zen de Python en Español parte 2](https://i.ibb.co/N6k4brF/zen-python-2.png)
![Zen de Python en Español parte 3](https://i.ibb.co/cTB5gf6/zen-python-3.png)
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