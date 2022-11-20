def register(username,password):
    try:
        with open('data/accounts.txt', 'r') as f:
            for line in f:
                if line.split(':')[0] == username:
                    return "Username already exists"
        with open('data/accounts.txt', 'a') as f:
            f.write(username + ':' + password + '\n')
        return "Registration successful"
    except:
        with open('data/accounts.txt', 'w') as f:
            f.write(username + ':' + password + '\n')
        return "Registration successful"