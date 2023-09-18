import math 

# FUNCTIONS
# non-void
def add(a, b) -> int:
    return a + b 

def subtract(a, b) -> int:
    return a - b 

def multiply(a, b) -> int:
    return a * b 

def divide(a, b) -> int:
    return a / b 


def modulus(a, b) -> int:
    return a % b 

def pow(a, b) -> int:
    return a ** b 

def sqrt(a, b) -> int:
    return math.sqrt(a, b)


# void
def banner() -> None:
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. %")
    print("6. **")
    print("7. sqrt")

def get_nums():
    correct_input = False

    while not correct_input:
        num1 = input("Enter a number: ")
        num2 = input("Enter another number: ")
         
        try: 
            num1 = int(num1)
            num2 = int(num2)
            correct_input = True

        except:
                print("*an error has occurred*")
                print("Enter type *int*\n")

    return [num1, num2] 


# DICTIONARY
dict_calc = {
    "+": add,
    "-": subtract,
    "*": multiply, 
    "/": divide,
    "%": modulus,
    "**": pow,
    "sqrt": sqrt 
}

def check_operation(op, n1, n2) -> None:
    try:
        print(dict_calc[op](n1, n2))   

    except:
        print("*an error has occurred*")
        print("operation may not exist in dictionary")
# ======================================
# <END>