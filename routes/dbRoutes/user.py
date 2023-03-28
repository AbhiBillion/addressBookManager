from fastapi import APIRouter
from models.dbModels import user as u
from helpers import dbTasks as db
from geopy.distance import distance
import os
from datetime import datetime

if not os.path.exists('log'):
    os.makedirs('log')

routes = APIRouter()

#to log error
async def logError(text):
    with open(f"errorLog/{str(datetime)}", "w") as f:
        f.write(text)

'''
SAVE ADDRESS
input parameter validaton with models
'''
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
        await logError(str(e))
        return out

'''
GET ADDRESS
enter the preferred range in Km
then give the source cordinates
based on the source coordinates and rnge, it will show the matching records
'''
@routes.get("/getAddressInfo", response_model= u.OutModel)
async def getAddress(getInfoAdr: u.getAddressByDistance):
    try:
        range = getInfoAdr.rangeKm
        cord1 = (getInfoAdr.longitude,getInfoAdr.latitute)
        addressList = await db.getAllAddressSQL
        addRangeList =[]
        for a in addressList:
            cord2 = (a['long'],a['lat'])
            r = distance(cord1,cord2).km
            if r < range:
                addRangeList(a)
        out = u.OutModel(status="success",
                        status_code=200,
                        comment="Data fetch successfully",
                        data=addRangeList)
        await logError(str(e))
        return out
    except Exception as e:
        out = u.OutModel(status="failure",
                        status_code=400,
                        comment="Data fetch failed",
                        data='')
        return out
    
'''
UPDATE ADDRESS
give the id, field name and the value
'''
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
        await logError(str(e))
        return out

'''
DELETE ADDRESS
enter the id to delete the record from DB'''
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
        await logError(str(e))
        return out











