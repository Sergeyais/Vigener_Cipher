from vigener_cipher_open_text import Vco

"""We are performing a brute force search through the alphabet for the vigener_cipher_open_text"""
chars = "abcdefghijklmnopqrstuvwxyz"
vco = Vco()
for item_chars in chars:
    vco.decipher("slpwzaklnmqmakwvxkc", item_chars)
