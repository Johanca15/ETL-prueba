from sqlalchemy import create_engine, text

# conexion
engine = create_engine("postgresql://avnadmin:AVNS_p0zuxjh8CTzz02T6Iif@pg-156ebb68-johancasantos15-a74f.d.aivencloud.com:12464/defaultdb?sslmode=require")


#vistas
create_views_sql = """
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
    conn.execute(text(create_views_sql))
    conn.commit()

print("Vistas creadas")
