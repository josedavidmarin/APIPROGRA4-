from sodapy import Socrata
import pandas as pd

def consultar_datos(departamento, municipio, cultivo, limit):
    # Cliente para interactuar con la API del Portal Nacional de Datos Abiertos
    client = Socrata("www.datos.gov.co", None)

    # Obtener los resultados de la API
    results = client.get("ch4u-f3i5", limit=limit)

    # Convertir los resultados a un DataFrame de Pandas
    results_df = pd.DataFrame.from_records(results)

    # Filtrar los resultados según el departamento, municipio y cultivo
    resultados_filtrados = results_df[(results_df['departamento'] == departamento) & 
                                      (results_df['municipio'] == municipio) & 
                                      (results_df['cultivo'] == cultivo)]

    # Extraer la tabla con las columnas requeridas
    tabla = resultados_filtrados[['departamento', 'municipio', 'cultivo', 'topografia']]
    

    # Calcular la mediana de las variables edáficas
    mediana = (resultados_filtrados['ph_agua_suelo_2_5_1_0'].apply(lambda x: float(x)) + resultados_filtrados['f_sforo_p_bray_ii_mg_kg'].apply(lambda x: float(x)) + resultados_filtrados['potasio_k_intercambiable_cmol_kg'].apply(lambda x: float(x)))/3
    tabla['media'] = mediana

    

    return tabla
