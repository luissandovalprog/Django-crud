## Requisitos previos

* [Docker](https://www.docker.com/) y Docker Compose instalados.
* Git (para clonar el repositorio).

---

## Instalación y ejecución con Docker

### 1. Clonar el repositorio

```bash
git clone https://github.com/luissandovalprog/django-crud.git
cd django-crud
```

### 2. Configurar las variables de entorno

Crea el archivo `.env` a partir de la plantilla de ejemplo:

* **En Linux / macOS / Git Bash:**
  ```bash
  cp .env.example .env
  ```
* **En Windows (PowerShell):**
  ```powershell
  Copy-Item .env.example .env
  ```

Asegúrate de que tu archivo `.env` contenga la configuración para entorno local (HTTP):

```env
SECRET_KEY=cambia-esta-clave-por-una-segura
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
SECURE_HSTS_SECONDS=0
```

### 3. Construir y levantar el contenedor

```bash
docker compose up --build -d
```

### 4. Aplicar las migraciones de la base de datos

> *Nota: Si el servicio en tu `compose.yaml` tiene un nombre distinto a `web`, reemplázalo en los siguientes comandos.*

```bash
docker compose exec web python manage.py migrate
```

### 5. Crear un usuario de prueba (Superusuario)

Para poder iniciar sesión y acceder al CRUD de productos, crea un usuario administrador:

```bash
docker compose exec web python manage.py createsuperuser
```

Sigue las instrucciones en consola para definir nombre de usuario, correo y contraseña.

---

## Acceso a la aplicación

Una vez levantado el contenedor, abre tu navegador e ingresa a:

* **Aplicación principal:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/) *(redirigirá automáticamente al inicio de sesión)*
* **Inicio de sesión:** [http://127.0.0.1:8000/accounts/login/](http://127.0.0.1:8000/accounts/login/)