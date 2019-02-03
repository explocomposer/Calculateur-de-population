# (STARTING POPULATION + (BIRTHRATE x WOMEN) ) - PAST GENERATION

population_start = int(input("Entrez une valeur correspondant à la population initiale: "))
birthrate = int(input("Entrez une valeur correspondant à la moyenne du nombre d'enfant par couple: "))
women = int(input("Entrez une valeur correspondant au nombre de femmes moyen dans la population: "))
past_generation = int(input("Entrez une valeur correspondant à la population précédente: "))

print(population_start,birthrate,women,past_generation)

result = birthrate * women + population_start - past_generation

print("la population actuelle est de",result,"habitants.")

