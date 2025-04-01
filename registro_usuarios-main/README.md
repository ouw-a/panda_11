# Proyecto de Registro de Usuarios

Este proyecto es una aplicación web desarrollada con Flask, HTML, CSS, JavaScript y SQLite para la gestión de usuarios. Permite registrar, listar y gestionar usuarios a través de una interfaz gráfica sencilla.

## Estructura del Proyecto

```
📂 registro_usuarios/
│── 📂 static/                 # Archivos estáticos como CSS y JS
│   │── 📂 css/                # Estilos de la aplicación
│       │── 📄 flash_message.css   # Estilos para mensajes flash o notificaciones
│       │── 📄 form_style.css      # Estilos para formularios
│       │── 📄 nav_style.css       # Estilos de navegación (header, sidebar, etc.)
│       │── 📄 table_style.css     # Estilos para tablas (listado de usuarios, datos, etc.)
│   │── 📂 js/                 # Scripts JavaScript
│       │── 📄 script.js       # Archivo principal de scripts JS (validaciones, interactividad)
│── 📂 templates/                # Archivos HTML con Jinja2 para renderizar vistas
│   │── 📄 index.html          # Página principal del sistema
│   │── 📄 users.html          # Página de gestión de usuarios
│── 📄 .gitignore              # Archivos y carpetas a excluir en Git
│── 📄 app.py                  # Archivo principal de Flask (define rutas y ejecuta la aplicación)
│── 📄 db_manager.py           # Módulo para el manejo de la base de datos SQLite
│── 📄 usuarios.db             # Base de datos SQLite (debe estar en .gitignore)
│── 📄 LICENSE                 # Licencia del proyecto
│── 📄 requirements.txt        # Dependencias necesarias para el proyecto
│── 📄 README.md               # Documentación del proyecto
```

## Instalación y Configuración

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/registro_usuarios.git
   cd registro_usuarios
   ```

2. Crear un entorno virtual e instalar dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Ejecutar la aplicación:
   ```bash
   python app.py
   ```

4. Acceder a la aplicación desde el navegador:
   ```
   http://127.0.0.1:5000/
   ```

## Uso

- **Registro de Usuarios:** Permite agregar nuevos usuarios.
- **Listado de Usuarios:** Muestra una tabla con los usuarios registrados.

## Tecnologías Utilizadas

- **Backend:** Flask (Python)
- **Base de Datos:** SQLite
- **Frontend:** HTML, CSS, JavaScript

## Mejoras Futuras

- Implementar Flask-SQLAlchemy para mayor flexibilidad.
- Migrar a MySQL para mejor escalabilidad.
- Agregar autenticación con Flask-Login.

## Licencia

Este proyecto está licenciado bajo la MIT License - ver el archivo **LICENSE** para más detalles.

---
