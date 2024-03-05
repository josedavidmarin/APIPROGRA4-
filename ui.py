def obtener_parametros():
    dep = input("Ingrese el nombre del departamento: ")
    mun = input("Ingrese el nombre del municipio: ")
    cult = input("Ingrese el nombre del cultivo: ")
    limit = int(input("Ingrese el número de registros a consultar: "))
    return dep, mun, cult, limit

def mostrar_resultados(tabla, mediana_variables_edaficas):
    print("Tabla de resultados:")
    print(tabla)
    print("\nMediana de las variables edáficas:")
    for variable, mediana in mediana_variables_edaficas.items():
        print(f"{variable}: {mediana}")
