import sqlite3
import csv

conn = sqlite3.connect("temperatura.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS clima(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   fecha TEXT NOT NULL,
                   dia TEXT NOT NULL,
                   hora TEXT NOT NULL,
                   celsius INTEGER NOT NULL,
                   fahrenheit INTEGER NOT NULL,
                   condicion TEXT NOT NULL
                   )
                   """)
    


#Abrimos el archivo CSV
f=open('clima.csv','r') 
#Omitimos la linea de encabezado
next(f, None)
reader = csv.reader(f, delimiter=',')


#Llenamos la BD con los datos del CSV
for row in reader:
    cursor.execute("INSERT INTO clima(id,fecha,dia, hora,celsius,fahrenheit,condicion) VALUES (null,?,?, ?, ?, ?,?)", (row[0], row[1], row[2], row[3], row[4],row[5]))


#Cerramos el archivo y la conexion a la bd
conn.commit()
conn.close()
