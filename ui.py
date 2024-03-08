def obtener_parametros():
    departamento = input("Ingrese el nombre del departamento: ")
    municipio = input("Ingrese el nombre del municipio: ")
    cultivo = input("Ingrese el nombre del cultivo: ")
    limit = int(input("Ingrese el número de registros a consultar: "))
    return departamento, municipio, cultivo, limit

def mostrar_resultados(tabla):
    print("Tabla de resultados:")
    print(tabla)
