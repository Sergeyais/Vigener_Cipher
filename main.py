from vigener_cipher_slogan import Vcs
from vigener_cipher_open_text import Vco
from vigener_cipher_close_text import Vcc


if __name__ == "__main__":
    """
    User interface for interacting with the program
    """
    mode = int(input("Enter the mode: "))
    if mode == 1:
        text = str(input("Enter the text: "))
        key = str(input("Enter the key: "))
        action = int(input("Enter an action(1-encrypt, 2-decipher): "))
        if action == 1:
            vcs = Vcs()
            print(vcs.encrypt(text, key))
        elif action == 2:
            vcs = Vcs()
            print(vcs.decipher(text, key))
        else:
            print("The mode is selected incorrectly!")
    elif mode == 2:
        text = str(input("Enter the text: "))
        key = str(input("Enter the key: "))
        action = int(input("Enter an action(1-encrypt, 2-decipher): "))
        if action == 1:
            vco = Vco()
            print(vco.encrypt(text, key))
        elif action == 2:
            vco = Vco()
            print(vco.decipher(text, key))
        else:
            print("The mode is selected incorrectly!")
    elif mode == 3:
        text = str(input("Enter the text: "))
        key = str(input("Enter the key: "))
        action = int(input("Enter an action(1-encrypt, 2-decipher): "))
        if action == 1:
            vcс = Vcc()
            print(vcс.encrypt(text, key))
        elif action == 2:
            vcс = Vcc()
            print(vcс.decipher(text, key))
        else:
            print("The mode is selected incorrectly!")
    else:
        print("The mode is selected incorrectly!")
