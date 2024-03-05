#!/ usr/bin/env python
# make sure to install these packages before running :
# pip install pandas
# pip install sodapy
import pandas as pd
from sodapy import Socrata
 # Unauthenticated client only works with public data sets . Note ’None ’
 # in place of application token , and no username or password :
# client = Socrata ("www.datos.gov.co", None )

 # Example authenticated client ( needed for non - public datasets ):
 # client = Socrata (www. datos .gov.co ,
 # MyAppToken ,
 # username =" user@example . com" ,
 # password =" AFakePassword ")

 # First 2000 results , returned as JSON from API / converted to Python
# list of
# dictionaries by sodapy .
# results = client.get("https://www.datos.gov.co/resource/ch4u-f3i5.json", limit =1000)
# Convert to pandas DataFrame
#  i need make a get of this https://www.datos.gov.co/resource/ch4u-f3i5.json

soda = Socrata("www.datos.gov.co", None)
results = soda.get("ch4u-f3i5", limit=46745)

#print(results)


def obtenerTabla(dep, mun, cult):
    for r in results:
        if(r["departamento"] == dep and r["municipio"] == mun and r["cultivo"] == cult):
            # prom = (float(r["ph_agua_suelo_2_5_1_0"]) + float(r["f_sforo_p_bray_ii_mg_kg"]) + float(r["potasio_k_intercambiable_cmol_kg"])) / 3
            print([r["departamento"], r["municipio"], r["cultivo"], r["topografia"]])
            


obtenerTabla("ANTIOQUIA", "ABEJORRAL", "Aguacate")