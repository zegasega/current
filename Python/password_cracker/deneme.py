
import random
import pyautogui
import time
from datetime import datetime



#Current time için
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


#karakter listesi
karakter = "abcçdefgğhıijklmnopqrsştuüvwxyz1234567890"
karakter_list = list(karakter)

#panel
password = pyautogui.password("Şifrenizi Giriniz ")
guess_password = ""

while(guess_password != password):
	guess_password = random.choices(karakter_list, k=len(password))
	print("<<"+ str(guess_password) + ">>")

	if(guess_password == list(password)):
		print("Şifreniz :  " + "".join(guess_password), "Bitiş Zamanı =", current_time)
		input()
		break








	