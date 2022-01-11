hosts = []
while 1:
    n = input(" How many people do you want to invite to the party (1-9)")
    if n.isdigit():
       n = int(n)
       if 0 < n < 10 :
           for i in range(n) :
                name = input(" host name : ")
                while  not name.isalpha() :
                    name = input( " wrong name ,please enter right host name : ")
                hosts.append(name)
                print(name," has been invited")
           break
       elif n < 1:
           print("the number should be more than 0")
       else :
           print("Too many people ")

    else:
        print("please enter a number")

