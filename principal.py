import random
from controller.login import realizar_login
from frases_motivacionais import frases

print("\nBem vindo ao The Thief !\n")
frase = frases[random.randint(0, len(frases) - 1)]
print(frase)

login_menu_op = -1

while login_menu_op != 0:
    login_menu_op = realizar_login()

frase = frases[random.randint(0, len(frases) - 1)]
print("\n" + frase)
print("\nPrograma encerrado. Volte sempre.\n")
