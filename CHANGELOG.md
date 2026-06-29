# Registro de cambios

Todos los cambios notables de este proyecto se documentan en este fichero.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y este proyecto adhiere a [Versionado Semántico](https://semver.org/lang/es/).

## Guía de uso

Cada versión se documenta bajo su número de versión y fecha de publicación.
Los cambios se agrupan en las siguientes categorías:

- **Añadido** — nuevas funcionalidades.
- **Cambiado** — cambios en funcionalidades existentes.
- **Obsoleto** — funcionalidades que serán eliminadas en versiones futuras.
- **Eliminado** — funcionalidades eliminadas en esta versión.
- **Corregido** — corrección de errores.
- **Seguridad** — correcciones de vulnerabilidades.

---

## [1.3.0] - 2026-06-30

### Corregido

- Corregidas las discrepancias de documentación de los endpoints añadiendo el prefijo `/v1` en `README.md` y `registro_capacidades_sistema.md`.
- Cambiado el autor por defecto (`NOVA_AUTHOR`) de `"David"` a `"Xeretre studios"` en código, composición de Docker, README y pruebas.
- Actualizada la versión documentada en `README.md` a `"2.0.0"` para alinearse con la configuración predeterminada.
- Corregida la referencia de la imagen de Docker en `README.md` para utilizar `danuser2018/system-service:latest`.

## [1.2.0] - 2026-06-28

### Cambiado

- Corregido el documento README.md para reflejar que la tecnología del microservicio es Python y FastAPI en lugar de Node.js.

### Añadido


- Nueva carpeta `.agent/skills` con información relevante para la IA.

## [1.1.0] - 2026-06-27

- Endpoint `POST /system/capabilities` para almacenar la lista de capacidades en memoria (reemplazo completo e idempotente).
- Endpoint `GET /system/capabilities` para recuperar la lista de capacidades registradas.
- Manejador global de excepciones en FastAPI para errores de validación de peticiones (`RequestValidationError`) para que retornen HTTP 400 Bad Request en lugar de HTTP 422.
- Documentación y modelo en `README.md` del nuevo contrato de capacidades del sistema.

## [1.0.0] - 2026-06-14

### Añadido

- Fichero `CONTRIBUTING.md` con el flujo de trabajo Trunk Based Development,
  convenciones de commits, guía de Pull Requests y buenas prácticas para
  desarrollo asistido con IA.
- Fichero `CHANGELOG.md` con el formato Keep a Changelog v1.1.0 en castellano.
- Fichero `README.md` con las características del servicio.
- Implementación completa del servicio en Python usando FastAPI.
- Configuración para cargar variables de entorno `NOVA_NAME`, `NOVA_AUTHOR`, `NOVA_VERSION` (por defecto `2.0.0`) y `NOVA_DESCRIPTION`.
- Endpoints expuestos: `GET /system/info` y `GET /health`.
- Dockerización con `Dockerfile` y `docker-compose.yml`.
- Pruebas unitarias e integradas con `pytest` y `FastAPI TestClient`.
- Workflow de GitHub Actions (`test.yml`) para ejecutar pruebas automatizadas en cada PR.

---

## Sin publicar

<!-- Plantilla para nuevas versiones:

## [X.Y.Z] - AAAA-MM-DD

### Añadido
-

### Cambiado
-

### Obsoleto
-

### Eliminado
-

### Corregido
-

### Seguridad
-

-->

[Sin publicar]: https://github.com/danuser2018/workspace/system-service/compare/HEAD...HEAD
