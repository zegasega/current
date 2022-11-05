import hashlib
from urllib.request import urlopen
url = "https://diziwatch.net/wp-login.php"

############# append the below code ################ 

def readwordlist(url):
    try:
        wordlistfile = urlopen(url).read()
    except Exception as e:
        print("Hey there was some error while reading the wordlist, error:", e)
        exit()
    return wordlistfile
 
 
def hash(password):
    result = hashlib.sha1(password.encode())
    return result.hexdigest()
 
 
def bruteforce(guesspasswordlist, actual_password_hash):
    for guess_password in guesspasswordlist:
        if hash(guess_password) == actual_password_hash:
            print("Hey! your password is:", guess_password,
                  "\n please change this, it was really easy to guess it (:")
            # If the password is found then it will terminate the script here
            exit()