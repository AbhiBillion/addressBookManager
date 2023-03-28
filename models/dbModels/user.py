from pydantic import BaseModel,Field
from typing import Any, Optional

class OutModel(BaseModel):
    status: str
    status_code: int
    comment: Optional[str]
    data: Any

class address(BaseModel):
    houseName: str = Field(example="Dream home")
    streetName: str = Field(example="Street 32/B")
    streetName2: str = Field(example="MG Road")
    city: str = Field(example="Menaka")
    district: str = Field(example="Ernakulam")
    state: str = Field(example="Kerala")
    zipcode: str = Field(example="62001")
    longitude: str = Field(example="40.748817")
    latitute: str = Field(example="-73.985428")

class getAddressByDistance(BaseModel):
    rangeKm : str = Field(example="10")
    longitude: str = Field(example="40.748817")
    latitute: str = Field(example="-73.985428")

class updateAdr(BaseModel):
    id : str = Field(example="1")
    fieldName : str = Field(example="houseName")
    value : str = Field(example="Dream home")