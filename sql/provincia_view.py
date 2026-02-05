from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine(
    "postgresql://avnadmin:AVNS_p0zuxjh8CTzz02T6Iif@pg-156ebb68-johancasantos15-a74f.d.aivencloud.com:12464/defaultdb?sslmode=require")

# Crear vistas
query1 = """
CREATE OR REPLACE VIEW vw_cobros_por_zona AS
SELECT
    zona,
    SUM(cobros_rd_mm) AS total_cobros_rd_mm
FROM cobros_edesur
GROUP BY zona;

CREATE OR REPLACE VIEW vw_cobros_por_zona_anio AS
SELECT
    zona,
    anio,
    SUM(cobros_rd_mm) AS total_cobros_rd_mm
FROM cobros_edesur
GROUP BY zona, anio;
"""

with engine.connect() as conn:
    conn.execute(text(query1))
    conn.commit()

print("Vista creada")


#salida
select_sql = """
SELECT *FROM vw_cobros_por_zona ORDER BY zona;
"""

with engine.connect() as conn:
    result = conn.execute(text(select_sql))

    for row in result.mappings():
        print(dict(row))
