women = int(input("Entrez une valeur correspondant au nombre de femmes moyen dans la population: "))
past_generation = int(input("Entrez une valeur correspondant à la population précédente: "))

print(population_start,birthrate,women,past_generation)

result = birthrate * women + population_start - past_generation

print("la population actuelle est de",result,"habitants.")

while True:
    past_generation = int(population_start)
    population_start = int(result)
    women = int(population_start / 2)
    birthrate = int(input("Entrez une valeur correspondant au nombre d'enfant moyen par couple: "))

    print(population_start,birthrate,women,past_generation)

    result = birthrate * women + population_start - past_generation

    print("la population actuelle est de",result,"habitants.")

