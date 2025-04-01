# Data wrangling
import math
import numpy as np
import pandas as pd
# Visualización de datos
import seaborn as sns
import matplotlib.pyplot as plt

def plot_histograms(df, variables, filename, n_cols=5):
    '''Función para graficar histogramas en verde'''
    sns.set(style="whitegrid")
    n_rows = math.ceil(len(variables) / n_cols)
    fig, axs = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(20, 4 * n_rows))
    axs = axs.flatten()

    for i, var in enumerate(variables):
        sns.histplot(data=df, x=var, kde=True, color="green", ax=axs[i])
        axs[i].set_title(f'Histograma de {var}')
    
    for ax in axs[i + 1:]:
        ax.set_visible(False)
    
    plt.tight_layout()
    plt.show()


def freq_discrete(df, features):
    '''Función para graficar las tablas de frecuencias de las variables categóricas'''
    for feature in features:
        print(f"Variable: {feature}")
        abs_ = df[feature].value_counts(dropna=False).to_frame().rename(columns={"count": "Frecuencia absoluta"})
        rel_ = df[feature].value_counts(dropna=False, normalize= True).to_frame().rename(columns={"proportion": "Frecuencia relativa"})
        freq = abs_.join(rel_)
        freq["Frecuencia acumulada"] = freq["Frecuencia absoluta"].cumsum()
        freq["Frecuencia relativa acumulada"] = freq["Frecuencia relativa"].cumsum()
        freq["Frecuencia absoluta"] = freq["Frecuencia absoluta"].map(lambda x: "{:,.0f}".format(x))
        freq["Frecuencia relativa"] = freq["Frecuencia relativa"].map(lambda x: "{:,.2%}".format(x))
        freq["Frecuencia acumulada"] = freq["Frecuencia acumulada"].map(lambda x: "{:,.0f}".format(x))
        freq["Frecuencia relativa acumulada"] = freq["Frecuencia relativa acumulada"].map(lambda x: "{:,.2%}".format(x))
        display(freq)