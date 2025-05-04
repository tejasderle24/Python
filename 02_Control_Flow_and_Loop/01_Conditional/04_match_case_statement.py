# match case statement (switch Statement) 

a = int(input("Enter you Number Between 1 to 10 : "))


match a:
    case 6 :
        print("You Won the Camera")
    case 3 :
        print("You Won the Car")
        
    case 4 :
        print("You Won the $100")
    case 3 :
        print("You Won the First Price")
    case _:
        print("Better Luck Next Time..!")
        