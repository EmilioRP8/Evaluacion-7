import pandas as pd
import os
import matplotlib.pyplot as plt
import json as js
import numpy as np

def cargar_dataset(archivo):
    import pandas as pd
    import os
    extension = os.path.splitext(archivo)[1].lower()
# Cargar el archivo según su extensión
    if extension == '.csv':
        df= pd.read_csv(archivo)
        return (df)
    elif extension == '.xlsx':
        df= pd.read_excel(archivo)
        return (df)
    else:
            raise ValueError(f"“Este formato no esta soportado para esta función: .formato”")
    
def sustituir_nulos(df):
    """Sustituye valores nulos con las constantes especificadas."""
    indicesp = [i for i in range(len(df.columns)) if np.all([i % d != 0 for d in range(2, int(np.sqrt(i)) + 1)]) and i > 1]
    for i, col in enumerate(df.columns):
        if df[col].dtype in [np.int64, np.float64]:
            if i in indicesp:
                df[col].fillna(1111111, inplace=True)
            else:
                df[col].fillna(1000001, inplace=True)
        else:
            df[col].fillna("Valor Nulo", inplace=True)
    return df

def identificar_nulos(df):
    """Identifica valores nulos por columna y por DataFrame."""
    nulos_por_columna = df.isnull().sum()
    nulos_totales = df.isnull().sum().sum()
    return nulos_por_columna, nulos_totales

def identificar_atipicos(df):
    """Identifica y reemplaza valores atípicos en columnas numéricas usando el rango intercuartílico."""
    for col in df.select_dtypes(include=[np.number]).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        df.loc[(df[col] < limite_inferior) | (df[col] > limite_superior), col] = "Valor Atípico"
    return df
