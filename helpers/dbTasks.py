import sqlite3


conn = sqlite3.connect('address.db')
cursor = conn.cursor()
#to save to DB
async def saveAddressSQL(house,st,st2,city,distr,state,zip,long,lat):
    cursor.execute("INSERT INTO address (houseName, streeName,streetName2, city,district, state, zipcode, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (house, st, st2,city,distr, state, zip, long, lat))
    conn.commit()
    return True

#to get from DB- fetch all values
async def getAllAddressSQL():
    cursor.execute('SELECT * FROM addresses')
    return cursor.fetchall()

#to update to DB
async def updateAddressSQL(id,field,value):
    cursor.execute("UPDATE addresses SET"+ field + "=" + str(value)+ " WHERE id= " + id)
    conn.commit()
    return True

#to delete address record by id
async def removeAddress(id):
    cursor.execute('DELETE FROM addresses WHERE id=' + (id,))
    conn.commit()
    return True
