from encrypt import encrypt
from decrypt import decrypt


def start():
    while True:
        print('The type of operation:')
        print('(encryption - e)')
        print('(decryption - d)')
        print('(exit  - ext)')
        operator = input("Please select one option: ")
        if operator == "ext":
            exit()
        elif operator == "e":
            encrypt()
            print("")
        elif operator == "d":
            decrypt()
            print("")
        else:
            print("Wrong type of operation, try again! ")
            print("")


if __name__ == '__main__':
    start()
