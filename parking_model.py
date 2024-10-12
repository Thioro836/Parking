"""TODO: DESCRIPTION."""

from pathlib import Path  # built-in usefull Path class
from pulp import PULP_CBC_CMD, LpProblem, LpVariable, lpSum, LpMinimize, value, LpStatus

# ============================================================================ #
#                                  SET MODEL                                   #
# ============================================================================ #
def set_model_parking(cars):
    """TODO: set the parking problem model."""
    # ------------------------------------------------------------------------ #
    # Linear problem with minimization
    # ------------------------------------------------------------------------ #
    prob = LpProblem(name='optimisation_du_probleme_de_parking',sense=LpMinimize)

   # ------------------------------------------------------------------------ #
     # The variables

    # ------------------------------------------------------------------------ #
    # TODO: set variables
    x = [LpVariable(f'x_{i}', cat='Binary') for i in range(len(cars))]
    max_length = LpVariable('max_length', lowBound=0)
    y = [LpVariable('y', cat='Binary')]
    z = [LpVariable('z', cat='Binary')]
    M=54.1
    EPSILON = 0.1
   # ------------------------------------------------------------------------ #
    # The objective function
    # ------------------------------------------------------------------------ #
    # TODO: write the objective function
    prob+= max_length
# ------------------------------------------------------------------------ #
    # The constraints
    
    # ------------------------------------------------------------------------ #
    # TODO: write constraints
    #longueur des deux côtés de la rue 
    long_left = lpSum ([cars[i] * x[i] for i in range(len(cars))])
    long_right = lpSum([cars[i] * (1- x[i]) for i in range(len(cars))])

   # Contrainte pour que max_length soit au moins la longueur de chaque côté
    prob += max_length >= long_left
    prob += max_length >= long_right

    # contrainte pour que la longueur du côté gauche soit <=20
    #prob+=long_left <= 20 - EPSILON
    # Contrainte pour que seulement un côté ait une longueur >= 16
    # Si y = 1, long_right doit être >= 16
    # Si y = 0, long_left doit être >= 16
    #prob += long_left <= 16 +(M * y[0])
    #prob += long_right <= 16 + (M * (1 - y[0]))
    # contrainte sur les voitures qui ont une longueur >=4 mètres doivent etre garés sur le côté gauche
    #for i in range (len(cars)):
        #if cars[i]> 4 :
        #  prob+= x[i]==1

    # contrainte lorsque la longueur du côté gauche est >=10 ,celle du côté droit doit être inférieur à 13
    #si long_left >=10 ,alors z=1
    #prob+=long_left >=10 -(M *(1-z[0])) -EPSILON
    #prob+=long_left <=10 +(M *z[0])-EPSILON
    #prob+= long_right <=13 + (M *(1-z[0]))-EPSILON
    return prob, x
def solve_simple_example():
    """Solve the simple example."""
    # Set data
    cars = [4, 4.5, 3, 4.1, 2.4, 4.2, 3.7, 3.5, 3.2, 4.5, 2.3, 3.3, 3.8, 4.6, 3 ]  # La longueur de chaque voiture en mètres

    # Resolution du problème en utilisant le modèle
    prob, x= set_model_parking(cars)
        
    #resoudre le problème
    status= prob.solve(PULP_CBC_CMD(msg=False))
      # Print the solver output

    print_log_output(prob, x, cars)
# ============================================================================ #
#                                   UTILITIES                                  #
# ============================================================================ #


def print_log_output(prob: LpProblem, x, cars):
    """Affiche les résultats et les statistiques du problème."""
    print()
    print('-' * 40)
    print('Stats')
    print('-' * 40)
    print()
    print(f'Number variables: {prob.numVariables()}')
    print(f'Number constraints: {prob.numConstraints()}')
    print(f'Solve status: {LpStatus[prob.status]}')
    print()
    
    # Récupérer la valeur optimale de la fonction objectif
    optimal_value = value(prob.objective)
    print('Solution')
    print(f'Valeur de la stratégie optimale: {optimal_value}')
    print()
    print('-' * 40)
    print("Description de la stratégie optimale")
    print('-' * 40)
    print('voiture\t longueur de la voiture\t \t côté')
    for i in range(len(cars)):
        cote = 'gauche' if x[i].varValue == 1 else 'droit'
        print(f'{i+1}\t\t{cars[i]}\t\t\t {cote}')
    
    left_side = sum(cars[i] for i in range(len(cars)) if x[i].varValue == 1)
    right_side = sum(cars[i] for i in range(len(cars)) if x[i].varValue == 0)
    print(f'\nLongueur côté gauche: {left_side}')
    print(f'Longueur côté droit: {right_side}')
if __name__ == '__main__':
    solve_simple_example()