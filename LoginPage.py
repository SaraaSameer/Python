import os

def Login():
    os.system("cls")
    print("\nEnter Your UserName: ")
    name=input()
    print("Enter Your Password: ")
    password= input()
    f=open("Login.txt","r")

    flag:bool =False
    for x in f:
        line= x.split()
        if line[0]==name:
            if line[1]== password:
                flag=True
                print("Welcome On Board")
                break
            else:
                flag=False
                break
    f.close()
    if flag==False:
        print("Username/Password doesnot match")
    os.system("pause")

def SignUp():
    while(1):
        print("\nEnter Your UserName: ")
        name=input()
        flag=False
        f=open("Login.txt","r")
        for x in f:
          string= x.split()
          if name==string[0]:
                flag=True
                print("Username already Exist, Pick a different one!")
                break
          else:
               continue
        f.close()
        f= open("Login.txt","a")
        if flag==False:
             f.write("\n")
             f.write(name+" ")
             print("Enter Your Password: ")
             password= input()
             f.write(password)
             print("Your Account is Created")
             os.system("pause")
             f.close()
             break
        else:
             continue

while(1):
    os.system("cls")
    choice = int(input("Press 1 to Login \nPress 2 to Sign In\nPress 3 to Exit : "))
    if choice == 1:
        Login()
    elif choice ==2:
        SignUp()
    elif choice==3:
        exit(0)



