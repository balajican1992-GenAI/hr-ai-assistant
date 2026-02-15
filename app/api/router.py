from fastapi import APIRouter
from app.api.endpoints import chat_endpoint, health_check

router = APIRouter()

router.add_api_route(
    "/chat",
    chat_endpoint,
    methods=["POST"],
    tags=["Chat"]
)

router.add_api_route(
    "/health",
    health_check,
    methods=["GET"],
    tags=["Health"]
)