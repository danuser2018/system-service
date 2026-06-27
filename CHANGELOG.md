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

## Sin publicar

- Documentación para el registro de capacidades del sistema

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
