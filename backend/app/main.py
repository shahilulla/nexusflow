from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.datasets import router as datasets_router
from app.api.executions import router as executions_router
from app.api.health import router as health_router
from app.api.monitoring import router as monitoring_router
from app.api.pipelines import router as pipelines_router
from app.core.config import settings
from app.core.logger import get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("=" * 60)
    logger.info("Starting NexusFlow Backend...")
    logger.info(f"Application : {settings.APP_NAME}")
    logger.info(f"Version     : {settings.APP_VERSION}")
    logger.info(f"API Prefix  : {settings.API_PREFIX}")
    logger.info("Backend started successfully.")
    logger.info("=" * 60)

    yield

    logger.info("=" * 60)
    logger.info("Shutting down NexusFlow Backend...")
    logger.info("=" * 60)


app = FastAPI(
    title=settings.APP_NAME,
    description="Production-Grade Data Platform",
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

# Register API Routers
app.include_router(health_router)
app.include_router(datasets_router, prefix=settings.API_PREFIX)
app.include_router(pipelines_router, prefix=settings.API_PREFIX)
app.include_router(executions_router, prefix=settings.API_PREFIX)
app.include_router(monitoring_router, prefix=settings.API_PREFIX)


@app.get("/", tags=["Root"])
async def root():
    logger.info("Root endpoint accessed.")

    return {
        "project": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "message": "Welcome to NexusFlow!",
        "docs": "/docs",
        "openapi": "/openapi.json",
        "health": "/health",
    }