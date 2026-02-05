from sqlalchemy import create_engine, text

# conexion
engine = create_engine("postgresql://avnadmin:AVNS_p0zuxjh8CTzz02T6Iif@pg-156ebb68-johancasantos15-a74f.d.aivencloud.com:12464/defaultdb?sslmode=require")


#vista
query2 = """
CREATE OR REPLACE VIEW vw_rnc_por_regimen_pago AS
SELECT
    regimen_pago,
    COUNT(*) AS cantidad_contribuyentes
FROM rnc
GROUP BY regimen_pago;
"""

with engine.connect() as conn:
    conn.execute(text(query2))
    conn.commit()

print("Vista creada")

#salida
select_sql = """
SELECT regimen_pago, cantidad_contribuyentes FROM vw_rnc_por_regimen_pago ORDER BY regimen_pago;
"""


with engine.connect() as conn:
    result = conn.execute(text(select_sql))

    for row in result.mappings():
        print(dict(row))
