#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        user_input = input("Veuillez entrer vos valeurs separees d'un espace \n")
        values = user_input.split()
        pass

    values.sort()
    print(values)
    return values


def anagrams(words: list = None) -> bool:
    if words is None:
        user_input = input("Veuillez entrer vos mots separes d'un espace \n")
        words = user_input.split()
        pass
   
    if(sorted(words[0]) == sorted(words[1])):
        print("Il s'agit d'un anagrame")
        return True

    print("Pas un anagramme")
    return False


def contains_doubles(items: list) -> bool:
    unique_elements_discovered = []

    for itm in items:
        if(itm in unique_elements_discovered):
            return True
        else:
            unique_elements_discovered.append(itm)

    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = ""
    best_average_grade = 0

    for key in student_grades:
        average_grade = sum(student_grades[key]) / 3
        if(average_grade > best_average_grade):
            best_average_grade = average_grade
            best_student = key

    output = {best_student: best_average_grade}
    return output


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    all_letters_frequency = {}

    for letter in sentence:
        if(letter != " " and letter != "."):
            if(not(letter in all_letters_frequency)):
                all_letters_frequency[letter] = 1
            else:
                all_letters_frequency[letter] += 1

    frequent_letters_frequency = {}
    for key in all_letters_frequency:
        if(all_letters_frequency[key] >= 5):
            frequent_letters_frequency[key] = all_letters_frequency[key]

    sorted_keys = sorted(frequent_letters_frequency, key=frequent_letters_frequency.get, reverse=True)
    output = {}
    
    for key in sorted_keys:
        output[key] = frequent_letters_frequency[key]

    print(output)
    return output


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name = input("Veuillez entrer le nom de la recette \n")
    ingredients = input("Veuillez entrer les ingredients separes par un espace \n").split()

    return {name : ingredients}
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    name = input("Veuillez entrer le nom de la recette \n")

    if(name in ingredients):
        print("Les ingredients necessaires sont " + ''.join(ing + " " for ing in ingredients[name]))
    else:
        print("Non.")
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
