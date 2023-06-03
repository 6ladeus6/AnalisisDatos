import pandas as pd
import matplotlib.pyplot as plt

def calcularPromedioSalariosPorEdad(dataframe,rangos,columnaInteres,columnaPromediar,nombreGrafica):
    plt.figure()

    #crear columna nueva por rango de edad
    dataframe['rangosEdad'] = pd.cut(dataframe[columnaInteres],bins=rangos)

    #calcular la suma de los salarios por rango de edad
    salarioPorRango = dataframe.groupby('rangosEdad')['salario'].sum()
    #Definimos los rangos
    salario = salarioPorRango.values
    rangosEdad = salarioPorRango.index
    plt.pie(salario, labels = rangosEdad, autopct = '%1.1f%%')
    plt.title("SALARIO POR RANGOS DE EDAD")
    plt.savefig(f'./assets/img/{nombreGrafica}.png')
