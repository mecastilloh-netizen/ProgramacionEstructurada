#Contar los numeros del 0 al 9
from colorama import Fore, Style
for number in range(10):
    if number % 2 == 0:
        print(Fore.GREEN + f"Numero: {number}" + Style.RESET_ALL)
        for num in range(number):
         print (f"Antesesor: {num}")
         for n in range(num):
            if n % 2 != 0: print(f"{n}")
else:
    print(Fore.RED + f"Numero: {number}" + Style.RESET_ALL)