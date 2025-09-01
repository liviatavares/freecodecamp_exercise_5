import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    # criando os parâmetros da regressão linear e passando os parâmetros x (variável independente) e y (variável dependente)
    # slope = coeficiente angular (o quanto Y muda para cada unidade de X)
    # intercept = coeficiente linear (valor de y quando x é zero)
    # r_value = coeficiente de correlação de pearson. mede o quanto duas variáveis são relacionadas entre si.
    # p_value = o p-valor para um teste de hipótese em que a hipótese nula é que o coeficiente angular é zero.
    # std_err = erro padrão do coeficiente angular estimado.
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = pd.Series(range(1880, 2051))
    best_fit = slope*years + intercept

    # Create second line of best fit
    # filtrando o df para mostrar anos acima de 2000
    df_new = df[df['Year'] >= 2000]
    years_new = pd.Series(range(2000, 2051))
    slope_new, intercept_new, r_value_new, p_value_new, std_err_new = linregress(df_new['Year'], df_new['CSIRO Adjusted Sea Level'])
    best_fit_new = slope_new*years_new + intercept_new

    # Add labels and title
    # plotando as retas e adicionando título e labels
    plt.plot(years, best_fit)
    plt.plot(years_new, best_fit_new)
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()