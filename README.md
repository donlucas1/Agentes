# 🌍 Turismo Multi-Agente

Aplicación ejemplo para planificar viajes utilizando tres agentes especializados:

1. **Alojamiento** – busca opciones de hospedaje (Airbnb/Booking).
2. **Visitas turísticas** – sugiere atracciones en la ciudad usando OpenTripMap.
3. **Requisitos de viaje** – consulta necesidades de visado y pasaporte con TravelBriefing.

La aplicación expone una API REST construida con [FastAPI](https://fastapi.tiangolo.com/) y está lista para desplegarse en [Railway](https://railway.app/).

## 🚀 Uso

```bash
# Instalar dependencias
pip install -r requirements.txt

# Iniciar servidor de desarrollo
uvicorn app.main:app --reload
```

### Endpoints principales
- `GET /accommodation?city=Barcelona&check_in=2024-01-01&check_out=2024-01-05`
- `GET /sightseeing?city=Barcelona`
- `GET /requirements?country_from=ARG&country_to=ESP`

Para producción en Railway se incluye un `Procfile` con el comando apropiado.

## 🔑 Variables de entorno
Algunos proveedores necesitan claves de API:

- `AIRBNB_API_KEY` – Clave del proveedor de alojamiento elegido.
- `OPENTRIPMAP_API_KEY` – Requerida para obtener atracciones turísticas.

## 📄 Licencia
MIT
