import pandas as pd
import numpy as np


# Premier dataset avec les données les plus complètes, on a supprimé les colonnes fourchette de prix au m² et fourchette de prix au m².1
# On a aussi supprimé les lignes avec des valeurs manquantes
def dataset1() : 
    # Initialiser une liste pour stocker les DataFrames de chaque année
    dataframes = []
    dfSalaireMoyen = pd.read_csv('../dataset/salaireModif3.csv', sep=';')
    # Boucle sur les années de 2014 à 2023
    for year in range(2014, 2024):
        # Charger le fichier CSV de prix moyen au m² pour l'année en cours
        prix_filepath = f'../dataset/prix-moyen-au-metre-carre-enregistre-par-commune-{year}.csv'
        
        try:
            dfPrixYear = pd.read_csv(prix_filepath, sep=';')
            # print(f"Fichier de prix pour {year} chargé avec succès.")
        except FileNotFoundError:
            print(f"Fichier pour {year} non trouvé. Passons à l'année suivante.")
            continue
        
        # Charger le fichier de densité pour l'année en cours
        dfDensite = pd.read_csv('../dataset/populationDensity.csv', sep=';')

        # Vérifier l'existence de l'année dans dfDensite
        if str(year) in dfDensite.columns:
            # Filtrer dfDensite pour ne garder que la colonne 'Période' (qui est la commune) et la colonne pour l'année courante
            dfDensiteYear = dfDensite[['Période', str(year)]]

            # Renommer les colonnes pour faciliter la fusion
            dfDensiteYear.columns = ['Commune', 'Densité par km²']

            # Filtrer dfDensite pour ne garder que les communes présentes dans dfPrixYear
            dfDensiteFiltre = dfDensiteYear[dfDensiteYear['Commune'].isin(dfPrixYear['Commune'])].copy()

            # Ajouter une colonne "Année" avec la valeur de l'année courante
            dfDensiteFiltre.loc[:, 'Année'] = year

            # Fusionner les deux DataFrames sur la colonne 'Commune'
            dfResultYear = pd.merge(dfPrixYear, dfDensiteFiltre, on='Commune', how='left')
            
            # Ajouter le DataFrame de l'année courante à la liste
            dataframes.append(dfResultYear)
            
            # Afficher un message pour confirmer la fusion
            # print(f"Fusion des données pour l'année {year} réussie.")
        else:
            print(f"L'année {year} n'est pas disponible dans le fichier de densité.")

    # Concaténer tous les DataFrames de chaque année
    dfFinal = pd.concat(dataframes, ignore_index=True)

    # renommer les colonnes de dfSalaireMoyen
    dfSalaireMoyen.columns = ['Commune', 'Année', 'Salaire moyen']
    #supprimer dans chaque ligne de Commune les 6 premiers caractères
    dfSalaireMoyen['Commune'] = dfSalaireMoyen['Commune'].str[6:]
    # Fusionner dfFinal et dfSalaireMoyen
    dfFinal = pd.merge(dfFinal, dfSalaireMoyen, on=['Commune', 'Année'], how='inner')

    # convertir commune en string
    dfFinal['Commune'] = dfFinal['Commune'].astype(str)
    # drop les colonnes fourchette de prix
    dfFinal = dfFinal.drop(['Fourchette de prix au m²', 'Fourchette de prix au m².1'], axis=1)
    # enlever le signe euro dans le df
    dfFinal['Prix moyen au m²'] = dfFinal['Prix moyen au m²'].str.replace('€', '')
    dfFinal['Prix moyen au m².1'] = dfFinal['Prix moyen au m².1'].str.replace('€', '')
    # On va prendre 2 décimales pour la densité et salaire moyen
    dfFinal['Salaire moyen'] = dfFinal['Salaire moyen'].round(2)
    dfFinal = dfFinal.replace('*', pd.NA)

    # suppression des lignes avec des valeurs manquantes
    dfFinal = dfFinal.dropna()

    # année en int 
    dfFinal['Année'] = dfFinal['Année'].astype(int)
    # Remplacer les virgules par des points
    dfFinal['Densité par km²'] = dfFinal['Densité par km²'].str.replace(',', '.', regex=False)
    # Supprimer les espaces
    dfFinal['Densité par km²'] = dfFinal['Densité par km²'].str.replace(' ', '', regex=False)
    dfFinal['Densité par km²'] = dfFinal['Densité par km²'].astype(float)
    dfFinal['Densité par km²'] = dfFinal['Densité par km²'].round(2)

    print(dfFinal)

    # Afficher un aperçu du DataFrame final
    # print(dfFinal.head())
    # Afficher le nombre de lignes pour chaque année pour vérifier la présence des données
    # print(dfFinal['Année'].value_counts())
    # sauvegarder le dataset
    dfFinal.to_csv('../dataset/dataset1.csv', index=False)

# Deuxième dataset avec les données les plus complètes, on a supprimé les colonnes fourchette de prix au m² et fourchette de prix au m².1
# On a aussi supprimé la colonne prix moyen au m² pour les VEFA et les lignes avec des valeurs manquantes
def dataset2():
    # Initialiser une liste pour stocker les DataFrames de chaque année
    dataframes = []
    dfSalaireMoyen = pd.read_csv('../dataset/salaireModif3.csv', sep=';')
    # Boucle sur les années de 2014 à 2023
    for year in range(2014, 2024):
        # Charger le fichier CSV de prix moyen au m² pour l'année en cours
        prix_filepath = f'../dataset/prix-moyen-au-metre-carre-enregistre-par-commune-{year}.csv'
        
        try:
            dfPrixYear = pd.read_csv(prix_filepath, sep=';')
            # print(f"Fichier de prix pour {year} chargé avec succès.")
        except FileNotFoundError:
            print(f"Fichier pour {year} non trouvé. Passons à l'année suivante.")
            continue
        
        # Charger le fichier de densité pour l'année en cours
        dfDensite = pd.read_csv('../dataset/populationDensity.csv', sep=';')

        # Vérifier l'existence de l'année dans dfDensite
        if str(year) in dfDensite.columns:
            # Filtrer dfDensite pour ne garder que la colonne 'Période' (qui est la commune) et la colonne pour l'année courante
            dfDensiteYear = dfDensite[['Période', str(year)]]

            # Renommer les colonnes pour faciliter la fusion
            dfDensiteYear.columns = ['Commune', 'Densité par km²']

            # Filtrer dfDensite pour ne garder que les communes présentes dans dfPrixYear
            dfDensiteFiltre = dfDensiteYear[dfDensiteYear['Commune'].isin(dfPrixYear['Commune'])].copy()

            # Ajouter une colonne "Année" avec la valeur de l'année courante
            dfDensiteFiltre.loc[:, 'Année'] = year

            # Fusionner les deux DataFrames sur la colonne 'Commune'
            dfResultYear = pd.merge(dfPrixYear, dfDensiteFiltre, on='Commune', how='left')
            
            # Ajouter le DataFrame de l'année courante à la liste
            dataframes.append(dfResultYear)
            
            # Afficher un message pour confirmer la fusion
            # print(f"Fusion des données pour l'année {year} réussie.")
        else:
            print(f"L'année {year} n'est pas disponible dans le fichier de densité.")

    # Concaténer tous les DataFrames de chaque année
    dfFinal = pd.concat(dataframes, ignore_index=True)

    # renommer les colonnes de dfSalaireMoyen
    dfSalaireMoyen.columns = ['Commune', 'Année', 'Salaire moyen']
    #supprimer dans chaque ligne de Commune les 6 premiers caractères
    dfSalaireMoyen['Commune'] = dfSalaireMoyen['Commune'].str[6:]
    # Fusionner dfFinal et dfSalaireMoyen
    dfFinal = pd.merge(dfFinal, dfSalaireMoyen, on=['Commune', 'Année'], how='inner')

    # convertir commune en string
    dfFinal['Commune'] = dfFinal['Commune'].astype(str)
    # drop les colonnes fourchette de prix
    dfFinal = dfFinal.drop(['Fourchette de prix au m²', 'Fourchette de prix au m².1', 'Prix moyen au m².1'], axis=1)
    # enlever le signe euro dans le df
    dfFinal['Prix moyen au m²'] = dfFinal['Prix moyen au m²'].str.replace('€', '')
    # On va prendre 2 décimales pour la densité et salaire moyen
    dfFinal['Salaire moyen'] = dfFinal['Salaire moyen'].round(2)
    dfFinal = dfFinal.replace('*', pd.NA)

    # suppression des lignes avec des valeurs manquantes
    dfFinal = dfFinal.dropna()

    # année en int 
    dfFinal['Année'] = dfFinal['Année'].astype(int)
    # Remplacer les virgules par des points
    dfFinal['Densité par km²'] = dfFinal['Densité par km²'].str.replace(',', '.', regex=False)
    # Supprimer les espaces
    dfFinal['Densité par km²'] = dfFinal['Densité par km²'].str.replace(' ', '', regex=False)
    dfFinal['Densité par km²'] = dfFinal['Densité par km²'].astype(float)
    dfFinal['Densité par km²'] = dfFinal['Densité par km²'].round(2)

    print(dfFinal)

    # Afficher un aperçu du DataFrame final
    # print(dfFinal.head())
    # Afficher le nombre de lignes pour chaque année pour vérifier la présence des données
    print(dfFinal['Année'].value_counts())
    # sauvegarder le dataset
    dfFinal.to_csv('../dataset/dataset2.csv', index=False)
    
