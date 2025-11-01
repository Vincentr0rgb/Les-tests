import os

#liste pour les nom et les mots de passe
password_Name = []
passwords = []
backup =[]
exit = False

#creer les Mots de passe
def createpassword ():
    name = input("créer un idantifiant")
    create = input("creer un mot de passe: ")
    password_Name.append(name)
    passwords.append(create)

#Gérer le ficher des Mots de passe
def filePasswods ():
    with open('passwords.txt', "a") as file:
        for passwordname, password in zip(password_Name,passwords):
            file.write(f"Nom : {passwordname} -- Mot de passe : {password} \n")

#Début du programe
# cherche si un ficher est existant
if os.path.exists("passwords.txt"):
    with open('passwords.txt', "r") as file:
        backup = file.read()
else:
    filePasswods()
while exit == False:
    navigation = input("Que voulez vous faire ?  "
                       "1 : créer un mot de passe ?    "
                       "2 : accèder à un mots de passe ?   "
                       "3 : Quiter ?   ")

    if navigation == "1":
        createpassword()
        filePasswods()
        with open("passwords.txt", "r") as file:
           backup = file.read()

    elif navigation == "2":
        if backup == []:
            print("Vous n'avez pas de mot de passe !")
        else:
            with open ("passwords.txt", "r") as file:
                print(backup)

    elif navigation == "3":
        isExit = input("Voulez vous quiter ? (y/n) ")
        if isExit == "y":

            exit = True

