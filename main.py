import ui
import api

def main():
    departamento, municipio, cultivo, limit = ui.obtener_parametros()
    tabla, mediana_variables_edaficas = api.consultar_datos(departamento, municipio, cultivo, limit)
    if tabla is not None:
        ui.mostrar_resultados(tabla, mediana_variables_edaficas)
    else:
        print("Error al consultar los datos.")

main()