from sqlalchemy import create_engine, text
import pandas as pd
from sqlalchemy import create_engine, text

# conexion
engine = create_engine("postgresql://avnadmin:AVNS_p0zuxjh8CTzz02T6Iif@pg-156ebb68-johancasantos15-a74f.d.aivencloud.com:12464/defaultdb?sslmode=require")

#Creacion de tabla
create_table_query = """
CREATE TABLE IF NOT EXISTS cobros_edesur (id SERIAL PRIMARY KEY,
    zona VARCHAR(100),
    cobros_rd_mm NUMERIC(14,4),
    mes VARCHAR(20),
    anio INTEGER);
"""

with engine.connect() as conn:
    conn.execute(text(create_table_query))
    conn.commit()

print("Tabla creada")


#extraccion dataset
df = pd.read_csv("dataset/edesur_cobros.csv", encoding="latin-1")

# normalizacion y limpieza dataset
df.columns = ["zona", "cobros_rd_mm", "mes", "anio"]
df["zona"] = df["zona"].str.strip()
df["mes"] = df["mes"].str.strip().str.capitalize()
df["anio"] = df["anio"].astype(int)
df["cobros_rd_mm"] = pd.to_numeric(df["cobros_rd_mm"], errors="coerce")

df = df.dropna()
df = df[df["cobros_rd_mm"] >= 0]


# Carga
df.to_sql(
    "cobros_edesur",
    engine,
    if_exists="append",
    index=False)

print("Dataset cargado")
