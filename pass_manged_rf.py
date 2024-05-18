def Pass_manage():
    pwd =input("What is the Master Password? ")

    def view():
        with open('passwords.txt','r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user , passwd = data.split("|")
                print("user: ",user,"\n","Password:",passwd)


    def add():
        name =input("Account Name: ")
        pwd = input("Password: ")
    
        with open('passwords.txt','a') as f:
          f.write(name +" | "+ pwd + "\n")



    while True:
        mode = input("Would you like to add a new Password or view existing ones(add,view) or q to Quit? ")
        if mode == "q":
            break
        elif mode == "add":
            add()
        elif mode == "view":
            view()
        else:
             print("Invalid mode.")
        continue

Pass_manage()