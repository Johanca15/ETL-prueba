from sqlalchemy import create_engine, text

# conexion
engine = create_engine("postgresql://avnadmin:AVNS_p0zuxjh8CTzz02T6Iif@pg-156ebb68-johancasantos15-a74f.d.aivencloud.com:12464/defaultdb?sslmode=require")


#vista
create_views_sql = """
CREATE OR REPLACE VIEW vw_rnc_por_regimen_pago AS
SELECT
    regimen_pago,
    COUNT(*) AS cantidad_contribuyentes
FROM rnc
GROUP BY regimen_pago;
"""

with engine.connect() as conn:
    conn.execute(text(create_views_sql))
    conn.commit()

print("Vista creada")