from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import (
    DatasetAlreadyExistsException,
    DatasetNotFoundException,
)


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(DatasetNotFoundException)
    async def dataset_not_found_handler(
        request: Request,
        exc: DatasetNotFoundException,
    ):
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "error": {
                    "code": 404,
                    "message": exc.message,
                },
                "timestamp": datetime.utcnow().isoformat(),
            },
        )

    @app.exception_handler(DatasetAlreadyExistsException)
    async def dataset_exists_handler(
        request: Request,
        exc: DatasetAlreadyExistsException,
    ):
        return JSONResponse(
            status_code=409,
            content={
                "success": False,
                "error": {
                    "code": 409,
                    "message": exc.message,
                },
                "timestamp": datetime.utcnow().isoformat(),
            },
        )