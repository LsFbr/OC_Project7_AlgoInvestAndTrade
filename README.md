<div style="display: flex; align-items: center; gap: 10px;">
    <h1 style="margin: 0;">AlgoInvest&Trade</h1>
    <img src="https://user.oc-static.com/upload/2020/09/18/1600429119334_P6.png" 
            alt="le logo d'AlgoInvest&Trade" 
            width="45" 
            height="36"/>
</div>

Ce projet a pour but d'optimiser des stratégies d'investissement par achat 
d'actions à l'aide d'algorithmes, en maximisant le profit à partir d'un investissement initial donné.

L'installation du projet et l'utilisation des programmes se fait depuis un terminal.

# Installation

## Prérequis :
- python 3
- pip
- git


## 1. Déplacer vous dans le répertoire où vous souhaitez cloner le projet
```
cd chemin/vers/le/repertoire
```

## 2. Clonez le projet et accédez à son répertoire
```
git clone https://github.com/LsFbr/OC_Project7_AlgoInvestAndTrade.git
cd OC_Project7_AlgoInvestAndTrade
```

## 3. Créez un environnement virtuel
#### Windows
```
python -m venv venv
```
#### Linux / MacOS  
```
python3 -m venv venv
```

## 4. Activez l'environnement virtuel
#### Windows
```
.\venv\Scripts\activate
```
#### Linux / MacOS
```
source venv/bin/activate
```

## 5. Installez les dépendances
```
pip install -r requirements.txt
``` 

# Utilisation
Deux programmes sont disponibles :
- bruteforce.py : algorithme de force brute
- optimized.py : algorithme de programmation dynamique

Ces deux programmes permettent d'aboutir au même résultat, c'est-à-dire de trouver la meilleure stratégie d'investissement pour un capital initial donné. Cependant, l'algorithme de force brute a une performance brute moins élevée que l'algorithme de programmation dynamique. Il consomme plus de ressources et de temps, et devient rapidement inutilisable pour des datasets de plus de 20 actions.

### Datasets : 
Pour pouvoir être utilisés, les datasets d'actions à traiter doivent :
- Être au format .csv
- les données contenues doivent être structurées en 3 colonnes dans cet ordre :
    - Nom de l'action
    - Coût d'achat
    - Taux de profit sur 2 ans (en %)
- Se trouver dans le dossier /datasets du projet.

## Exécution des programmes

Les deux programmes se lancent de la même façon :
#### Windows
```
python <nom_du_programme>.py <nom_du_dataset>.csv <capital_initial>
```
#### Linux / MacOS
```
python3 <nom_du_programme>.py <nom_du_dataset>.csv <capital_initial>
```
***

**Exemples :** 
- pour lancer le programme bruteforce.py avec le dataset dataset_base.csv et un capital initial de 500€ :
    #### Windows
    ```
    python bruteforce.py dataset_base.csv 500
    ```
    #### Linux / MacOS
    ```
    python3 bruteforce.py dataset_base.csv 500
    ```
    ***
- pour lancer le programme optimized.py avec le dataset dataset_2.csv et un capital initial de 500€ :

    #### Windows
    ```
    python optimized.py dataset_2.csv 500
    ```
    #### Linux / MacOS
    ```
    python3 optimized.py dataset_2.csv 500
    ```