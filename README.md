# DevOps Backend

A minimal FastAPI service used as a build/deploy target while practicing Docker and CI basics — not a feature project in itself.

## Endpoints

```
GET /           basic liveness message
GET /hello      sample endpoint
GET /time       current server time
GET /health     health check (app name + env from environment variables)
```

## Tech Stack

Python, FastAPI, Docker, GitHub Actions.

## Run it

```bash
docker build -t devops-backend .
docker run -p 8000:8000 devops-backend
curl http://localhost:8000/health
```

## CI

`.github/workflows/ci.yml` builds the Docker image on every push to `main` — a smoke test that the container still builds, not a full pipeline.
