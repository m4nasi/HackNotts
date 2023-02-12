import sys
from ast import literal_eval

username = ""
password = ""
information = ""
newAccount = False#from java script

if newAccount == True:
    username = ""#from java script
    password = ""#from java script
    information = []
    requirementInfo = [] #from java script

    accountsFile = open("accounts.txt", "r")
    users = accountsFile.readlines()
    for i in range(len(users)):
        user = literal_eval(users[i])
        user = list(user.keys())[0]
        if user == username:
            print("username already exists under that name.")
            accountsFile.close()
            #return back to java script with failed to create account
            sys.exit()
    accountsFile.close()        

    information.append(password)
    for i in range(len(requirementInfo)):
        information.append(requirementInfo[i])
    account = str({username: information})
    accountsFile = open("accounts.txt", "a")
    accountsFile.write(account)
    accountsFile.close()
    #return back to java script with successful account creation
    sys.exit()

else: #not creating account, accessing info
    username = ""#from java script
    password = ""#from java script
    information = []
    requirementInfo = [] #from java script

    accountsFile = open("accounts.txt", "r")
    users = accountsFile.readlines()
    for i in range(len(users)):
        user = literal_eval(users[i])
        user = list(user.keys())[0]
        if (user == username) and (user.get(username)[0] == password):
            accountsFile.close()
            for i in range(1, len(user.get(username))):
                information.append(user.get(username))[i]
            #return back to java script, successful login with allergy info
            sys.exit()
    accountsFile.close()
    #return back to java script, unsuccessful login
    sys.exit()


