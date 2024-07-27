def encode(password):
    encoded = ""
    for i in password:
        if i == "7":
            num = 0
        elif i == "8":
            num = 1
        elif i == "9":
            num = 2
        else:
            num = int(i)
            num += 3
        encoded += str(num)
    return encoded


def decode(password):
    decode = ""
    for i in password:
        if '0' <= i <= '9':
            decoded_i = str((int(i) - 3) % 10)
            decode += decoded_i
    return decode


def main():
    remain = True
    while remain:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            decoded = decode(encoded)
            print("The encoded password is ", encoded, " and the original password is ", decoded, ".\n", sep="")
        elif choice == 3:
            remain = False
        else:
            print("Invalid input.\n")


if __name__ == "__main__":
    main()
