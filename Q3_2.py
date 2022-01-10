print("enter three person's names to invite : ")
persons = []
persons.append(input("First person name : "))
persons.append(input("Second person name : "))
persons.append(input("Third person name : "))

while True:
    ans = input("Do you want to invite more ? Y/N ")
    if ans.lower()=='y' :
        new = input("Enter a name : ")
        persons.append(new)
    elif ans.lower()=='n' :
        print("number of persons in the list = ", len(persons))
        break

