# Tienda de Arriendo de Películas

Este proyecto es una aplicación web desarrollada con Django para la gestión de arriendo de películas. Permite administrar clientes, películas, géneros y realizar operaciones de arriendo y devolución.

## Características

- Registro, edición y eliminación de películas.
- Gestión de clientes.
- Administración de géneros de películas.
- Registro de arriendos y devoluciones.
- Panel de administración de Django.

## Estructura del Proyecto

```
III_Entrega_Tu_Primera_Pagina/
│
├── App_Arriendo_Peliculas/      # Aplicación principal (modelos, vistas, urls)
├── Proyecto_Tienda_Peliculas/   # Configuración del proyecto Django
├── static/                      # Archivos estáticos (CSS, JS, imágenes)
├── templates/                   # Plantillas HTML
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Este archivo
```

## Instalación

1. **Clona el repositorio o descarga el código fuente.**

2. **Crea y activa un entorno virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realiza las migraciones de la base de datos:**
   ```bash
   python manage.py migrate
   ```

5. **Ejecuta el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

6. **Accede a la aplicación:**
   - Sitio principal: [http://localhost:8000/](http://localhost:8000/)
   - Panel de administración: [http://localhost:8000/admin/](http://localhost:8000/admin/)
   - user admin = admin    ;   password admin = pato1234

## Uso

- Desde el panel de administración puedes gestionar Clientes, Películas y Generos.
- Desde la interfaz principal puedes registrar nuevos Clientes, Películas y Generos.
- Personaliza las plantillas HTML en la carpeta `templates/` y los estilos en `static/`.

## Dependencias Principales

- Django 5.2.3
- asgiref 3.8.1
- sqlparse 0.5.3
- tzdata 2025.2

## Autor

Desarrollado por Patricio Cárdenas Vásquez.

---

Siéntete libre de modificar este README según las características específicas de tu