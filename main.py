from ui.ui import obtener_parametros, mostrar_resultados
from api.api import consultar_datos

def main():
    departamento, municipio, cultivo, limit = obtener_parametros()
    tabla = consultar_datos(departamento, municipio, cultivo, limit)
    if tabla is not None:
        mostrar_resultados(tabla)
    else:
        print("Error al consultar los datos.")

main()
