# Auto_Registre_Jornada

Script para registrar la jornada de forma automática.

## Ejecución Local

Para ejecutar este script en tu entorno local, sigue estos pasos:

1. **Crear un Entorno Virtual**:

    ```bash
    python -m venv myvenv
    ```

2. **Activar el Entorno Virtual**:

    - Windows:

      ```cmd
      myvenv\Scripts\activate
      ```

    - macOS/Linux:

      ```bash
      source myvenv/bin/activate
      ```

3. **Instalar Dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecutar el Script**:

    ```bash
    python registre_jornada/app.py
    ```

5. **Desactivar el Entorno Virtual** (cuando hayas terminado):

    ```bash
    deactivate
    ```

## Configuración del archivo .env

Crea un archivo `.env` en el directorio raíz con la siguiente estructura:

```env
# dentro del archivo llamado .env

codigo_centro = "xxxxxxxxxxx"
username = "xxxxxxxxxxxx"
password = "xxxxxxxxxxxxx"
# ... (resto del contenido)
