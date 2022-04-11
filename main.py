import json
import sys

with open('data.txt') as f:
    data = json.load(f)

passwordRetry = True
passwordRetryCount = 3
while passwordRetry:
    username = input("Please input a username: ")

    password = input("Please input a password: ")
    for x in data['users']:
        if username == x['username'] and password == x['password']:
            print('login correct')
            sys.exit()
        elif passwordRetryCount == 0:
            sys.exit()
        else:
            print('Retrying: ' + passwordRetryCount.__str__() + ' more times ')
            passwordRetryCount -= 1
            break
