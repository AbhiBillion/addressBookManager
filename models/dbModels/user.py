from pydantic import BaseModel,Field
from typing import Any, Optional

class OutModel(BaseModel):
    status: str
    status_code: int
    comment: Optional[str]
    data: Any

class address(BaseModel):
    houseName: str
    streetName: str
    streetName2: str
    city: str
    district: str
    state: str
    zipcode: str
    longitude: str
    latitute: str

class getAddressByDistance(BaseModel):
    rangeKm : str
    longitude: str
    latitute: str

class updateAdr(BaseModel):
    id : str
    fieldName : str
    value : str