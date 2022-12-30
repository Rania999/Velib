# Flux Vélib
Réalisé dans le cadre du cours de Nouvelles données de mobilité des Ponts et Chaussées

## Contexte

Le trafic de vélos dans la métropole est en constante augmentation. La Ville de Paris a installé des compteurs sur ses pistes cyclables afin de mieux connaitre les flux. Cependant, ces données ne couvrent que la ville de Paris et les compteurs ne permettent pas forcément d'avoir une vision sur tout le territoire.

Depuis la 2007, le service Vélib' permet de louer des vélos mécaniques ou électriques dans la métropole du Grand Paris sans réservation. Le service fonctionne avec des stations réparties dans toutes les communes. Chaque station peut accueillir un nombre limité de vélos qui peuvent être empruntés. La forte densité de stations et la haute fréquence de mise à jour des données pourraient permettre d'avoir une idée des flux globaux de vélos dans la métropole au cours de la journée.

## Problématique

Est-ce que les données actuellement en open data de Vélib' permettent de reconstruire les flux de vélos dans la ville ?

Plusieurs profils types de journée sont attendus (journée en semaine, week-end, vacances scolaire). Aussi, les données Vélib' ne représentent qu'un type d'usagers du vélo. Le résultat sera à comparer aux résultats données par les compteurs fixes de la ville de Paris.

## API et données

- Emplacement des stations Vélib'
- Nombre de vélos disponibles et types dans chaque station
- Nombre de places disponibles dans chaque station

La base de donnée est mise à jour toutes les minutes.

Une attention particulière devra être portée au fait que Vélib' propose le service Park+ qui permet de stationner plus de vélos qu'il n'y a d'emplacements.

- Données totems vélo de la Ville de Paris (optionnel)

## Réalisation

Afin de reconstruire les flux de cyclistes à Paris, nous allons travailler sur les nombres de vélos dans les stations et leur évolution. A ce stade, nous ne disposons que des données agrégées (nombre de vélos par station), donc l'objectif premier est de produire un modèle pour identifier les flux sortants et entrants de chaque station. Notre modèle se basera sur une recherche du plus court chemin.


Mise en œuvre : partons de la station A qui se vide, les stations les plus proches (B, C, et D) se vident également donc on étend la recherche aux stations suivantes (E, F et G). E et G se remplissent donc constituent des candidats potentiels, et la distance entre A et G ( est inférieure à celle entre A et E (, donc nous considérons que le cycliste s'est rendu de A à G. Nous débuterons par les stations avec le plus de mouvements entrants/sortants.

Nous évaluerons la pertinence de cette méthode sur la base d'une comparaison entre ces flux et ceux produits par la ville de Paris, et, si possible, nous ferons des observations sur place.

Nous prévoyons de visualiser les données à l'aide l'outil QGIS et de la librairie géopandas en complément des libraires usuelles Python et celles qui nous sembleront pertinentes au moment de la programmation.

Afin de récupérer les données en continu sans avoir à laisser tourner nos ordinateurs, nous utiliserons un serveur distant et nous établirons la structure de transfert des données lors du projet comme indiqué sur l'échéancier.

## Idées à poursuivre
Nombre de stations sans utilisateurs X% du temps. 
Coéfficient de Gini dans une zone. 