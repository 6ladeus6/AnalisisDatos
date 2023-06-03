import matplotlib.pyplot as plt

def graficarPromedioSalarial(dataFrame, cargoX, salarioY, nombreGrafica):
    colores = ['green','red','blue']
    salarioPromedio = dataFrame.groupby(cargoX)[salarioY].mean()
    #generando la grafica
    plt.bar(salarioPromedio.index,salarioPromedio,color = colores)
    plt.title("PROMEDIO SALARIAL")
    plt.xlabel("Cargos")
    plt.ylabel("Salario Mensual")
    plt.savefig(f'./assets/img/{nombreGrafica}.png')

