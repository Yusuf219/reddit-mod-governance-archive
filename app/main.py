from fastapi import FastAPI, Query, Response, FileResponse
import os
from contextlib import asynccontextmanager
from storage.init_db import init_db
from reports.metrics import get_metrics, get_summary
from reports.exports import latest_export_path, export_now, latest_export_path
from collector.modlog_sync_fixture import ingest_fixture_events

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown (nothing yet)

app = FastAPI(
    title="Reddit Moderator Governance Archive",
    lifespan=lifespan
)

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)

@app.get("/")
def health_check():
    return {"status": "RMGA running"}

@app.get("/metrics")
def metrics(days: int = Query(30, ge=1, le=365)):
    return get_metrics(days=days)

@app.get("/summary")
def summary(days: int = Query(30, ge=1, le=365)):
    return get_summary(days=days)

@app.get("/exports/latest")
def exports_latest():
    path = latest_export_path()
    return {"latest": path}

@app.post("/exports/run")
def exports_run():
    return export_now()

@app.get("/exports/download/latest", include_in_schema=True)
def download_latest_export():
    path = latest_export_path()
    if not path or not os.path.exists(path):
        return {"error": "No export found. Run POST /exports/run first."}

    filename = os.path.basename(path)
    return FileResponse(path, media_type="text/csv", filename=filename)

@app.post("/fixtures/ingest")
def ingest_fixtures():
    return ingest_fixture_events()