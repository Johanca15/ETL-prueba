from sqlalchemy import create_engine

engine = create_engine("postgresql://avnadmin:AVNS_p0zuxjh8CTzz02T6Iif@pg-156ebb68-johancasantos15-a74f.d.aivencloud.com:12464/defaultdb?sslmode=require")

try:
    conn = engine.connect()
    print("Conectado")
    conn.close()
except Exception as e:
    print("Error")
    print(e)
