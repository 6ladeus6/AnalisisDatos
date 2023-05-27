from data.apartamentos import apartamento1,apartamento2
from helpers.crearTablasHtml import crearTabla
import pandas as pd

#Crear Dataframe
tabla1 = pd.DataFrame(apartamento1,columns=['edades'])
tabla2 = pd.DataFrame(apartamento2,columns=['edades'])
tabla3 = pd.read_csv("./data/empleados.csv")

#Efectuando filtros con python

#1.Condicion logica
empladosJovenesAnalista1 = tabla3.query('edad < 28 and cargo == "analista1"')
empleadosSalarioBajo = tabla3.query('salario < 5000000 and cargo == "analista2"')
empleadosADespedir = tabla3.query('edad <= 50')

#2. Creamos la tabla HTML con el html del frito
crearTabla(empladosJovenesAnalista1,"tablaJovenes")
crearTabla(empleadosSalarioBajo,"tablabajossalarios")
crearTabla(empleadosADespedir,"tablaoprtunidaddemejora")


