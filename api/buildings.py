import logging

from fastapi import APIRouter, HTTPException

from services.parser_service import ParserService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/buildings", tags=["Buildings"])

service = ParserService()


@router.get("/")
def get_data():
    try:
        return service.get_data()
    except Exception as e:
        logger.exception("Failed to get data")
        raise HTTPException(
            status_code=500,
            detail="Failed to get data"
        ) from e


@router.post("/parse")
def parse():
    try:
        return service.parse_data()
    except Exception as e:
        logger.exception("Failed to parse data")
        raise HTTPException(
            status_code=500,
            detail="Failed to parse data"
        ) from e