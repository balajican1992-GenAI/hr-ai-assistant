from fastapi import APIRouter
from app.api.endpoints import chat_endpoint, health_check,load_hr_policy,load_and_split_hr_policy

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



router.add_api_route(
    "/load-hr-policy",
    load_hr_policy,
    methods=["GET"],
    tags=["Document Loader"]
)

router.add_api_route(
    "/load-and-split",
    load_and_split_hr_policy,
    methods=["GET"],
    tags=["RAG - Document Processing"]
)