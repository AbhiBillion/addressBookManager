from fastapi import APIRouter
from models.dbModels import user as u
from helpers import dbTasks as db
import geopy.distance

routes = APIRouter()

@routes.post("/saveAddress", response_model=u.OutModel)
async def saveAddress(saveAdr: u.address):
    try:
        await db.saveAddressSQL(saveAdr.houseName,saveAdr.streetName,saveAdr.streetName2,
                                saveAdr.city,saveAdr.state,saveAdr.zipcode,saveAdr.longitude
                                ,saveAdr.latitute)
        
        out = u.OutModel(status="success",
                        status_code=200,
                        comment="Data saved successfully",
                        data= True)
        return out
    except Exception as e:
        out = u.OutModel(status="failed",
                       status_code=400,
                       comment="Data insert failed",
                       data=e)
        return out

@routes.get("/getAddressInfo", response_model= u.OutModel)
async def getAddress(getInfoAdr: u.getAddressByDistance):
    try:
        range = getInfoAdr.rangeKm
        cord1 = (getInfoAdr.longitude,getInfoAdr.latitute)
        addressList = await db.getAllAddressSQL
        addRangeList =[]
        for a in addressList:
            cord2 = (a['long'],a['lat'])
            r = geopy.distance.geodesic(cord1,cord2).km
            if r < range:
                addRangeList(a)
        out = u.OutModel(status="success",
                        status_code=200,
                        comment="Data fetch successfully",
                        data=addRangeList)
        return out
    except Exception as e:
        out = u.OutModel(status="failure",
                        status_code=400,
                        comment="Data fetch failed",
                        data='')
        return out
    
@routes.put("/updateAddress", response_model= u.OutModel)
async def recreate_stocklist(updateAdr : u.updateAdr):
    try:
        await db.updateAddressSQL(updateAdr.id,updateAdr.fieldName,updateAdr.value)
        out = u.OutModel(status="success",
                        status_code=200,
                        comment="Data update successfully",
                        data=True)
        return out
    except Exception as e:
        out = u.OutModel(status="failure",
                        status_code=400,
                        comment="Data update failed",
                        data='')
        return out

@routes.delete("/removeAddress", response_model= u.OutModel)
async def deleteAddress(id : str):
    try:
        await db.removeAddress(id)
        out = u.OutModel(status="success",
                        status_code=200,
                        comment="Data deleted successfully",
                        data=True)
        return out
    except Exception as e:
        out = u.OutModel(status="failure",
                        status_code=400,
                        comment="Data delete failed",
                        data='')
        return out











