# system-service — Registro de capacidades del sistema

## Objetivo

Ampliar `system-service` para que actúe como el **registro central de las capacidades disponibles en Nova**.

El servicio seguirá siendo ligero y sin dependencias externas, pero además de exponer la identidad del sistema será capaz de almacenar y servir la lista de funcionalidades actualmente disponibles.

La fuente de verdad seguirá siendo el **Orchestrator**.

---

# Motivación

Cuando el Orchestrator arranca:

1. Descubre todos los plugins.
2. Los registra internamente.
3. Publica la lista completa de funcionalidades en `system-service`.

A partir de ese momento cualquier servicio o plugin podrá consultar las capacidades disponibles sin necesidad de depender directamente del Orchestrator.

Esto desacopla el ecosistema y evita múltiples integraciones innecesarias.

---

# Principios de diseño

## El Orchestrator es la única fuente de verdad

Solo el Orchestrator conoce realmente qué plugins existen.

`system-service` nunca descubre plugins.

Únicamente almacena la información que recibe.

---

## Sustitución completa

Cada actualización reemplaza completamente la lista existente.

No existen operaciones para añadir o eliminar funcionalidades individuales.

El estado siempre representa exactamente lo que conoce el Orchestrator.

---

## Almacenamiento en memoria

No se utilizará ninguna base de datos.

La lista de capacidades permanecerá únicamente en memoria.

Si el servicio se reinicia, el Orchestrator volverá a publicarla durante su proceso de inicialización.

---

# Arquitectura

```text
                 Arranque

          +----------------+
          |  Orchestrator  |
          +----------------+
                  |
        Descubre plugins
                  |
                  |
POST /v1/system/capabilities
                  |
                  v
          +----------------+
          | system-service |
          +----------------+
                  |
         Guarda capacidades
                  |

--------------------------------------------

Cualquier servicio

GET /v1/system/capabilities

                  |
                  v

          +----------------+
          | system-service |
          +----------------+
                  |
        Devuelve capacidades
```

---

# API REST

## Registrar capacidades

### Endpoint

```http
POST /v1/system/capabilities
```

### Request

```json
{
  "capabilities": [
    {
      "id": "identity",
      "description": "Información sobre Nova"
    },
    {
      "id": "weather",
      "description": "Consultar el tiempo"
    },
    {
      "id": "mail",
      "description": "Enviar y consultar correo"
    }
  ]
}
```

### Comportamiento

* Sustituye completamente la lista almacenada.
* No realiza operaciones incrementales.
* Debe ser idempotente.
* Devuelve éxito si la lista queda almacenada correctamente.

### Response

```json
{
  "success": true
}
```

---

## Obtener capacidades

### Endpoint

```http
GET /v1/system/capabilities
```

### Response

```json
{
  "capabilities": [
    {
      "id": "identity",
      "description": "Información sobre Nova"
    },
    {
      "id": "weather",
      "description": "Consultar el tiempo"
    },
    {
      "id": "mail",
      "description": "Enviar y consultar correo"
    }
  ]
}
```

Si todavía no se ha registrado ninguna capacidad, devolver:

```json
{
  "capabilities": []
}
```

No debe producir error.

---

# Modelo de datos

```python
class Capability:
    id: str
    description: str
```

```python
class CapabilityList:
    capabilities: list[Capability]
```

---

# Service Layer

Crear un nuevo servicio:

```
CapabilityService
```

Responsabilidades:

* almacenar la lista en memoria
* reemplazar completamente la lista
* devolver la lista actual

No contiene ninguna lógica adicional.

---

# Controller

Añadir un nuevo controlador encargado de:

```
POST /v1/system/capabilities

GET /v1/system/capabilities
```

El controlador delegará toda la lógica en `CapabilityService`.

---

# Integración con el Orchestrator

Durante el proceso de inicialización:

```
Iniciar Orchestrator

↓

Descubrir plugins

↓

Construir lista de capacidades

↓

POST /v1/system/capabilities

↓

Sistema listo
```

El envío debe realizarse una única vez durante el arranque.

---

# Gestión de errores

## POST

Si la petición es válida:

```
HTTP 200
```

Si el cuerpo no cumple el contrato:

```
HTTP 400
```

---

## GET

Siempre devuelve:

```
HTTP 200
```

Aunque todavía no existan capacidades registradas.

---

# Consideraciones futuras

El modelo de datos se diseña pensando en futuras ampliaciones.

Más adelante cada capacidad podrá incorporar información adicional como:

* categoría
* versión
* permisos requeridos
* alias
* ejemplos de uso
* nombre visible para el usuario

Sin modificar el contrato básico del servicio.

---

# Resultado esperado

Una vez implementada esta fase:

* `system-service` seguirá siendo un servicio extremadamente ligero.
* El Orchestrator continuará siendo la fuente de verdad del ecosistema.
* Cualquier plugin podrá descubrir dinámicamente las capacidades disponibles mediante un único endpoint REST.
* El futuro plugin "¿Qué puedes hacer?" podrá utilizar directamente este endpoint sin necesidad de conocer el Orchestrator.

