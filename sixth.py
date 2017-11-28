names = list()
age = list()
email = list()

for counter in range(0, 3):
    name = input("Enter the name\n")
    names.append(name)


for counter in range(0, 3):
    ages = input("Enter the age\n")
    age.append(ages)


for counter in range(0, 3):
    mail = input("Enter the emailId\n")
    email.append(mail)


for counter in range(0, 3):
    print(names[counter])

for counter in range(0, 3):
    print(age[counter])

for counter in range(0, 3):
    print(email[counter])
