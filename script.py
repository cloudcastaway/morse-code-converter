from convert import Convert

if __name__ == '__main__':

    selection = input("Would you like to encrypt or decrypt a string? (e/d)").lower()
    while selection != "e" and selection != "d":
        selection = input("Enter \"e\" for encrypting or \"d\" for decrypting: ").lower()

    convert_string = Convert()
    invalid_char = True
    while invalid_char:
        string = input(f"Type in a word or sentence to {convert_string.get_method(selection)}: ")
        for char in string:
            if char not in convert_string.get_chart():
                print(f"You typed in an invalid character: {char}")
                break
        invalid_char = False

    if selection == "e":
        print(convert_string.encrypt(string))
    else:
        print(convert_string.decrypt(string))
        