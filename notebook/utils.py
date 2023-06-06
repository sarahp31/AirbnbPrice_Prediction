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

def lista_coefcients(diciconario, value_dic):
    return diciconario[value_dic]


def plot_coefPermutationTest(diferencas_amostradas, T_obs, nomeFeature):
    plt.hist(diferencas_amostradas, bins=30, density=True, edgecolor='black')
    plt.axvline(T_obs, color='red', linestyle='--', label='T_obs')
    plt.xlabel('Sample Differences')
    plt.ylabel('Frequency')
    plt.legend()
    plt.title(f'{nomeFeature}: Distribution of coefficients')
    plt.show()


def permutaionTeste_EntireHouse(listaFetures, coefCity1, coefCity2):

    for feture in listaFetures:
        coefcients1 = lista_coefcients(coefCity1, feture)
        coefcients2 = lista_coefcients(coefCity2, feture)

        T_obs = np.mean(coefcients1) - np.mean(coefcients2)

        num_permutation = 1000
        #num_samples = 500

        differences_samples = []

        # for _ in range(num_permutation):
        #     sample1 = np.random.choice(coefcients1, size=num_samples, replace=True)
        #     sample2 = np.random.choice(coefcients2, size=num_samples, replace=True)

        #     difference = np.mean(sample1) - np.mean(sample2)
        #     differences_samples.append(difference)
        all_coefcients = np.concatenate((coefcients1, coefcients2))

        for _ in range(num_permutation):
            np.random.shuffle(all_coefcients)

            sample1 = all_coefcients[:len(coefcients1)]
            sample2 = all_coefcients[len(coefcients1):]

            difference = np.mean(sample1) - np.mean(sample2)
            differences_samples.append(difference)

        plot_coefPermutationTest(differences_samples, T_obs, feture)

        num_permutation_GIT = sum(d >= T_obs for d in differences_samples)
