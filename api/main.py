# %%
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel 

# %% 
class Item(BaseModel):
    fecha: str
    dia: str
    hora:str
    celsius: int
    fahrenheit: int
    condicion: str

app = FastAPI()

# %%
@app.post("/agregar_elemento/") 
async def agregar_elemento(item: Item):
    conn = sqlite3.connect("temperatura.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clima (fecha,dia,hora,celsius,fahrenheit,condicion) VALUES (null,?, ?, ?,?,?,?)", (item.fecha,item.dia, item.hora, item.celsius,item.fahrenheit,item.condicion))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos agregados exitosamente"}

# %%
@app.get("/leer_elementos/")
async def leer_elementos():
    conn = sqlite3.connect("temperatura.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clima")
    resultados = cursor.fetchall()
    conn.close()
    if resultados:
        return [{"id": resultado[0], "fecha": resultado[1], "dia": resultado[2], "hora": resultado[3], "celsius": resultado[4], "fahrenheit": resultado[5], "condicion": resultado[6]} for resultado in resultados]
    else:
        return {"mensaje": "No hay datos en la base de datos"}

# %%
@app.get("/leer_elemento/{id}/")
async def leer_elemento(id: int):
    conn = sqlite3.connect("temperatura.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clima WHERE id=?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado is not None:
        return {"id": resultado[0], "fecha": resultado[1], "dia": resultado[2], "hora": resultado[3], "celsius": resultado[4], "fahrenheit": resultado[5], "condicion": resultado[6]}
    else:
        return {"mensaje": "Datos no encontrados"}

# %%
@app.put("/actualizar_elemento/{id}/")
async def actualizar_elemento(id: int, item: Item):
    conn = sqlite3.connect("temperatura.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE clima SET fecha=?,dia=?,hora=?,celsius=?,fahrenheit=?,condicion=? WHERE id=?", (item.fecha, item.dia, item.hora, item.celsius, item.fahrenheit, item.condicion, id))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos actualizados exitosamente"}

# %%
@app.delete("/eliminar_elemento/{id}/")
async def eliminar_elemento(id: int):
    conn = sqlite3.connect("temperatura.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM climaS WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos eliminados exitosamente"}

# %%