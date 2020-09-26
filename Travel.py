print("Welcome to World Travel Agency")
travelling = input("Yes or No ")

while travelling == 'Yes':
    num = int(input("Enter the Number of Passengers : "))
    for num in range(1,num+1):
        Name = input("Enter Name : ")
        Age = input("Enter Age : ")
        Gender = input("Male or Female : ")

        print(Name)
        print(Age)
        print(Gender)

    travelling = input("OOPS!!! Forget Someone : ")
