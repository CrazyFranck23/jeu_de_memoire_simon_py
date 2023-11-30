import random
import time
import os


# Cette fonction permet d'efffacer ce qui est afficher dans le terminal selon le system
def clear_screen():
    if os.name == 'posix':  # Systeme Mac ou Linux
        os.system('clear')
    else:
        os.system('cls')  # System Windows


print("Bienvenue - Jeu du Simon")

""" Generation d'un nbr aléatoire, un premier nb est généré, puis converti en string ensuite ajouté a la variable 
random_sequence_str et ainsi de suite jusqu'a obtenir 4 et sortir de la boucle """
random_sequence_str = ""
for i in range(4):
    n = random.randint(0, 9)
    random_sequence_str += str(n)

score = 0
good_answer = 1

while good_answer == 1:
    print("Retenez la sequence")
    time.sleep(1)
    print(random_sequence_str)
    time.sleep(2)
    clear_screen()

    user_answer = input("Votre réponse : ")

    if user_answer == random_sequence_str:
        score += 1
        print("Bonne réponse ! Votre score : ", score)
        new_number = str(random.randint(0, 9))  # Ici on genere un nouveau nbr
        random_sequence_str += new_number  # Puis ce nbr est ajouter a notre sequence déjà existante
        time.sleep(2)
        clear_screen()
    else:
        print("Mauvaise réponse, la sequence était : ", random_sequence_str)
        print(f"Votre score final : {score}")  # Utilisation des f string
        good_answer = 0
