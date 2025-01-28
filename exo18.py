import csv

def add_to_file(numbers):
    with open("numbers.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(numbers)
    return

def load_from_file():
    try:
        with open("numbers.csv", "r", newline="") as file:
            reader = csv.reader(file)
            return [int(x) for x in next(reader)]
    except FileNotFoundError:
        print("Le fichier numbers.csv n'existe pas.")
        return []
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {e}")
        return []

numbers = [1, 2, 3, 4, 5]

def display_menu():
    print("\nMenu:")
    print("1. Ajouter un nombre à la fin")
    print("2. Insérer un nombre à une position")
    print("3. Supprimer un nombre à une position")
    print("4. Supprimer un nombre spécifique")
    print("5. Trier la liste")
    print("6. Inverser la liste")
    print("7. Rechercher un élément")
    print("8. Enregistrer la liste dans un fichier")
    print("9. Charger la liste depuis un fichier")
    print("0. Quitter")

while True:
    display_menu()
    try:
        choice = int(input("Choisir une option (0-9): "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue

    print("Liste actuelle:", numbers)
    if choice == 1:
        try:
            append_value = int(input("Entrer un nombre pour ajouter: "))
            numbers.append(append_value)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    elif choice == 2:
        try:
            index = int(input("Entrer l'index: "))
            insert_value = int(input("Entrer un nombre pour insérer: "))
            numbers.insert(index - 1, insert_value)
        except ValueError:
            print("Veuillez entrer des valeurs valides.")
        except IndexError:
            print("Index hors de portée.")
    elif choice == 3:
        try:
            position_pop = int(input("Entrer la position pour supprimer: "))
            pop_value = numbers.pop(position_pop - 1)
            print("Valeur supprimée:", pop_value)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        except IndexError:
            print("Index hors de portée.")
    elif choice == 4:
        try:
            remove_value = int(input("Entrer le nombre à supprimer: "))
            numbers.remove(remove_value)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        except ValueError:
            print("Le nombre n'existe pas dans la liste.")
    elif choice == 5:
        numbers.sort()
        print("Liste triée:", numbers)
    elif choice == 6:
        numbers.sort()
        numbers.reverse()
        print("Liste inversée:", numbers)
    elif choice == 7:
        try:
            element = int(input("Entrer l'élément à rechercher: "))
            if element in numbers:
                print(element, "est dans la liste, position:", numbers.index(element) + 1)
            else:
                print(element, "n'existe pas!")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    elif choice == 8:
        add_to_file(numbers)
        print("La liste", numbers, "a été enregistrée avec succès!")
    elif choice == 9:
        numbers = load_from_file()
        print("Liste chargée depuis le fichier avec succès!")
    elif choice == 0:
        break
    else:
        print("Choix invalide. Veuillez choisir une option entre 0 et 9.")

print("Liste finale:", numbers)
