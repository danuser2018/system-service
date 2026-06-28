# system-service (Nova)

## 📌 Visión general

`system-service` es un microservicio del ecosistema Nova encargado de exponer **información básica de identidad del sistema** y actuar como el **registro central de capacidades del sistema**.

Los endpoints funcionales son:

* `GET /system/info`: Devuelve información estática de identidad sobre Nova.
* `POST /system/capabilities`: Permite al Orchestrator registrar las capacidades disponibles en el sistema.
* `GET /system/capabilities`: Permite consultar la lista de capacidades registradas.


---

## 🎯 Objetivo de la fase 1

El objetivo de este servicio es:

* Exponer información básica del sistema Nova
* Proveer una API simple, estable y predecible
* Servir como base de integración entre plugins y servicios
* Integrarse únicamente con el Orchestrator mediante el Identity Plugin

---

## 🧠 Principios de diseño

Este servicio sigue los siguientes principios fundamentales:

### 1. Single Responsibility

El servicio solo gestiona información de identidad del sistema.

---

### 2. Stateless

No mantiene estado en memoria ni dependencias externas en runtime.

---

### 3. Read-only API

En esta fase solo se exponen endpoints de lectura.

---

### 4. Simplicidad extrema

El servicio debe ser fácil de desplegar, mantener y extender.

---

### 5. Integración mínima

Solo existe una integración activa en esta fase: Orchestrator → Identity Plugin → system-service.

---

## 🧱 Arquitectura del sistema

### Flujo de integración

```text id="arch-flow"
Usuario
  ↓
Orchestrator
  ↓
Identity Plugin
  ↓
system-service
  ↓
GET /system/info
  ↓
Respuesta JSON
```

---

### Arquitectura interna del servicio

```text id="internal-arch"
system-service
├── API Layer (HTTP server)
├── Routes Layer
├── Controller Layer
├── Service Layer (SystemInfoService)
└── Configuration Layer (env vars + defaults)
```

---

## 🔧 Componentes internos

### 1. API Layer

Responsabilidades:

* Exponer servidor HTTP
* Gestionar requests/responses
* Exponer endpoints REST

---

### 2. Routes Layer

Responsabilidades:

* Definir rutas del servicio
* Mapear endpoints a controllers

---

### 3. Controller Layer

Responsabilidades:

* Recibir peticiones HTTP
* Invocar la lógica del service layer
* Formatear respuestas JSON

---

### 4. Service Layer

Clase principal:

```text id="service-class"
SystemInfoService
```

Responsabilidades:

* Construir objeto SystemInfo
* Leer variables de entorno
* Aplicar valores por defecto si es necesario

---

### 5. Configuration Layer

Responsabilidades:

* Gestionar variables de entorno
* Proveer configuración base del sistema

---

## 📥 API REST

## 🔹 System Info

### Endpoint

```http id="endpoint-system-info"
GET /system/info
```

---

### Descripción

Devuelve la información de identidad del sistema Nova.

---

### Response

```json id="response-system-info"
{
  "name": "Nova",
  "author": "David",
  "version": "0.1.0",
  "description": "Asistente personal de voz y automatización"
}
```

---

### Modelo de datos

```python id="model-system-info"
class SystemInfo(BaseModel):
    name: str
    author: str
    version: str
    description: str
```

---

### Fuente de datos

Los valores provienen de variables de entorno:

```bash id="env-vars"
NOVA_NAME=Nova
NOVA_AUTHOR=David
NOVA_VERSION=0.1.0
NOVA_DESCRIPTION=Asistente personal de voz y automatización
```

Si no están definidas, se usan valores por defecto hardcoded.

---

## 🔹 System Capabilities

### Endpoint (Registrar capacidades)

```http id="endpoint-post-capabilities"
POST /system/capabilities
```

---

### Descripción

Sustituye completamente la lista de capacidades en memoria. Operación idempotente.

---

### Request

```json id="request-post-capabilities"
{
  "capabilities": [
    {
      "id": "identity",
      "description": "Información sobre Nova"
    },
    {
      "id": "weather",
      "description": "Consultar el tiempo"
    }
  ]
}
```

---

### Response

```json id="response-post-capabilities"
{
  "success": true
}
```

---

### Endpoint (Obtener capacidades)

```http id="endpoint-get-capabilities"
GET /system/capabilities
```

---

### Descripción

Devuelve la lista actual de capacidades registradas. Si no hay ninguna, devuelve una lista vacía.

---

### Response

```json id="response-get-capabilities"
{
  "capabilities": [
    {
      "id": "identity",
      "description": "Información sobre Nova"
    },
    {
      "id": "weather",
      "description": "Consultar el tiempo"
    }
  ]
}
```

---

### Modelo de datos

```python id="model-capabilities"
class Capability(BaseModel):
    id: str
    description: str

class CapabilityList(BaseModel):
    capabilities: list[Capability]
```

---

## 🩺 Health Check

El servicio expone un endpoint de salud para verificar su estado operativo.

---

### Endpoint

```http id="health-endpoint"
GET /health
```

---

### Ejemplo de llamada

```bash id="health-curl"
curl http://localhost:8000/health
```

---

### Respuesta esperada

```json id="health-response"
{
  "status": "ok"
}
```

---

### Semántica

* `ok` → servicio operativo
* cualquier otro caso → servicio no saludable

---

### Uso en Docker

```yaml id="docker-healthcheck"
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
  interval: 30s
  timeout: 5s
  retries: 3
```

---

## 🐳 Docker

### 📦 Dockerfile

```dockerfile id="dockerfile"
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "-m", "src.main"]
```

---

### 🚀 Build de imagen

```bash id="docker-build"
docker build -t nova/system-service:1.0 .
```

---

### ▶️ Ejecutar contenedor

```bash id="docker-run"
docker run -d \
  --name system-service \
  -p 8000:8000 \
  -e NOVA_NAME=Nova \
  -e NOVA_AUTHOR=David \
  -e NOVA_VERSION=0.1.0 \
  -e NOVA_DESCRIPTION="Asistente personal de voz y automatización" \
  nova/system-service:1.0
```

---

## 📁 Estructura del proyecto

```text id="project-structure"
system-service/
├── src/
│   ├── api/
│   ├── config/
│   ├── controllers/
│   ├── routes/
│   ├── services/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🔌 Integración con Orchestrator (única en Fase 1)

El servicio no es consumido directamente por usuarios.

Flujo obligatorio:

```text id="integration-flow"
Usuario
  ↓
Orchestrator
  ↓
Identity Plugin
  ↓
HTTP GET /system/info
  ↓
Respuesta JSON
  ↓
Respuesta en lenguaje natural
```

---

## 🧩 Identity Plugin (contrato esperado)

El Identity Plugin debe:

* llamar a `/system/info`
* transformar JSON en respuesta natural
* responder preguntas como:

  * “¿quién eres?”
  * “¿qué eres Nova?”
  * “¿quién te creó?”

---

## 🧠 Reglas de implementación

### 1. No añadir endpoints adicionales

Solo `/system/info` y `/health`.

---

### 2. Respuesta determinista

La información del sistema no cambia en runtime.

---

### 3. Alta disponibilidad

Debe ser extremadamente ligero y rápido.

---

### 4. Sin dependencias externas obligatorias

No requiere base de datos ni servicios externos.

---

## 🚀 Evolución futura (no incluida en esta fase)

En futuras versiones se podrán añadir:

* `/system/status`
* `/config`
* métricas de sistema
* control avanzado del runtime

Esto queda fuera del alcance de Fase 1.

---

## 🧭 Filosofía del servicio

`system-service` representa la **identidad estática del sistema Nova**.

No ejecuta lógica de usuario.

No contiene inteligencia.

No decide nada.

Simplemente responde:

> “esto es Nova en este momento”
