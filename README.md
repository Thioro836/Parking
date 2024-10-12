# Parking
# Optimisation d'un problème de parking avec le langage PuLP
Ce projet vise à résoudre un problème d'optimisation lié à l'allocation optimale des voitures des deux côtés d'une rue en minimisant la longueur totale occupée.

# Les contraintes incluent :

Une limite maximale sur la longueur de chaque côté de la rue.
L'obligation de garer certaines voitures d'un côté selon leur longueur.
Des relations entre la longueur de chaque côté (gauche et droite).
Nous utilisons la programmation linéaire pour modéliser et résoudre ce problème à l'aide de la bibliothèque PuLP en Python.

# Fonctionnalités
Optimisation de la disposition des voitures des deux côtés de la rue.
Prise en compte des contraintes de longueur maximale de chaque côté.
Utilisation de variables binaires pour la prise de décision sur le côté où garer chaque voiture.
# Modèle mathématique
# Objectif : Minimiser la longueur maximale occupée par les voitures sur les deux côtés de la rue.
Variables :
x[i] : binaire indiquant si la voiture i est garée du côté gauche (x[i] = 1) ou du côté droit (x[i] = 0).
max_length : variable continue représentant la longueur maximale occupée d'un côté.
y, z : variables binaires utilisées pour activer certaines contraintes conditionnelles.
# Contraintes principales :
La somme des voitures garées d'un côté ne doit pas dépasser une certaine limite.
Si une certaine longueur est atteinte d'un côté, l'autre doit être inférieure à un seuil spécifique.
# Prérequis
Assurez-vous d'avoir Python 3.x et les bibliothèques nécessaires installées.
