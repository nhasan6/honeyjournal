from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
class HoneyCreate(BaseModel):
    name: str
    origin_country: str
    origin_city: str
    rating: int = Field(ge=0, le=10)
    notes: Optional[str] = None
    image_url: Optional[str] = None
    shop_name: Optional[str] = None
    latitude: float
    longitude: float
    color: str

class HoneyResponse(HoneyCreate):
    id: int
    created_at: datetime

class HoneyUpdate(BaseModel):
    name: Optional[str] = None
    origin_country: Optional[str] = None
    origin_city: Optional[str] = None
    rating: Optional[int] = None
    notes: Optional[str] = None
    image_url: Optional[str] = None
    shop_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    color: Optional[str] = None