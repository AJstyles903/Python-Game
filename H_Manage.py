'''
Diet (GYM) Menagment
Author : AJstyles903
Work : Manage Your Exersice And Food With Time In File 
'''

client_list = {1: "Aryan", 2: "jay", 3: "dhruval"}
log_list = {1: "Exercise", 2: "Food"}


def gettime():
    import datetime
    return datetime.datetime.now()


try:
    print("Select client name : ")
    for key, value in client_list.items():
        print("Press", key, "To Look", value, "\n", end="")
    client_name = int(input())
    print("Select client name", client_list[client_name], "\n", end="")
    print("Press 1 to log")
    print("Press 2 to Retrieve")
    op = int(input())
    if op is 1:
        for key, value in log_list.items():
            print("Press", key, "To Look", value, "\n", end="")
        log_name = int(input())
        print("Selected job ", log_list[log_name])
        f = open(client_list[client_name]+"_"+log_list[log_name]+".txt", "a")
        k = "y"
        while (k is not "n"):
            print("Enter", log_list[log_name], "\n", end="")
            mytext = input()
            f.write("["+str(gettime())+"] : "+mytext+"\n")
            k = input("Add more?? y/n:")
            continue
        f.close()

    elif op is 2:
        for key, value in log_list.items():
            print("Press", key, "To Retrive", value, "\n", end="")
        log_name = int(input())
        print(client_list[client_name], "-",
              log_list[log_name], "Report:", "\n", end="")
        f = open(client_list[client_name]+"_"+log_list[log_name]+".txt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()

    else:
        print("invalid input!!")

except Exception as e:
    print("Wrong input!!")
