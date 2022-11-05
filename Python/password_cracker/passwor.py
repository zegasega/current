import random
number = int(input("Syı Gir: "))
guess = 0
while (guess !=number):
    guess= random.randint(0,9999)
    print(guess)
print("Şifren  " + str(number))