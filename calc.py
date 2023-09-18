#
# ==================

# functions
# non-void
def add(a, b) -> int:
    return a + b 


# void
def banner() -> None:
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")

def check_operation(op) -> None:
    if op == "+":
        add()

# ==================


dict_calc = {

}
# ==================


# user input
num1 = input("Enter a number: ")
num2 = input("Enter another number")

operation = input("Select an operation: ")

# ===============================
def main():
    print("main")

if __name__ == "__main__":
    print("\n<END OF PROGRAM>")
# ===============================