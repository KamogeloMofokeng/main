#returns the sum of num1 and num2
def add(num1,num2):
    return num1 + num2

#returns the subratction of num1 and num2
def sub(num1,num2):
    return num1 - num2

#returns the multiplication of num1 and num2
def mul(num1,num2):
    return num1 * num2

#returns the division of num1 and num2
def div(num1,num2):
    return num1 / num2

def main():
    operation = input("what do you want to do(+,-,*,/):")
    if (operation != '+' and operation != '-' and operation != '*' and operation != '/'):
        print("you must enter a valid operation")
    else:
        num1 = int(input("enter num 1"))
        num2 = int(input("enter num 2"))
        if(operation == '+'):
            print(add(num1,num2))
        elif(operation == '-'):
            print(sub(num1,num2))
        elif(operation == '/'):
            print(div(num1,num2))
        else:
            print(mul(num1,num2))
        
main()