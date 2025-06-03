email = input("Enter your email: ")
k = d = 0
if len(email)>=6:
    if email[0].isalpha():
        if email[-4] == "." or email[-3] == ".":
            if ("@" in email) and (email.count("@")==1):
                for i in email:
                    if i.isspace():
                        k=1
                    elif i.isdigit():
                        continue
                    elif i=="."or i=="_" or i=="@":
                        continue
                    else:
                        d=1
                if  k==1 or d==1 :
                    print("Wrong email")
                else:
                    print("Right email")
            else:
                print("Wrong email")
        else:
            print("Wrong email")
    else:
        print("Wrong email")
else:
    print("Wrong email")