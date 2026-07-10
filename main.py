from fastapi import FastAPI, status, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI(title="API của Dương", description="Những API của Dương")


books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thu",
        "category": "programming",
        "year": 2022,
        "is_available": True,
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "web",
        "year": 2021,
        "is_available": True,
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available": False,
    },
]


class BaseReponse:
    statusCode: str
    message: str
    data: Any | None
    error: str | None
    timestamps: str
    path: str


def create_reponse(statusCode: int, message: str, data: None,timestamps = "", error=None, path=""):
    return JSONResponse(
        status_code=statusCode,
        content={
            "message": message,
            "data": data,
            "errors": error,
            "timestamps": timestamps,
            "path": path,
        },
    )


@app.get("/books")
def get_book(request: Request):
    return create_reponse(
        message="Lấy dữ liệu thành công",
        statusCode= status.HTTP_200_OK,
        data = books,
        error="",
        timestamps=datetime.now().isoformat(),
        path= request.url.path
    )
