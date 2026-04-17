from fastapi import FastAPI
from fastapi.responses import Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import os
import psycopg2

app = FastAPI()

# =========================
# 📊 METRICS (Prometheus)
# =========================
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests to the application"
)

# =========================
# 🗄️ DATABASE CONFIG
# =========================
DB_HOST = os.getenv("DB_HOST", "postgres-service")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_PORT = os.getenv("DB_PORT", "5432")


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )


# =========================
# 🚀 ENDPOINTS
# =========================

@app.get("/")
def root():
    REQUEST_COUNT.inc()
    return {"message": "API rodando com Kubernetes 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/db-check")
def db_check():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        cursor.close()
        conn.close()

        return {"database": "connected"}
    except Exception as e:
        return {"database": "error", "details": str(e)}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)