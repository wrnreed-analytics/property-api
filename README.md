# Property API

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

REST API for real estate property valuation and market intelligence. Built with FastAPI, backed by PostgreSQL, and designed to serve the 12-factor scoring engine from [property-market-analyzer](https://github.com/wrnreed-analytics/property-market-analyzer) over HTTP.

## Features

- **Property Scoring Endpoint** — Score individual properties against the 12-factor valuation model
- **Batch Operations** — Submit multiple properties in a single request
- **Market Intelligence** — Trends, inventory, and appreciation data by market
- **Health Checks** — Production-ready liveness and readiness probes
- **CORS Support** — Configured for cross-origin requests from the dashboard frontend
- **Docker Deployment** — Dockerfile included for containerized environments

## API Endpoints

```
GET  /health                              # Health check
GET  /api/v1/properties/{id}/score        # Score a single property
POST /api/v1/properties/batch-score       # Score multiple properties
GET  /api/v1/properties/search            # Search with filters (market, price, score)
GET  /api/v1/markets/{market}/trends      # Market trend data
```

### Example: Score a Property

```bash
curl http://localhost:8000/api/v1/properties/prop_00123/score
```

```json
{
  "id": "prop_00123",
  "address": "742 Evergreen Terrace, Seattle WA",
  "valuation_score": 82.4,
  "price_vs_comps_score": 88.0,
  "cap_rate_score": 76.0,
  "price_trend_score": 85.0,
  "estimated_value": 502000,
  "cap_rate": 4.2
}
```

## Quick Start

```bash
git clone https://github.com/wrnreed-analytics/property-api.git
cd property-api
pip install -r requirements.txt
uvicorn property_api.main:app --reload
```

The API is available at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

### Docker

```bash
docker build -t property-api .
docker run -p 8000:8000 property-api
```

## Project Structure

```
property-api/
├── property_api/
│   ├── __init__.py
│   ├── main.py              # FastAPI app, middleware, startup
│   ├── routers/
│   │   ├── __init__.py
│   │   └── properties.py    # Property scoring and search routes
│   └── services/
│       └── __init__.py       # Business logic layer
├── Dockerfile
├── requirements.txt
├── setup.py
└── LICENSE
```

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | — | PostgreSQL connection string |
| `REDIS_URL` | — | Redis URL for caching (optional) |
| `CORS_ORIGINS` | `*` | Allowed origins for CORS |
| `LOG_LEVEL` | `INFO` | Logging verbosity |

## Tech Stack

- **FastAPI** — async Python web framework
- **Uvicorn** — ASGI server
- **SQLAlchemy 2.0** — ORM and query builder
- **PostgreSQL** — primary data store
- **Redis** — optional response caching
- **Pydantic** — request/response validation
- **Locust** — load testing

## Related Repos

| Repo | Description |
|------|-------------|
| [property-market-analyzer](https://github.com/wrnreed-analytics/property-market-analyzer) | Core 12-factor scoring engine (used as a library) |
| [property-dashboard](https://github.com/wrnreed-analytics/property-dashboard) | Vue 3 frontend that consumes this API |
| [property-ml-models](https://github.com/wrnreed-analytics/property-ml-models) | ML models integrated for price prediction |
| [property-valuation-dataset](https://github.com/wrnreed-analytics/property-valuation-dataset) | Sample dataset for testing |

## License

MIT

---

**Wren Reed** — Data Analyst | Real Estate Intelligence | Python & SQL
[wren.reed.analytics@proton.me](mailto:wren.reed.analytics@proton.me) | [LinkedIn](https://linkedin.com/in/wrenreedanalytics)
