import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



data = pd.read_excel('../dataset/concat.xlsx')

# clean data
# remplacer les "*" par des NaN
data = data.replace('*', np.nan)
data.dropna(inplace=True)
data.reset_index(drop=True, inplace=True)

# save data
data.to_excel('../dataset/dataCleaned.xlsx', index=False)

# afficher l'évolution du prix moyen du m² par année
# plt.scatter(data['Annee'], data['Prix moyen au m²'])
# plt.xlabel('Année')
# plt.ylabel('Prix moyen au m2 en euros')
# plt.title('Evolution du prix moyen du m2 par année')
# plt.show()

# Créer le graphique en lignes avec Plotly
fig = px.line(
    data, 
    x='Annee', 
    y='Prix moyen au m²', 
    color='Commune', 
    markers=True,  # Ajouter des points pour chaque année
    title="Évolution du prix moyen du m² par commune",
    labels={
        'annee': 'Année',
        'prix_m2': 'Prix moyen du m²',
        'commune': 'Commune'
    }
)

# Améliorer le design du graphique
fig.update_layout(
    xaxis_title='Année',
    yaxis_title='Prix moyen du m²',
    hovermode='x unified',  # Afficher toutes les informations d'une année en même temps
    template='plotly',      # Style du graphique
    legend_title_text='Commune'
)

# Afficher le graphique
fig.show()