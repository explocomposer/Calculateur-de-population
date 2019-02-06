def calcul():
    global result
    result = birthrate * women + population_start - past_generation
    print("la population actuelle est de", result, "habitants. \nCalcul de la génération suivante:")

population_start = int(input("Entrez une valeur correspondant à la population initiale: "))
women = int(input("Entrez une valeur correspondant au nombre de femmes moyen dans la population: "))
birthrate = int(input("Entrez une valeur correspondant à la moyenne du nombre d'enfant par couple: "))
past_generation = int(input("Entrez une valeur correspondant à la population précédente: "))

print(population_start,women,birthrate,past_generation)

calcul()

while True:
    auto = input("Souhaitez-vous calculer automatiquement les 10 prochaines générations ? (oui,non)"
                 "\nConservation automatiques des paramêtres par défaut si oui. "
                 "\n>>> ")
    if auto == "oui":
        i = 0
        while i < 10:
            past_generation = int(population_start)
            population_start = int(result)
            women = int(population_start / 2)
            birthrate = int(birthrate)

            print(population_start, women, birthrate, past_generation)

            calcul()
            i += 1
            if i == 10:
                break
    else:
        past_generation = int(population_start)
        population_start = int(result)
        change = input("Souhaitez-vous influer sur le nombre de femmes pour la génération suivante? (oui,non)"
                       "\n>>> ")
        if change == "oui":
            women = int(input("Entrez une nouvelle valeur: "))
        elif change == "non":
            women = int(population_start / 2)
        birthrate = int(input("Entrez une valeur correspondant au nombre d'enfant moyen par couple: "))

        print(population_start,women,birthrate,past_generation)

        calcul()
