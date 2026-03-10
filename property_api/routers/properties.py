"""Property endpoints."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/properties", tags=["properties"])

class PropertyScore(BaseModel):
    id: str
    score: float
    estimated_value: float
    cap_rate: float

@router.get("/{property_id}/score")
async def score_property(property_id: str) -> PropertyScore:
    """Score a single property."""
    # TODO: Implement
    return PropertyScore(
        id=property_id,
        score=82.4,
        estimated_value=485000,
        cap_rate=4.2
    )

@router.post("/batch-score")
async def batch_score(property_ids: list[str]):
    """Score multiple properties in batch."""
    # TODO: Implement
    return [
        {
            "id": pid,
            "score": 82.4,
            "estimated_value": 485000,
            "cap_rate": 4.2
        }
        for pid in property_ids
    ]
