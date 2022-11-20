def login(username,password):
    with open('data/accounts.txt', 'r') as f:
        for line in f:
            if line.split(':')[0] == username:
                if line.split(':')[1][:-1] == password:
                    return "Login successful"
                else:
                    return "Login failed"
    return "Login failed"