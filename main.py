from calc import * 


def main():
    # title
    print("\nCALCULATOR")
    print("==========\n")

    # user input
    a = get_nums()

    # display operations
    print()
    banner()

    # select operation
    operation = input("\nSelect an operation: ")

    # result
    check_operation(operation, a[0], a[1])
# ===============================

if __name__ == "__main__":
    main()
    print("\n<END OF PROGRAM>")
# ===============================