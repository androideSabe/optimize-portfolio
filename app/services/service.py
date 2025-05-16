import pandas as pd
import numpy as np
import cvxpy as cp

def optimize_portfolio(df, risk_level, max_weight):
    try:
        # elimina primera columna (fechas)
        df = df.iloc[:, 1:]

        # aseguramos que todos los datos sean numericos
        df = df.apply(pd.to_numeric, errors='coerce').dropna()

        if df.empty:
            return {"El archivo CSV no contiene datos numéricos válidos"}

        # extra valores numericos del dataframe para pasarlos en forma de array numPy
        # forzando a que todos los valores sean de tipo float64
        returns = df.values.astype(np.float64)
        
        # obtenemos los nombres de las columnas del DataFrame (los tickers)
        tickers = df.columns.tolist()

        # matriz de varianza de los retornos 
        cov_matrix = np.cov(returns, rowvar=False)
        
        # forzamos que la matriz sea simétrica
        cov_matrix = (cov_matrix + cov_matrix.T) / 2

        #columnas del csv 
        n_assets = len(tickers)
        
        # peso que tendrá cada activo, vector de tamaño 12
        weights = cp.Variable(n_assets)

        # forma cuadrática para calcular el riesgo total del portafolio
        # es el riesgo total del portafolio considerando tanto la varianza individual como la relación entre activos
        portfolio_variance = cp.quad_form(weights, cov_matrix)
        
        # encontrar los pesos que minimicen el riesgo del portafolio 
        objective = cp.Minimize(portfolio_variance)

        
         
        constraints = [
            cp.sum(weights) == 1, #suma de todos los pesos debe ser 1
            weights >= 0,         #evitar los pesos negativos
            weights <= max_weight, #forzamos diversificación al establecer un limite 
            portfolio_variance <= risk_level # limite del riesgo permitido 
        ]

        # instancia del problema de optimización
        problem = cp.Problem(objective, constraints)
        
        # cvxpy busca la mejor combinación de pesos 
        result = problem.solve()

        if weights.value is not None: # si encuentra portafolio que cumpla las restricciones
            return {
                "optimal_portfolio": dict(zip(tickers, np.round(weights.value, 4)))
            }
        else:
            return {"error": "No se encontró una solución viable con los parámetros dados."}

    except Exception as e:
        return {"error": str(e)}
