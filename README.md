# Servicio de Optimización de Portafolios

Proyecto consiste en una API REST constru´da en **Python** con **Flask**, permite calcular un portafolio óptimo a partir de los retornos diarios de distintos activos. El objetivo es distribuir la inversión, limitando el riesgo y la concentración en un solo activo.

---

## Método de optimización utilizado

Se utilizó el modelo de **Markowitz**, que busca minimizar la varianza del portafolio, respetando restricciones de peso por activo y un riesgo máximo definido por el usuario. Lo usé por un enfoque más clásico y también por la facilidad de implementar con python y libería CVXPY


---

## Cómo funciona

- **Entrada**: El servicio recibe un archivo `.csv` con los retornos diarios.
- **Parámetros**:
  - `risk_level`: nivel de riesgo máximo aceptado.
  - `max_weight`: porcentaje máximo que se puede asignar a cada activo.
- **Salida**: JSON con los pesos óptimos asignados a cada activo

---

## Tecnologías utilizadas

- Python
- Flask
- Pandas
- NumPy
- CVXPY (para el problema de optimización)
- HTML/CSS (front simple con Bootstrap)
- Postman (para pruebas)

---

## Estructura del proyecto
optimiza-fintual/
│
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── optimizer.py
│ ├── templates/
│ │ └── index.html
│ └── static/
│ └── style.css
│
├── run.py
├── requirements.txt
└── README.md
