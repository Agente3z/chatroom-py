import string
import random

def generateCookie(username):
    cookie = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    with open('data/cookies/'+username,'w') as f:
        f.write(cookie)
    return cookie