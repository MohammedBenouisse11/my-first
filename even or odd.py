print("welcome in the even-odd game!")
print("please enter a numbers... And i will tell if it even or odd")
while True :
    num = input("enter different numbers with a comma between them :").split(',')
    even = []
    odd = []
    for x in range(len(num)):
        try :
            c = int(num[x])
            if(c % 2 == 0):
                even.append(num[x])

                print("the list of even numbers is :",even)
            else:
                odd.append(num[x])
                print("the list of odd numbers is:",odd)
        except ValueError :
            print("please enter a valid number!!!")
    print("___________________________")
