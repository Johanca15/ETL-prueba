import pandas as pd
from sqlalchemy import create_engine, text

# conexion aiven
engine = create_engine("postgresql://avnadmin:AVNS_p0zuxjh8CTzz02T6Iif@pg-156ebb68-johancasantos15-a74f.d.aivencloud.com:12464/defaultdb?sslmode=require")

# tabla rnc
create_table_sql = """
CREATE TABLE IF NOT EXISTS rnc (
    rnc VARCHAR(11) PRIMARY KEY,
    razon_social TEXT,
    actividad_economica TEXT,
    fecha_inicio_operaciones DATE,
    estado VARCHAR(20),
    regimen_pago VARCHAR(50));
"""

with engine.connect() as conn:
    conn.execute(text(create_table_sql))
    conn.commit()

print("Tabla creada")

# extraccion dataset
df = pd.read_csv("dataset/rnc.csv", encoding="latin-1")

# 3. Normalizacion y limpieza
df.columns = [
    "rnc",
    "razon_social",
    "actividad_economica",
    "fecha_inicio_operaciones",
    "estado",
    "regimen_pago"]

df["rnc"] = df["rnc"].astype(str)
df["fecha_inicio_operaciones"] = pd.to_datetime(
    df["fecha_inicio_operaciones"],
    dayfirst=True,
    errors="coerce")

df = df.dropna(subset=["rnc", "regimen_pago"])
df = df.drop_duplicates(subset=["rnc"])


# Carga
df.to_sql(
    "rnc",
    engine,
    if_exists="append",
    index=False)

print("Dataset cargado")
