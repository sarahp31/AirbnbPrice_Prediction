import matplotlib.pyplot as plt
import numpy as np


def plot_categoricals(data, cols, sorted=True):
    summary = data[cols] \
        .describe() \
        .transpose() \
        .sort_values(by='count')

    print(summary)

    for k, (col, val) in enumerate(summary['count'].items()):
        plt.figure()
        ser = data[col].value_counts()
        if sorted:
            ser = ser.sort_values()
        else:
            ser = ser.sort_index()
        ax = ser.plot.barh(color='pink')
        for container in ax.containers:
            ax.bar_label(container)
        plt.title(f'{col}, n={int(val)}')
        plt.show()



def plot_discretes(data, cols, sorted=True):
    summary = data[cols] \
        .describe() \
        .transpose() \
        .sort_values(by='count')

    print(summary)

    for k, (col, val) in enumerate(summary['count'].items()):
        plt.figure()
        ser = data[col].value_counts()
        if sorted:
            ser = ser.sort_values()
        else:
            ser = ser.sort_index()
        ax = ser.plot.barh(color='pink')
        for container in ax.containers:
            ax.bar_label(container)
        plt.title(f'{col}, n={int(val)}')
        plt.show()


def plot_continuous(data, cols, n_bins=20):
    for col in cols:
        plt.figure()
        data[col].hist(bins=n_bins, color='pink')
        plt.title(f'{col}, {n_bins} bins')
        plt.show()

def plot_coefModeloLasso(coeficientes_dict):
    # Itere sobre as chaves (features) do dicionário
    for feature in coeficientes_dict:
        # Obtenha a lista de coeficientes correspondente à feature
        coeficientes = coeficientes_dict[feature]
        
        # Calcule os percentis 2,5% e 97,5%
        percentil_2_5 = np.percentile(coeficientes, 2.5)
        percentil_97_5 = np.percentile(coeficientes, 97.5)
        
        # Crie um gráfico de boxplot para a feature
        plt.boxplot(coeficientes)
        plt.title(f'{feature}')
        plt.ylabel('Coeficiente')
        plt.xlabel('Feature')
        
        # Desenhe linhas horizontais para indicar os percentis
        plt.axhline(percentil_2_5, color='r', linestyle='--', label='2.5%')
        plt.axhline(percentil_97_5, color='g', linestyle='--', label='97.5%')
        
        # Exiba a legenda
        plt.legend()
        
        # Exiba o gráfico
        plt.show()