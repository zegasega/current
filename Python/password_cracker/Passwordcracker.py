
import random
import pyautogui
from time import time



#Current time için
start = time()


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
		print("Şifreniz :" + "".join(guess_password),(f'İşlem İçin Geçen Süre: {time() - start} saniye'))
		
		input()
		break



#Şifremiz ne kadar güvenli??
#1= 9
#2= 56
#3=843
#4= abc
#5=abc123
#6=balıkesir2022




	