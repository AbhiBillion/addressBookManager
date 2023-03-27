import sqlite3


conn = sqlite3.connect('address.db')
cursor = conn.cursor()

async def saveAddressSQL(house,st,st2,city,distr,state,zip,long,lat):
    cursor.execute("INSERT INTO address (houseName, streeName,streetName2, city,district, state, zipcode, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (house, st, st2,city,distr, state, zip, long, lat))
    conn.commit()
    return True

async def getAllAddressSQL():
    cursor.execute('SELECT * FROM addresses')
    return cursor.fetchall()

async def updateAddressSQL(id,field,value):
    cursor.execute("UPDATE addresses SET"+ field + "=" + str(value)+ " WHERE id= " + id)
    conn.commit()
    return True

async def removeAddress(id):
    cursor.execute('DELETE FROM addresses WHERE id=' + (id,))
    conn.commit()
    return True
